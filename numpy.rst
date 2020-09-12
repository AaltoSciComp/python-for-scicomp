Enter NumPy
===========

.. questions::

   - Why using numpy instead of pure python?
   - How to use basic numpy?

.. objectives::

   - Be able to use basic numpy functionality
   - Understand enough of numpy to seach for answers to the rest of your questions ;)


TODO:
  - Why is the array data structure good?
  - Why learn numpy?  You rarely use it directly, but almost any other package uses it.
  - Slice arrays, basic and fancy
  - Types of operations: scalar, ufunc, methods, functions

So, we already know about python lists, and that we can put all kinds of things in there.
But in scientific usage, lists are often not enough. They are slow and not very flexible.

Numpy is the most used library for scientific computing. 
(You will probably rarely use it directly, but many libraries use it in the background)
Numpy provides the high-performance multidimensional array object and tools to use it. 

An array is a 'grid' of values, with all the same types. It is indexed by tuples of 
non negative indices and provides the framework for multiple dimensions.

* List vs array performance demonstration

Array definition
-----------------
::

  a = np.array([1,2,3])               # 1-dimensional array (rank 1)
  b = np.array([[1,2,3],[4,5,6]])     # 2-dimensional array (rank 2)

  b.shape      # the shape (rows,columns)
  b.size       # number of elements 

Other ways of creating arrays

::

   np.zeros((2, 3))           # 2x3 array with all elements 0
   np.ones((1,2))             # 1x2 array with all elements 1
   np.full((2,2),7)           # 2x2 array with all elements 7
   np.eye(2)                  # 2x2 identity matrix

   np.arange(10)              # Evenly spaced values in an interval
   np.linspace(0,9,10)        # same as above

   np.load('x.npy')           # load an array from a .npy file

   c = np.ones((3,3))
   d = np.ones((3, 2), bool)  # 3x2 boolean array

   d.dtype                    # datatype of the array       


Exercise 1
-----------

* arange vs linspace, can you make them do same thing?

* playing around with reshape

* numpy I/O 


Array maths
------------

::

  a = np.array([[1,2],[3,4]])
  b = np.array([[5,6],[7,8]])

  c = a + b
  d = np.add(a,b)

Also: - (np.subtract()), * (np.multiply()), / (np.divide()), np.sqrt(), np.sum(), np.mean()

Exercise 2
-----------

*np.multiply vs np.dot
*np.sum(axis=1) vs np.sum(axis=0)


Indexing and Slicing
--------------------

::

  a = np.eye(4)      # 4x4 identity matrix
  a[0]               # first row
  a[:,0]             # first column
  a[1:3,1:3]         # middle 2x2 array

  a[(0, 1), (1, 1)]  #slicing with lists

Boolean indexing

::

  a = np.eye(4)
  idx = (a > 0)      # creates boolean matrix of same size as a 
  a[idx]             # array of trues
  a[a > 0]           # same as above in one line 


Exercise 3
-----------

a = np.eye(4)
b = a[:,0]
b[0,0] = 5

* how does a look, how to avoid? -> view vs copy


Exercise 4
-----------

* Understand when numpy arrays are still slow


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