Productivity tools
==================

.. questions::

   - Do you have preferences on the visual aspects of the code
     and how it should look?
   - Do you use any tools that help you create better looking
     code faster?

.. objectives::

   - Learn tools that can help you be more productive.
   - Learn how to follow standards that other people have created
     and how to pick your own favorite.

Spotting code problems with linters
-----------------------------------

Python as a programming language has a syntax that specifies the
rules that the code must follow. If the code is not written with
valid syntax, you will get an error.

.. code-block:: python

   # Valid syntax, returns 1
   a = 1
   print(a)

   # Invalid syntax, returns SyntaxError
   True = 1

Spotting syntax errors can be time consuming and to help this
programmers have created **linters**. Linters are tools that
check whether code's syntax is correct.

Some popular linters include:

- `Ruff <https://docs.astral.sh/ruff/>`__
- `Pylint <https://pylint.readthedocs.io/en/stable/>`__
- `flake8 <https://flake8.pycqa.org/en/latest/>`__

In the following example lets use ``pylint`` to check the following
script (:download:`lint_example.py
<../resources/code/productivity/lint_example.py>`: to easily download
to JupyterLab, use File → Open from URL → Paste URL → It will download
and open in a window.):

.. code-block:: python

   import numpy
   import matplotlib.pyplot as plt

   x = np.linspace(0, np.pi, 100))
   y = np.sin(x)

   plt.plot(x, y)

   plt.show()

To run ``pylint`` from the terminal in JupyterLab, File → New →
Terminal.  Make sure you are in the right directory, then you can run
``pylint``:

.. code-block:: console

   $ pylint lint_example.py 
   ************* Module lint_example
   lint_example.py:4:31: E0001: Parsing failed: 'unmatched ')' (<unknown>, line 4)' (syntax-error)


From here we can see that ``pylint`` says that there is a unmatched bracket
on line 4. We also get an message code E0001 (syntax-error). We can find
description for the message from
`Pylint's messages list <https://pylint.readthedocs.io/en/stable/user_guide/messages/messages_overview.html#error-category>`__
and look at the
`specific error page <https://pylint.readthedocs.io/en/stable/user_guide/messages/error/syntax-error.html>`__ to see an example that describes the error.

After fixing the problem with the bracket and running ``pylint`` again we
get more errors:

.. code-block:: console

   $ pylint lint_example.py 
   ************* Module lint_example
   lint_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
   lint_example.py:4:4: E0602: Undefined variable 'np' (undefined-variable)
   lint_example.py:4:19: E0602: Undefined variable 'np' (undefined-variable)
   lint_example.py:5:4: E0602: Undefined variable 'np' (undefined-variable)
   lint_example.py:1:0: W0611: Unused import numpy (unused-import)

   ------------------------------------------------------------------
   Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

Here we see the following suggestions:

- On line 1 we're missing a module docstring. This is a warning that we're
  going against a coding convetion and thus we get a ``CXXXX`` message code.
  This is not critical, so let's not focus on this for now.
- On lines 4 and 5 we have undefined variable ``np``. This will create
  error if we would execute the code and thus we get a ``EXXXX`` message code.
- On line 1 we have unused import for ``numpy`` module. This won't create an
  error, but Pylint flags this as unnecessary and will give a warning
  with ``WXXX`` message code.

At the end Pylint will give a rating for the code. In this case the
errors will give an overall rating of ``0.00/10`` as the code won't execute
correctly.

From these messages we can deduce that the main problem is that the import
statement does not use ``import numpy as np`` and thus ``np`` is undefined.

After changing the import stamement, the code works correctly and running
``pylint lint_example.py`` will only warn about the missing docstring.
You can also notice that the changes have increased the rating and
Pylint will show the improvement since last run.

.. code-block:: console

   $ pylint lint_example.py 
   ************* Module lint_example
   lint_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)

   ------------------------------------------------------------------
   Your code has been rated at 8.33/10 (previous run: 0.00/10, +8.33)


Exercise 1
----------

.. challenge:: Using Pylint

   The following code uses scikit-learn to fit a simple linear
   model to randomly generated data with some error. You can download it
   :download:`here <../resources/code/productivity/exercise1.py>` (see
   above for how to easily download and run in JupyterLab).

   It has four mistakes in it. One of these cannot be found by
   Pylint.

   Fix the following code with Pylint and try to determine why
   Pylint did not find the last mistake.

   .. code-block:: python

      """
      pylint exercise 1
      """
      import numpy as np
      import pandas as pd
      import matplotlib.pyplot as plt
      from sklearn import linear_model


      def f(x):
          """
          Example function:

          f(x) = x/2 + 2
          """"
          return 0.5*x + 2


      # Create example data
      x_data = np.linspace(0, 10, 100)
      err = 2 * np.random.random(x_data.shape[0])
      y_data = f(x_data) + err

      # Put data into dataframe
      df = pd.DataFrame({'x': x_data, 'y': y_data})

      # Create linear model and fit data
      reg = linear_model.LinearRegression(fit_intercept=True)

      reg.fit(df[['x'], df[['y']])

      slope = reg.coef_[0][0]
      intercept = reg.intercept_[0]

      df['pred'] = reg.predict(df[['x']])

      fig, ax = plt.subplots()

      ax.scater(df[['x']], df[['y']], alpha=0.5)
      ax.plot(df[['x']], df[['pred']]
              color='black', linestyle='--',
              label=f'Prediction with slope {slope:.2f} and intercept {intercept:.2f}')
      ax.set_ylabel('y')
      ax.set_xlabel('x')
      ax.legend()

      plt.show()

.. solution::

   Solution is available
   :download:`here <../resources/code/productivity/exercise1_solution.py>`.

   Errors were as follows:

   1. Line 15 has an extra ``"``-character, which results in syntax-error.
   2. Line 30 has a missing ``]``-bracker, which results in syntax-error.
   3. Line 40 is missing a comma at the end, which results in syntax-error.
   4. On line 39 the function ``scatter`` is misspelled. Pylint does not
      notice this as it does not run the code and thus it does not
      create the ax-object.

   .. code-block:: python

      """
      pylint exercise 1
      """
      import numpy as np
      import pandas as pd
      import matplotlib.pyplot as plt
      from sklearn import linear_model


      def f(x):
          """
          Example function:

          f(x) = x/2 + 2
          """
          return 0.5*x + 2


      # Create example data
      x_data = np.linspace(0, 10, 100)
      err = 2 * np.random.random(x_data.shape[0])
      y_data = f(x_data) + err

      # Put data into dataframe
      df = pd.DataFrame({'x': x_data, 'y': y_data})

      # Create linear model and fit data
      reg = linear_model.LinearRegression(fit_intercept=True)

      reg.fit(df[['x']], df[['y']])

      slope = reg.coef_[0][0]
      intercept = reg.intercept_[0]

      df['pred'] = reg.predict(df[['x']])

      fig, ax = plt.subplots()

      ax.scatter(df[['x']], df[['y']], alpha=0.5)
      ax.plot(df[['x']], df[['pred']],
              color='black', linestyle='--',
              label=f'Prediction with slope {slope:.2f} and intercept {intercept:.2f}')
      ax.set_ylabel('y')
      ax.set_xlabel('x')
      ax.legend()

      plt.show()

Enforcing consistent code style
-------------------------------

Python is a very flexible language which makes it possible to use
all kinds of coding styles.

For example, one could use the following naming styles for variables:

.. code-block:: python

   # Different variable styles
   myvariable = 1   # Lowercase
   myVariable = 1   # Camel case
   MyVariable = 1   # Pascal case
   my_variable = 1  # Snake case

Everyone has their own preference to what style to use and everybody
has freedom to use their preferred style, but to improve legibility
of code there are official style guides for
`code (PEP 8) <https://peps.python.org/pep-0008/>`__ and for
`docstrings (PEP 257) <https://peps.python.org/pep-0257/>`__.

There are many code checkers that give you suggestions on how
to modify your code or do the modifications automatically:

- `flake8 <https://flake8.pycqa.org/en/latest/>`__
- `black <https://github.com/psf/black>`__
- `Ruff <https://docs.astral.sh/ruff/>`__
- `yapf <https://github.com/google/yapf>`__

Let's use black and flake8 (with ``pep8-naming``-extension) to modify
:download:`code_style_example.py <../resources/code/productivity/code_style_example.py>`:

.. code-block:: python

   import  numpy  as np

   def  PI_estimate(n):
       """This function calculates an estimate of pi with dart thrower algorithm.
       """

       pi_Numbers =  np.random.random(size = 2*n)
       x = pi_Numbers[ :n ]
       y = pi_Numbers[ n: ]

       return 4*np.sum((x * x + y*y ) < 1)/n


   for number  in range(1,8):

       n = 10** number

       print(f'Estimate for PI with {n:8d} dart throws: {PI_estimate( n )}')


Running flake8 to check for style problems we get the following output:

.. code-block:: console

   $ flake8 code_style_example.py
   code_style_example.py:1:7: E271 multiple spaces after keyword
   code_style_example.py:1:14: E272 multiple spaces before keyword
   code_style_example.py:3:1: E302 expected 2 blank lines, found 1
   code_style_example.py:3:4: E271 multiple spaces after keyword
   code_style_example.py:3:6: N802 function name 'PI_estimate' should be lowercase
   code_style_example.py:7:6: N806 variable 'pi_Numbers' in function should be lowercase
   code_style_example.py:7:17: E222 multiple spaces after operator
   code_style_example.py:7:40: E251 unexpected spaces around keyword / parameter equals
   code_style_example.py:7:42: E251 unexpected spaces around keyword / parameter equals
   code_style_example.py:8:20: E201 whitespace after '['
   code_style_example.py:8:23: E202 whitespace before ']'
   code_style_example.py:9:20: E201 whitespace after '['
   code_style_example.py:9:23: E202 whitespace before ']'
   code_style_example.py:11:33: E202 whitespace before ')'
   code_style_example.py:14:11: E272 multiple spaces before keyword
   code_style_example.py:14:23: E231 missing whitespace after ','
   code_style_example.py:16:11: E225 missing whitespace around operator
   code_style_example.py:18:67: E201 whitespace after '('
   code_style_example.py:18:69: E202 whitespace before ')'

There are plenty of errors and warnings. We could fix these manually, but
instead let's use ``black`` to format the code. Black is an "uncompromising
Python code formatter" from Python Software Foundation and it automatically
modifies your code to match their recommended coding style.

It should fix most of the errors automatically without changing the
functionality.

After running ``black code_style_example.py`` the code looks like this:

.. code-block:: python

   import numpy as np


   def PI_estimate(n):
       """This function calculates an estimate of pi with dart thrower algorithm."""

       pi_Numbers = np.random.random(size=2 * n)
       x = pi_Numbers[:n]
       y = pi_Numbers[n:]

       return 4 * np.sum((x * x + y * y) < 1) / n


   for number in range(1, 8):
       n = 10**number

       print(f"Estimate for PI with {n:8d} dart throws: {PI_estimate( n )}")

Much cleaner. If we want to check for variable naming syntax we can still run
``flake8 code_style_example.py``:

.. code-block:: console

   $ flake8 code_style_example.py
   code_style_example.py:4:6: N802 function name 'PI_estimate' should be lowercase
   code_style_example.py:5:80: E501 line too long (81 > 79 characters)
   code_style_example.py:7:6: N806 variable 'pi_Numbers' in function should be lowercase
   code_style_example.py:17:67: E201 whitespace after '('
   code_style_example.py:17:69: E202 whitespace before ')'

Fixing these problems we get the final piece of code:

.. code-block:: python

   import numpy as np


   def pi_estimate(n):
       """
       This function calculates an estimate of pi with dart thrower algorithm.
       """

       pi_numbers = np.random.random(size=2 * n)
       x = pi_numbers[:n]
       y = pi_numbers[n:]

       return 4 * np.sum((x * x + y * y) < 1) / n


   for number in range(1, 8):
       n = 10**number

       print(f"Estimate for PI with {n:8d} dart throws: {pi_estimate(n)}")

Comparing the fixed one to the original one the code is much more legible.

.. admonition:: Problems with styles and writing your own kind of code
   :class: dropdown

   There style black uses is
   `a bit different to PEP 8 <https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html>`__
   and one can definitely argue that it
   `does not handle mathematical expressions in the optimal way <https://github.com/psf/black/issues/148>`__.

   However, one can turn formatting off for math heavy sections with ``# fmt: on``-
   and ``# fmt: off``-comments. Alternatively, you can use formatter such as
   `yapf <https://github.com/google/yapf>`__, which supports formatting based on
   arithmetic precedence:

   .. code-block:: console

      $ yapf --style='{based_on_style: pep8, arithmetic_precedence_indication=true}' --diff code_style_example.py
      --- code_style_example.py       (original)
      +++ code_style_example.py       (reformatted)
      @@ -10,7 +10,7 @@
           x = pi_numbers[:n]
           y = pi_numbers[n:]

      -    return 4 * np.sum((x * x + y * y) < 1) / n
      +    return 4 * np.sum((x*x + y*y) < 1) / n


       for number in range(1, 8):

   From this diff we see that ``yapf``  would change the multiplications to
   match the arithmetic precedence.

   All formatters allow for massive amounts of style changes and you can
   configure them by creating a configuration file in your repository.

   If the formatter makes a change that you do not like you can usually
   disable the change by changing the configuration of the formatter.


Exercise 2
----------

.. challenge:: Using black to format code

   Format
   :download:`this code <../resources/code/productivity/exercise2.py>`
   with black:

   .. code-block:: python

      import numpy as np
      import matplotlib.pyplot  as plt

      def dice_toss(n,m):

          """Throw n dice m times and the total value together."""
          dice_rolls    = np.random.randint(1,6,size=(m, n))

          roll_averages = np.sum(dice_rolls,axis = -1)

          return roll_averages
      fig,ax = plt.subplots( )

      n = int( input('Number of dices to toss:\n'))

      bins = np.arange(1, 6 * n+1)

      m = 1000

      ax.hist(dice_toss(n,m), bins = bins)

      ax.set_title(f'Histogram of {n} dice tosses')

      ax.set_xlabel('Total value' )

      ax.set_ylabel('Number of instances')

      plt.show()

.. solution:: 

   Running ``black exercise2.py`` will produce
   :download:`this piece of code <../resources/code/productivity/exercise2_solution.py>`.

   .. code-block:: python

      import numpy as np
      import matplotlib.pyplot as plt


      def dice_toss(n, m):
          """Throw n dice m times and the total value together."""
          dice_rolls = np.random.randint(1, 6, size=(m, n))

          roll_averages = np.sum(dice_rolls, axis=-1)

          return roll_averages


      fig, ax = plt.subplots()

      n = int(input("Number of dices to toss:\n"))

      bins = np.arange(1, 6 * n + 1)

      m = 1000

      ax.hist(dice_toss(n, m), bins=bins)

      ax.set_title(f"Histogram of {n} dice tosses")

      ax.set_xlabel("Total value")

      ax.set_ylabel("Number of instances")

      plt.show()


Integrating productivity tools with git
---------------------------------------

If you're using version control you can easily add tools such as
pylint, flake8, black and ruff as automatic using tools like
`pre-commit <https://pre-commit.com/>`__.

Pre-commit is a tool that makes it easy to automatically run various
code checkers when you're doing a new commit to the repository.

For more information see their website.


Other nice tools
----------------

- `isort <https://pycqa.github.io/isort/>`__ - Sorts import statements for you
- `jupyterlab_code_formatter <https://github.com/ryantam626/jupyterlab_code_formatter>`__ - Adds formatting functionality to jupyterlab.

.. keypoints::

   - Using linters and formatters can help you write cleaner code.
   - You should adapt your own code and documentation style based
     on standards that other people use.
   - Using pre-commit with your git repository can make many of the
     checks automatic.
