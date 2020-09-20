Parallel programming
====================

.. questions::

   - When you need more than one processor, what do you do?
   - What are the limitations of How to use basic NumPy?

.. objectives::

   - Understand the major strategies of parallelizing code
   - Understand mechanics of the ``multiprocessing`` package
   - Know when to use more advanced packages



Modes of parallelism
--------------------

You realize you do more computation than you can on one processor?
What do you do?

1. Profile your code, identify the *actual* slow spots.

2. Can you improve your code in those areas?  Use an existing library?

3. Are there are any low-effort optimizations that you can make?

4. Think about parallelizing.


Many times in science, you want to parallelize your code.  **Parallel
computing** is when many different tasks are carried out
simultaneously.  There are three main models:

* **Embarrassingly parallel:** the code is not parallel, but you run
  multiple copies of the code separately, and combine the results
  later.  If you can do this, great!  (array jobs, task queues)

* **Shared memory parallelism:** There is one process that can access
  the same memory (variables, state, etc).  (OpenMP)

* **Message passing:** Different processes communicate, sharing data
  as needed.  (Message Passing Interface (MPI)).

Programming shared memory or message passing is beyond the scope of
this course, but the simpler strategies are most often used anyway.

.. warning::

   Parallel programming is not magic, but many things can go wrong and
   you can get unexpected results or difficult to debug problems.
   Parallel programming is a fascinating world to get involved in, but
   make sure you invest enough time to do it well.

   See the entertaining video by Raymond Hettinger (See Also at bottom
   of page) for an entertaining take on this.



Multithreading and the GIL
--------------------------

Python has problems with threading: The **Global interpreter lock
(GIL)** means that only one thread in a process can run actual Python
code.  This is bad for parallelism.  *But it's not all bad!:*

* External libraries (NumPy, SciPy, pandas, etc) written in C or other
  languages can release the lock and run multi-threaded.  Also, most
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
   * We recommend you find a UNIX threading tutorial first.



multiprocessing
---------------

As opposed to threading, Python has a reasonable way of doing
something similar that uses multiple processes: the
:py:mod:`multiprocessing` module.

* The interface is a lot like threading, but in the background makes
  new processes to get around the global interpreter lock.

* There are low-level functions which have a lot of the same risks and
  difficulties as when using threading.

The `split-apply-combine <https://doi.org/10.18637%2Fjss.v040.i01>`__
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
  pool.map(square, [1, 2, 3, 4, 5, 6])



.. challenge:: Parallel-1, multiprocessing

   Here, you find some code which calculates pi by a stochastic
   algorithm.  You don't really need to worry how the algorithm works,
   but it computes random points in a 1x1 square, and computes the
   number that fall into a circle.  Copy it into a Jupyter notebook
   and use the ``%%timeit`` cell magic on the computation part (the
   one line after timeit below)

   ::

      import random

      def sample(n):
          """Make n trials of points in the square.  Return (n, number_in_circle)"""
          number_in_circle = 0
          for i in range(n):
              x = random.random()
              y = random.random()
              if x**2 + y**2 < 1:
                  number_in_circle += 1
          return n, number_in_circle

      %%timeit
      n, circle = sample(10**6)

      pi = circle / n * 4
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
      slow you down!

      You either need to be able to specify the number of CPUs to use
      (and pass it the right number), or make it aware of the cluster
      system.  For example, on a Slurm cluster you would check the
      environment variable ``SLURM_CPUS_PER_TASK``.

      Whatever you do, document what your code is doing under the
      hood, so that other users know what is going on (we've learned
      this from experience...).


MPI
---

.. todo::

   - Radovan


.. code-block:: python
   :emphasize-lines: 3,16-18,22,32,35

   from random import random
   import time
   from mpi4py import MPI


   def darts_inside_unit_circle(num_darts):
       num_inside = 0
       for _ in range(num_darts):
           x = random()
           y = random()
           if x * x + y * y < 1.0:
               num_inside += 1
       return num_inside


   comm = MPI.COMM_WORLD
   size = comm.Get_size()
   rank = comm.Get_rank()

   num_darts = 30000000

   if size > 1:
       num_darts_task = int(num_darts / size)
   else:
       num_darts_task = num_darts

   t0 = time.perf_counter()
   num_inside = darts_inside_unit_circle(num_darts_task)
   t = time.perf_counter() - t0

   print(f"before gather: rank {rank}, num_inside: {num_inside}")
   num_inside = comm.gather(num_inside, root=0)
   print(f"after gather: rank {rank}, num_inside: {num_inside}")

   if rank == 0:
       pi_estimate = 4.0 * sum(num_inside) / num_darts
       print(
           f"\nnumber of darts: {num_darts}, estimate: {pi_estimate}, time spent: {t:.2} seconds"
       )


Coupling to other languages
---------------------------

As mentioned further up in "Multithreading and the GIL", Python has the global
interpreter lock (GIL) which prevents us from using shared-memory
parallelization strategies like OpenMP "directly".

However, an interesting workaround for this can be to couple Python with other
languages which do not have the GIL.

Two strategies are common:

- Couple Python with compiled languages like C, C++, Fortran, or Rust and let those handle the shared-memory parallelization:

   - C: use the `cffi <https://cffi.readthedocs.io/>`__ package (C foreign function interface)
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

This is another strategy. Text needed here ...

.. todo::

    - Not sure who?



See also
--------

* `Thinking about Concurrency, Raymond Hettinger
  <https://youtu.be/Bv25Dwe84g0>`__.  Good introduction to simple and
  safe concurrent code.

.. keypoints::

   - Pure Python is not very good for highly parallel code.
   - Luckily it interfaces to many things which *are* good, and give
     you the full control you need.
