Introduction to Python
======================

.. questions::

   - What are the basic blocks of Python language?
   - How are functions and classes defined in Python? 

.. objectives::

   - Get a *very* short introduction to Python types and syntax
   - Be able to follow the rest of the examples in the course, even if you don't understand everything perfectly.

If you are not familiar with Python, a *very* short introduction;
first, the builtin scalar and collection types:

Scalars
-------

Scalar types, that is, single elements of various types:

::

   i = 42       # integer
   i = 2**77    # Integers have arbitrary precision
   g = 3.14     # floating point number
   c = 2 - 3j   # Complex number
   b = True     # boolean
   s = "Hello!" # String (Unicode)
   q = b'Hello' # bytes (8-bit values)


Collections
-----------

Collections are data structures capable of storing multiple values.

::

   l = [1, 2, 3]                      # list
   l[1]                               # lists are indexed by int
   l[1] = True                        # list elements can be any type
   d = {"Janne": 123, "Richard": 456} # dictionary
   d["Janne"]
   s = set(("apple", "cherry", "banana", "apple")) # Set of unique values
   s


Control structures
------------------

Python has the usual control structures, that is conditional
statements and loops:

::

   x = 2
   if x == 3:
       print('x is 3')
   elif x == 2:
       print('x is 2')
   else:
       print('x is something else')


While loops loop until some condition is met:

::

   x = 0
   while x < 42:
       print('x is ', x)
       x += 0.2


For loops loop over some collection of values:

::

   xs = [1, 2, 3, 4]
   for x in xs:
       print(x)


Often you want to loop over a sequence of integers, in that case the
``range`` function is useful:

::

   for x in range(9):
       print(x)

Another common need is to iterate over a collection, but at the same
time also have an index number. For this there is the ``enumerate``
function:

::

   xs = [1, 'hello', 'world']
   for ii, x in enumerate(xs):
       print(ii, x)


Functions and classes
---------------------

Python functions are defined by the ``def`` keyword. They take a
number of arguments, and return a number of return values.

::

   def hello(name):
       """Say hello to the person given by the argument"""
       print('Hello', name)
       return 'Hello ' + name
       
   hello("Anne")

Classes are defined by the ``class`` keyword:

::

   class Hello:
       def __init__(self, name):
           self._name = name
       def say(self):
           print('Hello', self._name)
           
   h = Hello("Richard")
   h.say()


Python type system
------------------

Python is strongly and dynamically typed.

Strong here means, roughly, that it's not possible to circumvent the
type system (at least, not easily, and not without invoking undefined
behavior).

::

   x = 42
   type(x)
   x + "hello"

Dynamic typing means that types are determined at runtime, and a
variable can be redefined to refer to an instance of another type:

::

   x = 42
   x = "hello"


*Jargon*: Types are associated with rvalues, not lvalues. In
statically typed language, types are associated with lvalues, and are
(typically) reified during compilation.


??? (lesson here)



.. keypoints::

   - Python offers a nice set of basic types as many other programming languages
   - Python is strongly typed and dynamically typed
