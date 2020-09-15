Pandas
======

.. questions::

   - How do I learn a new Python package?
   - How can I use pandas dataframes in my research? 

.. objectives::

   - Learn simple and some more advanced usage of pandas dataframes
   - Get a feeling for when pandas is useful and know where to find more information


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
example dataset containing the passenger list from the Titanic, which is often used in Kaggle competitions and data science tutorials. First step is to load the package::

    import pandas as pd

We can download the data from `this GitHub repository <https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv>`__
by visiting the page and saving it to disk, or by directly reading into 
a **dataframe**::

    url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/"
    df = pd.read_csv(url+"titanic.csv")

We can now view the dataframe to get an idea of what it contains and
print some summary statistics of its numerical data::

    # print the first 5 lines of the dataframe
    df.head()  
    
    # print summary statistics for each column
    df.describe()  


Ok, so we have information on passenger names, survival (0 or 1), age, 
ticket fare, number of siblings/spouses, etc. With the summary statistics we see that the average age is 29.7 years, maximum ticket price is 512 USD, 38\% of passengers survived, etc.

Let's say we're interested in the survival probability of different age groups. With two one-liners, we can find the average age of those who survived or didn't survive, and plot corresponding histograms of the age distribution::

    print(df.groupby("Survived")["Age"].mean())

::

    df.hist(column='Age', by='Survived', bins=25, figsize=(8,10), layout=(2,1), zorder=2, sharex=True, rwidth=0.9);
    

Clearly, pandas dataframes allows us to do advanced analysis with very few commands, but it takes a while to get used to how dataframes work so let's get back to basics.



What's in a dataframe?
----------------------

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
    df.Age          # same as above
    type(df["Age"])

The columns and rows can be inspected through the *columns* and *index* attributes::

    df.columns
    df.index

We saw above how to select a single column, but there are other ways of selecting 
single or multiple rows, columns and values::

    df.at[0,"Age"]            # select single value by row and column *name* (fast)
    df.iat[0,5]               # select same value by row and column *number* (fast)
    df.loc[0:2, "Name":"Age"] # slice the dataframe by row and column *names*
    df.iloc[0:2,3:6]          # same slice as above by row and column *numbers*

Finally, dataframes support boolean indexing, just like we saw for ``numpy`` 
arrays::

    df[df["Age"] > 70]
    df[df["Name"].str.contains("Margaret")]

Series and DataFrames have a lot functionality, but
how can we find out what methods are available? One way is to visit 
the `API reference <https://pandas.pydata.org/docs/reference/frame.html>`__ 
and searching through the list. 
Another way is use the autocompletion feature in Jupyter and type e.g. 
``df["Age"].`` in a notebook and then hit `TAB` twice - this should open 
up a list menu of available methods and attributes.

.. challenge:: Exploring dataframes

    - Have a look at the available methods and attributes using the 
      `API reference <https://pandas.pydata.org/docs/reference/frame.html>`__ 
      or the autocomplete feature in Jupyter. 
    - Try out a few methods and have a look at the docstrings (help pages) 
      of methods that pique your interest by either running a cell with 
      question mark after the method name (e.g. ``df.min?``) or by hitting 
      ``SHIFT`` + ``TAB`` after the method name.
    - Compute the mean age of the first 10 passengers by slicing and the ``mean`` method
    - (Advanced) Using boolean indexing, compute the survival rate 
      (mean of "Survived" values) among passengers over and under the average age.
    

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

   - pandas dataframes are a good data structure for tabular data
   - Dataframes allow both simple and advanced analysis in very compact form 
