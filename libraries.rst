Library ecosystem
=================

.. questions::

   - Q1
   - Q2

.. objectives::

   - O1
   - O2



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



Core numerics
-------------

* numpy
* scipy



Plotting
--------

* matplotlib
* seaborn
* mayavi
* PIL



Data analysis and other important core packages
-----------------------------------------------

* pandas
* statsmodels
* SymPy
* networkx
* h5py and PyTables
* dateutil and pytz



Interactive computing and human interface
-----------------------------------------
* Interactive computing

  * IPython
  * Jupyter (notebook, lab, hub, ...)

* Testing

  * pytest

* Documentation

  * Sphinx

* Development environments

  * Spyder

* Binder



Interfacing with other languages
--------------------------------

* ctypes
* cython
* f2py
* swig
* Boost.python
* cffi



Speeding up code and parallelism
--------------------------------
* PyMPI
* cython
* numba
* PyPy
* Dask
* Joblib
* IPyParallel
* numexpr



Machine learning
----------------

If you need some machine learning, you probably already know what you
need and this list is short and irrelevant.

- tensorflow
- pytorch
- nltk
- scikit-learn



Your stuff
----------

Every small project you do contributes a little bit to the Python and
SciPy ecosystem.  This course has sort of started you on that path,
and a `CodeRefinery workshop <https://coderefinery.org>` will make
sure you have the tools to produce high-quality, reusable code.



How do you know if you should use something?
--------------------------------------------

Do you trust a random package you find online?  Especially for your
scientific results, which *have* to be correct.  Still, you also
*can't* build everything yourself, so you have to decide what point to
start with.

* Are there releases?  Have they been going on for a while?

* Is there automated testing?

* Is there a community, or is it one person?  Is it backed by some
  organization?  Does it have a permanent home?

* Is it is a public hosting site (GitLab, GitHub, Bitbucket, etc)
  where a community *could* form?

* Do others post issues and make contributions?  Are these issues
  dealt with in a timely manner?  Can you search past bug reports?





See also
--------

* `Topical Software in the SciPy ecosystem
  <https://www.scipy.org/topical-software.html>`__ - relatively
  detailed (but not comprehensive) list of projects


.. keypoints::

   - K1
   - K2
