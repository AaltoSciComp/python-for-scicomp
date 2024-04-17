===============================
Python for Scientific Computing
===============================

.. admonition:: Attending the course 22-25.november.2022?

   `See the course page here
   <https://scicomp.aalto.fi/training/scip/python-for-scicomp-2022/>`__.
   Whether you are or aren't, the course material is below.

Python is a modern, object-oriented programming language, which has
become popular in several areas of software development. This course
discusses how Python can be utilized in scientific computing. The
course starts by introducing some of the main Python tools for
computing: Jupyter for interactive analysis, NumPy and SciPy for
numerical analysis, matplotlib for visualization, and so on.  In
addition, it talks about *how* python is used:
related scientific libraries, reproducibility, and the broader
ecosystem of science in Python, because your work is more than the raw
code you write.

This course (like any course) can't teach you Python... it can show
your some examples, let you see how experts do things, and prepare you
to learn yourself as you need to.

.. _prerequisites:

.. prereq::

   - Knowing basic Python syntax.  We assume that you can do some
     Python programming, but not much more that that.  We don't cover
     standard Python programming. `Here a short course on basic Python 
     syntax, with further references <https://coderefinery.github.io/data-visualization-python/python-basics/>`__.
   - Watch or read the `command line crash course
     <https://scicomp.aalto.fi/scicomp/shell/>`__, if you aren't
     familiar.
   - You should be able to use a text editor to edit files some.
   - The :doc:`software installation <installation>` described below
     (basically, anaconda).

   These are not prerequisites:

   - Any external libraries, e.g. numpy
   - Knowing how to make scripts or use Jupyter


.. admonition:: Videos

   Videos from the 2021 instance of this course can be found in
   `this YouTube playlist <https://www.youtube.com/playlist?list=PLZLVmS9rf3nOS7bHNmbcDoyTnMYaz_TJW>`__.


.. csv-table::
   :widths: auto
   :delim: ;

   (prereq) ; :doc:`python`
   30 min   ; :doc:`jupyter`
   60 min   ; :doc:`numpy` or :doc:`numpy-advanced`
   60 min   ; :doc:`pandas`
   60 min   ; :doc:`data-visualization`
   30 min   ; :doc:`data-formats`
   60 min   ; :doc:`scripts`
   30 min   ; :doc:`web-apis`
   15 min   ; :doc:`scipy`
   30 min   ; :doc:`libraries`
   45 min   ; :doc:`parallel`
   30 min   ; :doc:`dependencies`
   30 min   ; :doc:`binder`
   60 min   ; :doc:`packaging`


.. toctree::
   :maxdepth: 1
   :caption: The lesson
   :hidden:

   python
   jupyter
   numpy
   numpy-advanced
   pandas
   data-visualization
   data-formats
   scripts
   web-apis
   scipy
   libraries
   parallel
   dependencies
   binder
   packaging

.. toctree::
   :maxdepth: 1
   :caption: Reference

   installation
   quick-reference
   exercises
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

Python 3.0 came out in September 2008 and was just slightly different
enough that most code had to be changed, which meant that many
projects ignored it for many years.  It was about 3-5 years until the
differences were reduced enough (and better transition plans came out,
so that it was reasonable to use a single code for both versions) that
it become more and more adopted in the scientific community.  Python 2
finally became unsupported in 2020, and by now Python 3 is the defacto
standard.

At this point, all new projects should use Python 3, and existing
actively developed projects should be upgraded to use it.  Still, you
might find some old unmaintained tools that are only compatible with
Python 2.



Credits
=======

This course was originally designed by Janne Blomqvist.

In 2020 it was completely redesigned by a team of the following:

* Authors: Radovan Bast, Richard Darst, Anne Fouilloux, Thor Wikfeldt, ...
* Editor:
* Testers and advisors: Enrico Glerean

We follow The Carpentries Code of Conduct: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html


See also
========

* `High Performance Data Analytics in Python
  <https://enccs.github.io/HPDA-Python/>` is a logical follow-up to
  this lesson that goes more in-depth to tools of high-performance
  and large-scale Python.
