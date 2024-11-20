In depth analysis of some selected file formats
===============================================

Here is a selection of file formats that are commonly used in data science. They are somewhat ordered by their intended use.

Storing arbitrary Python objects
--------------------------------


.. _pickle:

Pickle
******

.. admonition:: Key features

   - **Type**: Binary format
   - **Packages needed:** None (:mod:`pickle`-module is included with Python).
   - **Space efficiency:** 🟨
   - **Arbitrary data:** ✅
   - **Tidy data:** 🟨
   - **Array data:** 🟨
   - **Long term archival/sharing:** ❌! See warning below.
   - **Best use cases:** Saving Python objects for debugging.

.. warning::

    Loading pickles that you have not created is
    risky as they can contain arbitrary executable code.

    Do not unpickle objects from sources that you do not trust!

:mod:`Pickle <pickle>` is Python's own serialization library.
It allows you to store Python objects into a binary file, but it is not a format you will want to use for long term storage or data sharing.
It is best suited for debugging your code by saving the Python variables for later inspection::

    import pickle

    with open('data_array.pickle', 'wb') as f:
        pickle.dump(data_array, f)

    with open('data_array.pickle', 'rb') as f:
        data_array_pickle = pickle.load(f)


Exercise 1
----------

.. challenge::

    - Create an arbitrary python object (for example, a string or a list). Pickle it.

      Read the pickled object back in and check if it matches the original one.

.. solution::

    .. code-block:: python

        import pickle

        my_object=['test', 1, 2, 3]

        with open('string.pickle', 'wb') as f:
            pickle.dump(my_object, f)


        with open('string.pickle', 'rb') as f:
            my_pickled_object = pickle.load(f)

        print(my_object, my_pickled_object)
        print(my_object == my_pickled_object)


Storing tidy data
-----------------

.. _csv:

CSV (comma-separated values)
****************************

.. admonition:: Key features

   - **Type:** Text format
   - **Packages needed:** numpy, pandas
   - **Space efficiency:** ❌
   - **Arbitrary data:** ❌
   - **Tidy data:** ✅
   - **Array data:** 🟨
   - **Long term archival/sharing:** ✅
   - **Best use cases:** Sharing data. Small data. Data that needs to be human-readable.

CSV is by far the most popular file format, as it is human-readable and easily shareable.
However, it is not the best format to use when you're working with big data.

Pandas has a very nice interface for writing and reading CSV files with `to_csv <https://pandas.pydata.org/docs/user_guide/io.html#io-store-in-csv>`__- and `read_csv <https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table>`__-functions::

    dataset.to_csv('dataset.csv', index=False)

    dataset_csv = pd.read_csv('dataset.csv')

Numpy has `routines <https://numpy.org/doc/stable/reference/routines.io.html#text-files>`__ for saving and loading arrays as CSV files as well::

    np.savetxt('data_array.csv', data_array)

    data_array_csv = np.loadtxt('data_array.csv')

.. admonition:: Storing data in CSVs can reduce data precision
   :class: dropdown

    When working with floating point numbers you should be careful to save the data with enough decimal places so that you won't lose precision.

    For example, double-precision floating point numbers have `~16 decimal places of precision <https://en.wikipedia.org/wiki/Double-precision_floating-point_format>`__, but if you use normal Python to write these numbers, you can easily lose some of that precision.
    Let's consider the following example:

    .. code-block:: python

        import numpy as np
        test_number = np.sqrt(2)
        # Write the number in a file
        test_file = open('sqrt2.csv', 'w')
        test_file.write('%f' % test_number)
        test_file.close()
        # Read the number from a file
        test_file = open('sqrt2.csv', 'r')
        test_number2 = np.float64(test_file.readline())
        test_file.close()
        # Calculate the distance between these numbers
        print(np.abs(test_number - test_number2))

    CSV writing routines in Pandas and numpy try to avoid problems such as these by writing the floating point numbers with enough precision, but even they are not infallible.
    We can check whether our written data matches the generated data:

    .. code-block:: python

        dataset.compare(dataset_csv)

        np.all(data_array == data_array_csv)

    In our case some rows of ``dataset_csv`` loaded from CSV do not match the original ``dataset`` as the last decimal can sometimes be rounded due to `complex technical reasons <https://docs.python.org/3/tutorial/floatingpoint.html#representation-error>`__.

    Storage of these high-precision CSV files is usually very inefficient storage-wise.

    Binary files, where floating point numbers are represented in their native binary format, do not suffer from such problems.


.. _feather:


Feather
*******

.. admonition:: Requires additional packages
   :class: dropdown


    Using Feather requires `pyarrow-package <https://arrow.apache.org/docs/python>`__ to be installed.

    You can try installing pyarrow with

    .. code-block:: bash

        !pip install pyarrow

    or you can take this as a demo.

.. admonition:: Key features

   - **Type:** Binary format
   - **Packages needed:** pandas, pyarrow
   - **Space efficiency:** ✅
   - **Arbitrary data:** ❌
   - **Tidy data:** ✅
   - **Array data:** ❌
   - **Long term archival/sharing:** ❌
   - **Best use cases:** Temporary storage of tidy data.

`Feather <https://arrow.apache.org/docs/python/feather.html>`__ is a file format for storing data frames quickly.
There are libraries for Python, R and Julia.

We can work with Feather files with :external+pandas:ref:`to_feather- and read_feather-functions <io.feather>`::

    dataset.to_feather('dataset.feather')
    dataset_feather = pd.read_feather('dataset.feather')

Feather is not a good format for storing array data, so we won't present an example of that here.


.. _parquet:


Parquet
*******

.. admonition:: Requires additional packages
   :class: dropdown

    Using Parquet requires `pyarrow-package <https://arrow.apache.org/docs/python>`__ to be installed.

    You can try installing PyArrow with

    .. code-block:: bash

        !pip install pyarrow

    or you can take this as a demo.

.. admonition:: Key features

   - **Type:** Binary format
   - **Packages needed:** pandas, pyarrow
   - **Space efficiency:** ✅
   - **Arbitrary data:** 🟨
   - **Tidy data:** ✅
   - **Array data:** 🟨
   - **Long term archival/sharing:** ✅
   - **Best use cases:** Working with big datasets in tidy data format. Archival of said data.

`Parquet <https://arrow.apache.org/docs/python/parquet.html>`__ is a standardized open-source
columnar storage format that is commonly used for storing big data.
Parquet is usable from many different languages (C, Java, Python, MATLAB, Julia, etc.).

We can work with Parquet files with :external+pandas:ref:`to_parquet- and read_parquet-functions <io.parquet>`::

    dataset.to_parquet('dataset.parquet')
    dataset_parquet = pd.read_parquet('dataset.parquet')

Parquet can be used to store arbitrary data and arrays as well, but doing that is more complicated so we won't do that here.


Exercise 2
----------

.. challenge::

    - Create the example ``dataset``:

      .. code-block:: python

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

    - Save the dataset ``dataset`` as CSV. Load the dataset into a variable ``dataset_csv``.
    - Use ``dataset.compare(dataset_csv)`` to check if loaded dataset matches the original one.

.. solution::

    .. code-block:: python

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

      dataset.to_csv('dataset.csv', index=False)

      dataset_csv = pd.read_csv('dataset.csv')

      print(dataset.compare(dataset_csv))

    Dataset might not be completely the same. Sometimes the CSV format cannot
    fully represent a floating point value, which will result in rounding errors.

Storing array data
------------------


.. _npy:


npy (numpy array format)
************************

.. admonition:: Key features

   - **Type**: Binary format
   - **Packages needed:** numpy
   - **Space efficiency:** 🟨
   - **Arbitrary data:** ✅
   - **Tidy data:** ❌
   - **Array data:** ✅
   - **Long term archival/sharing:** ❌
   - **Best use cases:** Saving numpy arrays temporarily.

If you want to temporarily store numpy arrays, you can use the :func:`numpy.save`- and :func:`numpy.load`-functions::

    np.save('data_array.npy', data_array)
    data_array_npy = np.load('data_array.npy')

There also exists :func:`numpy.savez`-function for storing multiple datasets in a single file::

    np.savez('data_arrays.npz', data_array0=data_array, data_array1=data_array)
    data_arrays = np.load('data_arrays.npz')
    data_arrays['data_array0']

For big arrays it's good idea to check other binary formats such as HDF5 or NetCDF4.

``np.save``- and ``np.savez``-functions work with
`sparse matrices <https://docs.scipy.org/doc/scipy/reference/sparse.html>`__,
but one can also use dedicated
`scipy.sparse.save_npz <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.save_npz.html>`__- and
`scipy.sparse.load_npz <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.load_npz.html>`__-functions.
Storing sparse matrices using these functions can give huge storage savings.


.. _hdf5:


HDF5 (Hierarchical Data Format version 5)
*****************************************

.. admonition:: Key features

   - **Type:** Binary format
   - **Packages needed:** numpy, pandas, PyTables, h5py
   - **Space efficiency:** ✅
   - **Arbitrary data:** ❌
   - **Tidy data:** ❌
   - **Array data:** ✅
   - **Long term archival/sharing:** ✅
   - **Best use cases:** Working with big datasets in array data format.

HDF5 is a high performance storage format for storing large amounts of data in multiple datasets in a single file.
It is especially popular in fields where you need to store big multidimensional arrays such as physical sciences.

Pandas allows you to store tables as HDF5 with `PyTables <https://www.pytables.org/>`_, which uses HDF5 to write the files.
You can create a HDF5 file with :external+pandas:ref:`to_hdf- and read_parquet-functions <io.hdf5>`::

    dataset.to_hdf('dataset.h5', key='dataset', mode='w')
    dataset_hdf5 = pd.read_hdf('dataset.h5')

For writing data that is not a table, you can use the excellent `h5py-package <https://docs.h5py.org/en/stable/>`__::

    import h5py

    # Writing:

    # Open HDF5 file
    h5_file = h5py.File('data_array.h5', 'w')
    # Write dataset
    h5_file.create_dataset('data_array', data=data_array)
    # Close file and write data to disk. Important!
    h5_file.close()

    # Reading:

    # Open HDF5 file again
    h5_file = h5py.File('data_array.h5', 'r')
    # Read the full dataset
    data_array_h5 = h5_file['data_array'][()]
    # Close file
    h5_file.close()


.. _netcdf4:


NetCDF4 (Network Common Data Form version 4)
********************************************

.. admonition:: Requires additional packages
   :class: dropdown

    Using NetCDF4 requires `netCDF4 <https://unidata.github.io/netcdf4-python>`__- or `h5netcdf <https://github.com/h5netcdf/h5netcdf>`__-package to be installed.
    h5netcdf is often mentioned as being faster to the official netCDF4-package, so we'll be using it in the example.

    A great NetCDF4 interface is provided by a `xarray-package <https://docs.xarray.dev/en/stable/getting-started-guide/quick-overview.html#read-write-netcdf-files>`__.

    You can try installing these packages with

    .. code-block:: bash

        !pip install h5netcdf xarray

    or you can take this as a demo.

.. admonition:: Key features

   - **Type**: Binary format
   - **Packages needed:** pandas, netCDF4/h5netcdf, xarray
   - **Space efficiency:** ✅
   - **Arbitrary data:** ❌
   - **Tidy data:** ❌
   - **Array data:** ✅
   - **Long term archival/sharing:** ✅
   - **Best use cases:** Working with big datasets in array data format. Especially useful if the dataset contains spatial or temporal dimensions. Archiving or sharing those datasets.

NetCDF4 is a data format that uses HDF5 as its file format, but it has standardized structure of datasets and metadata related to these datasets.
This makes it possible to be read from various different programs.

NetCDF4 is a common format for storing large data from big simulations in physical sciences.

Using interface provided by ``xarray``::

    # Write tidy data as NetCDF4
    dataset.to_xarray().to_netcdf('dataset.nc', engine='h5netcdf')
    # Read tidy data from NetCDF4
    import xarray as xr
    dataset_xarray = xr.open_dataset('dataset.nc', engine='h5netcdf')
    dataset_netcdf4 = dataset_xarray.to_pandas()
    dataset_xarray.close()

Working with array data is easy as well::

    # Write array data as NetCDF4
    xr.DataArray(data_array).to_netcdf('data_array.nc', engine='h5netcdf')
    # Read array data from NetCDF4
    data_array_xarray = xr.open_dataarray('data_array.nc', engine='h5netcdf')
    data_array_netcdf4 = data_array_xarray.to_numpy()
    data_array_xarray.close()

The advantage of NetCDF4 compared to HDF5 is that one can easily add other metadata e.g. spatial dimensions (``x``, ``y``, ``z``) or timestamps (``t``) that tell where the grid-points are situated.
As the format is standardized, many programs can use this metadata for visualization and further analysis.

Exercise 3
----------

.. challenge::

    - Create an example numpy array:

      .. code-block:: python

        n = 1000

        data_array = np.random.uniform(size=(n,n))

    - Store the array as a npy.
    - Read the dataframe back in and compare it to the original one. Does the data match?

.. solution::

   .. code-block:: python

      import numpy as np

      n = 1000

      data_array = np.random.uniform(size=(n,n))

      np.save('data_array.npy', data_array)
      data_array_npy = np.load('data_array.npy')
      np.all(data_array == data_array_npy)


Other file formats
------------------


.. _json:

JSON (JavaScript Object Notation)
*********************************

.. admonition:: Key features

   - **Type**: Text format
   - **Packages needed:** None (:mod:`json`-module is included with Python).
   - **Space efficiency:** ❌
   - **Arbitrary data:** 🟨
   - **Tidy data:** ❌
   - **Array data:** ❌
   - **Long term archival/sharing:** ✅
   - **Best use cases:** Saving nested/relational data, storing web requests.

JSON is a popular human-readable data format.
It is especially common when dealing with web applications (REST-APIs etc.).

You rarely want to keep your data in this format, unless you're working with
nested data with multiple layers or lots of interconnections.

Similarly to other popular files, Pandas can write and read json files with :meth:`~pandas.DataFrame.to_json`- and :func:`~pandas.read_json`-functions::

    dataset.to_json('dataset.json')
    dataset_json = pd.read_json('dataset.json')


.. _excel:

Excel
*****

.. admonition:: Requires additional packages
   :class: dropdown

   Using Excel files with Pandas requires `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`__-package to be installed.

.. admonition:: Key features

   - **Type**: Text format
   - **Packages needed:** `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`__
   - **Space efficiency:** ❌
   - **Arbitrary data:** ❌
   - **Tidy data:** 🟨
   - **Array data:** ❌
   - **Long term archival/sharing:** ✅
   - **Best use cases:** Sharing data in many fields. Quick data analysis.

Excel is very popular in social sciences and economics.
However, it is `not a good format <https://www.bbc.com/news/technology-54423988>`__ for data science.

See Pandas' documentation on :external+pandas:ref:`working with Excel files <io.excel>`.


.. _graph:

Graph formats (adjency lists, gt, GraphML etc.)
***********************************************

.. admonition:: Key features

   - **Type**: Many different formats
   - **Packages needed:** Depends on a format.
   - **Space efficiency:** 🟨
   - **Arbitrary data:** ❌
   - **Tidy data:** ❌
   - **Array data:** ❌
   - **Long term archival/sharing:** 🟨
   - **Best use cases:** Saving graphs or data that can be represented as a graph.

There are plenty of data formats for storing graphs.
We won't list them here as optimal data format depends heavily on the graph structure.

One can use functions in libraries such as
`networkx <https://networkx.org/documentation/stable/reference/readwrite/index.html>`__,
`graph-tool <https://graph-tool.skewed.de/static/doc/quickstart.html#graph-i-o>`__,
`igraph <https://igraph.readthedocs.io/en/stable/tutorial.html#igraph-and-the-outside-world>`__
to read and write graphs.

