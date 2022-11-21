.. _dependency_management:

Dependency management
=====================

.. questions::

   - Do you expect your code to work in one year?  Five?  What if it
     uses ``numpy`` or ``tensorflow`` or ``random-github-package`` ?
   - How can my collaborators get the same results as me? What about
     future me?
   - How can my collaborators easily install my codes with all the necessary dependencies?
   - How can I make it easy for my colleagues to reproduce my results?
   - How can I work on two (or more) projects with different and conflicting dependencies?

.. objectives::

   - Learn how to record dependencies
   - Be able to communicate the dependencies as part of a report/thesis/publication
   - Learn how to use isolated environments for different projects
   - Simplify the use and reuse of scripts and projects


How do you track dependencies of your project?
----------------------------------------------

* **Dependency**: Reliance on a external component.  In this case, a
  separately installed software package such as ``numpy``.



Exercises 1
-----------

.. challenge:: Dependencies-1 (15 min)

  Please discuss **in breakout rooms** and answer via **collaborative document** the
  following questions:

  - How do you install Python packages (libraries) that you use in your work?
    From PyPI using pip? From other places using pip? Using conda?
  - How do you track/record the dependencies? Do you write them into a file or README? Into
    ``requirements.txt`` or ``environment.yml``?
  - If you track dependencies in a file, why do you do this?
  - Have you ever experienced that a project needed a different version of a Python
    library than the one on your computer? If yes, how did you solve it?


.. _pypi:

PyPI (The Python Package Index) and (Ana)conda
----------------------------------------------

- PyPI (The Python Package Index) and Conda are popular packaging/dependency
  management tools.

- When you run ``pip install`` you typically install from `PyPI
  <https://pypi.org/>`__ but one can also ``pip install`` from a GitHub
  repository and similar.

- When you run ``conda install`` you typically install from `Anaconda Cloud
  <https://anaconda.org/>`__ but there are many community-driven conda channels
  and you can create your own.


Why are there two ecosystems?


.. admonition:: PyPI

   - **Installation tool:** ``pip``
   - **Summary:** PyPI is traditionally used for Python-only packages or
     for Python interfaces to external libraries. There are also packages
     with bundled external libraries (such as numpy).
   - **Amount of packages:** Huge number. Old versions are supported for
     a long time.
   - **How libraries are handled:** If your code depends on external
     libraries or tools, these things need to be either included in the
     pip-package or provided via some other installation system (like
     operating system installer or manual installation).
   - **Pros:**
       - Easy to use
       - Package creation is easy
   - **Cons:**
       - Installing packages that need external libraries can be complicated

.. admonition:: Conda

   - **Installation tool:** ``conda`` or ``mamba``
   - **Summary:** Conda aims to be a more general package distribution tool
     and it tries to provide not only the Python packages, but also libraries
     and tools needed by the Python packages. Most scientific software written
     in Python uses external libraries to speed up calculations and installing
     these libraries can often become complicated without conda.
   - **Amount of packages:** Most popular packages are provided. Other packages
     can be installed via pip.
   - **How libraries are handled:** Required libraries are installed as separate
     conda packages.
   - **Pros:**
       - Quite easy to use
       - Easier to manage packages that need external libraries
   - **Cons:**
       - Package creation is harder

.. solution:: Anaconda vs. miniconda vs. conda vs. mamba vs. Anaconda Cloud vs. conda-forge

  - `Anaconda <https://www.anaconda.com/>`__ - a distribution of conda packages
    made by Anaconda Inc.. It is free for academic and non-commercial use.
  - `Miniconda <https://conda.io/miniconda.html>`__ - a minimal installer for conda.
  - `conda <https://conda.io/>`__ - a package and environment management system
    used by Anaconda. It is an open source project maintained by Anaconda Inc..
  - `mamba <https://mamba.readthedocs.io/en/latest/index.html>`__ - a drop in
    replacement for conda that does installations faster.
  - `Anaconda Cloud <https://anaconda.org/>`__ - a package cloud maintained by
    Anaconda Inc. It is a free repository that houses conda package channels.
  - `Conda-forge <https://conda-forge.org/>`__ - the largest open source
    community channel.

In the packaging episode we will meet PyPI and Anaconda again and practice how
to share Python packages.


Creating isolated environments
------------------------------

Isolated environments solve a couple of problems:

- You can install specific, also older, versions of packages into them.

- You can create one environment for each project and you won't encounter any
  problems if the two projects require different versions of packages.

- If you make some mistake and install something you did not want or need, you
  can remove the environment and create a new one.

- You can export a list of packages in an environment and share it with your
  code. This makes replicating your results easier.


Exercises 2
-----------

.. challenge:: Dependencies-2 (15 min)

   .. highlight:: console

  Chloe just joined your team and will be working on her Master Thesis. She is
  quite familiar with Python, still finishing some Python assignments (due in a
  few weeks) and you give her a Python code for analyzing and plotting your
  favorite data. The thing is that your Python code has been developed by
  another Master Student (from last year) and requires a older version of
  Numpy (1.18.1) and Matplotlib (3.1.3) (otherwise the code fails). The code
  could probably work with a recent version of Python but has been validated with
  Python 3.7 only. Having no idea what the code does, she decides that the best
  approach is to **create an isolated environment** with the same dependencies
  that were used previously. This will give her a baseline for future upgrade and
  developments.

  For this first exercise, we will be using conda for creating an isolated environment.

  1. Create a conda environment::

     $ conda create --name python37-env python=3.7 numpy=1.18.1 matplotlib=3.1.3

  Conda environments can also be managed (create, update, delete) from the
  **anaconda-navigator**. Check out the corresponding documentation `here
  <https://docs.anaconda.com/anaconda/navigator/getting-started/#navigator-managing-environments>`_.

  2. Activate the environment::

     $ conda activate python37-env

     .. callout:: conda activate versus source activate

        If you do not have a recent version of Anaconda or anaconda has not been
        setup properly, you may encounter an error. With older version of anaconda,
        you can try::

          $ source activate python37-env

  3. Open a Python console and check that you have effectively the right version for each package::

      import numpy
      import matplotlib

      print('Numpy version: ', numpy.__version__)
      print('Matplotlib version: ', matplotlib.__version__)

     Or use the one-liner if you have access to a terminal like bash

     python -c "import numpy; print(numpy.__version__)"
     python -c "import matplotlib;print(matplotlib.__version__)"

  4. Deactivate the environment::

     $ conda deactivate

  5. Check Numpy and Matplotlib versions in the default environment to make
     sure they are different from **python37-env**.

  There is no need to specify the conda environment when using deactivate. It
  deactivates the current environment.

  .. callout:: Remark

    - Sometimes the package version you would need does not seem to be
      available. You may have to select another `conda channel
      <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>`_
      for instance `conda-forge <https://conda-forge.org/>`_. Channels can then
      be indicated when installing a package::

      $ conda install -c conda-forge matplotlib=3.1.3

    - We will see below that rather than specifying the list of dependencies as
      argument of ``conda create``, it is recommended to record dependencies in
      a file.



Exercises 3
-----------

.. challenge:: Dependencies-3 (15 min, optional)

  This is the same exercise as before but we use virtualenv rather than conda.


  1. Create a venv::

     $ python3 -m venv scicomp

     Here ``scicomp`` is the name of the virtual environment. It creates a new
     folder called ``scicomp``.

  2. Activate it. To activate your newly created virtual environment locate the
     script called ``activate`` and execute it.

     - **Linux/Mac-OSX**: look at ``bin`` folder in the ``scicomp`` folder::

       $ source scicomp/bin/activate

     - **Windows**: most likely you can find it in the ``Scripts`` folder.

  3. Install Numpy 1.18.1 and Matplotlib 3.1.3 into the virtual environment::

     $ pip install numpy==1.18.1
     $ pip install matplotlib==3.1.3

  4. Deactivate it::

     $ deactivate

Problems that might happen with manual installation
---------------------------------------------------

Running the install commands manually can result in unexpected behaviour
such as:

- The installer might remove an already installed packages or update them.
- The installer might not find a package that works with already installed packages.

The reason for this is that the installer does not know what commands
you ran in the past. It only knows the state of your environment and what
you're currently telling it to install.

For example, check what version of ``scipy`` you'll get if you run

.. code-block:: shell

  $ pip install scipy

or

.. code-block:: shell

  $ conda install scipy

Depending on your environment you can get ``scipy`` with versions from
``1.6.2`` with no numpy upgrade to ``1.9.3`` with automatic numpy upgrade.

These kinds of problems can be mitigated by recording dependencies in an
``environment.yml`` or ``requirements.txt``.

Recording dependencies
----------------------

There are two standard ways to record dependencies for Python projects:
``requirements.txt`` and ``environment.yml``.

``requirements.txt`` (used by virtual environment) is a simple
text file which looks like this::

   numpy
   matplotlib
   pandas
   scipy

``environments.yml`` (for conda) is a yaml-file which looks like this:

.. code-block:: yaml

   name: my-environment
   channels:
     - defaults
   dependencies:
     - numpy
     - matplotlib
     - pandas
     - scipy

If you need to recreate the exact same environment later on, it can be very
useful to **pin dependencies** to certain versions. For example, there
is usually a delay between doing research and that research being published.
During this time the dependencies might update and reviewers or interested
researchers might not be able to replicate your results or run your code.

Here are the two files again, but this time with versions pinned:

``requirements.txt`` with versions::

    numpy==1.18.1
    matplotlib==3.1.3
    pandas==1.1.2
    scipy==1.6.2

``environments.yml`` with versions:

.. code-block:: yaml

    name: my-environment
    channels:
      - defaults
    dependencies:
      - python=3.7
      - numpy=1.18.1
      - matplotlib=3.1.3
      - pandas=1.1.2
      - scipy=1.6.2

- Conda can also read and write ``requirements.txt``.
- ``requirements.txt`` can also refer to packages on Github.
- ``environments.yml`` can also contain a ``pip`` section.
- See also: https://coderefinery.github.io/reproducible-research/03-dependencies/#dependencies.

.. admonition:: Putting too strict requirements can be counter-productive

  Putting exact version numbers can be good for single-use applications,
  like replicating a research paper, but it is usually bad for long-term
  maintenance because the program won't update at the same time as it's
  requirements do.

  If you're creating a library, adding strict dependencies can also create
  a situation where the library cannot coexist with another library.

Dependencies 4
--------------

.. challenge:: Dependencies-4 (15 min)

  - Create the file ``environment.yml`` or ``requirements.txt``

  - Create an environment based on these dependencies:
     - Conda: ``$ conda env create --file environment.yml``
     - Virtual environment: First create and activate, then ``$ pip install -r requirements.txt``

  - Freeze the environment:
     - Conda: ``$ conda env export > environment.yml``
     - Virtual environment: ``$ pip freeze > requirements.txt``

  - Have a look at the generated ("frozen") file.

.. admonition:: Hint: Updating packages from dependency files

  Instead of installing packages with ``$ pip install somepackage``,
  you can add ``somepackage`` to ``requirements.txt`` and re-run
  ``$ pip install -r requirements.txt``.

  With conda, you can add the package to ``environment.yml`` and
  run ``$ conda env update --file environment.yml``


How to communicate the dependencies as part of a report/thesis/publication
--------------------------------------------------------------------------

Each notebook or script or project which depends on libraries should come with
either a ``requirements.txt`` or a ``environment.yml``, unless you are creating
and distributing this project as Python package (see next section).

- Attach a ``requirements.txt`` or a ``environment.yml`` to your thesis.
- Even better: put ``requirements.txt`` or a ``environment.yml`` in your Git repository along your code.
- Even better: also binderize your analysis pipeline (more about that in a later session).


.. _version_pinning:

Version pinning for package creators
------------------------------------

We will talk about packaging in a different session but when you create a library and package
projects, you express dependencies either in ``setup.py`` or ``pyproject.toml``
(PyPI) or ``meta.yaml`` (conda).

These dependencies will then be used by either other libraries (who in turn
write their own ``setup.py`` or ``pyproject.toml`` or ``meta.yaml``) or by
people directly (filling out ``requirements.txt`` or a ``environment.yml``).

Now as a library creator you have a difficult choice. You can either pin versions very
narrowly like here (example taken from ``setup.py``):

.. code-block:: python
   :emphasize-lines: 3-6

   # ...
   install_requires=[
      'numpy==1.19.2',
      'matplotlib==3.3.2'
      'pandas==1.1.2'
      'scipy==1.5.2'
   ]
   # ...

or you can define a range or keep them undefined like here (example taken from
``setup.py``):

.. code-block:: python
   :emphasize-lines: 3-6

   # ...
   install_requires=[
      'numpy',
      'matplotlib'
      'pandas'
      'scipy'
   ]
   # ...

Should we pin the versions here or not?

- Pinning versions here would be good for reproducibility.

- However pinning versions may make it difficult for this library to be used in a project alongside other
  libraries with conflicting version dependencies.

- Therefore **as library creator make the version requirements as wide as possible**.

  - Set minimum version when you know of a reason: ``>=2.1``

  - Sometimes set maximum version to next major version (``<4``) (when
    you currently use ``3.x.y``) when you expect issues with next
    major version.

- As the "end consumer" of libraries, define your dependencies as narrowly as possible.


See also
--------

Other tools for dependency management:

- `Poetry <https://python-poetry.org/>`__: dependency management and packaging
- `Pipenv <https://pipenv.pypa.io/>`__: dependency management, alternative to Poetry
- `pyenv <https://github.com/pyenv/pyenv>`__: if you need different Python versions for different projects
- `micropipenv <https://github.com/thoth-station/micropipenv>`__: lightweight tool to "rule them all"
- `mamba <https://mamba.readthedocs.io/en/latest/index.html>`__: a drop in replacement for
  conda that does installations faster.
- `miniforge & mambaforge <https://github.com/conda-forge/miniforge>`__: Miniconda alternatives with
  conda-forge as the default channel and optionally mamba as the default installer.

Other resources:

- https://scicomp.aalto.fi/scicomp/packaging-software/


.. keypoints::

   - Install dependencies by first recording them in ``requirements.txt`` or
     ``environment.yml`` and install using these files, then you have a trace.
   - Use isolated environments and avoid installing packages system-wide.
