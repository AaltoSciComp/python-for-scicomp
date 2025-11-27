.. _numpy:

NumPy
=====

.. questions::

   - Why using NumPy instead of pure python?
   - How to use basic NumPy?
   - What is vectorization?

.. objectives::

   - Understand the Numpy array object
   - Be able to use basic NumPy functionality
   - Understand enough of NumPy to seach for answers to the rest of your questions ;)

   We expect most people to be able to do all the basic exercises
   here.  It is probably quite easy for many people; we have advanced
   exercises at the end in that case.



So, we already know about python lists, and that we can put all kinds of things in there.
But in scientific usage, lists are often not enough. They are slow and
not very flexible.

.. highlight:: python

What is an array?
-----------------

For example, consider ``[1, 2.5, 'asdf', False, [1.5, True]]`` -
this is a Python list but it has different types for every
element.  When you do math on this, every element has to be handled separately.

NumPy is the most used library for scientific computing. 
Even if you are not using it directly, chances are high that some library uses it in the background.
NumPy provides the high-performance multidimensional array object and tools to use it. 

An array is a 'grid' of values, with all the same types. It is indexed by tuples of
non negative indices and provides the framework for multiple
dimensions.  An array has:

* :ref:`dtype <arrays.dtypes>` - data type.  Arrays always contain one type
* :term:`shape` - shape of the data, for example ``3×2`` or ``3×2×500`` or even
  ``500`` (one dimensional) or ``[]`` (zero dimensional).
* :attr:`data <numpy.ndarray.data>` - raw data storage in memory.  This can be passed to C or
  Fortran code for efficient calculations.


To test the performance of pure Python vs NumPy we can write in our jupyter notebook:

Create one list and one 'empty' list, to store the result in ::

  a = list(range(10000))
  b = [ 0 ] * 10000

In a new cell starting with ``%%timeit``, loop through the list ``a`` and fill the second list ``b`` with ``a`` squared ::
  
  %%timeit
  for i in range(len(a)):
    b[i] = a[i]**2

That looks and feels quite fast. But let's take a look at how NumPy performs for the same task.

So for the NumPy example, create one array and one 'empty' array to store the result in ::

  import numpy as np
  a = np.arange(10000)
  b = np.zeros(10000)

In a new cell starting with ``%%timeit``, fill ``b`` with ``a`` squared ::

  %%timeit
  b = a ** 2

We see that compared to working with numpy arrays, working with traditional python lists is actually slow.


Creating arrays
---------------

There are different ways of creating arrays (:func:`numpy.array`, :attr:`numpy.ndarray.shape`, :attr:`numpy.ndarray.size`)::

  a = np.array([1,2,3])               # 1-dimensional array (rank 1)
  b = np.array([[1,2,3],[4,5,6]])     # 2-dimensional array (rank 2)

  b.shape                             # the shape (rows,columns)
  b.size                              # number of elements 

In addition to above ways of creating arrays, there are many other ways of creating arrays depending on content (:func:`numpy.zeros`, :func:`numpy.ones`, :func:`numpy.full`, :func:`numpy.eye`, :func:`numpy.arange`, :func:`numpy.linspace`)::

   np.zeros((2, 3))             # 2x3 array with all elements 0
   np.ones((1,2))               # 1x2 array with all elements 1
   np.full((2,2),7)             # 2x2 array with all elements 7
   np.eye(2)                    # 2x2 identity matrix

   np.arange(10)                # Evenly spaced values in an interval
   np.linspace(0,9,10)          # same as above, see exercise

   c = np.ones((3,3))
   d = np.ones((3, 2), 'bool')  # 3x2 boolean array

Arrays can also be stored and read from a (.npy) file (:func:`numpy.save`, :func:`numpy.load`):: 

   np.save('x.npy', a)           # save the array a to a .npy file
   x = np.load('x.npy')          # load an array from a .npy file and store it in variable x

In many occasions (especially when something goes different than expected) it is useful to check and control the datatype of the array (:attr:`numpy.ndarray.dtype`, :meth:`numpy.ndarray.astype`)::

   d.dtype                    # datatype of the array
   d.astype('int')            # change datatype from boolean to integer

In the last example, ``.astype('int')``, it will make a **copy** of the
array, and re-allocate data - unless the dtype is exactly the same as
before.  Understanding and minimizing copies is one of the most
important things to do for speed.



Exercises 1
-----------

.. challenge:: Exercises: Numpy-1

   1. **Datatypes** Try out :func:`np.arange(10) <numpy.arange>` and :func:`np.linspace(0,9,10) <numpy.linspace>`, what is the difference? Can you adjust one to do the same as the other?

   2. **Datatypes** Create a 3x2 array of random float numbers (check :func:`numpy.random.random`) between 0 and 1. Now change the arrays datatype to int (:meth:`array.astype <numpy.ndarray.astype>`). How does the array look like? 

   3. **Reshape** Create a 3x2 array of random integer numbers between 0 and 10. Change the shape of the array (check :meth:`array.reshape <numpy.ndarray.reshape>`) in any way possible. What is not possible?

   4. **NumPyI/O** Save above array to .npy file (:func:`numpy.save`) and read it in again.

.. solution:: Solutions: Numpy-1

   1. **Datatypes**

     - ``np.arange(10)`` results in ``array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`` with dtype **int64**,
     - while ``np.linspace(0,9,10)`` results in ``array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])`` with dtype **float64**.

     Both ``np.linspace`` and ``np.arange`` take dtype as an argument and can be adjusted to match each other in that way.

   2. **Datatypes** eg ``a = np.random.random((3,2))``. ``a.astype('int')`` results in an all zero array, not as maybe expected the rounded int (all numbers [0, 1) are cast to 0).

   3. **Reshape** eg ``b = np.random.randint(0,10,(3,2))``.

     ``b.reshape((6,1))`` and ``b.reshape((2,3))`` possible.

     It is not possible to reshape to shapes using more or less elements than ``b.size = 6``, so for example ``b.reshape((12,1))`` gives an error.

   4. **NumPyI/O** ``np.save('x.npy', b)`` and ``x = np.load('x.npy')`` 



Array maths and vectorization
-----------------------------

Clearly, you can do math on arrays.  Math in NumPy is very fast because it is
implemented in C or Fortran - just like most other high-level languages such as
R, Matlab, etc do.

By default, basic arithmetic (``+``, ``-``, ``*``, ``/``) in NumPy is
element-by-element.  That is, the operation is performed for each element in the
array without you having to write a loop.  We say an operation is "vectorized"
when the looping over elements is carried out by NumPy internally, which uses
specialized CPU instructions for this that greatly outperform a regular Python
loop.

Note that unlike Matlab, where ``*`` means matrix multiplication, NumPy uses
``*`` to perform element-by-element multiplication and uses the ``@`` symbol to
perform matrix multiplication::

  a = np.array([[1,2],[3,4]])
  b = np.array([[5,6],[7,8]])

  # Addition
  c = a + b
  d = np.add(a,b)

  # Matrix multiplication
  e = a @ b
  f = np.dot(a, b)

Other common mathematical operations include: ``-`` (:data:`numpy.subtract`), ``*`` (:data:`numpy.multiply`), ``/`` (:data:`numpy.divide`), ``.T`` (:func:`numpy.transpose`), :data:`numpy.sqrt`, :func:`numpy.sum`, :func:`numpy.mean`, ...



Exercises 2
-----------

.. challenge:: Exercises: Numpy-2

   - **Matrix multiplication** What is the difference between :data:`numpy.multiply` and :func:`numpy.dot` ? Try it.
   - **Axis** What is the difference between :func:`np.sum(axis=1) <numpy.sum>` vs
     :func:`np.sum(axis=0) <numpy.sum>` on a two-dimensional array? What if you leave out the axis parameter?


.. solution:: Solutions: Numpy-2

   - **Matrix multiplication** ``np.multiply`` does elementwise multiplication on two arrays, while ``np.dot`` enables matrix multiplication.
   - **Axis** ``axis=1`` does the operation (here: ``np.sum``) over each row, while axis=0 does it over each column. If axis is left out, the sum of the full array is given.



Indexing and Slicing
--------------------

.. seealso::

   :ref:`Numpy basic indexing docs <basics.indexing>`

NumPy has many ways to extract values out of arrays:

- You can select a single element
- You can select rows or columns
- You can select ranges where a condition is true.

Clever and efficient use of these operations is a key to NumPy's
speed: you should try to cleverly use these selectors (written in C)
to extract data to be used with other NumPy functions written in C or
Fortran.  This will give you the benefits of Python with most of the
speed of C.

::

  a = np.arange(16).reshape(4, 4)  # 4x4 matrix from 0 to 15
  a[0]                             # first row
  a[:,0]                           # first column
  a[1:3,1:3]                       # middle 2x2 array

  a[(0, 1), (1, 1)]                # second element of first and second row as array

Boolean indexing on above created array::

  idx = (a > 0)      # creates boolean matrix of same size as a 
  a[idx]             # array with matching values of above criterion
  
  a[a > 0]           # same as above in one line 



Exercises 3
-----------

.. challenge:: Exercise: Numpy-3

   ::

      a = np.eye(4)
      b = a[:,0]
      b[0] = 5

   - **View vs copy** Try out above code. How does ``a`` look like before ``b`` has changed and after? How could it be avoided?

.. solution:: Solution: Numpy-3

   - **View vs copy** The change in ``b`` has also changed the array ``a``!
     This is because ``b`` is merely a view of a part of array ``a``.  Both
     variables point to the same memory. Hence, if one is changed, the other
     one also changes. If you need to keep the original array as is, use
     ``np.copy(a)``.


Types of operations
-------------------

There are different types of standard operations in NumPy:

**ufuncs**, ":ref:`universal functions <ufuncs>`": These are element-by-element
functions with standardized arguments:

- One, two, or three input arguments
- For example, ``a + b`` is similar to :data:`np.add(a, b) <numpy.add>` but the ufunc
  has more control.
- ``out=`` output argument, store output in this array (rather than
  make a new array) - saves copying data!
- See the `full reference
  <https://numpy.org/doc/stable/reference/ufuncs.html>`__

- They also do **broadcasting** (:ref:`ref <basics.broadcasting>`).  Can you add a 1-dimensional array of shape `(3)`
  to an 2-dimensional array of shape `(3, 2)`?   With broadcasting you
  can!

  ::

     a = np.array([[1, 2, 3],
                   [4, 5, 6]])
     b = np.array([10, 10, 10])
     a + b                       # array([[11, 12, 13],
                                 #        [14, 15, 16]])

  Broadcasting is smart and consistent about what it does, which I'm
  not clever enough to explain quickly here: `the manual page on
  broadcasting
  <https://numpy.org/doc/stable/user/basics.broadcasting.html>`__.
  The basic idea is that it expands dimensions of the smaller array so
  that they are compatible in shape.

**Array methods** do something to one array:

- Some of these are the same as ufuncs::

     x = np.arange(12)
     x.shape = (3, 4)
     x                    #  array([[ 0,  1,  2,  3],
                          #         [ 4,  5,  6,  7],
                          #         [ 8,  9, 10, 11]])
     x.max()              #  11
     x.max(axis=0)        #  array([ 8,  9, 10, 11])
     x.max(axis=1)        #  array([ 3,  7, 11])

**Other functions**: there are countless other functions covering
linear algebra, scientific functions, etc.



Exercises 4
-----------

.. challenge:: Exercises: Numpy-4

   - **In-place addition**: Create an array, add it to itself using a
     ufunc.

   - **In-place addition** (advanced): Create an array of
     ``dtype='float'``, and an array of ``dtype='int'``.  Try to use the
     int array is the output argument of the first two arrays.

   - **Output arguments and timing** Repeat the initial ``b = a **
     2`` example using the output arguments and time it.  Can you make
     it even faster using the output argument?

.. solution:: Solution: Numpy-4

   - **in-place addition**::

       x = np.array([1, 2, 3])
       id(x)                        # get the memory-ID of x
       np.add(x, x, x)              # Third argument is output array
       np.add(x, x, x)
       print(x)
       id(x)                        # get the memory-ID of x
                                    # - notice  it is the same

     You note that ``np.add()`` has a third argument that is the
     output array (same as ``out=``), *and* the function returns that
     same array.


   - **Output arguments and timing** In this case, on my computer, it was
     actually slower (this is due to it being such a small array!)::

        a = np.arange(10000)
	b = np.zeros(10000)

     ::

	%%timeit
	numpy.square(a, out=b)

     This is a good example of why you always need to time things
     before deciding what is best.


Linear algebra and other advanced math
--------------------------------------

In general, you use :class:`arrays <numpy.ndarray>` (n-dimensions), not :class:`matrixes <numpy.matrix>`
(specialized 2-dimensional) in NumPy.

Internally, NumPy doesn't invent its own math routines: it relies on
`BLAS
<https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms>`__
and `LAPACK <https://en.wikipedia.org/wiki/LAPACK>`__ to do this kind
of math - the same as many other languages.

- `Linear algebra in numpy
  <https://numpy.org/doc/stable/reference/routines.linalg.html>`__

- `Many, many other array functions
  <https://numpy.org/doc/stable/reference/routines.html>`__

- `Scipy <https://docs.scipy.org/doc/scipy/reference/>`__ has even
  more functions

- Many other libraries use NumPy arrays as the standard data
  structure: they take data in this format, and return it similarly.
  Thus, all the other packages you may want to use are compatible

- If you need to write your own fast code in C, NumPy arrays can be
  used to pass data.  This is known as `extending Python
  <https://docs.python.org/3/extending/>`__.




Additional exercises
--------------------

.. challenge:: Numpy-5

   If you have extra time, try these out.  These are advanced and
   optional, and will not be done in most courses.

   1. Reverse a vector. Given a vector, reverse it such that the last
      element becomes the first, e.g. ``[1, 2, 3]`` => ``[3, 2, 1]``

   2. Create a 2D array with zeros on the borders and 1 inside.

   3. Create a random array with elements [0, 1), then add 10 to all
      elements in the range [0.2, 0.7).

   4. What is :func:`np.round(0.5) <numpy.round_>`? What is ``np.round(1.5)``? Why?

   5. In addition to ``np.round``, explore :data:`numpy.ceil`, :data:`numpy.floor`,
      :data:`numpy.trunc`. In particular, take note of how they behave with
      negative numbers.

   6. Recall the identity :math:`\sin^2(x) + \cos^2(x) = 1`. Create a
      random 4x4 array with values in the range [0, 10). Now test the
      equality with :data:`numpy.equal`. What result do you get with
      :func:`numpy.allclose` instead of ``np.equal``?

   7. Create a 1D array with 10 random elements. Sort it.

   8. What's the difference between :meth:`np_array.sort() <numpy.ndarray.sort>` and
      :func:`np.sort(np_array) <numpy.sort>`?

   9. For the random array in question 8, instead of sorting it, perform
      an indirect sort. That is, return the list of indices which would
      index the array in sorted order.

   10. Create a 4x4 array of zeros, and another 4x4 array of ones. Next
       combine them into a single 8x4 array with the content of the zeros
       array on top and the ones on the bottom.  Finally, do the same,
       but create a 4x8 array with the zeros on the left and the ones on
       the right.

   11. NumPy functionality Create two 2D arrays and do matrix multiplication
       first manually (for loop), then using the np.dot function. Use %%timeit
       to compare execution times. What is happening?


.. solution:: Solution Numpy-5

   1. One solution is:: 
    
       a = np.array([1, 2, 3])
       a[::-1]
        
   2. One solution is::
        
       b = np.ones((10,10))
       b[:,[0, -1]]=0
       b[[0, -1],:]=0

   3. A possible solution is::
        
       x = np.random.rand(100)
       y = x + 10*(x >= 0.2)*(x < 0.7)
    
   4. For values exactly halfway between rounded decimal values, NumPy rounds to the nearest even value.

   5. Let's test those functions with few negative and positive values::

       a = np.array([-3.3, -2.5, -1.5, -0.75, -0.5, 0.5, 0.75, 1.5, 2.5, 3])
       np.round(a)
       np.ceil(a)
       np.floor(a)
       np.trun(a)

   6. One solution is::

       x = 10*np.random.rand(4,4)
       oo = np.ones((4,4))
       s2c2 = np.square(np.sin(x))+np.square(np.cos(x))
       np.equal(oo,s2c2)
       np.allclose(oo,s2c2)

   7. Sorting the array itself, without copying it::
        
       x = np.random.rand(10)
       x.sort()

   8. NumPy.sort() returns a sorted copy of an array. 

   9. ``np.argsort(x)``

   10. One solution is::

        z = np.zeros((4,4))
        o = np.ones((4,4))
        np.concatenate((z,o))
        np.concatenate((z,o),axis=1)
    
   11. Using numpy without numpy functionality (np.dot) in this case, is still slow.



See also
--------

* `NumPy manual <https://numpy.org/doc/stable/reference/>`__

  * `Basic array class reference <https://numpy.org/doc/stable/reference/arrays.html>`__
  * `Indexing
    <https://numpy.org/doc/stable/reference/arrays.indexing.html>`__
  * `ufuncs <https://numpy.org/doc/stable/reference/ufuncs.html>`__

* `2020 Nature paper on NumPy's role and basic concepts <https://www.nature.com/articles/s41586-020-2649-2>`__



.. keypoints::

   - NumPy is a powerful library every scientist using python should know about, since many other libraries also use it internally.
   - Be aware of some NumPy specific peculiarities
