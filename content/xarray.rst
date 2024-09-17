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

