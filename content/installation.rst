Software installation
=====================

This page contains instructions for installing the required software
on your computer.  Please make sure before the course that you have
all the required software installed or some other way access to it.
For example, the workshop could be done with a remote Jupyter server,
as long as you can use the terminal from the Jupyter (you need to be
able to access the command line for some lessons).


.. admonition:: Do you need help?
   :class: important

   Participants from a partner institution are invited to install help
   sessions. (Hint: ask your institution to become a partner if it
   isn't already!)

   Otherwise, if you need installation help, show this page to someone
   around you and they can probably help.  These are relatively
   standard tools.

   Don't be afraid to ask for help.  Installing scientific software is
   *harder than it should be* and it helps to have someone guide you
   through it.



Generic list of tools required
------------------------------

Note: The actual installation instructions are below.  This is a
generic description, for those who already know how to install Python
and conda.

* **Python 3** (A conda-based distribution is recommended, for example
  miniforge, miniconda, or Anaconda)

  * With some extra packages installed.  They are all included in
    Anaconda, and are listed in the ``environment.yml`` file you can
    find under miniconda below.

* Text editor (several lessons, can also be done through Jupyterlab)
* Command-line shell (several lessons, can also be done through Jupyterlab)
* git (not needed, this lesson is usually done as a demo)



Python
------

We expect you to have a working Python installation with some common
libraries.  The `Anaconda Python distribution
<https://docs.continuum.io/anaconda/install/>`__ conveniently packages
everything, but its license does not allow large organizations to use
it for research.  **Thus, we currently recommend Miniforge, which
includes the base and packages through a different, freely usable
channel.**

.. admonition:: Python, conda, anaconda, miniforge, etc?
   :class: dropdown

   Unfortunately there's a lot of jargon.  We'll go over this in the
   course but here is a crash course:

   * **Python** is a programming language very commonly used in
     science, it's the topic of this course.
   * **Conda** is a package manager: it allows distributing and
     installing packages, and is designed for complex scientific
     code.
   * **Mamba** is a re-implementation of Conda to be much faster with
     resolving dependencies and installing things.
   * An **Environment** is a self-contained collections of packages
     which can be installed separately from others.  They are used so
     each project can install what it needs without affecting others.
   * **Anaconda** is a commercial distribution of Python+Conda+many
     packages that all work together.  It used to be freely usable for
     research, but since ~2023-2024 it's more limited.  Thus, we don't
     recommend it (even though it has a nice graphical user interface).
   * **conda-forge** is another channel of distributing packages that
     is maintained by the community, and thus can be used by anyone.
     (Anaconda's parent company also hosts conda-forge packages)
   * **miniforge** is a distribution of conda pre-configured for
     conda-forge.  It operates via the command line.
   * **miniconda** is a distribution of conda pre-configured to use
     the Anaconda channels.

.. tabs::

   .. group-tab:: Miniforge

      This is our recommended method - it can be used for any purpose
      and makes a strong base for the future.

      Follow the `instructions on the miniforge web page
      <https://github.com/conda-forge/miniforge>`__.  This installs
      the base, and from here other packages can be installed.

      ..
        You can read how to install miniconda from the `CodeRefinery
        installation instructions
        <https://coderefinery.github.io/installation/conda/>`__.

      Miniforge uses the command line - this gives you the most power
      but can feel unfamiliar.  See the `command line crash course
      <https://scicomp.aalto.fi/scicomp/shell/>`__ for an intro.

      Linux/MacOS: Each time you start a new shell, you can activate
      Miniforge by running ``source ~/miniforge3/bin/activate``.  This
      is not needed if you choose "Do you wish to update your shell
      profile to automatically initialize conda?".

      Windows: Use the "Miniforge Prompt" to start Miniforge.  This
      will set up all the paths so that ``conda`` and ``mamba`` are
      available.

   .. group-tab:: Anaconda

      Anaconda is easier to get started with, but may be more limiting
      in the future.

      The `Anaconda Navigator
      <https://docs.anaconda.com/navigator/>`__ provides a convenient
      way to access the software. It can be installed from that page.

      Note the license of Anaconda - for organizations of more than 50
      people, it can't be used for research purposes without a license.


   .. group-tab:: Other options

      Any other Python distribution which you can install libraries into
      would work, but because there are so many different ways to do this,
      we don't support them.  You would need the extra libraries mentioned
      in the Miniforge instructions.

      We don't currently provide a ``requirements.txt`` for installing
      the required packages without Conda/Mamba, though.


Python for SciComp software environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. group-tab:: Miniforge

      This `this environment file
      <https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/software/environment.yml>`__
      contains all packages needed, and can be installed with:

      .. code:: console

	 $ mamba env create -f https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/software/environment.yml

      Each time you start a new command line, you need to activate
      miniforge (if you don't do run the ``conda init`` option), and
      then you need to activate the proper environment with ``conda
      activate python-for-scicomp``.

   .. group-tab:: Anaconda

      Anaconda includes most of the things needed for the course
      automatically, but as of 2024 not everything.  You can use the
      navigator to create new environments from this `this environment
      file
      <https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/software/environment.yml>`__.
      You'll have to download it and then `import it
      <https://docs.anaconda.com/navigator/tutorials/manage-environments/#importing-an-environment>`__.


   .. group-tab:: Other options

      **Minoconda, Anaconda command line, other conda/mamba command
      line tools**: see "Miniforge" instructions.

      Virtual environments: we don't currently provide a
      ``requirements.txt`` but many package names can probably be
      copied from the ``environment.yml`` file.

      Any other Python distribution which you can install libraries into
      would work, but because there are so many different ways to do this,
      we don't support them.  You would need the extra libraries mentioned
      in the Miniforge instructions.




JupyterLab
~~~~~~~~~~

We do most of the lessons from JupyterLab (and JupyterLab provides
most of the other tools we need).

.. tabs::

   .. group-tab:: Miniforge

      First, start the Miniforge command line interface.

      Linux/MacOS: remember, you may need to activate it by running
      ``source ~/miniforge3/bin/activate`` if you didn't update your
      shell profile to automatically initialize conda.

   .. group-tab:: Anaconda

      If you install the full Anaconda distribution, this will be
      available and can be started either through Anaconda Navigator
      or command line.

      Make sure the CodeRefinery environment is selected and you can
      start JupyterLab.



Verification of Python and JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Watch the video

   See this `verification in video form
   <https://youtu.be/OEX1ss_HCHc>`__ - if you can do this, you are
   ready to go for day one.  Your exact steps may be a bit different.


.. tabs::

   .. group-tab:: Miniforge

      You can start JupyterLab from the command line:

      .. code-block:: console

         $ jupyter-lab
         (... Jupyter starts in a web browser)


   .. group-tab:: Anaconda

      **You should be able to start JupyterLab.**  You can do this from the
      `Anaconda Navigator <https://docs.anaconda.com/anaconda/navigator/>`__ (recommended if you have it):

      .. figure:: img/installation/anaconda-navigator-jupyterlab.png
         :class: with-border

         Starting JupyterLab from the Anaconda Navigator.

      ... or you can start JupyterLab from the command line:

      .. code-block:: console

         $ jupyter-lab
         (... Jupyter starts in a web browser)



**Verify that you can start a Jupyter notebook.** We will learn how to
do this in day 1, but you can try running ``print("Hello, world!")``
if you want.

.. figure:: img/installation/jupyterlab-notebook.png
   :class: with-border

   Starting a Jupyter Notebook from JupyterLab.



Text editor
-----------

For one portion of the course, you will need a text editor.  **If you
don't know what to use, you can use the text editor that comes from
JupyterLab and it will do everything you need - no extra installation
needed.**

.. admonition:: Other editors
   :class: toggle

   Because we need to be simple in our teaching, we only teach the
   most basic editors.  We encourage you to try out more advanced ones
   yourself.

   For other editors, see the `CodeRefinery instructions
   <https://coderefinery.github.io/installation/editors/>`__.  You don't
   exactly need a terminal editor - the graphical ones, such as VSCode or
   whatever you use now, will work as well.



Command line
------------

**You need access to the command line for some lessons.  JupyterLab
includes it, so no extra installation is needed.**  If you want to
test in advance:

* You can start it from JupyterLab (recommended):

  .. figure:: img/installation/jupyterlab-terminal.png
     :class: with-border
     :scale: 75%

     From the JupyterLab launcher, select "Terminal".

.. admonition:: Other ways to access the command line
   :class: toggle

   * From the Anaconda Navigator:

     .. figure:: img/installation/anaconda-prompt.png
	:class: with-border

	From the Anaconda Navigator, you can select "environments" on the
	left, then click on one, then the arrow, then "Open terminal".

   * From your operating system's terminal applications, if you activate
     Anaconda.



Verification of the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify command line usage, type the following commands (without the
``$``), and you should see the corresponding output that lists the
Python version:

.. code-block:: console

   $ python3 -V
   Python 3.8.3

   ## Or python... if it's installed as that
   $ python -V
   Python 3.8.3

Any recent version of Python 3 should work for the course (for example
3.8 or higher).



Zoom
----

If this is an online workshop, it might use Zoom.  You can see
`CodeRefinery instructions for it
<https://coderefinery.github.io/installation/zoom/>`__.



Need help?
----------

If you have access, come to one of the installation help sessions.
Or, ask your colleagues: these are standard tools and you can
definitely find someone can help you get set up!



See also
--------

* `Research Software Hour on conda
  <https://www.youtube.com/watch?v=ddCde5Nu2qo&list=PLpLblYHCzJAB6blBBa0O2BEYadVZV3JYf>`__
* `Conda manual <https://docs.conda.io/en/latest/>`__ (technical)
* `Anaconda individual edition home
  <https://www.anaconda.com/products/distribution>`__
* `Anaconda getting started
  <https://docs.anaconda.com/anaconda/user-guide/getting-started/>`__
