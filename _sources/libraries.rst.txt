Library ecosystem
=================

.. questions::

   - Beyond what we discuss in this course, what is available?
   - How do you decide what to build on for your work?

.. objectives::

   - Know of some other available packages, but don't necessarily know
     how to use them.



In this part, we'll talk about the broader Python and SciPy ecosystem.
It's all lecture and discussion, no hands-on.  Our goal isn't to teach
you about all of these packages, or even that you remember them.
Instead, you should see how things broadly fit together and how you
can always search for something that serves your purposes.



Python
------

The base of it all.  Python is written in C, and thus has great C
interfaces.  This contributes to two things:

* **Extending Python** by writing your own modules in C.

  * It's actually common to first have (or write) an analysis package
    in C or C++, then make the Python interface.  Then it can be
    supported by other languages, too.

* **Embedding Python**, where you have another primary application
  that uses Python under the hood.

These features aren't exactly unique to Python, but Python does
support them very well.



Core numerics
-------------

* `numpy <https://numpy.org/doc/stable/>`__ - arrays and array math.
* `scipy <https://docs.scipy.org/doc/scipy/reference/>`__ - software
  for math, science, and engineering.



Plotting
--------

* `matplotlib <https://matplotlib.org/>`__ - base plotting package,
  somewhat low level but almost everything builds on it.
* `seaborn <https://seaborn.pydata.org/>`__ - higher level plotting
  interface; statistical graphics.
* `mayavi <https://docs.enthought.com/mayavi/mayavi/>`__ - 3D plotting
* `PIL <https://python-pillow.org/>`__ - image manipulation.  The
  original PIL is no longer maintained, the new "Pillow" is a drop-in
  replacement.



Data analysis and other important core packages
-----------------------------------------------

* `pandas <https://pandas.pydata.org/docs/user_guide/>`__ - columnar
  data analysis
* `statsmodels <https://www.statsmodels.org/stable/>`__ - just what it says
* `SymPy <https://www.sympy.org/>`__ - symbolic math
* `networkx <https://networkx.github.io/>`__ - graph and network analysis
* `h5py <https://www.h5py.org/>`__ and `PyTables <https://www.pytables.org/>`__ - interfaces to
  the `HDF5 <https://en.wikipedia.org/wiki/Hierarchical_Data_Format>`__ on-disk file format
* `dateutil <https://dateutil.readthedocs.io/>`__ and `pytz
  <https://pythonhosted.org/pytz/>`__ - date arithmetic and handling,
  timezone database and conversion



Interactive computing and human interface
-----------------------------------------
* Interactive computing

  * `IPython <http://ipython.org/>`__ - nicer interactive interperter
  * `Jupyter <http://jupyter.org/>`__ (notebook, lab, hub, ...) -
    web-based interface to IPython and other languages

* Testing

  * `pytest <https://docs.pytest.org/>`__ - automated testing interface

* Documentation

  * `Sphinx <https://www.sphinx-doc.org/>`__ - documentation generator
    (also used for this lesson...)

* Development environments

  * `Spyder <https://www.spyder-ide.org/>`__ - interactive Python
    development environment.

* `Binder <https://mybinder.org/>`__ - load any git repository in
  Jupyter automatically, good for reproducible research



Interfacing with other languages
--------------------------------

* `cffi <https://cffi.readthedocs.io/>`__ and `ctypes
  <https://docs.python.org/3/library/ctypes.html>`__ - interface to C
  and compatible libraries
* `cython <https://cython.org/>`__ - easily make C extensions for
  Python, also interface to C libraries
* `f2py <https://numpy.org/doc/stable/f2py/>`__ - interface to Fortran
  code
* `swig <http://swig.org/>`__ - connect to a variety of programming languages.
* ``Boost.python`` - Another Python/C++ interface



Speeding up code and parallelism
--------------------------------
* `PyMPI <https://sourceforge.net/projects/pympi/>`__ - Message
  Passing Interface (MPI) in Python for parallelizing jobs.
* `cython <http://cython.org/>`__ - easily make C extensions for
  Python, also interface to C libraries
* `numba <https://numba.pydata.org/>`__ - just in time compiling of
  functions for speed-up
* `PyPy <https://www.pypy.org/>`__ - Python written in Python so that
  it can internally optimize more.
* `Dask <https://dask.org/>`__ - distributed array data structure for
  distributed computation
* `Joblib <https://joblib.readthedocs.io/>`__ - easy embarrasingly
  parallel computing
* `IPyParallel <https://ipyparallel.readthedocs.io/>`__ - easy
  parallel task engine
* `numexpr <https://numexpr.readthedocs.io/>`__ - Fast evaluation of
  array expressions by automatically compiling the arithmetic.



Machine learning
----------------

If you need some machine learning, you probably already know what you
need and this list is short and irrelevant.

- `tensorflow <https://www.tensorflow.org/>`__
- `pytorch <https://pytorch.org/>`__
- `nltk <https://www.nltk.org/>`__ - natural language processing
- `scikit-learn <https://scikit-learn.org/>`__ - simple tools for
  predictive data analysis



Your stuff
----------

Every small project you do contributes a little bit to the Python and
SciPy ecosystem.  This course has sort of started you on that path,
and a `CodeRefinery workshop <https://coderefinery.org>`__ will make
sure you have the tools to produce high-quality, reusable code.



How do you know if you should use something?
--------------------------------------------

Do you trust a random package you find online?  Especially for your
scientific results, which *have* to be correct.  Still, you also
*can't* build everything yourself, so you have to decide what point to
start with.

* Are there releases?  Have they been going on for a while?

* Are releases installable and handle dependencies well?

* Is there good documentation, that not just tells how to use it but
  how it works?

* Is there automated testing?  What's your evaluation of the risk of
  undetectable scientific errors?

* Is there a community, or is it one person?  Is it backed by some
  organization?  Does it have a permanent home?

* Is it is a public hosting site (GitLab, GitHub, Bitbucket, etc)
  where a community *could* form?

* Do others post issues and make contributions?  Are these issues
  dealt with in a timely manner?  Can you search past bug reports?

* Is the software citeable?



See also
--------

* `Topical Software in the SciPy ecosystem
  <https://www.scipy.org/topical-software.html>`__ - relatively
  detailed (but not comprehensive) list of projects


.. keypoints::

   - Almost everything you need can already be found, except your
     incremental work.
   - When do you build on that other work, and when do you create
     things yourself?
