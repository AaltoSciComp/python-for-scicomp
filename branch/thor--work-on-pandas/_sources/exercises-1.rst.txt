Exercises 1
===========

Exercise 1.1
------------

Who needs numpy anyway? Implement matrix multiplication with nested
lists as your matrix representation. *Hint for beginners*: Create one
function

::

   def creatematrix(n, m):
       # ...

which creates an NxM matrix filled with random values
(e.g. random.random()). Then create another function

::

   def matrixmult(a, b):
       # ...

which multiplies together two matrices a and b.


Exercies 1.2
------------

Lets continue with the previous example, and add some object oriented
scaffolding around our matrix code.  Create a Matrix class with a
constructor to create the random matrix, and overload the '*' operator
to multiply two Matrix instances. Reuse the code from the previous
exercise.


Exercise 1.3
------------

The essence of science is experiment and measurement.  So lets measure
our matrix multiplication implementation, and calculate how fast it
can multiply matrices, in terms of "Gflops/s" (Giga floating point
operations per second). *Hint*: A "flop" is a floating point multiply
or addition/subtraction.  First figure out of many flops are needed to
multiply two matrices. Then you need to time it; for this you can use
the IPython magic %timeit command. And finally, equipped with this
information, you can calculate a Gflops/s score for you multiplication
method.

Exercise 1.4
------------

Basic file I/O. Run the following python snippet to create a file
``pangrams.txt``:

::

   with open('pangrams.txt', 'w') as f:
       f.write("""The quick brown fox jumps over the lazy dog
   Sphinx of black quartz, judge my vow
   The dog ate my homework
   Pack my box with five dozen liquor jugs
   """)

Next, create Python code to read that file, and check each line
whether it's a pangram. A pangram is a sentence to uses all the
letters of the alphabet.
