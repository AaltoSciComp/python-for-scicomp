===============================
Python for Scientific Computing
===============================

.. admonition:: Attending the course 14-23.sep?

   `See the course page here
   <https://scicomp.aalto.fi/training/scip/python-for-scicomp/>`__,
   below is the course material.

Python is a modern, object-oriented programming language, which has
become popular in several areas of software development. This course
discusses how Python can be utilized in scientific computing. The
course starts by introducing the main Python package for numerical
computing, NumPy, and discusses then SciPy toolbox for various
scientific computing tasks as well as visualization with the
Matplotlib package.  In addition, it talks about *how* python is used:
related scientific libraries, reproducibility, and the broader
ecosystem of science in Python.

This course (like any course) can't teach you Python... it can show
your some examples, let you see how experts do things, and prepare you
to learn yourself as you need to.

.. _prerequisites:

.. prereq::

   - Knowing basic Python syntax.  We assume that you can do some
     Python programming, but not much more that that.  We don't cover
     standard Python programming.
   - Watch or read the `command line crash course
     <https://scicomp.aalto.fi/scicomp/shell/>`__, if you aren't
     familiar.
   - You should be able to use a text editor to edit files some.
   - The :doc:`software installation <installation>` described below
     (basically, anaconda).

   These are not prerequisites:

   - Any external libraries, e.g. numpy
   - Knowing how to make scripts or use Jupyter



.. csv-table::
   :widths: auto
   :delim: ;

   (prereq) ; :doc:`python`
   30 min   ; :doc:`jupyter`
   60 min   ; :doc:`numpy`
   60 min   ; :doc:`data-visualization`
   60 min   ; :doc:`scripts`
   60 min   ; :doc:`packaging`
   ?? min   ; :doc:`scipy`
   ?? min   ; :doc:`pandas`
   ?? min   ; :doc:`libraries`
   ?? min   ; :doc:`dependencies`
   ?? min   ; :doc:`binder`


.. toctree::
   :maxdepth: 1
   :caption: The lesson
   :hidden:

   python
   jupyter
   numpy
   data-visualization
   scripts
   packaging
   scipy
   pandas
   libraries
   dependencies
   binder

.. toctree::
   :maxdepth: 1
   :caption: Reference

   installation
   quick-reference
   guide


.. _learner-personas:

Who is the course for?
======================

The course is targeted towards these learner personas:

* A is a early career PhD researcher who has been using Python a bit,
  but is not sure what they know or don't know.  They want to be able
  to do their research more efficiently and make sure that they are
  using the right tools.  A may know that numpy exists, etc. and could
  theoretically read some about it themselves, but aren't sure if they
  are going in the right direction.

* A2 can use numpy and pandas, but have learned little bits here and
  there and hasn't had a comprehensive introduction.  They want to
  ensure they are using best practices.  (Baseline of high-level
  packages)

* B is a mid-to-late undergraduate student who has used Python in some
  classes.  They have possibly learned the syntax and enough to use it
  in courses, but in a course-like manner where they are expected to
  create everything themselves.


Motivation
==========

Why Python
----------

Python has become popular, largely due to good reasons. It's very easy
to get started, there's lots of educational material, a huge amount of
libraries for doing everything imaginable.  Particularly in the
scientific computing space, there is the Numpy, Scipy, and matplotlib
libraries which form the basis of almost everything.  Numpy and Scipy
are excellent examples of using Python as a glue language, meaning to
glue together battle-tested and well performing code and present them
with an easy to use interface.  Also machine learning and deep
learning frameworks have embraced python as the glue language of
choice.  And finally, Python is open source, meaning that anybody can
download and install it on their computer, without having to bother
with acquiring a license or such.  This makes it easier to distribute
your code e.g. to collaborators in different universities.


Why not Python for Scientific Computing
---------------------------------------

While Python is extremely popular in scientific computing today, there
are certainly things better left to other tools.

- Implementing performance-critical kernels.  Python is a **very**
  slow language, which often doesn't matter if you can offload the
  heavy lifting to fast compiled code, e.g. by using Numpy array
  operations.  But if what you're trying to do isn't *vectorizable*
  then you're out of luck.  An alternative to Python, albeit much less
  mature and with a smaller ecosystem, but which provides very fast
  generated code, is *Julia*.

- Creating libraries that can be called from other languages.  In this
  case you'll often want to create a library with a C interface, which
  can then be called from most languages.  Suitable languages for this
  sort of task, depending on what you are doing, could be Rust, C,
  C++, or Fortran.

- You really like static typing, or functional programming
  approaches. *Haskell* might be what you're looking for.


Python 2 vs Python 3
--------------------

There are two slightly incompatible versions of Python being used
today, 2 and 3.  Most large projects have supported 3 for a long time
already, and have announced dropping Python 2 support for future
versions (or have already done so), so at this point you should use
version 3 unless you're working on an existing project that for some
reason hasn't yet been ported to version 3.  Accordingly, in this
course we will use Python 3. For more info, see `Python 3
statement <https://python3statement.org/>`_ by many other the major
projects.



Credits
=======

This course was originally designed by Janne Blomqvist.

In 2020 it was completely redesigned by a team of the following:

* Authors: Radovan Bast, Richard Darst, Anne Fouilloux, ...
* Editor:
* Testers and advisors: Enrico Glerean

We follow The Carpentries Code of Conduct: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html

