Dependency management
=====================

.. questions::

   - How can my collaborators get the same results as me?
   - How can I get the same results as the past me?
   - How can my collaborators easily install my codes with all the necessary dependencies?
   - How can make it easy for my colleagues to reproduce my results?
   - How can I work on two (or more projects) with different and conflicting dependencies?

.. objectives::

   - Learn how to record dependencies
   - Be able to communicate the dependencies as part of a report/thesis/publication
   - Learn how to use isolated environments for different projects
   - Simplify the use and reuse of my codes


How do you track dependencies of your project?
----------------------------------------------

.. challenge:: Dependencies-1

  Please discuss via collaborative document the following questions:

  - How do you install Python packages (libraries) that you use in your work?
    From PyPI using pip? From other places using pip? Using conda?
  - How do you track/record the dependencies? Do you write them into a file or README? Into
    ``requirements.txt`` or ``environment.yml``? How do you track this?
  - If you track dependencies in a file, why do you do this?
  - Have you ever experienced that a project needed a different version of a Python
    library than the one on your computer? If yes, how did you solve it?


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


Creating isolated environments
------------------------------

Isolated environments solve a couple of problems:

- You can install specific, also older, versions into them.

- You can create one for each project and no problem if the two projects
  require different versions.

- If you make some mistake and install something you did not want or need, you
  can remove the environment and create a new one.

.. instructor-note::

   Exercise needs some work ...


.. challenge:: Dependencies-2

  Chloe just joined your team and will be working on her Master Thesis. She is quite familiar with Python, still finishing some Python assignments (due in a few weeks) and you give her a python code for analyzing your favorite data. The thing is that your python code has been developed by another Master Student (from last year) and requires a pretty old version of Numpy <= 1.13.x (otherwise your code fails). Having no idea what the code does, she decides that the best approach is to create a virtual environment for running it.

  1. Create a venv

  ::
  
   virtualenv -p python scicomp

  Here **scicomp** is the name of the virtual environment. It creates a new folder called **scicomp**.

   2. Activate it

   To activate your newly created virtual environment locate the script called **activate** and execute it. 

       - **Linux/Mac-OSX**: look at **bin** folder in **scicomp** folder.
       - **Windows**: most likely you can find it in **Scripts** folder.


  3. Install Numpy 1.13.1


  4. Deactivate it
  

.. challenge:: Dependencies-3

  This is the same exercise as before but we use conda rather than venv.

  1. Create a conda environment
  2. Activate it
  3. Install Numpy 1.13.1
  4. Deactivate it


Recording dependencies
----------------------

.. instructor-note::

  Discussion based on https://coderefinery.github.io/reproducible-research/03-dependencies/#dependencies
  (I think we should perhaps copy/condense some and refer to that link?)


.. challenge:: Dependencies-3

  - Write requirements.txt or environment.yml
  - Create an environment based on these
  - Freeze the environment

  Could be nice to have an example that requires a version > Y for a package (such ad matplotlib (3D plotting?).


How to communicate the dependencies as part of a report/thesis/publication
--------------------------------------------------------------------------

Each notebook or script or project which depends on libraries should come with
either a ``requirements.txt`` or a ``environment.yml``, unless you are creating
and distributing this project as Python package (see next section).

- Attach a ``requirements.txt`` or a ``environment.yml`` to your thesis.
- Even better: put ``requirements.txt`` or a ``environment.yml`` in your Git repository along your code.
- Even better: also binderize your analysis pipeline (more about that in a later session).


Version pinning for package creators
------------------------------------

We will talk about packaging in a different session but when you create a library and package
projects, you express dependencies either in ``setup.py`` or ``pyproject.toml``
(PyPI) or ``meta.yaml`` (conda).

These dependencies will then be used by either other libraries (who in turn
write their own ``setup.py`` or ``pyproject.toml`` or ``meta.yaml``) or by
people directly (filling out ``requirements.txt`` or a ``environment.yml``).

Now as a library creator you have a choice. You can either pin versions very
narrowly like here (example taken from ``setup.py``):

.. instructor-note::

   Need to add something here.

or you can define a range or keep them undefined like here (example taken from
``setup.py``):

.. instructor-note::

   Need to add something here.

Should we pin the versions here or not?

- Pinning versions here is good for reproducibility.

- However pinning versions may make it difficult for this library to be used in a project with other
  libraries with conflicting version dependencies.

- Therefore **as library creator make the version requirements as wide as possible**.

- As the "end consumer" of libraries, define your dependencies as narrowly as possible.


Other tools for dependency management
-------------------------------------

.. instructor-note::

  For each of these we should add a link and a sentence summarizing when this
  can be useful.

- poetry
- pyenv
- micropipenv


.. keypoints::

   - Conda, pip, Virtualenv, Pipenv, pyenv, Poetry, requirements.txt
