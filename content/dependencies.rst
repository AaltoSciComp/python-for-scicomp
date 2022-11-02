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

- PyPI is traditionally for Python-only packages but it is no problem to also
  distribute packages written in other languages as long as they provide a
  Python interface.

- Conda is more general and while it contains many Python packages and packages
  with a Python interface, it is often used to also distribute packages which
  do not contain any Python (e.g. C or C++ packages).

- Many libraries and tools are distributed in both ecosystems.


In the packaging episode we will meet PyPI and Anaconda again and practice how
to share Python packages.


Creating isolated environments
------------------------------

Isolated environments solve a couple of problems:

- You can install specific, also older, versions into them.

- You can create one for each project and no problem if the two projects
  require different versions.

- If you make some mistake and install something you did not want or need, you
  can remove the environment and create a new one.



Exercises 2
-----------

.. challenge:: Dependencies-2 (15 min)

   .. highlight:: console

  Chloe just joined your team and will be working on her Master Thesis. She is
  quite familiar with Python, still finishing some Python assignments (due in a
  few weeks) and you give her a Python code for analyzing and plotting your
  favorite data. The thing is that your Python code has been developed by
  another Master Student (from last year) and requires a pretty old version of
  Numpy (1.13.1) and Matplotlib (2.2.2) (otherwise the code fails). The code
  could probably work with a recent version of Python but has been validated with
  Python 3.6 only. Having no idea what the code does, she decides that the best
  approach is to **create an isolated environment** with the same dependencies used
  previously. This will give her a baseline for future upgrade and
  developments.

  For this first exercise, we will be using conda for creating an isolated environment.

  1. Create a conda environment::

     $ conda create --name python36-env python=3.6 numpy=1.13.1 matplotlib=2.2.2

  Conda environments can also be managed (create, update, delete) from the
  **anaconda-navigator**. Check out the corresponding documentation `here
  <https://docs.anaconda.com/anaconda/navigator/getting-started/#navigator-managing-environments>`_.

  2. Activate the environment::

     $ conda activate python36-env

     .. callout:: conda activate versus source activate

        If you do not have a recent version of Anaconda or anaconda has not been
        setup properly, you may encounter an error. With older version of anaconda,
        you can try::

          $ source activate python36-env

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
     sure they are different from **python36-env**.

  There is no need to specify the conda environment when using deactivate. It
  deactivates the current environment.

  .. callout:: Remark

    - Sometimes the package version you would need does not seem to be
      available. You may have to select another `conda channel
      <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>`_
      for instance `conda-forge <https://conda-forge.org/>`_. Channels can then
      be indicated when installing a package::

      $ conda install -c conda-forge matplotlib=2.2.0

    - We will see below that rather than specifying the list of dependencies as
      argument of ``conda create``, it is recommended to record dependencies in
      a file.



Exercises 3
-----------

.. challenge:: Dependencies-3 (15 min, optional)

  This is the same exercise as before but we use virtualenv rather than conda.


  1. Create a venv::

     $ python -m venv scicomp

     Here ``scicomp`` is the name of the virtual environment. It creates a new
     folder called ``scicomp``.

  2. Activate it. To activate your newly created virtual environment locate the
     script called ``activate`` and execute it.

     - **Linux/Mac-OSX**: look at ``bin`` folder in the ``scicomp`` folder::

	$ source scicomp/bin/activate

     - **Windows**: most likely you can find it in the ``Scripts`` folder.

  3. Install Numpy 1.13.1 and Matplotlib 2.2.2 into the virtual environment::

     $ pip install numpy==1.13.1
     $ pip install matplotlib==2.2.2

  4. Deactivate it::

     $ deactivate


Recording dependencies
----------------------

There are two standard ways to record dependencies for Python projects.:

Using a ``requirements.txt`` (used by virtual environment) file which
looks like this::

   numpy
   matplotlib
   pandas
   scipy

Or using an ``environments.yml`` (for conda) file which looks like this:

.. code-block:: yaml

   name: my-environment

   dependencies:
     - numpy
     - matplotlib
     - pandas
     - scipy

But all of these dependencies evolve so before publishing our work
it can be very useful for future generations and for the future you
to **pin dependencies** to versions.

Here are the two files again, but this time with versions pinned:

``requirements.txt`` with versions::

   numpy==1.19.2
   matplotlib==3.3.2
   pandas==1.1.2
   scipy==1.5.2

``environments.yml`` with versions:

.. code-block:: yaml

   name: my-environment

   dependencies:
     - python=3.6
     - numpy=1.19.2
     - matplotlib=3.3.2
     - pandas=1.1.2
     - scipy=1.5.2

- Conda can also read and write ``requirements.txt``.
- ``requirements.txt`` can also refer to packages on Github.
- ``environments.yml`` can also contain a ``pip`` section.
- See also: https://coderefinery.github.io/reproducible-research/03-dependencies/#dependencies.



Dependencies 4
--------------

.. challenge:: Dependencies-4 (15 min)

  - Create the file ``environment.yml`` or ``requirements.txt``

  - Create an environment based on these dependencies:
     - Conda: ``$ conda create --name myenvironment --file requirements.txt``
     - Virtual environment: First create and activate, then ``$ pip install -r requirements.txt``

  - Freeze the environment:
     - Conda: ``$ conda list --export > requirements.txt`` or ``$ conda env export > environment.yml``
     - Virtual environment: ``$ pip freeze > requirements.txt``

  - Have a look at the generated ("frozen") file.


Tip: instead of installing packages with ``$ pip install somepackage``, what I do is
to add ``somepackage`` to ``requirements.txt`` or ``environment.yml`` and install
from the file, then you have a trace of all installed dependencies.


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

Other resources:

- https://scicomp.aalto.fi/scicomp/packaging-software/


.. keypoints::

   - Install dependencies by first recording them in ``requirements.txt`` or
     ``environment.yml`` and install using these files, then you have a trace.
   - Use isolated environments and avoid installing packages system-wide.
