.. _xarray:

Xarray
======

.. questions::

        - How shall we deal with real-world datasets that are usually more than just raw numbers?
        - What is the advantage of using labelled multidimensional arrays?
        - What does Xarray add to Numpy and Pandas to address these questions?
     
.. objectives::

        - Learn how to apply operations over dimensions and select values by label
        - Understand Xarray's DataArrays and Datasets
        - Learn how to easily plot data in Xarray
        - Learn how to turn your own data into an Xarray Dataset


.. highlight:: python


With NumPy and Pandas we have already encountered two powerful libraries that can significantly simplify working with scientific data. Unfortunately, working with real-world data with these two libraries can still be challenging and cumbersome, especially when working with multi-dimensional data. Let's consider the following example: 

Imagine we have a dataset representing temperature measurements across different height, latitudes, and longitudes. We can store the temperature data as a 3D array where each axis corresponds to one of these dimensions: :: 

        import numpy as np
        # Create a 3D numpy array: height x latitude x longitude
        data = np.random.rand(10, 5, 5)  # 10 heights, 5 latitudes, 5 longitudes


So far, so good. Let's assume now we want to take a look at a specific value in the dataset at a certain height, latitude, and longitude. We could do this by indexing the array with the corresponding indices: ::

        # Get the temperature at height 3, latitude 2, longitude 4
        temperature = data[3, 2, 4]

OK, we got a value, but how do we know whether this value corresponds to the correct height, latitude and longitude? Are we sure that latitude was the second dimension in the dataset? Was it the second or third index that corresponds to the correct position? In pure NumPy, we are mostly left in the dark and need to manually keep track of these things. 

Unfortunately, Pandas isn't of much help either since it is not designed for data with more than 2 dimensions. Fortunately, some clever climate scientists have come up with a solution to this problem and created Xarray.

What is Xarray?
----------------

Xarray is a powerful Python library that introduces labelled multidimensional arrays.  
We will first download an dataset similar to the example above to illustrate the advantages of Xarray. We will cover how to transform your own data into an Xarray Dataset later in this lecture.

Let us open a python shell and download a public dataset: ::
        
        >>> from pythia_datasets import DATASETS
        >>> filepath = DATASETS.fetch('CESM2_sst_data.nc')

We can now import xarray and open the dataset. Le'ts take a look at the dataset: ::

        >>> import xarray as xr
        >>> ds = xr.open_dataset(filepath)
        >>> ds
        <xarray.Dataset> Size: 15MB
        Dimensions:                       (time1: 1, isobaric1: 29, y: 119, x: 268)
        Coordinates:
          * time1                         (time1) datetime64[ns] 8B 1993-03-13
          * isobaric1                     (isobaric1) float32 116B 100.0 125.0 ... 1e+03
          * y                             (y) float32 476B -3.117e+03 ... 714.1
          * x                             (x) float32 1kB -3.324e+03 ... 5.343e+03
        Data variables:
            u-component_of_wind_isobaric  (time1, isobaric1, y, x) float32 4MB ...
            LambertConformal_Projection   int32 4B ...
            lat                           (y, x) float64 255kB ...
            lon                           (y, x) float64 255kB ...
            Geopotential_height_isobaric  (time1, isobaric1, y, x) float32 4MB ...
            v-component_of_wind_isobaric  (time1, isobaric1, y, x) float32 4MB ...
            Temperature_isobaric          (time1, isobaric1, y, x) float32 4MB ...
        Attributes:
            Originating_or_generating_Center:     US National Weather Service, Nation...
            Originating_or_generating_Subcenter:  North American Regional Reanalysis ...
            GRIB_table_version:                   0,131
            Generating_process_or_model:          North American Regional Reanalysis ...
            Conventions:                          CF-1.6
            history:                              Read using CDM IOSP GribCollection v3
            featureType:                          GRID
            History:                              Translated to CF-1.0 Conventions by...
            geospatial_lat_min:                   10.753308882144761
            geospatial_lat_max:                   46.8308828962289
            geospatial_lon_min:                   -153.88242040519995
            geospatial_lon_max:                   -42.666108129242815

That was a lot of information at once, but let's break it down. 

        - Close to the top of the output we see the dimensions of the dataset: time1, isobaric1, y, and x. 
        - Below the dimensions, we see the coordinates of the dataset. These are the labels for the dimensions and give us the values of the dimension at each index.
        - The data variables are the actual data stored in the dataset.
        - At the bottom, we see the attributes of the dataset. This is a dictionary that stores metadata about the dataset.


The following image shows the structure of an Xarray Dataset:

        .. image:: img/xarray/xarray_dataset_image.png


Accessing and manipulating data in Xarray
-----------------------------------------

We can select a Data variable from the dataset using a dictionary-like syntax: ::

        temperature_data = ds['Temperature_isobaric']

The new variable ``temperature_data`` is a ``DataArray`` object. An xarray ``Dataset`` typically consists of multiple ``DataArrays``.

Xarray uses Numpy arrays under the hood, we can always access the raw data using the ``.values`` attribute: ::

        temperature_numpy = ds['Temperature_isobaric'].values

Xarray allows you to select data using the ``.sel()`` method, which uses the labels of the dimensions to extract data: ::

        ds['Temperature_isobaric'].sel(x='-3292.0078')

We can still access the same data by index using the ``.isel()`` method: ::

        ds['Temperature_isobaric'].isel(x=1)

Xarray also provides a wide range of aggregation methods such as ``sum()``, ``mean()``, ``median()``, ``min()``, and ``max()``. We can use these methods to aggregate data over one or multiple dimensions: ::

        # Calculate the mean over the 'isobaric1' dimension
        ds['Temperature_isobaric'].mean(dim='isobaric1')

Let's take a look at a concrete example and compare it to NumPy. We will calculate the max temperature over the 'isobaric1' dimension at a specific value for x: ::

        # Xarray
        ds['Temperature_isobaric'].sel(x='-3259.5447').max(dim='isobaric1').values

        # NumPy
        np.max(temperature_numpy[:, :, :, 2 ], axis = 1)


As you can see, the Xarray code is much more readable and we didn't need to keep track of the right indexes and order of the dimensions.

Plotting data in Xarray
-----------------------



Why use Xarray?
---------------

Personally, I believe it is more pedagogical to start with an existing dataset and showing all the cool Xarray features there instead of starting with setting up a dataset from scratch. Setting up a new dataset can be a little bit tedious. I suggest to address the following in this section:

        - Find open dataset that users can download and test (one option is the 'CESM2_sst_data' dataset used in https://foundations.projectpythia.org/core/xarray/computation-masking.html, the only downside of this dataset is the custom type for the time dimension which adds an additional layer of complexity)
        - Explain setup of Datasets (Dimensions, Coordinates, Data Variables, Attributes)
        - Explain how Xarray interacts with NumPy and Pandas
        - Arithmetic Operations on DataArrays
        - Selecting Data by Label
        - Aggregation Methods (sum(), mean(), median(), min(), and max())
        - Show comparison of Xarray and Numpy for the same operations (similar to https://nbviewer.org/github/TomNicholas/CPSFR_xarray_talk/blob/master/CPSFR_xarray.ipynb section "numpy vs xarray: Clearer syntax for typical operations")
        - Plotting Data in 1D and 2D and show histogram plot for higher dimensions
        - Mention gorupby() if time allows


Exercises 1 (if time allows)
----------------------------

.. challenge:: Exercises: Xarray-1

        Take example dataset and perform a series of operations on it using labels. If we use the global surface temperature data set the exercise could be to find the month with the highest average temperature at a given latitude.  

.. solution:: Solutions: Xarray-1

        Solution to Exercise 1 coming soon. 


Creating your own Xarray Dataset
--------------------------------

        - Show how to creation of a DataArray object
        - Show how to assign dimensions, coordinates, and attributes
        - Show how to create a Dataset object from multiple DataArrays
        - Show how to convert Xarray objects to and from pandas
        - Mention how to transform other dataformats into Xarray Datasets (e.g. NetCDF, HDF5, Zarr)


Exercises 2 (if time allows)
----------------------------

.. challenge:: Exercises: Xarray-2

        Provide two 3D numpy arrays and let participants turn them into an Xarray Dataset with the correct dimensions and coordinates.

.. solution:: Solutions: Xarray-2

        Solution to Exercise 2 coming soon.


Advanced Topics 
---------------

This will probably be a further reading section as I don't think we will have time to cover this in the workshop. 

        - Explain how xarray uses lazy loading into memory
        - Explain how to use Dask for parallel computing with memory chunking
        - Mention alternative numpy-like arrays (duck arrays), specifically Cupy (for GPU arrays) and Pint (adding units to arrays)
        - Explain xarray.register_dataset_accessor() for custom methods (this might seem very niche but I find myself using this all the time)

