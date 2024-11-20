SciPy
=====

.. questions::

   - When you need more advanced mathematical functions, where do you
     look?

.. objectives::

   - Understand that SciPy exists and what kinds of things it has.
   - Understand the importance of using external libraries and how to
     use them.
   - Understand the purpose of wrapping existing C/Fortran code.
   - Non-objective: know details of everything (or anything) in SciPy.

.. seealso::

   * Main article: `SciPy documentation <https://docs.scipy.org/doc/scipy/reference/>`__



SciPy is a library that builds on top of NumPy. It contains a lot of
interfaces to battle-tested numerical routines written in Fortran or
C, as well as python implementations of many common algorithms.



What's in SciPy?
----------------

Briefly, it contains functionality for

- Special functions (Bessel, Gamma, etc.)
- Numerical integration
- Optimization
- Interpolation
- Fast Fourier Transform (FFT)
- Signal processing
- Linear algebra (more complete than in NumPy)
- Sparse matrices
- Statistics
- More I/O routine, e.g. Matrix Market format for sparse matrices,
  MATLAB files (.mat), etc.

Many (most?) of these are not written specifically for SciPy, but use
the best available open source C or Fortran libraries.  Thus, you get
the best of Python and the best of compiled languages.

Most functions are documented ridiculously well from a scientific
standpoint: you aren't just using some unknown function, but have a
full scientific description and citation to the method and
implementation.



Exercises: use SciPy
--------------------

These exercises do not exist because *you* might need *these*
functions someday.  They are because *you* will need to *read
documentation and understand documentation of an an external library*
eventually.

1: Numerical integration
~~~~~~~~~~~~~~~~~~~~~~~~

.. challenge::

   Do the following exercise **or** read the documentation and
   understand the relevant functions of SciPy:

   Define a function of one variable and using
   `scipy.integrate.quad <https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad>`__
   calculate the integral of your function in the
   interval ``[0.0, 4.0]``. Then vary the interval and also modify the function and check
   whether scipy can integrate it.


.. solution::

   .. code-block:: python

      from scipy import integrate

      def myfunction(x):
          # you need to define result
          return result

      integral = integrate.quad(myfunction, 0.0, 4.0)
      print(integral)

   `quad
   <https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad>`__
   uses the Fortran library QUADPACK, which one can assume is pretty
   good.  You can also see a whole lot of scientific information about
   the function on the docs page - including the scientific names of
   the methods used.



2: Sparse matrices
~~~~~~~~~~~~~~~~~~

.. challenge::

   Do the following exercise **or** read the documentation and
   understand the relevant functions of SciPy:

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

.. solution::

   The basic code to do the test is:

   .. code-block::

      import numpy
      import scipy.sparse

      vector = numpy.random.random(10000)
      matrix = scipy.sparse.rand(10000, 10000, density=.05, format='csc')

      # We time this line
      matrix.dot(vector)

   From the top of the `spare matrix module documentation
   <https://docs.scipy.org/doc/scipy/reference/sparse.html>`__, we can
   see there are a variety of different available sparse matrix types:
   ``bsr``, ``coo``, ``csr``, ``csc``, etc.  These each represent a
   different way of storing the matrices.

   It seems that ``csr`` and ``csc`` are fairly fast.  ``lil`` and
   ``dok`` are slow but it says that these are good for creating
   matrices with random insertions.

   For example, ``csr`` takes 7ms, ``lil`` 42ms, ``dok`` 1600ms, and
   converting to a non-sparse array ``matrix.toarray()`` and
   multiplying takes 64ms on one particular computer.

   This code allows us to time the performance at different
   densities.  It seems that with the ``csr`` format, sparse is better
   below densities of around .4 to .5:

   ..code-block::

      for density in [.01, .05, .1, .2, .3, .4, .5]:
          matrix = scipy.sparse.rand(10000, 10000, density=density, format='csr')
	  time_sparse = timeit.timeit('matrix.dot(vector)', number=10, globals=globals())
	  matrix2 = matrix.toarray()
	  time_full = timeit.timeit('matrix2.dot(vector)', number=10, globals=globals())
	  print(f"{density} {time_sparse:.3f} {time_full:.3f}")



See also
--------

* `SciPy general introduction <https://docs.scipy.org/doc/scipy/reference/tutorial/general.html>`__
* `SciPy documentation
  <https://docs.scipy.org/doc/scipy/reference/>`__



.. keypoints::

   - When you need advance math or scientific functions, let's just
     admit it: you do a web search first.
   - But when you see something in SciPy come up, you know your
     solutions are in good hands.
