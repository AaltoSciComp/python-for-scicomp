Packaging
=========

.. questions::

   - How to organize Python projects larger than one script?
   - What is a good file and folder structure for Python projects?
   - How can you make your Python functions most usable by your collaborators?
   - How to prepare your code to make a Python package?
   - How to publish your Python package?

.. objectives::

   - Learn to identify the components of a Python package
   - Learn to create a Python package
   - Learn to publish a Python package


Organizing Python projects
--------------------------

Python projects often start as a single script or Jupyter notebook but
they can grow out of a single file.

In the :ref:`scripts` episode we have also learned how to import functions
and objects from other Python files (modules). Now we will take it a step further.

**Recommendations**:

- Collect related functions into modules (files).
- Collect related modules into packages (we will show how).
- Add a ``LICENSE`` file to your code
  see `Software Licensing and Open source explained with cakes <https://github.com/coderefinery/social-coding/blob/main/licensing-and-cakes.md>`__)
- Write a ``README.md`` file describing what the code does and how to use it.
- It is also recommended to `document your package <https://coderefinery.github.io/documentation/>`__.
- When the project grows, you might need `automated testing <https://coderefinery.github.io/testing/>`__.

To have a concrete example but still simple example, we will create a project
consisting of 3 functions, each in its own file. We can then imagine that each
file would contain many more functions. To make it more interesting,
one of these functions will depend on an external library: ``scipy``.

These are the 3 files:

.. literalinclude:: packaging-example-project/calculator/adding.py
   :caption: adding.py

.. literalinclude:: packaging-example-project/calculator/subtracting.py
   :caption: subtracting.py

.. literalinclude:: packaging-example-project/calculator/integrating.py
   :caption: integrating.py

We will add a fourth file:

.. literalinclude:: packaging-example-project/calculator/__init__.py
   :caption: __init__.py

This ``__init__.py`` file will be the interface of our package/library.
It also holds the package docstring and the version string.
Note how it imports functions from the various modules using *relative imports*
(with the dot).

This is how we will arrange the files in the project folder/repository:

.. code-block:: none
   :emphasize-lines: 3-6

   project-folder
   ├── calculator
   │   ├── adding.py
   │   ├── __init__.py
   │   ├── integrating.py
   │   └── subtracting.py
   ├── LICENSE
   └── README.md

Now we are ready to test the package. For this we need to be in the "root"
folder, what we have called the *project-folder*.  We also need to have
``scipy`` available in our environment:

.. literalinclude:: packaging-example-project/test.py

The package is not yet pip-installable, though. We will make this possible in
the next section.


Testing a local pip install
---------------------------

To make our example package pip-installable we need to add one more file:

.. code-block:: none
   :emphasize-lines: 9

   project-folder
   ├── calculator
   │   ├── adding.py
   │   ├── __init__.py
   │   ├── integrating.py
   │   └── subtracting.py
   ├── LICENSE
   ├── README.md
   └── setup.py

This is how ``setup.py`` looks:

.. literalinclude:: packaging-example-project/setup.py
   :caption: setup.py
   :emphasize-lines: 18-20

Note how our package requires ``scipy`` and we decided to not pin the version
here (see :ref:`version_pinning`).

Now we have all the building blocks to test a local pip install. This is a good
test before trying to upload a package to PyPI or test-PyPI
(see :ref:`pypi`)



Exercises 1
-----------

.. challenge:: Packaging-1

   To test a local pip install:

   - Create a new folder outside of our example project
   - Create a new virtual environment (:ref:`dependency_management`)
   - Install the example package from the project folder
     into the new environment: ``$ pip install /path/to/project-folder/``
   - Test the local installation:

   .. literalinclude:: packaging-example-project/test.py


Sharing packages via PyPI
-------------------------

Once we are able to pip-install the example package locally, we are ready for
upload.

We exercise by uploading to `test-PyPI <https://test.pypi.org/>`__, not the
real `PyPI <https://pypi.org/>`__, so that if we mess things up, nothing bad
happens.

We need two more things:

- We will do this using `Twine <https://twine.readthedocs.io/>`__ so you need
  to pip install that, too.
- You need an account on `test-PyPI <https://test.pypi.org/>`__.

.. highlight:: console

Let's try it out. First we create the distribution package::

  $ python setup.py sdist

We need twine::

  $ pip install twine

And use twine to upload the distribution files to test-PyPI::

  $ twine upload -r testpypi dist/*

  Uploading distributions to https://test.pypi.org/legacy/
  Enter your username:
  Enter your password:

Once this is done, create yet another virtual environment and try to install from test-PyPI (adapt "myname")::

  $ pip install -i https://test.pypi.org/simple/ calculator-myname


Tools that simplify sharing via PyPI
------------------------------------

The solution that we have used to create the example package (using
``setuptools`` and ``twine``) is not the only approach. There are many ways to
achieve this and we avoided going into too many details and comparisons to not
confuse too much. If you web-search this, you will also see that recently the
trend goes towards using ``pyproject.toml`` as more general alternative to
``setup.py``.

There are at least two tools which try to make the packaging and PyPI interaction easier:

- `Poetry <https://python-poetry.org/>`__
- `Flit <https://flit.readthedocs.io/>`__


Building a conda package and share it
-------------------------------------

.. demo::

   Most people will watch and observe this, due to speed which we will
   move.

.. callout:: Prerequisites

  To create a conda package, `conda-build` package is required. You may install it with **Anaconda Navigator** or from the command line::

    $ conda install conda-build


The simplest way for creating a conda package for your python script is to
first publish it in `PyPI <https://pypi.org/>`__ following the steps explained
above.


Building a python package with conda skeleton pypi
***************************************************

Once build, the conda package can be installed locally. For this example, we
will use `runtest <https://pypi.org/project/runtest/>`__.  `runtest
<https://github.com/bast/runtest>`__ is a numerically tolerant end-to-end test
library for research software.

1. Create pypi skeleton::

      $ conda skeleton pypi runtest

   The command above will create a new folder called `runtest` containing a file `meta.yaml`, the conda recipe for `runtest`.

2. Edit `meta.yaml` and update requirements:

   .. code-block:: yaml

      requirements:
        host:
          - pip
          - python
          - flit
        run:
          - python
          - flit

   In the requirements above, we specified what is required for the `host <https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#host>`__ and for `running <https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#run>`__  the package.

   .. callout:: Remark

      For pure python recipes, this is all you need for building a python package with conda.
      If your package needs to be built (for instance compilation), you would need additional files e.g. `build.sh` (to build on Linux/Mac-OSX) and `bld.bat` (to build on Windows systems). You can also add test scripts for testing your package. See `documentation <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html#writing-the-build-script-files-build-sh-and-bld-bat>`__


3. Build your package with conda

   Your package is now ready to be build with conda::

     $ conda-build runtest


   .. callout:: Conda package location

      Look at the messages produced while building. The location of the local conda package is given (search for `anaconda upload`)::

	~/anaconda3/conda-bld/win-64/runtest-2.2.1-py38_0.tar.bz2

      The prefix `~/anaconda3/` may be different on your machine and depending on your operating system (Linux, Mac-OSX or Windows) the sub-folder `win-64` differs too (for instance `linux-64` on Linux machines).

      The conda package we have created is specific to your platform (here `win-64`). It can be converted to other platforms using `conda convert <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html#converting-a-package-for-use-on-all-platforms>`__.

4. Check within new environment

   It is not necessary to create a new conda environment to install it but as explained in previous episode, it is good practice to have isolated environments.

   ::

      $ conda create -n local-runtest --use-local runtest

   We can then check `runtest` has been successfully installed in `local-runtest` conda environment. Open a new Terminal with `local-runtest` environment (either from the command line::

     $ conda activate local-runtest

   or via **Anaconda Navigator** (Open Terminal), import runtest and
   check its version:

   .. code-block:: python

     import runtest
     print(runtest.__version__)


.. callout:: Building a conda package from scratch

  It is possible to build a conda package from scratch without using conda skeleton. We recommend you to check the `conda-build documentation <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html>`__ for more information.

To be able to share and install your local conda package anywhere (on other platforms), you would need to upload it to a `conda channel <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>`__ (see below).



Publishing a python package
***************************

- Upload your package to *Anaconda.org*: see instructions `here
  <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html#optional-uploading-packages-to-anaconda-org>`__.
  Please note that you will have to create an account on Anaconda.

- Upload your package to `conda-forge <https://conda-forge.org/>`__:
  conda-forge is a conda channel: it contains community-led collection of
  recipes, build infrastructure and distributions for the conda package
  manager. Anyone can public conda packages to conda-forge if certain
  `guidelines <https://conda-forge.org/docs/>`__ are respected.

- Upload your package to `bioconda <https://bioconda.github.io/>`_: bioconda is
  a very popular channel for the conda package manager specializing in
  bioinformatics software. As for conda-forge, you need to follow their
  `guidelines <https://bioconda.github.io/contributor/guidelines.html>`__ when
  building conda recipes.

You can also `create your own conda channel
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/create-custom-channels.html>`__
for publishing your packages.


.. keypoints::

   - Organize your code for publishing
   - Pypi
   - conda
