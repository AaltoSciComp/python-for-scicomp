SciPy
=====

.. questions::

   - Q1
   - Q2

.. objectives::

   - O1
   - O2



SciPy is a library that builds on top of NumPy. It contains a lot of
interfaces to battle-tested numerical routines written in Fortran or
C, as well as python implementations of many common
algorithms. Briefly, it contains functionality for

- Special functions (Bessel, Gamma, etc.)
- Numerical integration
- Optimization
- Interpolation
- Fast Fourier Transform (FFT)
- Linear algebra (more complete than in NumPy)
- Sparse matrices
- Statistics
- More I/O routine, e.g. Matrix Market format for sparse matrices,
  MATLAB files (.mat), etc.


Exercise 3.1
------------

Using scipy, calculate the integral of the function ``sin`` in the
interval ``[0, pi]``, and compare with the analytical result.


Exercise 3.2
------------

Use the SciPy sparse matrix functionality to create a random sparse
matrix with a probability of non-zero elements of 0.05 and size 10000
x 10000. The use the SciPy sparse linear algebra support to calculate
the matrix-vector product of the sparse matrix you just created and a
random vector. Use the %timeit macro to measure how long it
takes. Does the optional ``format`` argument when you create the
sparse matrix make a difference?

Then, compare to how long it takes if you'd instead first convert the
sparse matrix to a normal NumPy dense array, and use the NumPy ``dot``
method to calculate the matrix-vector product.

Can you figure out a quick rule of thumb when it's worth using a
sparse matrix representation vs. a dense representation?


(lesson here)



.. keypoints::

   - K1
   - K2
