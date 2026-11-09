Organizing Python code
----------------------

Start Python scripts with

::

   #!/usr/bin/env python3

This ensures you get the correct python3 for the environment you are
using.

In general, don't put executable statements directly into the top
level scope in your files (modules), as this code is then run if you
try to import the module.

Instead, use this common idiom:

::

   if __name__ == '__main__':
       # your code goes here


When developing code it's often convenient to be able to reload a
module into your IPython (or IPython notebook) session without having
to restart the entire session. This can be done with the ``reload``
function:

::

   from importlib import reload
   import foo
   foo.bar()
   # Edit foo.py
   reload(foo)
   foo.bar()
