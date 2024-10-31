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

.. challenge:: Dependencies-1: Discuss dependency management (5 min)

  Please discuss and answer via **collaborative document** the
  following questions:

  - How do you install Python packages (libraries) that you use in your work?
    From PyPI using pip? From other places using pip? Using conda?
  - How do you track/record the dependencies? Do you write them into a file or README? Into
    ``requirements.txt`` or ``environment.yml``?
  - If you track dependencies in a file, why do you do this?
  - Have you ever experienced that a project needed a different version of a Python
    library than the one on your computer? If yes, how did you solve it?


.. _pypi:

PyPI (The Python Package Index) and conda ecosystem
---------------------------------------------------

PyPI (The Python Package Index) and conda are popular packaging/dependency
management tools:

- When you run ``pip install`` you typically install from `PyPI
  <https://pypi.org/>`__, but you can also ``pip install`` from a GitHub
  repository and similar.

- When you run ``conda install`` you typically install from `Anaconda Cloud
  <https://anaconda.org/>`__ where there are conda channels maintained
  by Anaconda Inc. and by various communities.


Why are there two ecosystems?


.. admonition:: PyPI

   - **Installation tool:** ``pip``
   - **Summary:** PyPI is traditionally used for Python-only packages or
     for Python interfaces to external libraries. There are also packages
     that have bundled external libraries (such as numpy).
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
   - **Amount of packages:** Curated list of packages in defaults-channel, huge
     number in community managed channels. Other packages can be installed via pip.
   - **How libraries are handled:** Required libraries are installed as separate
     conda packages.
   - **Pros:**
       - Quite easy to use
       - Easier to manage packages that need external libraries
   - **Cons:**
       - Package creation is harder


Conda ecosystem explained
-------------------------

.. warning::

   Anaconda has recently changed its licensing terms, which affects its
   use in a professional setting. This caused uproar among academia
   and Anaconda modified their position in
   `this article <https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research>`__.

   Main points of the article are:

   - conda (installation tool) and community channels (e.g. conda-forge)
     are free to use.
   - Anaconda repository and **Anaconda's channels in the community repository**
     are free for universities and companies with fewer than 200 employees.
     Non-university research institutions and national laboratories need
     licenses.
   - Miniconda is free, when it does not download Anaconda's packages.
   - Miniforge is not related to Anaconda, so it is free.

   For ease of use on sharing environment files, we recommend using
   Miniforge to create the environments and using conda-forge as the main
   channel that provides software.

- Package repositories:

  - `Anaconda Community Repository (anaconda.org) <https://anaconda.org/>`__
    aka. Anaconda Cloud is a package cloud maintained by Anaconda Inc.
    It is a repository that houses mirrors of Anaconda's channels and
    community maintained channels.
  - `Anaconda Repository (repo.anaconda.com) <https://repo.anaconda.com>`__
    houses Anaconda's own proprietary software channels.

- Major package channels:

  - Anaconda's proprietary channels: ``main``, ``r``, ``msys2`` and ``anaconda``.
    These are sometimes called ``defaults``.
  - `conda-forge <https://conda-forge.org/>`__ is the largest open source
    community channel. It has over 27,000 packages that include open-source
    versions of packages in Anaconda's channels.

- Package distributions and installers:

  - `Anaconda <https://www.anaconda.com/>`__ is a distribution of conda packages
    made by Anaconda Inc.. When using Anaconda remember to check that your
    situation abides with their licensing terms.
  - `Miniconda <https://conda.io/miniconda.html>`__ is a minimal installer
    maintained by Anaconda Inc. that has conda and uses Anaconda's channels
    by default. Check licensing terms when using these packages.
  - `Miniforge <https://github.com/conda-forge/miniforge>`__ is an open-source
    Miniconda replacement that uses conda-forge as the default channel.
    Contains mamba as well.
  - `micromamba <https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html>`__
    is a tiny stand-alone version of the mamba package manager written in C++.
    It can be used to create and manage environments without installing
    base-environment and Python. It is very useful if you want to automate
    environment creation or want a more lightweight tool.

- Package managers:

  - `conda <https://conda.io/>`__ is a package and environment management system
    used by Anaconda. It is an open source project maintained by Anaconda Inc..
  - `mamba <https://mamba.readthedocs.io/en/latest/index.html>`__ is a drop in
    replacement for conda. It used be much faster than conda due to better
    dependency solver but nowadays conda
    `also uses the same solver <https://conda.org/blog/2023-11-06-conda-23-10-0-release/>`__.
    It still has some UI improvements.

Exercises 2
-----------

.. challenge:: Dependencies-2: Package language detective (2 min)

   Think about the following sentences:

   1. Yes, you can install my package with pip from GitHub.
   2. I forgot to specify my channels, so my packages came from the defaults.
   3. I have a Miniforge installation and I use mamba to create my environments.

   What hidden information is given in these sentences?

   .. solution::

     1. The package is provided as a pip package. However, it is most likely
        not uploaded to PyPI as it needs to be installed from a repository.
     2. In this case the person saying the sentence is most likely using
        Anaconda or Miniconda because these tools use the ``defaults``-channel
        as the default channel. They probably meant to install software from
        conda-forge, but forgot to specify the channel.
     3. Miniforge uses conda-forge as the default channel. So unless some
        other channel has been specified, packages installed with these
        tools come from conda-forge as well.

Python environments
-------------------

An **environment** is a basically a folder that contains a Python
interpreter and other Python packages in a folder structure similar
to the operating system's folder structure.

These environments can be created by the
`venv-module <https://docs.python.org/3/library/venv.html>`__ in base
Python, by a pip package called
`virtualenv <https://virtualenv.pypa.io/en/latest/>`_
or by conda/mamba.

Using these environments is highly recommended because they solve the
following problems:

- Installing environments won't modify system packages.

- You can install specific versions of packages into them.

- You can create an environment for each project and you won't encounter any
  problems if different projects require different versions of packages.

- If you make some mistake and install something you did not want or need, you
  can remove the environment and create a new one.

- Others can replicate your environment by reusing the same specification
  that you used to create the environment.


Creating Python environments
----------------------------

.. tabs::

  .. group-tab:: Creating conda environment from environment.yml

     Record channels and packages you need to a file called
     ``environment.yml``:

     .. code-block:: yaml

        name: my-environment
        channels:
          - conda-forge
        dependencies:
          - python
          - numpy
          - matplotlib
          - pandas

     The ``name`` describes the name of the environment,
     ``channels``-list tells which channels should be search for packages
     (channel priority goes from top to bottom) and ``dependencies``-list
     contains all packages that are needed.

     Using this file you can now create an environment with:

     .. code-block:: console

        $ conda env create --file environment.yml

     .. admonition:: You can also use mamba

        If you have mamba installed, you can replace conda
        with mamba in each command.

     You can then activate the environment with:

     .. code-block:: console

        $ conda activate my-environment

     .. callout:: conda activate versus source activate

        ``conda activate`` will only work if you have run ``conda init``
        in the past. Running ``conda init`` will make loading environments
        easier as you will always have a conda environment loaded.

        However, this can also cause problems as programs in the
        main environment will be constantly loaded and they might be used
        even when they're not supposed to be used. A common example is
        not having ``pip`` installed in a conda environment which results
        ``pip`` from main environment to be used instead.

     You can then check e.g. installed versions of Python and ``numpy``:

     .. code-block:: console

        $ python -c 'import sys; import numpy; print(f"Python version: {sys.version}\nNumPy version: {numpy.__version__}")'
        Python version: 3.13.0 | packaged by conda-forge | (main, Oct  8 2024, 20:04:32) [GCC 13.3.0]
        NumPy version: 2.1.2

     To deactivate the environment, you can run:

     .. code-block:: console

        $ conda deactivate

  .. group-tab:: Creating virtual environment from requirements.txt

     Record packages you need to a file called
     ``requirements.txt``:

     .. code-block:: txt

        numpy
        matplotlib
        pandas

     This is simply a text file that lists all of the packages that
     you need. It is usually called ``requirements.txt``.

     Now you can create a virtual environment with:

     .. code-block:: console

        $ python -m venv my-environment

     You can then activate the environment by sourcing a file called
     ``activate``.

     - **Linux/Mac OSX**:
       .. code-block:: console

          $ source my-environment/bin/activate

     - **Windows**: most likely you can find it in the Scripts folder.

     Now the environment should be active. You can then install packages
     listed in ``requirements.txt`` with

     .. code-block:: console

        $ python -m pip install -r requirements.txt

     You can then check e.g. installed versions of Python and ``numpy``:

     .. code-block:: console

        $ python -c 'import sys; import numpy; print(f"Python version: {sys.version}\nNumPy version: {numpy.__version__}")'
        Python version: 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0]
        NumPy version: 2.1.2

     To deactivate the environment, you can run:

     .. code-block:: console

        $ deactivate


.. admonition:: Creating environments without environment.yml/requirements.txt

   It is possible to create environments with manual commands, but this
   is highly discouraged for continuous use.

   Firstly, replicating the environment becomes much harder.

   Secondly, running package installation commands manually in an
   environment can result in unexpected behaviour such as:

   - Package manager might remove an already installed packages or update them.
   - Package manager might not find a package that works with already
     installed packages.

   The reason for this behavior is that package managers does not know what
   commands you ran in the past. It only knows the state of your environment
   and what you're currently telling it to install.

   These kinds of problems can be mitigated by recording dependencies in an
   ``environment.yml`` or ``requirements.txt`` and using the relevant
   package manager to update / recreate the environment.


Exercises 3
-----------

.. challenge:: Dependencies-3: Create a Python environment (15 min)

    Use conda or venv to create the environment presented in the
    example.


Adding more packages to existing environments
---------------------------------------------

Quite often when you're creating a new environment you might forget
to add all relevant packages to ``environment.yml`` or
``requirements.txt``.

In these cases the best practice is to add missing packages to
``environment.yml`` or ``requirements.txt`` and to update the environment.

.. tabs::

   .. group-tab:: Adding new packages to a conda environment

      Add new packages that you want to install to
      ``dependencies`` in
      ``environment.yml``.

      Afterwards, run

      .. code-block:: console

         $ conda env update --file environment.yml

      to update the environment.

   .. group-tab:: Adding new packages to a virtual environment

      Add new packages that you want to install to
      ``requirements.txt``.

      Afterwards, activate the environment and re-run

      .. code-block:: console

         $ pip install -r requirements.txt

      to update the environment.

Sometimes the new packages are incompatible with the ones already
in the environment. Maybe they have different dependencies that are
not satisfied with the current versions, maybe the package you're installing
is incompatible with the ones installed. In these cases the safest approach
is to re-create the environment. This will let the dependency solvers
to start from clean slate and with a full picture of what packages
need to be installed.


Pinning package versions
------------------------

Sometimes your code will only work with a certain range of dependencies.
Maybe you use a function or a class that was introduced in a later version
or a newer version has modified its API.

In these situations, you'll want to **pin the package versions**.

For example, there is usually a delay between doing research and that
research being published. During this time packages used in the research
might update and reviewers or interested researchers might not be able
to replicate your results or run your code if new versions are not
compatible.

.. tabs::

   .. group-tab:: environment.yml with pinned versions

      When pinning versions in ``environment.yml`` one can use a
      variety of comparison operators:

      .. code-block:: yaml

          name: my-environment
          channels:
            - conda-forge
          dependencies:
            # Use python 3.11
            - python=3.11
            # numpy that is bigger or equal than version 1, but less than version 2
            - numpy>=1,<2
            # matplotlib greater than 3.8.2
            - matplotlib>3.8.2
            # pandas that is compatible with 2.1
            - pandas~=2.1

   .. group-tab:: requirements.txt with pinned versions

      When pinning versions in ``requirements.txt`` one can use a
      variety of comparison operators:

      .. code-block:: txt

          # numpy that is bigger or equal than version 1, but less than version 2
          numpy>=1,<2
          # matplotlib greater than 3.8.2
          matplotlib>3.8.2
          # pandas that is compatible with 2.1
          pandas~=2.1

For more information on all possible specifications, see
`this page <https://packaging.python.org/en/latest/specifications/version-specifiers/>`__
from Python's packaging guide.

See also: https://coderefinery.github.io/reproducible-research/dependencies/

.. admonition:: To pin or not to pin? That is the question.

  Pinning versions means that you pin the environment to
  **that instance in time** when these specific versions of the
  dependencies were being used.

  This can be good for single-use applications, like replicating a research
  paper, but it is usually bad for the long-term maintainability of the software.

  Pinning to major versions or to compatible versions is usually the best
  practice as that allows your software to co-exist with other packages even
  when they are updated.

  Remember that at some point in time you **will** face a situation where
  newer versions of the dependencies are no longer compatible with your
  software. At this point you'll have to update your software to use the newer
  versions or to lock it into a place in time.


Exporting package versions from an existing environment
-------------------------------------------------------

Sometimes you want to create a file that contains the exact versions
of packages in the environment. This is often called *exporting* or
*freezing* and environment.

Doing this will create a file that does describe the installed
packages, but it won't tell which packages are **the most important
ones** and which ones are just dependencies for those packages.

Using manually created ``environment.yml`` or ``requirements.txt``
are in most cases better than automatically created ones because they
shows which packages are the important packages needed by the software.

.. tabs::

   .. group-tab:: Exporting environment.yml from a conda environment

     Once you have activated the environment, you can run

     .. code-block:: console

       $ conda env export > environment.yml

     If package build versions are not relevant for the use case,
     one can also run

     .. code-block:: console

       $ conda env export --no-builds > environment.yml

     which leaves out the package build versions.

     Alternatively one can also run

     .. code-block:: console

       $ conda env export --from-history > environment.yml

     which creates the ``environment.yml``-file based on
     what packages were asked to be installed.

     .. admonition:: conda-lock

       For even more reproducibility, you should try out
       `conda-lock <https://github.com/conda/conda-lock>`__.
       It turns your ``environment.yml`` into a ``conda.lock``
       that has all information needed to **exactly** create
       the same environment. You can use ``conda.lock``-files
       in same way as ``environment.yml`` when you create
       an environment:

       .. code-block:: console

          $ conda env create --file conda.lock

   .. group-tab:: Exporting requirements.txt from a virtual environment

     Once you have activated the environment, you can run

     .. code-block:: console

        $ pip freeze > requirements.txt



Exercise 4
----------

.. challenge:: Dependencies-4: Export an environment (15 min)

   Export the environment you previously created.


Additional tips and tricks
--------------------------

.. tabs::

   .. group-tab:: Creating a conda environment from requirements.txt

      conda supports installing an environment from ``requirements.txt``.

      .. code-block:: console

        $ conda env create --name my-environment --channel conda-forge --file requirements.txt

      To create an ``environment.yml`` from this environment that mimics
      the ``requirements.txt``, activate it and run

     .. code-block:: console

       $ conda env export --from-history > environment.yml

   .. group-tab:: Adding pip packages into conda environments

      conda supports installing pip packages in an ``environment.yml``.

      Usually this is done to add those packages that are missing
      from conda channels.

      To do this you'll want to install ``pip`` into the environment
      and then add pip-installed packages to a list called ``pip``.

      See this example ``environment.yml``:

      .. code-block:: yaml

         name: my-environment
         channels:
           - conda-forge
         dependencies:
           - python
           - pip
           - pip:
             - numpy
             - matplotlib
             - pandas

      One can even add a full ``requirements.txt`` to the environment:

      .. code-block:: yaml

         name: my-environment
         channels:
           - conda-forge
         dependencies:
           - python
           - pip
           - pip:
             - "-r requirements.txt"

      Do note that in both methods the pip-packages come from PyPI
      and not from conda channels. The installation of these packages
      is done after conda environment is created and this can also
      remove or update conda packages installed previously.

   .. group-tab:: Installing pip packages from GitHub

      Packages available in GitHub or other repositorios
      can be given as a URL in ``requirements.txt``.

      For example, to install a development version of the 
      `black code formatter <https://github.com/psf/black>`__, one can
      write the following ``requirement.txt``.

      .. code-block:: txt

         git+https://github.com/psf/black

      or

      .. code-block:: txt

         https://github.com/psf/black/archive/master.zip

      First one would use git to clone the repository, second would
      download the zip archive of the repository.


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
projects, you express dependencies either in ``pyproject.toml`` (or ``setup.py``)
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
- `miniforge <https://github.com/conda-forge/miniforge>`__: Miniconda alternative with
  conda-forge as the default channel and optionally mamba as the default installer.
- `micromamba <https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html>`__:
  tiny version of Mamba as a static C++ executable. Does not need base environment or
  Python for installing an environment.

Other resources:

- https://scicomp.aalto.fi/scicomp/packaging-software/


.. keypoints::

   - Install dependencies by first recording them in ``requirements.txt`` or
     ``environment.yml`` and install using these files, then you have a trace.
   - Use isolated environments and avoid installing packages system-wide.
