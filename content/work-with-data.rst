Working with Data
=================

.. questions::

   - How do you store your data right now?
   - Are you doing data cleaning / preprocessing every time you load the data?

.. objectives::

   - Learn benefits/drawbacks of common data formats.   
   - Learn how you can read and write data in a variety of formats.


..  figure:: https://imgs.xkcd.com/comics/norm_normal_file_format.png

    Source: `xkcd #2116 <https://xkcd.com/2116/>`__


What is a data format?
----------------------

Data format can mean two different things

1. `data structure <https://en.wikipedia.org/wiki/Data_structure>`__ or how you're storing the data in memory while you're working on it;
2. `file format <https://en.wikipedia.org/wiki/File_format>`__ or the way you're storing the data in the disk.

Let's consider this randomly generated DataFrame with various columns::

    import pandas as pd
    import numpy as np

    n_rows = 100000

    dataset = pd.DataFrame(
        data={
            'string': np.random.choice(('apple', 'banana', 'carrot'), size=n_rows),
            'timestamp': pd.date_range("20130101", periods=n_rows, freq="s"),
            'integer': np.random.choice(range(0,10), size=n_rows),
            'float': np.random.uniform(size=n_rows),
        },
    )

    dataset.info()

This DataFrame is structured in the *tidy data* format.
In tidy data we have multiple columns of data that are collected in a Pandas DataFrame, where each column 
represents a value of a specific type.

..  image:: img/pandas/tidy_data.png

Let's consider another example::

    n = 1000

    data_array = np.random.uniform(size=(n,n))
    np.info(data_array)


Here we have a different data structure: we have a two-dimensional array of numbers.
This is different to a Pandas DataFrame as data is stored as one contiguous block instead of individual columns.
This also means that the whole array must have one data type.


..  figure:: https://github.com/elegant-scipy/elegant-scipy/raw/master/figures/NumPy_ndarrays_v2.png

    Source: `Elegant Scipy <https://github.com/elegant-scipy/elegant-scipy>`__

Now the question is: **Can the data be saved to the disk without changing the data format?**

For this we need a **file format** that can easily store our **data structure**.

.. admonition:: Data type vs. data structure vs. file format
   :class: dropdown

   - **Data type:** Type of a single piece of data (integer, string, float, ...).
   - **Data structure:** How the data is organized in memory (individual columns, 2D-array, nested dictionaries, ...).
   - **File format:** How the data is organized when it is saved to the disk (columns of strings, block of binary data, ...).

   For example, a black and white image stored as a .png-file (**file format**)
   might be stored in memory as an NxM array (**data structure**) of integers (**data type**) with each entry representing 
   the color value of the pixel.

What to look for in a file format?
----------------------------------

When deciding which file format you should use for your program, you should remember the following:

**There is no file format that is good for every use case.**

and

**It is very likely, that a good format already exists for your use case.**

There are, indeed, various standard file formats for various use cases:

.. figure:: https://imgs.xkcd.com/comics/standards.png

   Source: `xkcd #927 <https://xkcd.com/927/>`__.

Usually, you'll want to consider the following things when choosing a file format:

1. Is the file format good for my data structure (is it fast/space efficient/easy to use)?
2. Is everybody else / leading authorities in my field recommending a certain format?
3. Do I need a human-readable format or is it enough to work on it using code?
4. Do I want to archive / share the data or do I just want to store it while I'm working?

Pandas supports `many file formats <https://pandas.pydata.org/docs/user_guide/io.html>`__ for tidy data and Numpy supports `some file formats <https://numpy.org/doc/stable/reference/routines.io.html>`__ for array data.
However, there are many other file formats that can be used through other libraries.

Table below describes some data formats:

.. list-table::
   :header-rows: 1

   * - | Name:
     - | Human
       | readable:
     - | Space
       | efficiency:
     - | Arbitrary
       | data:
     - | Tidy
       | data:
     - | Array
       | data:
     - | Long term
       | storage/sharing:

   * - :ref:`Pickle <pickle>`
     - ❌
     - 🟨
     - ✅
     - 🟨
     - 🟨
     - ❌

   * - :ref:`CSV <csv>`
     - ✅
     - ❌
     - ❌
     - ✅
     - 🟨
     - ✅

   * - :ref:`Feather <feather>`
     - ❌
     - ✅
     - ❌
     - ✅
     - ❌
     - ❌

   * - :ref:`Parquet <parquet>`
     - ❌
     - ✅
     - 🟨
     - ✅
     - 🟨
     - ✅

   * - :ref:`npy <npy>`
     - ❌
     - 🟨
     - ❌
     - ❌
     - ✅
     - ❌

   * - :ref:`HDF5 <hdf5>`
     - ❌
     - ✅
     - ❌
     - ❌
     - ✅
     - ✅

   * - :ref:`NetCDF4 <netcdf4>`
     - ❌
     - ✅
     - ❌
     - ❌
     - ✅
     - ✅

   * - :ref:`JSON <json>`
     - ✅
     - ❌
     - 🟨
     - ❌
     - ❌
     - ✅

   * - :ref:`Excel <excel>`
     - ❌
     - ❌
     - ❌
     - 🟨
     - ❌
     - 🟨

   * - :ref:`Graph formats <graph>`
     - 🟨
     - 🟨
     - ❌
     - ❌
     - ❌
     - ✅

.. important::

    - ✅ : Good
    - 🟨 : Ok / depends on a case
    - ❌ : Bad


A More in depth analysis of the file formats mentioned above, can be found `here <work-with-data>``

Pros and cons
-------------

Let's have a general look at pros and cons of some types of file formats

Binary File formats
~~~~~~~~~~~~~~~~~~~

Good things 
+++++++++++

- Can represent floating point numbers with full precision.
- Can potentially save lots of space, especially, when storing numbers.
- Data reading and writing is usually much faster than loading from text files, since the format contains information
  about the data structure, and thus memory allocation can be done more efficiently.  
- More explicit specification for storing multiple data sets and metadata in the same file.
- Many binary formats allow for partial loading of the data.
  This makes it possible to work with datasets that are larger than your computer's memory.

Bad things
++++++++++

- Commonly requires the use of a specific library to read and write the data
- Library specific formats can be version dependent
- Not human readable
- Sharing can be more difficult ( requires some expertise to be able to read the data )
- Might require more documentation efforts

Textual formats
~~~~~~~~~~~~~~~

Good things
+++++++++++

- Human readable
- Easy to check for (structural) errors
- Supported by many tool out of the box
- Easily shared

Bad things
++++++++++

- Can be slow to read and write
- high potential to increase required disk space substantially (e.g. when storing floating point numbers as text)
- Prone to loosing precision when storing floating point numbers
- Muli-dimensional data can be hard to represent
- While the data format might be specified, the data structure might not be clear when starting to read the data.

Further considerations
~~~~~~~~~~~~~~~~~~~~~~

- The closer your stored data is to the code, the more likely it depends on the environment you are working in. 
  If you e.g. `pickle` a generated model, you can only be sure, that the model will work as intended, if you 
  load it in an environment, that has the same versions of all libraries the model depends on. 


Exercise
--------

.. challenge::

    You have a model that you have been training for a while. 
    Lets assume it's a relatively simple neural network (consisting of a network structure and it's associated weights).
    
    Let's consider 2 scenarios

    A: You have a different project, that is supposed to take this model, and do some processing with it to determine
       it's efficiency after different times of training. 

    B: You want to publish the model and make it available to others. 

    What are good options to store the model in each of these scenarios?

.. solution::

    A: Some export into a binary format that can be easily read. E.g. pickle or a specific export function from the libbrary you use.
       It also depends, on whether you intend to make the intermediary steps available to others.
       If you do, you might also want to consider storing structure and weights separately or use a format specific for the 
       type of model you are training, to keep the data independent of the library.

    B: You might want to consider a more general format, that is supported by many libraries, e.g. ONNX, or a format that is 
       specifically designed for the type of model you are training. 
       You might also want to consider additionally storing the model in a way that is easily readable by humans, to make it easier for others
       to understand the model.


Efficient use of untidy data
----------------------------

Many data analysis tools (like Pandas) require tidy data, but some data is not in a suitable format.
What we have seen often in the past is people then not using the powerful tools, but write comple scripts that 
extract individual pieces from the data each time they need to do a calculation. 

Example of "questionable pipeline":
length_array = []

for entry in data:
    length_array.append(len(entry['length']))
...




Example of pipeline with initial conversion to pandas e.g. via json_normalize






Things to remember
------------------

1. **There is no file format that is good for every use case.**
2. Usually, your research question determines which libraries you want to use to solve it.
   Similarly, the data format you have determines file format you want to use.
3. However, if you're using a previously existing framework or tools or you work in a specific field, you should prioritize using the formats that are used in said framework/tools/field.
4. When you're starting your project, it's a good idea to take your initial data, clean it, and store the results in a good binary format that works as a starting point for your future analysis.
   If you've written the cleaning procedure as a script, you can always reproduce it.
5. Throughout your work, you should use code to turn important data to human-readable format (e.g. plots, averages, :meth:`pandas.DataFrame.head`), not to keep your full data in a human-readable format.
6. Once you've finished, you should store the data in a format that can be easily shared to other people.


See also
--------

- `Pandas' IO tools <https://pandas.pydata.org/docs/user_guide/io.html>`__
- `Tidy data comparison notebook <https://github.com/AaltoSciComp/python-for-scicomp/tree/master/extras/data-formats-comparison-tidy.ipynb>`__
- `Array data comparison notebook <https://github.com/AaltoSciComp/python-for-scicomp/tree/master/extras/data-formats-comparison-array.ipynb>`__


.. keypoints::

   - Pandas can read and write a variety of data formats.
   - There are many good, standard formats, and you don't need to create your own.
   - There are plenty of other libraries dedicated to various formats.
