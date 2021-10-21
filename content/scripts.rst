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

Jupyter notebooks can be parameterized for instance using `papermill <https://papermill.readthedocs.io/en/latest/>`_. It can be an attractive approach when you have short notebooks (to generate automatically plots/reports) but as soon as you have more complex tasks to execute, we strongly recommend to generate python scripts. This will also force you to modularize your code.

Within JupyterLab, you can export any jupyter notebook to a python script:

.. figure:: https://jupyterlab.readthedocs.io/en/stable/_images/exporting_menu.png

   Select File (top menu bar) → Export Notebook as → **Export notebook to Executable Script**.
   


Actually, you could also export your notebook in many other formats. 
Check `JupyterLab documentation <https://jupyterlab.readthedocs.io/en/stable/user/export.html>`_ for more information.
If you keep working in the jupyterlab folder, you can also convert files in the terminal (File -> New -> Terminal) by running::


  jupyter nbconvert --to script your_notebook_name.ipynb


Exercises 1
-----------

.. challenge:: Scripts-1


  1. Download the `weather_observations.ipynb <../resources/code/scripts/weather_observations.ipynb>`_ and the weather_data file and upload them to your jupyterlab. The script plots the temperature data for Tapiola in Espoo for the time range from 
  	
  2. Open a terminal in jupyter (File -> New -> Terminal). 

  3. Convert the jupyter script to a python script by calling:  
  
     ``jupyter nbconvert --to script weather_observations.ipynb``

  4. Run the script: 
  
     ``python  weather_observations.py`` 
     
     *Note: you may have* **python3** *rather than python*.
     
Importing other python files
----------------------------

We have a very short notebook that loads and plots data. but even in this script, we have to do a bit of processing (changing the format of the dates). We also extract a subset of our data for a 
given date range. 

In general, it is good practice to separate processing from plotting. The reason is that you often need to generate multiple plots using the data while pre-processing data once only. 
When data preprocessing is expensive this is even more important.

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
    
    url = "https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_tapiola.csv"
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

We have better organized our code but it still cannot easily process time ranges or a 
specified output file name. For this, rather than copying several time the same code for
different time ranges or output file names, we can update the main code to take the 
start/end time and output file name from the command line

**Example**: We create a Python script and pass both the start and end time and the output
file name as command line arguments. Create a file named myscript.py with the following content:

.. code-block:: python
   
   import sys
   start_date = sys.argv[1]
   end_date = sys.argv[2]
   output_file_name = sys.argv[3]

   # to keep things simple we only print them out:
   print(f"Start date is {start_date}")
   print(f"End date is {end_date}")
   print(f"output file is {output_file_name}")


We can try it out::

   $ python myscript.py start end output


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
   parser.add_argument('-o', '--output', type=str, default="Out.png"
                       help="output filename")
   args = parser.parse_args()

   if args.output:
       print(f"output file is {args.output}")



Exercises 3
-----------

.. challenge:: Scripts-3

  1. Take the python script we have written in the preceding exercise and use
     ``argparse`` to specify the input and output files and allow the start and end dates to be set.

  2. Execute your script for a few different time intervals (e.g. form January 2019 to June 2020, or from Mai 2020 to October 2020).
     Also use data for cairo (``https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_cairo.csv``)


.. solution::

   .. literalinclude:: ../resources/code/scripts/weather_observations_argparse.py
     :language: python
     :emphasize-lines: 2,5-9,11,14,17-18,27

   


.. discussion::

   **What was the point of doing this?**

   Now you can do this::

      $ python weather_observations.py --help
      $ python weather_observations.py https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_tapiola.csv temperature_tapiola.png 
      $ python weather_observations.py -s 1/12/2020 -e 31/12/2020 https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_tapiola.csv temperature_tapiola_dec.png
      $ python weather_observations.py -s 1/2/2021 -e 28/2/2021 https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_tapiola.csv temperature_tapiola_feb.png
      $ python weather_observations.py --input https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_cairo.csv --output temperature_cairo.png

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
from the dataset, define specific X and Y labels, write their own title etc. Now imagine to put all this into the command line::


   $ python weather_observations.py --input https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_cairo.csv --output rain_in_tapiola.png --xlabel "Days in June" --ylabel "Rainfall in mm" --title "Rainfall in Cairo" --data_column RRR --start 01/06/2021 --end 30/06/2021
   
   
This is an even larger line, needs scrolling and becomes quite inconvenient to modify.
Instead of putting all of this into the command line, you could think about storing and modifying the arguments in a config file.
There are several ways, how config files can be stored. You can use a simple ``Parameter = Value``
format, and parse it yourself, or you can use e.g. the ``JSON`` or ``YAML`` formats.
For both parsers exist that can save you some work, and both formats also allow you to use
more complex input data, like lists, or dictionaries. We won't go into the details of the formats, and will only give
a short example using yaml here.

The yaml file format can be simple or very complex allowing a large variety of data structures to be stored.
One benefit of yaml is that there is already a python module (``yaml``) available for parsing it and it
directly parses numbers as numbers and text as strings, making conversions unnecessary.

The python module `optionsparser.py <../resources/code/scripts/optionsparser.py>`_ provides a simple parser for yaml styled options files.
Similar to argparse, it takes a dict of required options, along with a dict of optional parameters.
Required arguments need to specify a type. Optional argument types are derived from their default values.

In our example above, we could for example add optional parameters that allow the selection of other weather data
from the dataset (precipitation ...), set the labels and titles explicitly etc.

In the yaml format, names and values are separated by ``:``. Our above example would therefore translate to the following yaml file:

.. code-block:: yaml

    input:        https://raw.githubusercontent.com/tpfau/python-for-scicomp/ScriptUpdate/resources/data/scripts/weather_cairo.csv
    output:       rain_in_cairo.png
    xlabel:       Days in June
    ylabel:       Rainfall in mm
    title:        Rainfall in Cairo
    data_column:  RRR
    start:        01/06/2021
    end:          30/06/2021

Exercises 4 (opional)
---------------------

.. challenge:: Scripts-4

  1. Modify the previous script to use a config file parser to read all arguments. The config file is passed in as a single argument on the command line 
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

  
    
Some information on YAML (optional)
-----------------------------------

Note, that you don't need ``""`` around the strings in yaml files. 
If you have long Strings, yaml offers two ways to use line breaks::

	1. Value1: |
	           This is some
	           Text with a line break.
	2. Value2: >
	           This is some text
	           without line breaks, that
	           will just end up in one line.	


For dictionaries and Lists you can use::

	DictParam: 
	    Entry1: This is the first entry
	    Entry2: This is the value for Entry2
	
	ListParam:
	    - This is the First List entry
	    - This is the second List entry

There are much more complex settings that can be handled with yaml. If you want to know about them, `here <https://yaml.org/>`_ are the docs.


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

 Press ``Ctrl + Shift + C`` to start the command palette, search "jupytext", then **Pair notebook with percent script** (**NOT** what you see in the image).


After few seconds, **test_inflammation.py** will be created and synchronized with **test_inflammation.ipynb**.

Double click on the python script to edit it and add (on the top of the script):

::

  #!/usr/bin/env python


This will make sure you can execute it from the command line.

*Note that, it can also be added in the jupyter notebook by editing notebook metadata (Property Inspector)*.


.. keypoints::

   - Synchronize your Jupyter notebooks & python scripts with ``jupytext``
   - ``import`` other python files
   - Command line arguments in python scripts
   - Real programs allow you to automate calculations and scale up
