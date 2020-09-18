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

.. todo::

   - Richard



Multithreading and the GIL
--------------------------

.. todo::

   - Richard
   - quick since not really used, but explain GIL



``multiprocessing``
-------------------

.. todo::

   - example
   - Richard



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

.. todo::

   - OpenMP
   - Radovan



Dask and task queues
--------------------

.. todo::

    - Radovan?



See also
--------


.. keypoints::

   - K1
   - K2
