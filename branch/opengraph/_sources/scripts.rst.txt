.. _scripts:

Scripts
=======

.. questions::

   - Why are command line programs useful, compared to Jupyter
     notebooks and similar?
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

Jupyter notebooks can be parameterized for instance using `papermill <https://papermill.readthedocs.io/en/latest/>`_. It can be an attractive approach when you have short notebooks (to generate automatically plots/reports) but as soon as you have more complex tasks to execute, we strongly recommend to generate python scripts. This will also force you to modularize your code.  See `CodeRefinery's lesson on Modular code development <https://coderefinery.github.io/modular-type-along/>`__.

Within JupyterLab, you can export any jupyter notebook to a python script:

.. figure:: https://jupyterlab.readthedocs.io/en/stable/_images/exporting_menu.png

   Select File (top menu bar) → Export Notebook as → **Export notebook to Executable Script**.


.. highlight:: console

Actually, you could also export your notebook in many other formats.
Check the `JupyterLab documentation <https://jupyterlab.readthedocs.io/en/stable/user/export.html>`_ for more information.
If you keep working in the jupyterlab folder, you can also convert files in the terminal (File -> New -> Terminal) by running::


  $ jupyter nbconvert --to script your_notebook_name.ipynb


Exercises 1
-----------

.. challenge:: Scripts-1

  .. highlight:: console


  1. Download the :download:`weather_observations.ipynb <../resources/code/scripts/weather_observations.ipynb>` and the weather_data file and upload them to your jupyterlab. The script plots the temperature data for Tapiola in Espoo. The data is originally from `rp5.kz <https://rp5.kz>`_ and was slightly adjusted for this lecture.

     **Note:** If you haven't downloaded the file directly to your jupyterlab folder, it will be located in your **Downloads** folder or the folder you selected. In jupyterlab click on the 'upload file' button, navigate to the folder containing the file and select it to load it into your jupyterlab folder.

  2. Open a terminal in jupyter (File -> New -> Terminal).

  3. Convert the jupyter script to a python script by calling::

     $ jupyter nbconvert --to script weather_observations.ipynb

  4. Run the script (note: you may have ``python3`` rather than ``python``)::

     $ python weather_observations.py

Importing other python files
----------------------------

We have a very short notebook that loads and plots data. But even in this script, we have to do a bit of processing (changing the format of the dates). We also extract a subset of our data for a
given date range.

In general, it is good practice to separate processing from plotting. The reason is that you often need to generate multiple plots using the data while pre-processing data once only.
When data preprocessing is expensive this is even more important.

.. highlight:: python

For example, we can create a new python file (**weather_functions.py**) containing a function to adjust the dates in our dataset::

  import pandas as pd

  def preprocess(dataset, start_date, end_date):
    dataset['Local time'] = pd.to_datetime(dataset['Local time'],dayfirst=True)
    dataset = dataset[dataset['Local time'].between(start_date,end_date)]
    return dataset

and modify the ``weather_observations.py`` file to

.. code-block:: python
    :emphasize-lines: 2,11

    import pandas as pd
    import weather_functions

    url = "https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_tapiola.csv"
    # read the data skipping comment lines
    weather = pd.read_csv(url,comment='#')
    # set start and end time
    start_date=pd.to_datetime('01/06/2021',dayfirst=True)
    end_date=pd.to_datetime('01/10/2021',dayfirst=True)
    # preprocess the data
    weather = weather_functions.preprocess(weather, start_date, end_date)
    ...


Exercises 2
-----------

.. challenge:: Scripts-2 (optional)

  1. Create **weather_functions.py** with the above function and add an additional function for plotting the dataset.

  2. Update **weather_observations.py** to call it.

.. solution::

   **weather_observations.py**:

   .. literalinclude:: ../resources/code/scripts/weather_observations.py
     :language: python
     :emphasize-lines: 5,13,16

   **weather_functions.py**:

   .. literalinclude:: ../resources/code/scripts/weather_functions.py
     :language: python
     :emphasize-lines: 2, 12-21


Command line arguments with ``sys.argv``
----------------------------------------

We now have a better organized code but it still cannot easily process time ranges or a
specified output file name. To achieve this, rather than copying the same code several times for
different time ranges or output file names, we can update the main code to take the
start/end time and output file name from the command line

**Example**: We modify the **weather_observations.py** script such that we allow start
and end times as well as the output file to be passed in as arguments to the function:

.. code-block:: python
   :emphasize-lines: 1,6-7,9

   import sys
   import pandas as pd
   import weather_functions

   # set start and end time
   start_date = pd.to_datetime(sys.argv[1],dayfirst=True)
   end_date = pd.to_datetime(sys.argv[2],dayfirst=True)

   output_file_name = sys.argv[3]

   ...

   # preprocess the data
   weather = weather_functions.preprocess(weather, start_date, end_date)

   ...

   fig.savefig(output_file_name)

We can try it out:

.. code-block:: console

   $ python weather_observations.py 01/03/2021 31/05/2021 spring_in_tapiola.png


.. discussion::

  - Does it work?

  - Why is this better than modifying the script every time I want it to
    plot data for a different period?

  - What problems do you expect when using this approach (using ``sys.argv``)?

This approach is brittle and more robust solutions exist that allow to fully
customize your scripts and generate help texts at the same time:

- `argparse <https://docs.python.org/3/library/argparse.html>`__:
  built-in to Python, this is the one that we will show below.
- `doctopt <http://docopt.org/>`__: you write the help text and this generates a parser for you.
- `click <https://click.palletsprojects.com//>`__: another nice
  library for command line interfaces - very easy to use.


Parsing command line arguments with ``argparse``
------------------------------------------------

This example not only gives you descriptive command line
arguments, it also automatically generates a ``--help`` option for you:

.. code-block:: python
   :emphasize-lines: 1,5-14

   import argparse
   import pandas as pd
   import weather_functions

   parser = argparse.ArgumentParser()
   # set start and end time
   parser.add_argument('-o', '--output', type=str, default="Out.png"
		    help="end time")
   parser.add_argument('-s', '--start', type=str, default="1/1/2019"
		    help="start time")
   parser.add_argument('-e', '--end', type=str, default="1/1/2021"
		    help="output filename")

   args = parser.parse_args()

   start_date = pd.to_datetime(args.start,dayfirst=True)
   end_date = pd.to_datetime(args.end,dayfirst=True)

   ...

   # preprocess the data
   weather = weather_functions.preprocess(weather, start_date, end_date)

   ...

   fig.savefig(args.output)



Exercises 3
-----------

.. challenge:: Scripts-3

  1. Take the python script we have written in the preceding exercise and use
     ``argparse`` to specify the input and output files and allow the start and end dates to be set.

  2. Execute your script for a few different time intervals (e.g. from January 2019 to June 2020, or from Mai 2020 to October 2020).
     Also use data for cairo (``https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_cairo.csv``)


.. solution::

   .. literalinclude:: ../resources/code/scripts/weather_observations_argparse.py
     :language: python
     :emphasize-lines: 2,5-9,11,14,17-18,27




.. discussion::

   **What was the point of doing this?**

   Now you can do this:

   .. code-block:: console

      $ python weather_observations.py --help
      $ python weather_observations.py https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_tapiola.csv temperature_tapiola.png
      $ python weather_observations.py -s 1/12/2020 -e 31/12/2020 https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_tapiola.csv temperature_tapiola_dec.png
      $ python weather_observations.py -s 1/2/2021 -e 28/2/2021 https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_tapiola.csv temperature_tapiola_feb.png
      $ python weather_observations.py https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_cairo.csv --output temperature_cairo.png

   - We can now process different input files without changing the script.
   - We can select multiple time ranges without modifying the script.
   - This way we can also loop over file patterns (using shell loops or similar) or use
     the script in a workflow management system and process many files in parallel.
   - By changing from ``sys.argv`` to ``argparse`` we made the script more robust against
     user input errors and also got a help text (accessible via ``--help``).


Load larger option lists using config files
-------------------------------------------

In the above example we only allowed the input and output files along with start and end dates to be selected by command line arguments.
This already leads to a quite large command line call. Now imagine, that we also want to allow the user to select more specific information
from the dataset, define specific X and Y labels, write their own
title etc. Now imagine to put all this into the command line:

.. code-block:: console


   $ python weather_observations.py --input https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/data/scripts/weather_cairo.csv --output rain_in_tapiola.png --xlabel "Days in June" --ylabel "Rainfall in mm" --title "Rainfall in Cairo" --data_column RRR --start 01/06/2021 --end 30/06/2021


This is an even larger line, needs scrolling and becomes quite inconvenient to modify.
Instead of putting all of this into the command line, you could think about storing and modifying the arguments in a config file.
There are several ways, how config files can be stored. You can use a simple ``Parameter = Value``
format, and parse it yourself, or you can use e.g. the ``JSON`` or ``YAML`` formats.
For both parsers exist that can save you some work, and both formats also allow you to use
more complex input data, like lists, or dictionaries. We won't go into the details of the formats, and will only give
a short example using YAML here.

The YAML file format can be simple or very complex allowing a large variety of data structures to be stored.
One benefit of YAML is that there is already a python module (``yaml``) available for parsing it and it
directly parses numbers as numbers and text as strings, making conversions unnecessary (the same is true for JSON
with the ``json`` package).

The python module :download:`optionsparser.py <../resources/code/scripts/optionsparser.py>` provides a simple parser for YAML styled options files.
Similar to argparse, it takes a dict of required options, along with a dict of optional parameters.
Required arguments need to specify a type. Optional argument types are derived from their default values.

In our example above, we could for example add optional parameters that allow the selection of other weather data
from the dataset (precipitation ...), set the labels and titles explicitly etc.

In the YAML format, names and values are separated by ``:``. Our above example would therefore translate to the following YAML file:

.. literalinclude:: ../resources/code/scripts/weather_options.yml
   :language: yaml

Exercises 4 (optional)
----------------------

.. challenge:: Scripts-4

  1. Download the :download:`optionsparser.py <https://raw.githubusercontent.com/AaltoSciComp/python-for-scicomp/master/resources/code/scripts/optionsparser.py>`
     function and load it into your working folder in jupyterlab.
     Modify the previous script to use a config file parser to read all arguments. The config file is passed in as a single argument on the command line
     (using e.g. argparse or sys.argv) still needs to be read from the command line.


  2. Run your script with different config files.


.. solution::

   The modified **weather_observations.py** script:

   .. literalinclude:: ../resources/code/scripts/weather_observations_config.py
     :language: python
     :emphasize-lines: 5,16-27,31,34,44,47

   The modified **weather_functions.py** script:

   .. literalinclude:: ../resources/code/scripts/weather_functions_config.py
     :language: python
     :emphasize-lines: 12,16-18


.. admonition:: Further reading

  - Linking Jupyterlab notebooks to python scripts (making linking ``.py``- and ``.ipynb``-files easier) using `jupytext <https://jupytext.readthedocs.io/en/latest/paired-notebooks.html>`_
  - The `wikipedia page about YAML <https://en.wikipedia.org/wiki/YAML>`_ contains a lot of additional information on the YAML syntax.
  - `The Coderefinery Lesson about reproducible research <https://coderefinery.github.io/reproducible-research/>`_ can give additional information about good coding practices and workflow automation.

  - `CodeRefinery's lesson on Modular code development <https://coderefinery.github.io/modular-type-along/>`__
