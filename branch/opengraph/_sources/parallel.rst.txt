Parallel programming
====================

.. questions::

   - When you need more than one processor, what do you do?
   - How can we use more than one processor/core in Python?

.. objectives::

   - Understand the major strategies of parallelizing code
   - Understand mechanics of the ``multiprocessing`` package
   - Know when to use more advanced packages or approaches



Modes of parallelism
--------------------

You realize you do have more computation to do than you can on one processor?
What do you do?

1. Profile your code, identify the *actual* slow spots.

2. Can you improve your code in those areas?  Use an existing library?

3. Are there are any low-effort optimizations that you can make?

4. Think about parallelizing.


Many times in science, you want to parallelize your code: either if the computation
takes too much time on one core or when the code needs to be parallel to even
be allowed to run on a specific hardware (e.g. supercomputers).

**Parallel computing** is when many different tasks are carried out
simultaneously.  There are three main models:

* **Embarrassingly parallel:** the code does not need to synchronize/communicate
  with other instances, and you can run
  multiple instances of the code separately, and combine the results
  later.  If you can do this, great!  (array jobs, task queues)

* **Shared memory parallelism:** Parallel threads need to communicate and do so via
  the same memory (variables, state, etc). (OpenMP)

* **Message passing:** Different processes manage their own memory segments. They share data
  by communicating (passing messages) as needed. (Message Passing Interface (MPI)).

Programming shared memory or message passing is beyond the scope of
this course, but the simpler strategies are most often used anyway.

.. warning::

   Parallel programming is not magic, but many things can go wrong and
   you can get unexpected results or difficult to debug problems.
   Parallel programming is a fascinating world to get involved in, but
   make sure you invest enough time to do it well.

   See the video by Raymond Hettinger ("See Also" at bottom
   of page) for an entertaining take on this.



Multithreading and the GIL
--------------------------

The designers of the Python language made the choice
that **only one thread in a process can run actual Python code**
by using the so-called **global interpreter lock (GIL)**.
This means that approaches that may work in other languages (C, C++, Fortran),
may not work in Python without being a bit careful.
At first glance, this is bad for parallelism.  *But it's not all bad!:*

* External libraries (NumPy, SciPy, Pandas, etc), written in C or other
  languages, can release the lock and run multi-threaded.  Also, most
  input/output releases the GIL, and input/output is slow.

* If speed is important enough you need things parallel, you usually
  wouldn't use pure Python.

We won't cover threading in this course.

.. seealso::

   * `More on the global interpreter lock
     <https://wiki.python.org/moin/GlobalInterpreterLock>`__
   * `Threading python module
     <https://docs.python.org/3/library/threading.html>`__.  This is
     very low level and you shouldn't use it unless you really know what
     you are doing.
   * We recommend you find a UNIX threading tutorial first before embarking
     on using the `threading
     <https://docs.python.org/3/library/threading.html>`__ module.



multiprocessing
---------------

As opposed to threading, Python has a reasonable way of doing
something similar that uses multiple processes: the
:py:mod:`multiprocessing` module.

* The interface is a lot like threading, but in the background creates
  new processes to get around the global interpreter lock.

* There are low-level functions which have a lot of the same risks and
  difficulties as when using :py:mod:`threading`.

To show an example,
the `split-apply-combine <https://doi.org/10.18637%2Fjss.v040.i01>`__
or `map-reduce <https://en.wikipedia.org/wiki/MapReduce>`__ paradigm is
quite useful for many scientific workflows.  Consider you have this::

  def square(x):
      return x*x

You can apply the function to every element in a list using the
:py:func:`map` function:

.. code-block:: pycon

  >>> list(map(square, [1, 2, 3, 4, 5, 6]))
  [1, 4, 9, 16, 25, 36]

The :py:class:`multiprocessing.pool.Pool` class provides an equivalent but
parallelized (via multiprocessing) way of doing this.  The pool class,
by default, creates one new process per CPU and does parallel
calculations on the list:

.. code-block:: pycon

  >>> from multiprocessing import Pool
  >>> with Pool() as pool:
  ...     pool.map(square, [1, 2, 3, 4, 5, 6])
  [1, 4, 9, 16, 25, 36]



Exercises, multiprocessing
--------------------------

.. challenge:: Parallel-1, multiprocessing

   Here, you find some code which calculates pi by a stochastic
   algorithm.  You don't really need to worry how the algorithm works,
   but it computes random points in a 1x1 square, and computes the
   number that fall into a circle.  Copy it into a Jupyter notebook
   and use the ``%%timeit`` cell magic on the computation part (the
   one highlighted line after timeit below):

   .. code-block:: python
      :emphasize-lines: 20

      import random

      def sample(n):
          """Make n trials of points in the square.  Return (n, number_in_circle)

          This is our basic function.  By design, it returns everything it\
          needs to compute the final answer: both n (even though it is an input
          argument) and n_inside_circle.  To compute our final answer, all we
          have to do is sum up the n:s and the n_inside_circle:s and do our
          computation"""
          n_inside_circle = 0
          for i in range(n):
              x = random.random()
              y = random.random()
              if x**2 + y**2 < 1.0:
                  n_inside_circle += 1
          return n, n_inside_circle

      %%timeit
      n, n_inside_circle = sample(10**6)

      pi = 4.0 * (n_inside_circle / n)
      pi

   Using the :py:class:`multiprocessing.pool.Pool` code from the lesson, run
   the ``sample`` function 10 times, each with ``10**5`` samples
   only.  Combine the results and time the calculation.  What is the
   difference in time taken?

   (optional, advanced) Do the same but with
   :py:class:`multiprocessing.pool.ThreadPool` instead.  This works identically
   to ``Pool``, but uses threads instead of different processes.
   Compare the time taken.

   .. solution::

      See the finished notebook here:

      .. toctree::

	 parallel-pi-multiprocessing

      You notice the version with ``ThreadPool`` is no faster, and
      probably takes even longer.  This is because this is a
      pure-Python function which can not run simultaneously in
      multiple threads.

.. challenge:: (advanced) Parallel-2 Running on a cluster

   How does the pool know how many CPUs to take?  What happens if you
   run on a computer cluster and request only part of the CPUs on a
   node?

   .. solution::

      Pool by default uses one process for each CPU on the node - it
      doesn't know about your cluster's scheduling system.  It's
      possible that you have permission to use 2 CPUs but it is trying
      to use 12.  This is generally a bad situation, and will just
      slow you down (and make other users on the same node upset)!

      You either need to be able to specify the number of CPUs to use
      (and pass it the right number), or make it aware of the cluster
      system.  For example, on a Slurm cluster you would check the
      environment variable ``SLURM_CPUS_PER_TASK``.

      Whatever you do, document what your code is doing under the
      hood, so that other users know what is going on (we've learned
      this from experience...).


MPI
---

The message passing interface (MPI) approach to parallelization
is that:

- Tasks (cores) have a rank and are numbered 0, 1, 2, 3, ...
- Each task (core) manages its own memory
- Tasks communicate and share data by sending messages
- Many higher-level functions exist to distribute information to other tasks
  and gather information from other tasks
- All tasks typically run the entire code and we have to be careful to avoid
  that all tasks do the same thing

Introductory MPI lessons where Python is included:

- https://rantahar.github.io/introduction-to-mpi/
- https://pdc-support.github.io/introduction-to-mpi/

These blog posts are good for gentle MPI/mpi4py introduction:

- https://www.kth.se/blogs/pdc/2019/08/parallel-programming-in-python-mpi4py-part-1/
- https://www.kth.se/blogs/pdc/2019/11/parallel-programming-in-python-mpi4py-part-2/

Those who use MPI in C, C++, Fortran, will probably understand the steps in the
following example. For learners new to MPI, we can explore this example
together.

Here we reuse the example of approximating pi with a stochastic
algorithm from above, and we have highlighted the lines which are important
to get this MPI example to work:

.. code-block:: python
   :emphasize-lines: 3,23-25,29,39,42

   import random
   import time
   from mpi4py import MPI


   def sample(n):
       """Make n trials of points in the square.  Return (n, number_in_circle)

       This is our basic function.  By design, it returns everything it\
       needs to compute the final answer: both n (even though it is an input
       argument) and n_inside_circle.  To compute our final answer, all we
       have to do is sum up the n:s and the n_inside_circle:s and do our
       computation"""
       n_inside_circle = 0
       for i in range(n):
           x = random.random()
           y = random.random()
           if x ** 2 + y ** 2 < 1.0:
               n_inside_circle += 1
       return n, n_inside_circle


   comm = MPI.COMM_WORLD
   size = comm.Get_size()
   rank = comm.Get_rank()

   n = 10 ** 7

   if size > 1:
       n_task = int(n / size)
   else:
       n_task = n

   t0 = time.perf_counter()
   _, n_inside_circle = sample(n_task)
   t = time.perf_counter() - t0

   print(f"before gather: rank {rank}, n_inside_circle: {n_inside_circle}")
   n_inside_circle = comm.gather(n_inside_circle, root=0)
   print(f"after gather: rank {rank}, n_inside_circle: {n_inside_circle}")

   if rank == 0:
       pi_estimate = 4.0 * sum(n_inside_circle) / n
       print(
           f"\nnumber of darts: {n}, estimate: {pi_estimate}, time spent: {t:.2} seconds"
       )



Exercises, MPI
--------------

.. challenge:: Parallel-2, MPI

   We can do this as **exercise or as demo**. Note that this example requires ``mpi4py`` and a
   MPI installation such as for instance `OpenMPI <https://www.open-mpi.org/>`__.

   - Try to run this example on one core: ``$ python example.py``.
   - Then compare the output with a run on multiple cores (in this case 2): ``$ mpiexec -n 2 python example.py``.
   - Can you guess what the ``comm.gather`` function does by looking at the print-outs right before and after.
   - Why do we have the if-statement ``if rank == 0`` at the end?
   - Why did we use ``_, n_inside_circle = sample(n_task)`` and not ``n, n_inside_circle = sample(n_task)``?


Coupling to other languages
---------------------------

As mentioned further up in "Multithreading and the GIL", Python has the global
interpreter lock (GIL) which prevents us from using shared-memory
parallelization strategies like OpenMP "directly".

However, an interesting workaround for this can be to couple Python with other
languages which do not have the GIL.  This also works just as well when you don't
need parallelism, but need to make an optimized algorithm for a small part of the code.

Two strategies are common:

- Couple Python with compiled languages like C, C++, Fortran, or Rust and let those handle the shared-memory parallelization:

   - C: use the `cffi <https://cffi.readthedocs.io/>`__ package (C foreign function interface).  :py:mod:`ctypes` is a similar but slightly more primitive module that is in the standard library.
   - C++: use `pybind11 <https://pybind11.readthedocs.io/>`__
   - Fortran: create a C interface using ``iso_c_binding`` and then couple the C layer to Python
     using `cffi <https://cffi.readthedocs.io/>`__
   - Rust: use `PyO3 <https://pyo3.rs/>`__

- Let compiled languages do the shared-memory parallelization part (as in above
  point) and let Python do the MPI work and distribute tasks across nodes using
  an ``mpi4py`` layer.

Coupling Python with other languages using the above tools is not difficult but
it goes beyond the scope of this course.

Before you take this route, **profile the application** first to be sure where
the bottleneck is.

Of course sometimes coupling languages is not about overcoming bottlenecks but
about combining existing programs which have been written in different
languages for whatever reason.



Dask and task queues
--------------------

There are other strategies that go completely beyond the manual
parallelization methods above.  We won't go into much detail.

Dask
~~~~

`Dask <https://dask.org/>`__ is a array model extension and task
scheduler.  By using the new array classes, you can automatically
distribute operations across multiple CPUs.

Dask is very popular for data analysis and is used by a number of high-level python library:

- Dask arrays scale Numpy (see also `xarray <http://xarray.pydata.org/en/stable/>`__ 
- Dask dataframes scale Pandas workflows
- Dask-ML scales Scikit-Learn

Dask divides arrays into many small pieces (chunks), as small as necessary to fit it into memory. Operations are delayed (lazy computing) e.g. tasks are queue and no computation is performed until you actually ask values to be computed (for instance print mean values). Then data is loaded into memory and computation proceeds in a streaming fashion, block-by-block.

.. discussion:: Example from dask.org

   .. code-block::

      # Arrays implement the Numpy API
      import dask.array as da
      x = da.random.random(size=(10000, 10000),
                           chunks=(1000, 1000))
      x + x.T - x.mean(axis=0)
      # It runs using multiple threads on your machine.
      # It could also be distributed to multiple machines



Exercises, Dask
---------------

.. challenge:: Dask-Examples (optional)

  `Dask examples <https://github.com/dask/dask-examples>`__ illustrate the usage of dask and can be run interactively through `mybinder <https://mybinder.org/>`__. Start an `interactive session on mybinder <https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab>`__ and test/run a few dask examples.

.. warning: dask on HPC

  On HPC, it is important to use `dask-mpi <https://github.com/dask/dask-mpi>`__ that deploys dask using MPI4Py. The setup can be a bit tricky and we recommend the usage of `dask-jobqueue and dask-drmaa <https://docs.dask.org/en/latest/setup/hpc.html#dask-jobqueue-and-dask-drmaa>`__: these packages need to be installed on the target platform (not through conda) to fully benefit from the native underlying MPI libraries.

Task queues
~~~~~~~~~~~

A **task queue** has a scheduler which takes a list of small jobs and
distributes them to runners for computation.  It serves as a
synchronization layer and may be useful for *embarrassingly parallel* jobs.

There are different descriptions of `task queues in Python
<https://www.fullstackpython.com/task-queues.html>`__. Job runners ask
the queue for the task which needs to be done next.  If you can divide
your job into many small parts, this may be useful to you.  However,
if you have a cluster with a job scheduler, this may be a bit
redundant.



See also
--------

* `Thinking about Concurrency, Raymond Hettinger
  <https://youtu.be/Bv25Dwe84g0>`__.  Good introduction to simple and
  safe concurrent code.

.. keypoints::

   - Pure Python is not very good for highly parallel code.
   - Luckily it interfaces to many things which *are* good, and give
     you the full control you need.
   - Combining vectorized functions (numpy, scipy, pandas, etc.) with
     the parallel strategies listed here will get you very far.
