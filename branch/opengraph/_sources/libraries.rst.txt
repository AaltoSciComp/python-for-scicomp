Library ecosystem
=================

.. questions::

   - What happens when you need some method Beyond what we discuss in this course, what is available?
   - How do you decide what to build on for your work?

.. objectives::

   - Know of some other available packages, but don't necessarily know
     how to use them.
   - Be able to evaluate what you should reuse and what you should
     develop yourself.

You can't do everything yourself.  In fact, once we heard a quote such
as this:

    When you are a student, you are expected to do everything
    yourself, and that is how you are evaluated.  When you become a
    researcher, you *have* to be able to reuse what others have done.
    We don't have much practice in doing this.
    -- A student

In this lesson, we'll talk about the broader ecosystem in Python: all
the resources you have available to you.  Perhaps we can even classify
this into two types:

- Well-maintained libraries that are used by many others.
- A wide variety of public code that might work but isn't necessarily
  well-maintained (for example, code from articles).

We'll start with the first then go to the second.



Glossary
--------

Library
    A collection of code used by a program.

Package
    A library that has been made easily installable and reusable.
    Often published on public repositories such as the `Python Package
    Index <https://pypi.python.org>`__

Dependency
    A requirement of another program, not included in that program.



The Python/SciPy ecosystem
--------------------------

This section is nothing more than a tour of what exists in Python.
You aren't expected to particularly remember any of these right now,
but searching for these repositories is a starting point of a lot of
future work.

The "core" packages `could be considered
<https://www.scipy.org/about.html>`__.  Many other packages build on
these, and others that try to do similar things often try to conform
to their interfaces (especially numpy):

* Python
* Numpy - arrays, everything builds on this
* Scipy - scientific functions (not necessarily a lot builds on this)
* matplotlib - plotting, many other plotting tools build on this
* pandas - data structures
* IPython / Jupyter: interactive work



Core numerics libraries
~~~~~~~~~~~~~~~~~~~~~~~

* `numpy <https://numpy.org/doc/stable/>`__ - arrays and array math.
* `scipy <https://docs.scipy.org/doc/scipy/reference/>`__ - software
  for math, science, and engineering.



Plotting
~~~~~~~~

* `matplotlib <https://matplotlib.org/>`__ - base plotting package,
  somewhat low level but almost everything builds on it.
* `seaborn <https://seaborn.pydata.org/>`__ - higher level plotting
  interface; statistical graphics.
* `mayavi <https://docs.enthought.com/mayavi/mayavi/>`__ - 3D plotting
* `PIL <https://python-pillow.org/>`__ - image manipulation.  The
  original PIL is no longer maintained, the new "Pillow" is a drop-in
  replacement.



Data analysis and other important core packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Interactive computing

  * `IPython <http://ipython.org/>`__ - nicer interactive interpreter
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



Speeding up code and parallelism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
* `Joblib <https://joblib.readthedocs.io/>`__ - easy embarrassingly
  parallel computing
* `IPyParallel <https://ipyparallel.readthedocs.io/>`__ - easy
  parallel task engine
* `numexpr <https://numexpr.readthedocs.io/>`__ - Fast evaluation of
  array expressions by automatically compiling the arithmetic.



Machine learning
~~~~~~~~~~~~~~~~

If you need some machine learning, you probably already know what you
need and this list is short and irrelevant.

- `tensorflow <https://www.tensorflow.org/>`__
- `pytorch <https://pytorch.org/>`__
- `nltk <https://www.nltk.org/>`__ - natural language processing
- `scikit-learn <https://scikit-learn.org/>`__ - simple tools for
  predictive data analysis



Connecting Python to other languages
------------------------------------

As we discussed with Scipy, very many of the above packages aren't
written in Python: they are written in some other language and have a
Python interface.  Python is written in C, and thus has great C
interfaces.  This contributes to two things:

* **Extending Python** by writing your own modules in C.

  * It's actually common to first have (or write) an analysis package
    in C or C++, then make the Python interface.  Then it can be
    supported by other languages, too.

  * Or one starts an analysis package in Python, and slowly moves bits
    of it to C over time as there is need.

* **Embedding Python**, where you have another primary application
  that uses Python under the hood as an internal scripting language.

These features aren't exactly unique to Python, but Python does
support them very well.  Read more: `Extending and embedding Python
<https://docs.python.org/extending/index.html>`__.



Tools for interfacing with other languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These days, one rarely directly extends the Python interpreter, but uses

* `cffi <https://cffi.readthedocs.io/>`__ and `ctypes
  <https://docs.python.org/3/library/ctypes.html>`__ - interface to C
  and compatible libraries
* `cython <https://cython.org/>`__ - easily make C extensions for
  Python, also interface to C libraries
* `f2py <https://numpy.org/doc/stable/f2py/>`__ - interface to Fortran
  code
* `swig <http://swig.org/>`__ - connect to a variety of programming languages.
* ``Boost.python`` - Another Python/C++ interface
* TODO: Julia modules for Python?



Evaluating Python packages for reuse
------------------------------------

Above, we talked about well-maintained mainstream packages.  **Do you
trust random code you find online (for example included in a paper)?**

Especially consider scientific results, which *have* to be correct.
Still, you also *can't* build everything yourself, so you have to
carefully evaluate the situation.

Below are some things to consider:

* Are there releases?  Have they been going on for a while?

* Are releases installable without copy-paste?

* Are dependencies handled well?

* Does the code randomly change, so that it no longer works with your
  code.  Is this relevant?

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



Is your work reuseable?
-----------------------

Every small project you do contributes a little bit to the Python and
SciPy ecosystem.  This course has sort of started you on that path,
and a `CodeRefinery workshop <https://coderefinery.org>`__ will make
sure you have the tools to produce high-quality, reusable code.



What's next?
------------

* The `CodeRefinery workshop <https://coderefinery.org>`__ mentioned
  above will prepare you for others to reuse your code and for you to
  contribute to other code.
* The upcoming :doc:`dependencies` lesson will teach you how to
  record and manage dependencies so that anyone can seamlessly reuse
  your code.



Exercises
---------

.. exercise:: Libraries 1.1: Libraries in your work

   What libraries do you use in your work?  What have you made, which
   you could have reused from some other source.  What have you used
   from some other source that you wished you had re-created?

   Discuss in your groups or HackMD.

.. solution:: Libraries 1.1

   ... is there anything to say here?


.. exercise:: Libraries 1.2: Evaluating packages

   Below are some links to some packages, both public and made by the
   authors of this lesson.  Evaluate them, considering "would I use
   this in my project?"

   a) https://github.com/networkx/networkx/
   b) some code on webpage in a paper's footnote
   c) https://github.com/rkdarst/pcd
   d) https://github.com/dftlibs/numgrid
   e) https://github.com/rkdarst/dynbench
   f) https://vpython.org/

.. solution:: Libraries 1.2

   a) networkx: This seems to be a relatively large, active project
      using best practices.  Probably usable.
   b) I would probably use it if I had to, but would prefer not to.
   c) This (written by one of the authors of this lesson) has no
      documenting, no community, no best practices, and is very old.
      Probably not a good idea to try to use it
   d) This project uses best practices, but doesn't seem to have a big
      community.  It's probably fine to use, but who knows if it will
      be maintained 10 years from now.  It does have automated tests
      via Github Actions (``.github/workflows`` and the green checks),
      so the authors have put some work into making it correct.
   e) This (also written by one of the authors) looks like it was made
      for a paper of some sort.  It has some minimal documentation,
      but still is missing many best practices and is clearly not
      maintained anymore (look at the ancient pull request).  Probably
      not a good idea to use unless you have to.
   f) This project has a pretty website, and some information.  But
      seems to not be using best practices of an open repository, and
      custom locations which could disappear at any time.

   You notice that several of the older projects here were written by
   one of the authors of this lesson.  It goes to show that everyone
   starts somewhere and improves over time - don't feel bad if your
   work isn't perfect, as long as you keep trying to get better!



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
