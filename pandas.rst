Pandas
======

.. questions::

   - How do we learn a new Python package?
   - How can I use pandas dataframes in my research? 

.. objectives::

   - Get a feeling for what can be done with the pandas package
   - Learn basic usage of pandas dataframes



Pandas is a Python package that provides high-performance and easy to use 
data structures and data analysis tools.  
This page provides a brief overview of pandas, but the open source community 
developing the pandas package has also created excellent documentation and training 
material, including: 

- a  `Getting started guide <https://pandas.pydata.org/getting_started.html>`__ 
  (including tutorials and a 10 minute flash intro)
- a `"10 minutes to pandas" <https://pandas.pydata.org/docs/user_guide/10min.html#min>`__
  tutorial
- thorough `Documentation <https://pandas.pydata.org/docs/>`__ containing a user guide, 
  API reference and contribution guide
- a `cheatsheet <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>`__ 
- a `cookbook <https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook>`

Let's get a flavor of what we can do with pandas. We will be working with an
example dataset containing the passenger list from the Titanic, which is often used in Kaggle competitions and data science tutorials.

To download the data either go to [this GitHub repository](https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv) and save it to a file (e.g. by right-clicking and clicking "Save As"), or type inside Jupyter Notebook (if you have wget installed on OSX or Linux):


!wget https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv


We now 
- import the pandas package 
- load the dataset into a **dataframe** 
- view the dataframe to get an idea of what it contains 
- print summary statistics of all numerical data in the dataframe

::

    import pandas as pd

    df = pd.read_csv("titanic.csv")
    # print the first 5 lines of the dataframe
    df.head()  
    
::

    # print summary statistics for each column
    df.describe()  


Ok, so we have information on passenger names, survival (0 or 1), age, 
ticket fare, number of siblings/spouses, etc. With the summary statistics we see that the average age is 29.7 years, maximum ticket price is 512 USD, 38\% of passengers survived, etc.

Let's say we're interested in the survival probability of different age groups. With two one-liners, we can find the average age of those who survived or didn't survive, and plot corresponding histograms of the age distribution::

    print(df.groupby("Survived")["Age"].mean())

::

    df.hist(column='Age', by='Survived', bins=25, figsize=(8,10), layout=(2,1), zorder=2, sharex=True, rwidth=0.9);
    

Clearly, pandas dataframes allows us to do advanced analysis with very few commands, but it takes a while to get used to how dataframes work so let's get back to basics.



What is a dataframe?
--------------------

Pandas dataframes are a powerful tool for working with tabular data, 
e.g. from databases or spreadsheets. A pandas 
`DataFrame object <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame>`__ 
is composed of rows and columns:

.. image:: img/01_table_dataframe.svg

Each column of a dataframe is a Series object - a dataframe is thus a collection 
of series. Let's inspect one column of the Titanic passanger list data 
(first downloading and reading the titanic.csv datafile into a dataframe if needed, 
see above)::

    df["Age"]
    type(df["Age"])

We can inspect the column names through the `columns` attribute::

    df.columns

Series and DataFrames have a lot functionality, for example statistical 
methods::

    df["Age"].min()
    df["Age"].max()
    df["Age"].mean()
    df["Age"].std()

How can we find out what methods are available? One way is to visit 
the `API reference <https://pandas.pydata.org/docs/reference/frame.html>`__ 
and searching through the list. 
Another way is use the autocompletion feature in Jupyter and type e.g. 
``df["Age"].`` in a notebook and then hit `TAB` twice - this opens up a list menu of available methods and attributes.


We saw above how we can read in data into a dataframe using the ``read_csv`` method.
Pandas also understands multiple other formats, for example using ``read_excel``,  
``read_hdf``, ``read_json``, etc. 
But often you would want to create a dataframe from scratch. Also this can be done 
in multiple ways, for example from a numpy array::

    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

or from a dictionary::

    df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20130102'), 
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})



- loading data and writing data
- indexing ([] and .at / .iat)
- new columns, adding existing columns etc


Working with dataframes
-----------------------

- join, merge, split, apply
- sort_values, pivot and pivot_table
- groupby (one vs two categories, e.g. survival and sex, calc mean/max/min wrt age)
    - hierarchical indexing

Time series superpowers
-----------------------

Tidy data
---------

- missing values, dropna, dropna(how="all"), fill-forward (ffill) etc



.. challenge:: Extracting information from a dataframe

    Investigate the family size of the passengers, i.e. the "SibSp" column.

    - What different family sizes exist in the passenger list? Hint: try the `unique` method 
    - What are the names of the people in the largest family group?
    - Create a histogram showing the distribution of family sizes 

.. keypoints::

   - K1
   - K2
