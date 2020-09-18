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

So far we have been learning python using Jupyter notebooks. It is very convenient: it allowed us to experiment and prototype python code so we may think that is more than enough for your day to day work.

But after several weeks of hard work with python, you may end up:

- either with 10 different notebooks (so that you can run them concurrently)
- or with a very long notebook which is becoming hardly readable!

Let's imagine you have created 10 notebooks to run for 10 different input parameters and now you are willing to experiment with 1000 sets of input parameters.
Suppose you find a bug in the original notebook and need to rerun everything: are you willing to re-create manually your 1000 notebooks?

In this episode, we will learn how to automate your work using python scripts so that

* you do not need to manually configure your notebooks to be able to run with different parameters
* can easily run you work via other tools, such as on computing clusters.


From jupyter notebooks to python scripts
-----------------------------------------

Save as python script
---------------------

Jupyter notebooks can be parameterized for instance using `papermill <https://papermill.readthedocs.io/en/latest/>`_. It can be an attractive approach when you have short notebooks (to generate automatically plots/reports) but as soon as you have more complex tasks to execute, we strongly recommend to generate python scripts. This will also force you to modularize your code.

Within JupyterLab, you can export any jupyter notebook to a python script:

.. figure:: https://jupyterlab.readthedocs.io/en/stable/_images/exporting_menu.png

   Select File (top menu bar) → Export Notebook as → **Export notebook to Executable Script**.

Actually, you could also export your notebook in many other formats. Check `JupyterLab documentation <https://jupyterlab.readthedocs.io/en/stable/user/export.html>`_ for more information.


.. challenge:: Scripts-1


  1. Create a fresh jupyter notebook and rename it  **plot_inflammation.ipynb**

  2. Download the `first dataset <https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv>`_ and load it in python. Below is an example on how you can proceed::

       from io import StringIO

       import numpy as np
       import requests
       url='https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv'
       s=requests.get(url).text

       data = np.loadtxt(fname=StringIO(s), delimiter=',')

     *Note that later in the course, you will learn how to use* `pandas <https://pandas.pydata.org/>`_ *python package where loading such dataset from an url would become much simpler.*

  3. Plot the dataset (you may simply use ``imshow`` from ``matplotlib.pyplot``) and save the resulting plot in a file called **plot.png**::

       import matplotlib.pyplot as plt

       plt.imshow(data)

       plt.savefig('plot.png')

     *Feel free to customize your plot as you learned in the preceding episode*.

  4. Export your notebook as a python script and check that you have a new file called **plot_inflammation.py**. Please note that the file may be located in your **Downloads** folder (in that case, make sure you move it to your working directory).

  5. Open a Terminal and navigate to the folder where you have exported your notebook to run it::

       ./plot_inflammation.py

Run a python script
-------------------

Let's understand why our python script ran out of the box. Open **plot_inflammation.py** with your favorite editor (from JupyerLab, you can double click on the file to open it). You should have, at the very top of your script::

  #!/usr/bin/env python

*Note: you may have* **python3** *rather than python*.

In the exercise above, a few things can go wrong:

- if you get an error such as::

     can't open file 'test_inflammation.py': [Errno 2] No such file or directory

  That's probably because you try to run **plot_inflammation.py** from a different folder. The solution is to check **plot_inflammation.py** is in the current folder.

- or::

    bash: python: command not found

This happens if the python command is not in your **PATH**. You may have to specify the full path to the python command.



Importing other python files
----------------------------

We have a very short notebook that loads and plots data but let's imagine we need to process data after loading them. For instance, we can normalize data::

  data = data / np.linalg.norm(data)


In that case, it is good practice to separate processing from plotting. The reason is that you usually need to generate your plot several time while processing data once only (especially when data processing is computational intensive).

For example, we can create a new python file (**inflammation_functions.py**) containing a function to normalize our dataset::

  import numpy as np

  def processing(dataset):
      return dataset / np.linalg.norm(dataset)

and a second file calling this function:

.. code-block::
    :emphasize-lines: 6,16

    from io import StringIO

    import numpy as np
    import requests

    import inflammation_functions

    url='https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv'
    s=requests.get(url).text

    data = np.loadtxt(fname=StringIO(s), delimiter=',')


    # call processing function from inflammation_functions

    data = inflammation_functions.processing(data)



.. challenge:: Scripts-2 (optional)

  1. Update **inflammation_functions.py** to add a new function for plotting the dataset.

  2. Update **test_inflammation.py** to call it.


Command line arguments with ``sys.argv``
----------------------------------------

We have better organized our code but it still cannot easily process different
input files. For this, rather than copying several time the same code for
different input files, we can update the main code to take the input file from the command
line.

**Example**: We create a Python script and pass the input file and the output file
name as command line arguments:

.. code-block:: python
   :emphasize-lines: 3-4

   import sys

   input_file_name = sys.argv[1]
   output_file_name = sys.argv[2]

   # to keep things simple we only print them out:
   print(f"input file is {input_file_name}")
   print(f"output file is {output_file_name}")


We can try it out::

   $ python myscript.py myinput myoutput


.. discussion::

  - Does it work?

  - Why is this better than modifying the script every time I want it to
    operate on a different file?

  - What problems do you expect when using this approach (using ``sys.argv``)?

This approach is brittle and more robust solutions exist that allow to fully
customize your scripts and generate help texts at the same time:

- `argparse <https://docs.python.org/3/library/argparse.html>`__: this is the one that we will show
- `doctopt <http://docopt.org/>`__: you write the help text and this generates a parser for you
- `click <https://click.palletsprojects.com//>`__: another nice library for command line interfaces


Parsing command line arguments with ``argparse``
------------------------------------------------

This example not only gives you descriptive command line
arguments, it also automatically generates a ``--help`` option for you:

.. code-block:: python

   #!/usr/bin/env python

   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('-o', '--output', type=str,
                       help="output filename")
   args = parser.parse_args()

   if args.output:
       print(f"output file is {args.output}")


.. challenge:: Scripts-3

  1. Take the python script we have written in the preceding exercise and use
     ``argparse`` to be able to read any input file and save the resulting image in an output file (filename is specified via command line argument).

  2. Execute your script for all the **inflammation** files (there are 12 files numbered from 01 to 12).


.. solution::

   .. code-block::
      :emphasize-lines: 5,7-10,12,19

      from io import StringIO
      import numpy as np
      import requests
      import matplotlib.pyplot as plt
      import argparse

      parser = argparse.ArgumentParser()
      parser.add_argument("-i", "--input", type=str, help="input data file (URL)")
      parser.add_argument("-o", "--output", type=str, help="output plot file")
      args = parser.parse_args()

      url = args.input
      s = requests.get(url).text

      data = np.loadtxt(fname=StringIO(s), delimiter=",")

      plt.imshow(data)

      plt.savefig(args.output)


.. discussion::

   **What was the point of doing this?**

   Now you can do this::

      $ python test_inflammation.py --help
      $ python test_inflammation.py --input https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv --output 01.png
      $ python test_inflammation.py --input https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-02.csv --output 02.png

   - We can now process different input files without changing the script.
   - This way we can also loop over file patterns (using shell loops or similar) or use
     the script in a workflow management system and process many files in parallel.
   - By changing from ``sys.argv`` to ``argparse`` we made the script more robust against
     user input errors and also got a help text (accessible via ``--help``).


Synchronize with Jupytext (optional)
------------------------------------

`jupytext <https://jupytext.readthedocs.io/en/latest/>`_ is a python package you can use for automatically synchronizing your notebooks into python scripts.

To install it from the command line (make sure you use JupyterLab 2.x)::

  pip install jupytext --upgrade

or

::

  conda install -c conda-forge jupytext

Please note that you may also use `Anaconda navigator <https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/>`_ (if installed) to install ``jupytext``.

Installing Jupytext will trigger a build of the JupyterLab extension the next time you open it. If you prefer, you can trigger the build manually with

::

  jupyter lab build


Once installed, you can pair your notebook:

.. figure:: https://raw.githubusercontent.com/mwouts/jupytext/master/packages/labextension/jupytext_commands.png

   Select "Commands" from left toolbar, search "jupytext", then **Pair notebook with percent script** (**NOT** what you see in the image).


After few seconds, **test_inflammation.py** will be created and synchronized with **test_inflammation.ipynb**.

Double click on the python script to edit it and add (on the top of the script):

::

  #!/usr/bin/env python


This will make sure you can execute it from the command line.

*Note that, it can also be added in the jupyter notebook by editing notebook metadata (Property Inspector)*.


.. keypoints::

   - synchronize your jupyter notebooks & python scripts with ``jupytext``
   - ``import`` other python files
   - command line arguments in python scripts
