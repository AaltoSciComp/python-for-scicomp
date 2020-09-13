NumPy
=====

.. questions::

   - Why using numpy instead of pure python?
   - How to use basic numpy?

.. objectives::

   - Be able to use basic numpy functionality
   - Understand enough of numpy to seach for answers to the rest of your questions ;)


So, we already know about python lists, and that we can put all kinds of things in there.
But in scientific usage, lists are often not enough. They are slow and
not very flexible.


What is an array?
-----------------

For example, consider `[1, 2.5, 'asdf', False, [1.5, True]]` -
this is a Python list but it has different types for every
element.  When you do math on this, every element has to be handled separately.

Numpy is the most used library for scientific computing. 
(Even if you are not using it directly, chances are high that some library uses it in the background)
Numpy provides the high-performance multidimensional array object and tools to use it. 

An array is a 'grid' of values, with all the same types. It is indexed by tuples of
non negative indices and provides the framework for multiple
dimensions.  An array has:

* `dtype` - data type.  Arrays always contain one type
* `shape` - shape of the data, for example `3×2` or `3×2×500` or even
  `500` (one dimensional) or `[]` (zero dimensional).
* `data` - raw data storage in memory.  This can be passed to C or
  Fortran code for efficient calculations.

* TODO: List vs array performance demonstration using %timeit similar to: https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference

Creating arrays
---------------

There are different ways of creating arrays::

  a = np.array([1,2,3])               # 1-dimensional array (rank 1)
  b = np.array([[1,2,3],[4,5,6]])     # 2-dimensional array (rank 2)

  b.shape                             # the shape (rows,columns)
  b.size                              # number of elements 

In addition to above ways of creating arrays, there are many other ways of creating arrays depending on content::

   np.zeros((2, 3))           # 2x3 array with all elements 0
   np.ones((1,2))             # 1x2 array with all elements 1
   np.full((2,2),7)           # 2x2 array with all elements 7
   np.eye(2)                  # 2x2 identity matrix

   np.arange(10)              # Evenly spaced values in an interval
   np.linspace(0,9,10)        # same as above, see exercise

   c = np.ones((3,3))
   d = np.ones((3, 2), bool)  # 3x2 boolean array

Arrays can also be stored and read from a (.npy) file:: 

   np.save('x.npy')           # save an array to a .npy file
   np.load('x.npy')           # load an array from a .npy file

In many occasions (especially when something goes different than expected) it is useful to check and control the datatype of the array::

   d.dtype                    # datatype of the array
   d.astype('int')            # change datatype from boolean to integer

In the last example, `.astype('int')`, it will make a **copy** of the
array, and re-allocate data - unless the dtype is exactly the same as
before.  Understanding and minimizing copies is one of the most
important things to do for speed.


.. challenge::

   - **Datatypes** Try out ``np.arange(10)`` and ``np.linspace(0,9,10)``, what is the difference? Can you adjust one to do the same as the other?

   - **Datatypes** Create a 3x2 array of random float numbers (check np.random) between 0 and 1. Now change the arrays datatype to int (array.astype). How does the array look like? 

   - **Reshape** Create a 3x2 array of random integer numbers between 0 and 10. Reshape the array in any way possible. What is not possible?

   - **NumpyI/O** Save above array to .npy file (np.save) and read it in again.

.. solution::

   - **Datatypes** ``np.arange(10)`` results in ``array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`` with dtype **int64**, 
   while ``np.linspace(0,9,10)`` results in ``array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])`` with dtype **float64**. 
   Both ``np.linspace`` and ``np.arange`` take dtype as an argument and can be adjusted to match each other in that way.

   - **Datatypes** eg ``a = np.random.random((3,2))``. ``a.astype('int')`` results in an all zero array, not as maybe expected the rounded int.

   - **Reshape** eg ``b = np.random.randint(0,10,(3,2)``. ``b.reshape((6,1))`` and ``b.reshape((2,3))`` possible. It is not possible to reshape to shapes using more or less elements than ``b.size = 6``.

   - **NumpyI/O** ``np.save('x.npy')`` and ``np.load('x.npy')`` 



Array maths
------------

Clearly, you can do math on arrays.  Math in numpy, is very fast
because it is implemented in C or Fortran - just like most other
high-level languages such as R, Matlab, etc do.

By default, in numpy all math is element-by-element.  This is unlike
Matlab, where most things are element-by-element, but ``*`` becomes
array multiplication.  Numpy values consistency and does not treat
2-dimensional arrays specially::

  a = np.array([[1,2],[3,4]])
  b = np.array([[5,6],[7,8]])

  c = a + b
  d = np.add(a,b)

Also: - (``np.subtract()``), * (``np.multiply()``), / (``np.divide()``), ``np.sqrt()``, ``np.sum()``, ``np.mean()``, ...


.. challenge::

   - **Matrix multiplication** What is the difference between ``np.multiply`` and ``np.dot`` ? Try it.
   - **Axis** What is the difference between ``np.sum(axis=1)`` vs
     ``np.sum(axis=0)`` on a two-dimensional array? What if you leave out the axis parameter?


.. solution::

   - **Matrix multiplication** ``np.multiply`` does elementwise multiplication on two arrays, while ``np.dot`` enables matrix multiplication.
   - **Axis** axis=1 does the operation (here: ``np.sum``) over each row, while axis=0 does it over each column. If axis is left out, the sum of the full array is given.



Indexing and Slicing
--------------------

Numpy has many ways to extract values out of arrays:

- You can select a single element
- You can select rows or columns
- You can select ranges where a condition is true.

Clever and efficient use of these operations is a key to numpy's
speed: you should try to cleverly use these selectors (written in C)
to extract data to be used with other numpy functions written in C or
Fortran.  This will give you the benefits of Python with most of the
speed of C.

::

  a = np.eye(4)      # 4x4 identity matrix
  a[0]               # first row
  a[:,0]             # first column
  a[1:3,1:3]         # middle 2x2 array

  a[(0, 1), (1, 1)]  # second element of first and second row as array

Boolean indexing::

  a = np.eye(4)
  idx = (a > 0)      # creates boolean matrix of same size as a 
  a[idx]             # array with matching values of above criterion
  
  a[a > 0]           # same as above in one line 


.. challenge::

   ::

      a = np.eye(4)
      b = a[:,0]
      b[0,0] = 5

   - **View vs copy** Try out above code. How does a look like before b has changed and after? How could it be avoided?

.. solution::

   - **View vs copy**


.. challenge::

   - **Numpy functionality** Create two 2D arrays and do matrix multiplication first manually (for loop), then using the ``np.dot`` function. Use ``%%timeit`` to compare execution times. What is happening?

.. solution::

   - **Numpy functionality**


..keypoints::

   - Numpy is a powerful library every scientist using python should know about, since many other libraries also use it internally.
   - Be aware of some numpy specific pecularities



Types of operations
-------------------

There are different types of standard operations in numpy:

**ufuncs**, "universal functions": These are element-by-element
functions with standardized arguments:

- One, two, or three input arguments
- ``out=`` output argument, store output in this array (rather than
  make a new array) - saves copying data!
- See the `full reference <https://numpy.org/doc/stable/reference/ufuncs.html>`__

**Array methods** do something about the array itself::

  x = np.arange(12)
  x.shape = (3, 4)
  x                    #  array([[ 0,  1,  2,  3],
                                 [ 4,  5,  6,  7],
                                 [ 8,  9, 10, 11]])
  x.max()              #   11
  x.max(axis=0)        #  array([ 8,  9, 10, 11])
  x.max(axis=1)        #  array([ 3,  7, 11])

**Other functions**: there are countless other functions covering
linear algebra, scientific functions, etc.


.. challenge::

   - **In-place addition**: Create an array, add it to itself using a unfunc.



Linear algebra
--------------

In addition to the array type, there is a ``matrix`` type which is
specialized:

- two-dimensional only
- ``*`` operator is matrix multiplication


.. challenge::

   - **Matrixes are always 2D**  Make a 2x3 array and a 2x3 matrix.
     Extract just the first row of each of them and check the ``.shape``.



Additional Exercises
--------------------

1. Reverse a vector. Given a vector, reverse it such that the last
   element becomes the first, e.g. [1, 2, 3] => [3, 2, 1]

2. Create a 2D array with zeros on the borders and 1 inside.

3. Create a random array with elements [0, 1), then add 10 to all
   elements in the range [0.2, 0.7).

4. What is ``np.round(0.5)``? What is ``np.round(1.5)``? Why?

5. In addition to ``np.round``, explore ``np.ceil``, ``np.floor``,
   ``np.trunc``. In particular, take note of how they behave with
   negative numbers.

6. Recall the identity :math:`\sin^2(x) + \cos^2(x) = 1`. Create a
   random 4x4 array with values in the range [0, 10). Now test the
   equality with ``np.equal``. What result do you get with
   ``np.allclose`` instead of ``np.equal``?

7. Create a 1D array with 10 random elements. Sort it.

8. What's the difference between ``np_array.sort()`` and
   ``np.sort(np_array)``?

9. For the random array in question 8, instead of sorting it, perform
   an indirect sort. That is, return the list of indices which would
   index the array in sorted order.

10. Create a 4x4 array of zeros, and another 4x4 array of ones. Next
    combine them into a single 8x4 array with the content of the zeros
    array on top and the ones on the bottom.  Finally, do the same,
    but create a 4x8 array with the zeros on the left and the ones on
    the rigth.
