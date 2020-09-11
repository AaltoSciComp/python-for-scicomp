Scripts
=======

.. questions::

   - Why moving from Jupyter notebooks to scripts?
   - How to create a python script?
   - How to generalize a python script?

.. objectives::

   - Learn how to streamline your python notebooks by creating repeatable python scripts
   - Learn how to import other python files
   - Learn to parse command line arguments in python


Why scripts?
-------------

So far we have been learning python using Jupyter notebook. It is very convenient: it allowed us to experiment and prototype python code so we may think that is more than enough for your day to day work.

But after several weeks of hard work with python, you may end up:

- either with 10 different notebooks (so that you can run them concurrently)
- or with a very long notebook which is becoming hardly readable!

Let's imagine you have created 10 notebooks to run for 10 different input parameters and now you are willing to experiment with 1000 sets of input parameters. 
Suppose you find a bug in the original notebook and need to rerun everything: are you willing to re-create manually your 1000 notebooks?

In this episode, we will learn how to automate your work using python scripts so that you do not need to configure manually your notebooks to be able to run with different parameters.


From jupyter notebooks to python scripts
----------------------------------------- 

Save as python script
======================

Jupyter notebooks can be parameterized for instance using `papermill <https://papermill.readthedocs.io/en/latest/>`_. It can be an attractive approach when you have short notebooks (to generate automatically plots/reports) but as soon as you have more complex tasks to execute, we strongly recommend to generate python scripts. This will also force you to modularize your code.

Within JupyterLab, you can export any jupyter notebook to a python script:

.. image:: https://jupyterlab.readthedocs.io/en/stable/_images/exporting_menu.png

Actually, you could also export your notebook in many other formats. Check `JupyterLab documentation <https://jupyterlab.readthedocs.io/en/stable/user/export.html>`_ for more information.


.. challenge::

  1. Download the `first dataset <https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv>`_ in your working area.

  2. Create a fresh jupyter notebook, read (for instance using `loadtxt` from `numpy`) and plot the dataset (you may simply use `imshow` from `matplotlib.pyplot`).

  3. Rename your notebook to a meaningful name; for instance **plot_inflammation.ipynb**

  4. Export your notebook as a python script and check that you have a new file called **plot_inflammation.py** in your working directory.

  5. Open a Terminal and navigate to the folder where you have exported your notebook to run it

::

   python plot_inflammation.py

Run a python script 
====================

TODO: Explain how to create a script with `#!`  to run it:

::
  
  plot_inflammation.py


Synchronize with Jupytext
==========================

`jupytext <https://jupytext.readthedocs.io/en/latest/>`_` is a python package you can use for automatically synchronizing your notebooks into python scripts.

To install it from the command line (make sure you use JupyterLab 2.x):

:: 

  pip install jupytext --upgrade

or

::

  conda install -c conda-forge jupytext

Please note that you may also use `Anaconda navigator <https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/>`_ (if installed) to install `jupytext`.

Installing Jupytext will trigger a build of the JupyterLab extension the next time you open it. If you prefer, you can trigger the build manually with

::

  jupyter lab build


Once installed, you can pair your notebook (select `pair notebook with percent script`).

.. image:: https://raw.githubusercontent.com/mwouts/jupytext/master/packages/labextension/jupytext_commands.png


Generalize your python script
------------------------------

Importing other python files
=============================

To avoid having large notebook/scripts, it is recommended to organize your python code in modules.

For instance, it is good practice to only keep plotting (or report generation) in a notebook/script and separate data analysis from it.

**Example**

TODO: show an example where we create a module that we import in the python script.


Parameterize your inputs
========================


Command line arguments with `sys.argv`
======================================


**Example**

We create a python script to sum two integers and print the result. The two integers are passed as arguments.

::

  import sys

  print(int(sys.argv[1]) + int(sys.argv[2]))


Parsing command line arguments with `argparse`
==============================================

::

  #!/usr/bin/env python

  import argparse

  # help flag provides flag help
  # store_true actions stores argument as True

  parser = argparse.ArgumentParser()
     
  parser.add_argument('-o', '--output', action='store_true', 
                      help="shows output")
  args = parser.parse_args()

  if args.output:
	     print("This is the name of the output file")

.. challenge::

  1. Take the python script we have written in the preceding exercise and use
     `argparse` to be able to read any input file and save the resulting image in an output file (filename is specified via command line argument).

.. keypoints::

   - synchronize your jupyter notebooks & python scripts with `jupytext`
   - `import` other python files
   - command line arguments in python scripts
