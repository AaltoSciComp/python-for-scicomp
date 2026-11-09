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
- a `cookbook <https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook>`__.

Let's get a flavor of what we can do with pandas. We will be working with an
example dataset containing the passenger list from the Titanic, which is often used in Kaggle competitions and data science tutorials. First step is to load pandas::

    import pandas as pd

We can download the data from `this GitHub repository <https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv>`__
by visiting the page and saving it to disk, or by directly reading into 
a **dataframe**::

    url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"
    titanic = pd.read_csv(url)

We can now view the dataframe to get an idea of what it contains and
print some summary statistics of its numerical data::

    # print the first 5 lines of the dataframe
    titanic.head()  
    
    # print summary statistics for each column
    titanic.describe()  


Ok, so we have information on passenger names, survival (0 or 1), age, 
ticket fare, number of siblings/spouses, etc. With the summary statistics we see that the average age is 29.7 years, maximum ticket price is 512 USD, 38\% of passengers survived, etc.

Let's say we're interested in the survival probability of different age groups. With two one-liners, we can find the average age of those who survived or didn't survive, and plot corresponding histograms of the age distribution::

    print(titanic.groupby("Survived")["Age"].mean())

::

    titanic.hist(column='Age', by='Survived', bins=25, figsize=(8,10), 
                 layout=(2,1), zorder=2, sharex=True, rwidth=0.9);
    

Clearly, pandas dataframes allows us to do advanced analysis with very few commands, but it takes a while to get used to how dataframes work so let's get back to basics.


What's in a dataframe?
----------------------

As we saw above, pandas dataframes are a powerful tool for working with tabular data. 
A pandas 
`DataFrame object <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame>`__ 
is composed of rows and columns:

.. image:: img/pandas/01_table_dataframe.svg

Each column of a dataframe is a 
`series object <https://pandas.pydata.org/docs/user_guide/dsintro.html#series>`__ 
- a dataframe is thus a collection of series. Let's inspect one column of 
the Titanic passanger list data (first downloading and reading the 
titanic.csv datafile into a dataframe if needed, see above)::

    titanic["Age"]
    titanic.Age          # same as above
    type(titanic["Age"])

The columns, rows and dtypes can be listed through corresponding
attributes::

    titanic.columns
    titanic.index
    titanic.dtypes

We saw above how to select a single column, but there are other ways of selecting 
(and setting) single or multiple rows, columns and values::

    titanic.at[0,"Age"]            # select single value by row and column *name* (fast)
    titanic.at[0,"Age"] = 42       # set single value by row and column *name* (fast)
    titanic.iat[0,5]               # select same value by row and column *number* (fast)
    titanic.loc[0:2, "Name":"Age"] # slice the dataframe by row and column *names*
    titanic.iloc[0:2,3:6]          # same slice as above by row and column *numbers*
    titanic["foo"] = "bar"         # set a whole column

Dataframes also support boolean indexing, just like we saw for ``numpy`` 
arrays::

    titanic[titanic["Age"] > 70]
    # ".str" creates a string object from a column
    titanic[titanic["Name"].str.contains("Margaret")]

What if your dataset has missing data? Pandas uses the value ``np.nan`` 
to represent missing data, and by default does not include it in any computations.
We can find missing values, drop them from our dataframe, replace them
with any value we like or do forward or backward filling::

    titanic.isna()                    # returns boolean mask of NaN values
    titanic.dropna()                  # drop missing values
    titanic.dropna(how="any")         # or how="all"
    titanic.dropna(subset=["Cabin"])  # only drop NaNs from one column
    titanic.fillna(0)                 # replace NaNs with zero
    titanic.fillna(method='ffill')    # forward-fill NaNs


.. callout:: Getting help

    Series and DataFrames have a lot functionality, but
    how can we find out what methods are available and how they work? One way is to visit 
    the `API reference <https://pandas.pydata.org/docs/reference/frame.html>`__ 
    and reading through the list. 
    Another way is to use the autocompletion feature in Jupyter and type e.g. 
    ``titanic["Age"].`` in a notebook and then hit ``TAB`` twice - this should open 
    up a list menu of available methods and attributes.

    Jupyter also offers quick access to help pages (docstrings) which can be 
    more efficient than searching the internet. Two ways exist:

    - Write a function name followed by question mark and execute the cell, e.g.
      write ``titanic.hist?`` and hit ``SHIFT + ENTER``.
    - Write the function name and hit ``SHIFT + TAB``.

.. challenge:: Exploring dataframes

    - Have a look at the available methods and attributes using the 
      `API reference <https://pandas.pydata.org/docs/reference/frame.html>`__ 
      or the autocomplete feature in Jupyter. 
    - Try out a few methods using the Titanic dataset and have a look at 
      the docstrings (help pages) of methods that pique your interest
    - Compute the mean age of the first 10 passengers by slicing and the ``mean`` method
    - (Advanced) Using boolean indexing, compute the survival rate 
      (mean of "Survived" values) among passengers over and under the average age.
    
.. solution:: 

    - Mean age of the first 10 passengers: ``titanic.iloc[:10,:]["Age"].mean()`` 
      or ``titanic.loc[:9,"Age"].mean()`` or ``df.iloc[:10,5].mean()``.
    - Survival rate among passengers over and under average age: 
      ``titanic[titanic["Age"] > titanic["Age"].mean()]["Survived"].mean()`` and 
      ``titanic[titanic["Age"] < titanic["Age"].mean()]["Survived"].mean()``.


Tidy data
---------

The above analysis was rather straightforward thanks to the fact 
that the dataset is *tidy*.

.. image:: img/pandas/tidy_data.png

In short, columns should be variables and rows should be measurements, 
and adding measurements (rows) should then not require any changes to code 
that reads the data.

What would untidy data look like? Here's an example from 
some run time statistics from a 1500 m running event::

    df = pd.DataFrame([
            {'Runner': 'Runner 1', 400: 64, 800: 128, 1200: 192, 1500: 240},
            {'Runner': 'Runner 2', 400: 80, 800: 160, 1200: 240, 1500: 300},
            {'Runner': 'Runner 3', 400: 96, 800: 192, 1200: 288, 1500: 360},
             ])

To make untidy data tidy, a common operation is to "melt" it, 
which is to convert it from wide form to a long form::

    df = pd.melt(df, id_vars="Runner", 
                 value_vars=[400, 800, 1200, 1500], 
                 var_name="distance", 
                 value_name="time"
                )

In this form it's easier to **filter**, **group**, **join** 
and **aggregate** the data, and it's also easier to model relationships 
between variables.

The opposite of melting is to *pivot* data, which can be useful to 
view data in different ways as we'll see below.

For a detailed exposition of data tidying, have a look at 
`this article <http://vita.had.co.nz/papers/tidy-data.pdf>`__.



Working with dataframes
-----------------------

We saw above how we can read in data into a dataframe using the ``read_csv`` method.
Pandas also understands multiple other formats, for example using ``read_excel``,  
``read_hdf``, ``read_json``, etc. (and corresponding methods to write to file: 
``to_csv``, ``to_excel``, ``to_hdf``, ``to_json``, etc.)  

But sometimes you would want to create a dataframe from scratch. Also this can be done 
in multiple ways, for example starting with a numpy array::

    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

or a dictionary::

    df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C': np.array([3] * 8, dtype='int32'),
                       'D': np.random.randn(8),
                       'E': np.random.randn(8)})

There are many ways to operate on dataframes. Let's look at a 
few examples in order to get a feeling of what's possible
and what the use cases can be.

We can easily split and concatenate or append dataframes::

    sub1, sub2, sub3 = df[:2], df[2:4], df[4:]
    pd.concat([sub1, sub2, sub3]])
    sub1.append([sub2, sub3])      # same as above

Dataframes can also be merged similarly to in SQL::

    m1 = df.loc[:3, "A":"B"]
    m2 = df.loc[3:6, ["A", "D", "E"]]
    # merge two dataframes on column "A"
    pd.merge(m1, m2, on="A")

In fact, much of what can be done in SQL 
`is also possible with pandas <https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html>`__.

Functions can be applied to a whole dataframe or parts of it::

    df.apply(np.cumsum)   # you can also pass your own custom functions
    df.loc[:, "C":"E"].apply(np.cumsum)

Most common statistical functions are in fact already available 
as dataframe methods, like ``std()``, ``min()``, ``max()``, 
``cumsum()``, ``median()``, ``skew()``, ``var()`` etc. 

``pivot_table()`` and ``groupby()`` are two powerful methods which 
are applied to dataframes to split and aggregate data in groups.
They work similarly but differ in the shape of the result.
To see what's possible, let's return to the Titanic dataset.
We start by rounding all ages to the nearest decade and then create 
a pivot table showing the mean of fares split by gender and survival::

    titanic["Age"] = titanic["Age"].round(-1)
    pd.pivot_table(titanic, values="Fare", index=["Sex", "Survived"], 
                   columns=["Age"], aggfunc=np.mean)

The same operation with group-by is::

    titanic.groupby(["Sex", "Survived", "Age"])["Fare"].mean()


.. challenge:: Analyze the Titanic passenger list dataset

    In the Titanic passenger list dataset, 
    investigate the family size of the passengers (i.e. the "SibSp" column).

    - What different family sizes exist in the passenger list? Hint: try the `unique` method 
    - What are the names of the people in the largest family group?
    - (Advanced) Create histograms showing the distribution of family sizes for 
      passengers split by the fare, i.e. one group of high-fare passengers (where 
      the fare is above average) and one for low-fare passengers 
      (Hint: you can use the lambda function 
      ``lambda x: "Poor" if df["Fare"].loc[x] < df["Fare"].mean() else "Rich"``)

.. solution:: Solution

    - Existing family sizes: ``df["SibSp"].unique()``
    - Names of members of largest family(ies): ``df[df["SibSp"] == 8]["Name"]``
    - ``df.hist("SibSp", lambda x: "Poor" if df["Fare"].loc[x] < df["Fare"].mean() else "Rich", rwidth=0.9)``




Time series superpowers
-----------------------

An introduction of pandas wouldn't be complete without mention of its 
special abilities to handle time series. To show just a few examples, 
we will use a new dataset of Nobel prize laureates::

    nobel = pd.read_csv("http://api.nobelprize.org/v1/laureate.csv")
    nobel.head()

This dataset has three columns for time, "born"/"died" and "year". 
These are represented as strings and integers, respectively, and 
need to be converted to datetime format::

    # the errors='coerce' argument is needed because the dataset is a bit messy
    nobel["born"] = pd.to_datetime(nobel["born"], errors ='coerce')
    nobel["died"] = pd.to_datetime(nobel["died"], errors ='coerce')
    nobel["year"] = pd.to_datetime(nobel["year"], format="%Y")

Pandas knows a lot about dates::

    print(nobel["born"].dt.day)
    print(nobel["born"].dt.year)
    print(nobel["born"].dt.weekday)
    
We can add a column containing the (approximate) lifespan in years rounded 
to one decimal::

    nobel["lifespan"] = round((nobel["died"] - nobel["born"]).dt.days / 365, 1)

and then plot a histogram of lifespans::

    nobel.hist(column='lifespan', bins=25, figsize=(8,10), rwidth=0.9)
    
Finally, let's see one more example of an informative plot 
produced by a single line of code::

    nobel.boxplot(column="lifespan", by="category")

.. challenge:: Analyze the Nobel prize dataset

    - What country has received the largest number of Nobel prizes, and how many?
      How many countries are represented in the dataset? Hint: use the `describe()` method
      on the ``bornCountryCode`` column.
    - Create a histogram of the age when the laureates received their Nobel prizes.
      Hint: follow the above steps we performed for the lifespan. 
    - List all the Nobel laureates from your country.

    Now more advanced steps:
    
    - First add a column “number” to the nobel dataframe containing 1’s 
      (to enable the counting below).          
    - Now define an array of 4 countries of your choice and extract 
      only laureates from these countries::
      
          countries = np.array([COUNTRY1, COUNTRY2, COUNTRY3, COUNTRY4])
          subset = nobel.loc[nobel['bornCountry'].isin(countries)]

    - Create a pivot table to view a spreadsheet like structure, and view it::

        table = subset.pivot_table(values="number", index="bornCountry", columns="category", aggfunc=np.sum)
        
    - (Optional) Install the **seaborn** visualization library if you don't 
      already have it, and create a heatmap of your table::
      
          import seaborn as sns
          sns.heatmap(table,linewidths=.5);

    - Play around with other nice looking plots::
    
        sns.violinplot(y="year", x="bornCountry",inner="stick", data=subset);

      ::

        sns.swarmplot(y="year", x="bornCountry", data=subset, alpha=.5);

      ::

        subset_physchem = nobel.loc[nobel['bornCountry'].isin(countries) & (nobel['category'].isin(['physics']) | nobel['category'].isin(['chemistry']))]
        sns.catplot(x="bornCountry", y="year", col="category", data=subset_physchem, kind="swarm");

      ::
      
        sns.catplot(x="bornCountry", col="category", data=subset_physchem, kind="count");



.. keypoints::

   - pandas dataframes are a good data structure for tabular data
   - Dataframes allow both simple and advanced analysis in very compact form 
