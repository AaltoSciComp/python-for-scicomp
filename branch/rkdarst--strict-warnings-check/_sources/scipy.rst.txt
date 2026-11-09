SciPy
=====

.. questions::

   - When you need more advanced mathematical functions, where do you look?

.. objectives::

   - Understand that SciPy exists and what kinds of things it has.
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



Example: Numerical integration
------------------------------

.. challenge::

   Define a function of one variable and using
   `scipy.integrate.quad <https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html#scipy.integrate.quad>`__
   calculate the integral of your function in the
   interval ``[0.0, 4.0]``. Then vary the interval and also modify the function and check
   whether scipy can integrate it.


.. solution::

   :class: toggle-shown

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
