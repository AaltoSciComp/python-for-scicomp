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

    n_rows = 1000

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

Now the question is: can we store this data in a file in a way that **keeps our data format intact**?

For this we need a **file format** that supports our chosen **data format**.

Fortunately Pandas has support for many data formats for tidy data.
More info on is provided in the excellent `Pandas' IO tools-page <https://pandas.pydata.org/docs/user_guide/io.html>`__ .

Let's go through some of the most popular file formats and how to use them.


File formats
------------

All file formats can be split into two types:

1. Text-based formats, that store the data as human-readable text.
2. Binary-based formats, that store the data as machine-readable binary.

We'll check the differences after we introduce the formats.


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

    dataset.to_hdf('dataset.h5')
    dataset_hdf5 = pd.read_hdf('dataset.h5')
    
PyTables comes installed with the default Anaconda installation.

For writing data that is not a table, you can use the excellent `h5py-package <https://docs.h5py.org/en/stable/>`__. It comes with Anaconda as well. 

NetCDF4 (binary)
****************

NetCDF4 (Network Common Data Form) is a data format that uses HDF5 as its file format, but it has standardized structure of datasets and metadata related to these datasets.
This makes it possible to be read from various different programs.

NetCDF4 is by far the most common format for storing large data from big simulations in physical sciences.

You can use `NetCDF-Python-package <https://unidata.github.io/netcdf4-python>`__ and the excellent `xarray-package <https://xarray.pydata.org/en/stable/getting-started-guide/quick-overview.html#read-write-netcdf-files>`__ for accessing NetCDF4 files.
You need to install `netCDF4` and `xarray` packages for this::

    # Write dataset as NetCDF4
    dataset_xarray_write = dataset.to_xarray()
    dataset_xarray_write.to_netcdf('dataset.nc')
    # Read dataset from NetCDF4
    import xarray as xr
    dataset_xarray_read = xr.open_dataset('dataset.nc')
    dataset_xarray = dataset_xarray_read.to_pandas()

Why would I need to use a binary format?
----------------------------------------

Binary formats come with various benefits.


Exercises 1
-----------

.. challenge:: Title

    - ...

.. solution::

    - ...
    
Other file formats
------------------

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

See Pandas' documentation on `working with Excel files <https://pandas.pydata.org/docs/user_guide/io.html#excel-files>`_.

Using Excel files with Pandas requires `openpyxl-package <https://openpyxl.readthedocs.io/en/stable/>`_ to be installed.

Real-world usage
----------------

Usually, the research question the libraries you want to use to solve it.
Similarly, the data defines the Python libraries you want to use to access the data.



Section
-------



See also
--------

...



.. keypoints::

   - Pandas can read and write a variety of data formats.
   - There are many good, standard formats, and you don't need to
     create your own.
   - There are plenty of other libraries dedicated to various
     formats.
