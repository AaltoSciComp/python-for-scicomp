Data formats with Pandas and Numpy
==================================

.. questions::

   - How do you store your data right now?
   - How much time do you think is spent doing your calculation vs
     reading/writing your data?

.. objectives::

   - Learn the distinguishing characteristics of different data formats
   - Learn how Pandas to read and write data in a variety of formats


What is a data format?
----------------------

Whenever you have data (e.g. measurement data, simulation results, analysis results), you'll need a way to store it.
This applies both when

1. you're storing the data in memory while you're working on it
2. you're storing it to a disk for later work

Let's consider the following Pandas DataFrame with various different columns::

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

    print(dataset.head())

This DataFrame already has a data format: it is in the tidy data format!
In tidy data format we have multiple columns of data that are collected in a Pandas DataFrame.

Let's consider another example::

    n = 1000

    data_array = np.random.uniform(size=(n,n))
    data_array

Here we have a different data format: we have a two-dimentional array of numbers.
This is different to Pandas DataFrame as data is stored as one contiguous block instead of individual columns.
This also means that the whole array must have one specified data type.

Now the question is: can we store these datasets in a file in a way that **keeps our data format intact**?

For this we need a **file format** that supports our chosen **data format**.

Fortunately Pandas has support for many data formats for tidy data.
More info on is provided in the excellent `Pandas' IO tools-page <https://pandas.pydata.org/docs/user_guide/io.html>`__ .

Let's go through some of the most popular file formats and how to use them.


Quick overview of different file formats
----------------------------------------

All file formats can be split into two types:

1. Text-based formats, that store the data as human-readable text.
2. Binary-based formats, that store the data as machine-readable binary.

We'll check the difference between text-based and binary-based formats after we introduce the formats.

Another way of thinking about file formats is to consider the usability (speed, data size) with certain use cases:

1. Formats that are meant for storing tidy data aka. columnar data. In this data format the data is organized as columns with multiple rows (for example, Pandas DataFrames).
2. Formats that are meant for storing numeric arrays of (possibly) multiple dimensions. In this data format the data is organized as arrays of numbers (for example, multidimensional Numpy arrays).

Third way of thinking about file format is its longevity:

1. Formats that are easy to share or archive.
2. Formats that are meant for temporary storage of the data.

Here's a list of common data formats and use cases:

+-------------+----------------+-----------------------+------------------------+--------------+
| File format | Format type    | Usability (tidy data) | Usability (array data) | Longevity    |
+=============+================+=======================+========================+==============+
| CSV         | text           | bad                   | bad                    | Good         |
+-------------+----------------+-----------------------+------------------------+--------------+
| Feather     | binary         | great                 | bad                    | Bad          |
+-------------+----------------+-----------------------+------------------------+--------------+
| Parquet     | binary         | great                 | it's complicated       | Good         |
+-------------+----------------+-----------------------+------------------------+--------------+
| HDF5        | binary         | good with numbers     | good                   | Ok           |
+-------------+----------------+-----------------------+------------------------+--------------+
| NetCDF4     | binary         | good with numbers     | good                   | Good         |
+-------------+----------------+-----------------------+------------------------+--------------+
| npy         | binary         | really bad            | good                   | Bad          |
+-------------+----------------+-----------------------+------------------------+--------------+
| pickle      | binary         | ok                    | ok                     | Really bad   |
+-------------+----------------+-----------------------+------------------------+--------------+
| json        | text           | bad                   | bad                    | Good         |
+-------------+----------------+-----------------------+------------------------+--------------+


+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| File format | Format type    | Packages needed  | Best use cases                                                                      |
+=============+================+==================+=====================================================================================+
| CSV         | text           | pandas           | Sharable data. Small data. Human readable debug data.                               |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| Feather     | binary         | pyarrow          | Temporary storage for tabular data while you're working on the data.                |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| Parquet     | binary         | pyarrow          | Storage for large-scale tabular data. Multidimensional arrays need to be flattened. |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| HDF5        | binary         | PyTables, h5py   | Storage of large scale numeric data.                                                |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| NetCDF4     | binary         | netCDF4, xarray  | Storage and archival of large scale numeric data.                                   |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| npy         | binary         | numpy            | Temporary storage of Numpy arrays while you're working on the data.                 |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| pickle      | binary         | none             | Temporary storage of Python objects for debugging.                                  |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+
| json        | text           | none             | Sharable data. Especially data from internet services. Dictionary data.             |
+-------------+----------------+------------------+-------------------------------------------------------------------------------------+

Typically, you'll want to choose a file format that is suitable for your data format and your specific needs.
It is important to note, that if you're using a previously existing framework or tools or you work in a specific field, you should prioritize using the formats that are used in said framework/tools/field.


Using different file formats
----------------------------


CSV (text)
**********

CSV is by far the most popular data format, as it is human-readable and easily shareable.
However, it is not the best format to use when you're working with big data.

Pandas has a very nice interface for writing CSV files.
Let's write our dataset into a CSV file using the `to_csv-function <https://pandas.pydata.org/docs/user_guide/io.html#io-store-in-csv>`__::

    dataset.to_csv('dataset.csv', index=False)

This will create a ``dataset.csv``-file.
We can load the new CSV-file using Pandas' `read_csv-function <https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table>`__::

    dataset_csv = pd.read_csv('dataset.csv')

Numpy has `routines <https://numpy.org/doc/stable/reference/routines.io.html#text-files>`__ for saving and loading CSV files as arrays as well ::

    np.savetxt('data_array.csv', data_array)

    data_array_csv = np.loadtxt('data_array.csv')


Feather (binary)
****************

`Feather <https://arrow.apache.org/docs/python/feather.html>`_ is a file format for storing data frames quickly in a language agnostic way (there are libraries for Python, R and Julia).

Again, we can work with Feather files with `to_feather- and read_feather-functions <https://pandas.pydata.org/docs/user_guide/io.html#io-feather>`__::

    dataset.to_feather('dataset.feather')
    dataset_feather = pd.read_feather('dataset.feather')

Using Feather requires `pyarrow-package <https://arrow.apache.org/docs/python>`__ to be installed.


Parquet (binary)
****************

`Parquet <https://arrow.apache.org/docs/python/parquet.html>`_ is a standardized open-source columnar storage format that is commonly used for storing big data in machine learning.

Again, we can work with Parquet files with `to_parquet-and read_parquet-functions <https://pandas.pydata.org/docs/user_guide/io.html#io-parquet>`__::

    dataset.to_parquet('dataset.parquet')
    dataset_parquet = pd.read_parquet('dataset.parquet')

Like Feather, using Parquet requires `pyarrow-package <https://arrow.apache.org/docs/python/>`__ to be installed.


HDF5 (binary)
*************

HDF5 (Hierarchical Data Format) is a high performance storage format for storing large amounts of data in multiple datasets in a single file.
It is especially popular in fields where you need to store big multidimensional arrays such as physical sciences.

Pandas allows you to store tables as HDF5 with `PyTables <https://www.pytables.org/>`_, which uses HDF5 to write the files.
You can create a HDF5 file with `to_hdf- and `read_parquet-functions <https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5>`__::

    dataset.to_hdf('dataset.h5', key='dataset', mode='w')
    dataset_hdf5 = pd.read_hdf('dataset.h5')
    
PyTables comes installed with the default Anaconda installation.

For writing data that is not a table, you can use the excellent `h5py-package <https://docs.h5py.org/en/stable/>`__. It comes with Anaconda as well. 


NetCDF4 (binary)
****************

NetCDF4 (Network Common Data Form) is a data format that uses HDF5 as its file format, but it has standardized structure of datasets and metadata related to these datasets.
This makes it possible to be read from various different programs.

NetCDF4 is by far the most common format for storing large data from big simulations in physical sciences.

You can use `NetCDF-Python-package <https://unidata.github.io/netcdf4-python>`__ and the excellent `xarray-package <https://xarray.pydata.org/en/stable/getting-started-guide/quick-overview.html#read-write-netcdf-files>`__ for accessing NetCDF4 files::

    # Write dataset as NetCDF4
    dataset_xarray_write = dataset.to_xarray()
    dataset_xarray_write.to_netcdf('dataset.nc')
    # Read dataset from NetCDF4
    import xarray as xr
    dataset_xarray_read = xr.open_dataset('dataset.nc')
    dataset_xarray = dataset_xarray_read.to_pandas()


npy (binary)
************

If you want to temporarily store numpy arrays, you can use the `numpy.save-function <https://numpy.org/doc/stable/reference/generated/numpy.save.html>`_ to quickly store a numpy array::

    np.save('data_array.npy', data_array)
    data_array_npy = np.load('data_array.npy')

For big arrays it's good idea to check other binary formats such as HDF5 or xarray.


Why would I need to use a binary format?
----------------------------------------

Binary files come with various benefits compared to text files.

1. They can represent floating point numbers with full precision.
   By storing a floating point number in a CSV-file, you usually reduce the precision from double precision (:math:`\epsilon \approx (10^{-16})`) to the number of digits you have specified.
   For example, try::

       dataset.compare(dataset_csv)

       dataset.compare(dataset_hdf5)

2. Storing data in binary format can potentially save lots of space.
   This is because you do not need to write numbers as characters.
   Additionally some file formats support compression of the data.
3. Data loading from binary files is usually much faster than loading from text files.
   This is because memory can be allocated for the data before data is loaded as the type of data in columns is known.
4. You can often store multiple datasets and metadata to the same file.
5. Many binary formats allow for partial loading of the data.
   This makes it possible to work with datasets that are larger than your computer's memory.

For the tidy ``dataset`` we had, we can test the performance of the different file formats:

**Performance when writing tidy dataset:**

+-------------+----------------+-----------------+----------------+----------------------+
| File format | File size [MB] | Write time [ms] | Read time [ms] | Data matches exactly |
+=============+================+=================+================+======================+
| CSV         | 4.571571       | 0.355826        | 0.355826       | False                |
+-------------+----------------+-----------------+----------------+----------------------+
| Feather     | 2.202845       | 0.014178        | 0.014178       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+
| Parquet     | 1.820971       | 0.043103        | 0.043103       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+
| HDF5        | 4.892296       | 0.050013        | 0.050013       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+
| NetCDF4     | 8.396764       | 0.124124        | 0.124124       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+

The relatively poor performance of HDF5 based formats in this case is due to the data being mostly one dimensional columns full of character strings.
For writing the floating point array `data_array`, the performance is be much better.

**Performance when writing data array:**

+-------------+----------------+-----------------+----------------+----------------------+
| File format | File size [MB] | Write time [ms] | Read time [ms] | Data matches exactly |
+=============+================+=================+================+======================+
| CSV         | 23.841858      | 0.919903        | 0.870455       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+
| npy         | 7.629517       | 0.013368        | 0.002773       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+
| NetCDF4     | 7.637207       | 0.016921        | 0.007093       | True                 |
+-------------+----------------+-----------------+----------------+----------------------+

For this kind of a data, HDF5 formats are much better.


Things to remember
------------------

1. Usually, your research question determines which libraries you want to use to solve it.
   Similarly, the data format you have chosen determines file format you want to use.
2. However, if you're using a previously existing framework or tools or you work in a specific field, you should prioritize using the formats that are used in said framework/tools/field.
3. When you're starting your project, it's a good idea to take your initial data, clean it, and store the results in a good binary format that works as a starting point for your future analysis.
   If you've written the cleaning procedure as a script, you can always reproduce it.
4. Throughout your work, you should use code to turn important data to human-readable format (e.g. plots, averages, ``DataFrame.head()``), not to keep your full data in a human-readable format.
5. Once you've finished, you should store the data in a format that can be easily shared to other people.

Exercise 1
----------

.. challenge::

    - Create a dataframe. Store it as a CSV.
    - Read the dataframe back in and compare it to the original one. Does the data match?
    - Store the dataframe in a binary format (for example, PyTables).
    - Read the dataframe back in and compare it to the original one. Does the data match?

.. solution::

   .. code-block:: python

      import numpy as np
      import pandas as pd

      data = pd.DataFrame({ 'my_data': [3.1415, 2.718, 1.6180]})

      data.to_csv('data.csv', index=False)

      data_from_csv = pd.read_csv('data.csv')
      data.compare(data_from_csv)

      data.to_hdf('data.h5', key='dataset', mode='w')

      data_from_hdf = pd.read_hdf('data.h5')
      data.compare(data_from_hdf)


Exercise 2
----------

.. challenge::

    - Create a numpy array. Store it as a npy.
    - Read the dataframe back in and compare it to the original one. Does the data match?

.. solution::

   .. code-block:: python

      import numpy as np

      my_array = np.array(10)

      np.save('my_array.npy', my_array)
      my_array_npy = np.load('my_array.npy')
      np.all(my_array == my_array_npy)


Other file formats
------------------

Pickle (binary)
***************

.. warning::

    Loading pickles that have been provided from untrusted sources is
    risky as they can contain arbitrary executable code.

`Pickle <https://docs.python.org/3/library/pickle.html>`__ is Python's own serialization library.
It allows you to store Python objects into a binary file.
It is not a format you will want to use in the long term.
It is best suited for debugging your code by saving the Python variables for later inspection::

    import pickle

    with open('data_array.pickle', 'wb') as f:
        pickle.dump(data_array, f)

    with open('data_array.pickle', 'rb') as f:
        data_array_pickle = pickle.load(f)


JSON (text)
***********

JSON is another popular human-readable data format.
It is especially common when dealing with web applications (REST-APIs etc.).
However, when you're working with big data, you rarely want to keep your data in this format.

Similarly to other popular files, Pandas can write and read json files with `to_json- <https://pandas.pydata.org/docs/user_guide/io.html#io-json-writer>`_ and `read_json <https://pandas.pydata.org/docs/user_guide/io.html#io-json-reader>`_-functions::

    dataset.to_json('dataset.json')
    dataset_json = pd.read_csv('dataset.json')

However, JSON is often used to represent hierarchical data with multiple layers or multiple connections. 
For such data you might need to do a lot more processing.


Excel (binary)
**************

Excel is very popular in social sciences and economics.
However, it is `not a good format <https://www.bbc.com/news/technology-54423988>`__ for data science.

See Pandas' documentation on `working with Excel files <https://pandas.pydata.org/docs/user_guide/io.html#excel-files>`_.

Using Excel files with Pandas requires `openpyxl-package <https://openpyxl.readthedocs.io/en/stable/>`_ to be installed.


See also
--------

- `Pandas' IO tools <https://pandas.pydata.org/docs/user_guide/io.html>`__ .
- `Tidy data comparison notebook <https://github.com/AaltoSciComp/python-for-scicomp/tree/master/extras/data-formats-comparison-tidy.ipynb>`__
- `Array data comparison notebook <https://github.com/AaltoSciComp/python-for-scicomp/tree/master/extras/data-formats-comparison-array.ipynb>`__


.. keypoints::

   - Pandas can read and write a variety of data formats.
   - There are many good, standard formats, and you don't need to create your own.
   - There are plenty of other libraries dedicated to various formats.