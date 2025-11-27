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
---------------------

Jupyter notebooks can be parameterized for instance using `papermill <https://papermill.readthedocs.io/en/latest/>`_. It can be an attractive approach when you have short notebooks (to generate automatically plots/reports) but as soon as you have more complex tasks to execute, we strongly recommend to generate python scripts. This will also force you to modularize your code.

Within JupyterLab, you can export any jupyter notebook to a python script:

.. image:: https://jupyterlab.readthedocs.io/en/stable/_images/exporting_menu.png

Select **Export Notebook to Executable Script**.

Actually, you could also export your notebook in many other formats. Check `JupyterLab documentation <https://jupyterlab.readthedocs.io/en/stable/user/export.html>`_ for more information.


.. challenge:: Exercise 1


  1. Create a fresh jupyter notebook and rename it  **plot_inflammation.ipynb**
  
  2. Download the `first dataset <https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv>`_ and load it in python. Below is an example on how you can proceed:
  
  ::

    from io import StringIO

    import numpy as np
    import requests
    url='https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv'
    s=requests.get(url).text

    data = np.loadtxt(fname=StringIO(s), delimiter=',')



  *Note that later in the course, you will learn how to use* `pandas <https://pandas.pydata.org/>`_ *python package where loading such dataset from an url would become much simpler.*

  3. Plot the dataset (you may simply use `imshow` from `matplotlib.pyplot`) and save the resulting plot in a file called **plot.png**.

  ::

    import matplotlib.pyplot as plt

    plt.imshow(data)

    plt.savefig('plot.png')

  *Feel free to customize your plot as learn in the preceding episode*.

  4. Export your notebook as a python script and check that you have a new file called **plot_inflammation.py**. Please note that the file may be located in your **Downloads** folder (in that case, make sure you move it to your working directory).

  5. Open a Terminal and navigate to the folder where you have exported your notebook to run it

  ::

    ./plot_inflammation.py

Run a python script 
-------------------

Let's understand why our python script ran out of the box. Open **plot_inflammation.py** with your favorite editor (from JupyerLab, you can double click on the file to open i). You should have, at the very top of your script:


::

  #!/usr/bin/env python

*Note: you may have* **python3** *rather than python*.

In the exercise above, a few things can go wrong:

- if you get an error such as :

::

   can't open file 'test_inflammation.py': [Errno 2] No such file or directory

That's probably because you try to run **plot_inflammation.py** from a different folder. The solution is to check **plot_inflammation.py** is in the current folder.

- or:

::

  bash: python: command not found

This happens if the python command is not in your **PATH**. You may have to specify the full path to the python command.



Synchronize with Jupytext
-------------------------

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


After few seconds, **test_inflammation.py** will be created and synchronized with **test_inflammation.ipynb**.

Double click on the python script to edit it and add (on the top of the script):

::

  #!/usr/bin/env python


This will make sure you can execute it from the command line.

*Note that, it can also be added in the jupyter notebook by editing notebook metadata (Property Inspector)*.


Importing other python files
----------------------------

We have a very short notebook that loads and plots data but let's imagine we need to process data after loading them. For instance, we can normalize data:

::

  data = data / np.linalg.norm(data)


In that case, it is good practice to separate processing from plotting. The reason is that you usually need to generate your plot several time while processing data once only (especially when data processing is computational intensive).

For example, we can create a new python file (**inflammation_functions.py**) containing a function to normalize our dataset:

::

  import numpy as np

  def processing(dataset):
    return dataset / np.linalg.norm(dataset)

and a second file calling this function:

::

    from io import StringIO

    import numpy as np
    import requests

    import inflammation_functions

    url='https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv'
    s=requests.get(url).text

    data = np.loadtxt(fname=StringIO(s), delimiter=',')


    # call processing function from inflammation_functions

    data = inflammation_functions.processing(data)



.. challenge:: Exercise 2 (optional)

  1. Update **inflammation_functions.py** to add a new function for plotting the dataset.

  2. Update **test_inflammation.py** to call it.


Command line arguments with `sys.argv`
--------------------------------------

We have better organized our code but it still cannot easily process different input files. For this, rather than copying several time the same code for different input files, we can update the main code to pass it from the command line. 

**Example**

We create a python script to sum two integers and print the result. The two integers are passed as arguments.

::

  import sys

  print(int(sys.argv[1]) + int(sys.argv[2]))


This approach is not very flexible and does not fully allow to customize your scripts. A better approach is to use **argparse**.

Parsing command line arguments with `argparse`
----------------------------------------------

::

  #!/usr/bin/env python

  import argparse

  # help flag provides flag help

  parser = argparse.ArgumentParser()
     
  parser.add_argument('-o', '--output', type=str,  
                      help="output filename")
  args = parser.parse_args()

  if args.output:
	     print("This is the name of the output file")

.. challenge::

  1. Take the python script we have written in the preceding exercise and use
     `argparse` to be able to read any input file and save the resulting image in an output file (filename is specified via command line argument).

  2. Execute your script for all the **inflammation** files (there are 12 files numbered from 01 to 12).

.. keypoints::

   - synchronize your jupyter notebooks & python scripts with `jupytext`
   - `import` other python files
   - command line arguments in python scripts
