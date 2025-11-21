.. _cython:

Extending Python with Cython
============================

.. questions::

   - How does runtime performance of Python compare to languages like C, C++
     or Fortran?
   - How do we use code written in other languages from within Python? In what
     situations is this useful?


.. objectives::

   - Understand how compiled extension modules can speed up code execution. 
   - Build your first compiled extension module with Cython.
   - Learn to optimize your Cython code with static type declarations.
   - Learn to use Numpy arrays in Cython code and implement common performance
     enhancements for Cythonized arrays.

.. callout::

   Using Cython requires that you have a working environment for compiling
   C code. This goes beyond the software requirements for this course, so the
   teaching will be given in form of demonstrations and no exercises.
   You may still follow along with the code examples but you will need to have
   Cython and a working C compiler available. You can install both to your
   Conda environment with `conda install -c conda-forge cython c-compiler`.


Python and performance
----------------------

Interpreted languages like Python are rather slow to execute compared to
languages like C or Fortran that are compiled to machine code ahead of
execution. Python in particular is both strongly typed and dynamically typed:
this means that all variables have a type that matters for operations that
can be performed on the variable, and that the type is determined only during
runtime by the Python interpreter. The interpreter does a lot of
"unboxing" of variable types when performing operations, and this comes with
significant overhead. For example, when just adding two integers

.. code:: python
   
   a = 7
   b = 6
   c = a + b
   
the Python interpreter needs to:

  1. Check the types of both operands
  2. Check whether they both support the **+** operation
  3. Extract the function that performs the **+** operation (due to operator
     overloading objects can have a custom definition for addition)
  4. Extract the actual values of the objects
  5. Perform the **+** operation
  6. Construct a new integer object for the result ("boxing")

  .. image:: img/cython/unboxing-boxing.svg
   :class: center
   :width: 90.0%

Meanwhile in languages like C, the types are known at compilation time, which
allows the compiler to optimize many of the above steps away for better
performance at runtime.

Scientific programs often include computationally expensive sections (e.g.
simulations of any kind). So how do we make Python execute our code faster in
these situations? Well that's the neat part: we don't! Instead, we write the
performance critical parts in a faster language and make them usable
from Python.

This is called extending Python, and usually boils down to writing C-code
with Python-specific boilerplate, or using a specialized tool for generating
such C code from Python code (so-called *transpilers*). The C-code is compiled
into a shared library, in this context called a **Python extension module**.
Most scientific Python libraries (Numpy, Scipy etc) do exactly this: their
computationally intensive parts are either written in a compiled language,
or they call an external library written in such language.

When working on your own Python project, you may find that there is a C
library that does exactly what you need, but it doesn't provide a Python
interface. Or you may have computationally intensive code that doesn't
vectorize nicely for Numpy. In cases like these it can be useful to write
your own extension modules that you then import into your Python code.

Here we discuss one popular approach for extending Python with compiled code:
using a tool called Cython.

Cython
------

`Cython <https://cython.org/>`__ is a framework for writing Python-like code
that can be processed with the Cython compiler to produce optimized code.
Cython is designed to provide C-like performance for code that is mostly
written in Python by adding only a few C-like declarations to existing
Python code. As such, Cython aims to provide the best of the both worlds:
the good programmer productivity of Python together with the high performance
of C. Cython also makes it easy to interact with external C/C++ code.

The Cython compiler processes code written in Python, or more
commonly the Cython extension of Python language, and turns it into valid
C-code which is then compiled into a Python extension module using a
C compiler (GCC, Clang, MSVC, ...). The Cython programming language is a 
superset of Python that adds C-like static type declarations and other
features that make it possible to generate efficient machine code.

.. callout::

   Unlike plain Python code, Cython code must be compiled ahead of time before
   it can be executed. This is usually done during the build phase of a
   project. Note that Cython is *not* a just-in-time (JIT) compiler like e.g.
   Numba, although you *can* call the Cython compiler at runtime for JIT-like
   behavior if you really want to.


Your first Cython module
------------------------

Suppose we have a Python module called **my_module.py** that contains:

.. code:: python

   def add(x, y):
       result = x + y
       return result

Cython allows one to compile **my_module.py** directly to machine code while
still allowing its contents to be imported and used from Python code. We can
Cythonize the module "manually" from command line:

.. code:: bash

   $ cythonize -i my_module.py

This produces a file called **my_module.c**, full of C code. One can
investigate the generated **.c** file but it is not really meant for humans to
read, because of all the boilerplate that Cython adds in order to make the
compiled code available to Python. Already this simple function results in
over 7000 lines of C code!

The option **-i** (meaning inplace) tells Cython to also compile the generated
**.c** file into an extension module in the same directory.
This could also be done manually by invoking a C-compiler of your choice.
On Linux/Mac systems the compiled module will be called something
like **my_module.cpython-314-x86_64-linux-gnu.so**, on Windows the suffix will
be **.pyd**.

The extension module can be imported from Python in the same way as one would
import a pure Python module, e.g.:

.. code:: python

   from my_module import add
   z = add(4, 5)


Usually when working with Cython, one does not Cythonize the whole program but
only selected modules. A typical Cython project is separated into plain Python
modules (file suffix **.py**), and Cython code files (suffix **.pyx**).
The **.pyx** files will usually contain Cython-specific code like static type
information, so that they are not valid Python code anymore and must be
Cythonized before use.

.. callout::

   Real-world project don't usually invoke Cython from the command line and
   instead use an established build tool like **setuptools** to handle the
   Cythonization during the project's build phase. More info is available on
   the `Cython documentation <https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compilation>`__.
   See also the :doc:`course page on packaging <packaging>`.


Using Cython with Jupyter
-------------------------
.. important::

   Due to a `known issue`_ with ``%%cython -a`` in ``jupyter-lab`` we have to use the ``jupyter-nbclassic`` interface
   for this episode.

.. _known issue: https://github.com/cython/cython/issues/7319

Jupyter supports Cython compilation directly inside notebooks via `an extension <https://cython.readthedocs.io/en/latest/src/quickstart/build.html#using-the-jupyter-notebook>`__,
assuming your environment has Cython installed.

We first load the Cython extension, e.g. in the very first cell: ::

   %load_ext Cython

We can Cythonize cell contents using the magic `%%cython`:

.. code:: python

   %%cython
   def add(x, y):
       result = x + y
       return result


The compiled function can then be called from other cells.

.. demo::

   There is also `%%cython --annotate`, or `%%cython -a` for short, which is
   useful for analyzing the generated C code. Try executing the code for
   `add()` with this magic command in Jupyter. Upon doing so:

   1. Estimate the amount of interactions with the Python runtime, by the intensity of the yellow background colour.
   2. You will be able to inspect the underlying C code.

   .. solution::

      .. image:: img/cython/jupyter-cython-annotate.png


Adding static type information
------------------------------

So far our Cythonized extension module is rather minimal. We have reduced some
of the interpreting overhead by compiling the code, but it's still using Python's
fully dynamic type system with the same boxing and unboxing overhead as in
standard Python. This is because there are no type declarations in the code
that Cython could use to optimize.

When Cythonizing a Python code, static type information can be added
either:

-  In function signatures by prefixing the formal arguments by their
   type.
-  By declaring variables with the **cdef** Cython keyword, followed by
   the the type.

To make Cython function that adds two integers and returns the result as
an integer, we would write:

.. code:: python

   def add(int x, int y):
       cdef int result
       result = x + y
       return result

The function works now only with integers but with less boxing/unboxing
overhead. Store this as **my_module.pyx** (note the file extension) and
Cythonize as before:

.. code:: bash

   $ cythonize -i my_module.pyx

Import this into Python and confirm that it works as expected with integers.
However, if passing floating-point numbers the function is forced to interpret
the inputs as integers before performing the addition. For example,
**add(1.4, 2.7)** would return 3. This happens because there is an automatic
conversion from the input Python objects to the
declared C-types, in this case integers, when calling the Cythonized function
from Python. Similarly the returned C variable is converted to a corresponding
Python object.

To make the function work with floats we'd instead declare the types to be
either **float** (32-bit) or **double** (64-bit) type instead of **int**.
The table below lists the most common C types and their corresponding
Python types. More information can be found in the `Cython
documentation <https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html>`__.

================= =============
From Python types To C types
================= =============
int               int, long
int, float        float, double
str/bytes         char \*
================= =============


Using Numpy arrays with Cython
------------------------------

Cython has built-in support for Numpy arrays.

As discussed in the :doc:`Numpy lectures <numpy-advanced>`, Numpy arrays provide
great performance for vectorized operations. In contrast, thing like
**for**-loops over Numpy arrays should be avoided because of interpreting
overhead inherent to Python **for**-loops. There is also overhead from
accessing individual elements of Numpy arrays.

With Cython we can bypass both restrictions and write efficient loops over
Numpy arrays. Consider e.g. a double loop that sets values of a 2D array:

.. code:: python
   
   import numpy as np

   def slow_looper(N):
      """"""
      data = np.empty((N, N), dtype=int)
      
      counter = 0
      for i in range(N):
         for j in range(N):
               data[i, j] = counter
               counter += 1 


We can Cythonize this as before to optimize the **for**-loops. A quick check 
with **timeit** shows that with **N=100**, the pure Python version takes 820μs
and the Cythonized version (without any static typing) takes 700μs. This is
nice, but we are still bottlenecked by array lookups and assignments, i.e. the
**[]** operator, which invokes Python code.

We can get a huge speedup by adding a static type declaration for the Numpy
array, and for the other variables too while we are at it. To do this we must
import compile-time information about the Numpy module using the
Cython-specific **cimport** keyword, then use Cython's Numpy interface to
declare the array's datatype and dimensions:

.. code:: python
   
   import numpy as np   # Normal Numpy import
   cimport numpy as cnp # Import for Numpy C-API

   def fast_looper(int N):
      """"""

      # Type declaration: 2D array of 32-bit integers 
      cdef cnp.ndarray[cnp.int32_t, ndim=2] data
      data = np.empty((N, N), dtype=np.int32)
      
      cdef int counter = 0    
      # double loop is done at nearly C speed
      for i in range(N):
         for j in range(N):
               data[i, j] = counter
               counter += 1


Cythonizing and running the function with **timeit** shows that the function
now only takes 3.30μs with **N = 100**. This is ~250 times faster than the
pure Python implementation!

.. callout::

   `cimport numpy` needs access to Numpy C-headers which are usually included
   in Python distributions. This usually works out of the box for Jupyter
   notebooks. However, if using the command line `cythonize` tool you may need
   to manually set include paths for the C compiler.
   Refer to `the docs <https://cython.readthedocs.io/en/latest/src/userguide/numpy_tutorial.html#compilation>`__
   for more details.

.. callout::

   It is good practice to also call `cnp.import_array()` after doing the
   `cimport` of Numpy. This is required for accessing attributes (like
   `.shape`) of typed Numpy arrays.


More Numpy indexing enhancements
--------------------------------

When indexing arrays, Numpy does some bounds checking in an attempt to catch
logic errors (e.g. attempting to access element at index 100 of an array of
length 10). Numpy also checks for negative indices to support wraparound
syntax like **a[-1]**. We can tell Cython to disable these checks for some
extra performance:

.. code:: python

   import numpy as np
   cimport numpy as cnp
   cimport cython

   @cython.boundscheck(False)
   @cython.wraparound(False)
   def fast_looper(int N):
      # ... Same function body as above ...


Whether these decorators *actually* result in faster code or not depends on
how complicated your array usage is. In this simple example there is likely
no measurable improvement: even if the checks are kept, modern compilers and
processors are rather good at predicting unlikely branches and optimize the
execution accordingly ("branch prediction").

Disabling bounds checking of course means that out-of-bounds indexing will go
undetected and lead to undefined behavior. It may crash your program or cause
memory corruption, so be very careful if using these decorators!


When to Cythonize?
------------------

Static typing in Cython is a tradeoff between performance and the dynamical
nature of Python code. You most certainly do not want to Cythonize your whole
project: at that point you may just as well pick a different programming
language!

Here are some rules of thumb to keep in mind when optimizing your code with
Cython (see also `Cython docs <https://cython.readthedocs.io/en/latest/src/quickstart/cythonize.html#determining-where-to-add-types>`__):

- Only Cythonize the modules/functions for which performance is *really*
  needed. Profiling tools help at identifying such bottlenecks.  
- Static type declarations work the best for fundamental data types (integers,
  floats, strings) and for contiguous arrays. Operations on heterogeneous lists
  and dictionaries do not usually benefit much from Cython.


Alternatives to Cython
----------------------

`Numba <https://numba.pydata.org/>`__ is a tool that compiles Python code to
optimized machine code on the fly without needing a manual compilation step.
It works with Numpy but does not support all of Python's features.

For creating compiled extension modules there are a plethora of tools and
libraries. If you already have a working C/C++ codebase and would like
to use it from Python, consider using one of the following:

- `ctypes <https://docs.python.org/3/library/ctypes.html>`__: part of Python standard library.
- `CFFI <https://cffi.readthedocs.io/en/stable/index.html>`__: somewhat similar to `ctypes` but with more features and probably better for large projects.
- `pybind11 <https://pybind11.readthedocs.io/en/stable/index.html>`__: very robust and modern way of creating extension modules. C++ only.
- `PyO3 <https://pyo3.rs/v0.27.1/>`__ for Rust code.

Further reading
---------------

- Cython `memory views <https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html>`__
  are a newer and more general way of interfacing with Numpy arrays and other buffer-like objects.
- `Calling C functions from Cython <https://cython.readthedocs.io/en/latest/src/tutorial/external.html>`__


Acknowledgements
----------------

This material has been adapted from the "Python for HPC" course by CSC - IT Center for Science.
