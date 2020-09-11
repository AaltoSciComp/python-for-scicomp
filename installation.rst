Software installation
=====================

This page contains instructions for installing the required software
on your computer.  The workshop could be done with a remote Jupyter
server, as long as you can use the terminal from the Jupyter (you need
to be able to access the command line sometime).



Python
------

We expect you to have a working Python installation with some common
libraries.  We recommend that you install the `Anaconda python
distribution <https://docs.continuum.io/anaconda/install/>`__.  For
more information on installing anaconda, you can see `the CodeRefinery
instructions <https://coderefinery.github.io/installation/python/>`__.

Any other Python distribution which you can install libraries into
would work, but because there are so many different ways to do this,
we don't support them.



Verify the installation
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Watch the video

   See this `verification in video form
   <https://youtu.be/OEX1ss_HCHc>`__ - if you can do this, you are
   ready to go for day one.

After activating the conda environment, you should be able to check
the Python version from the command line.  Any version of python3
should work:

You should be able to start JupyterLab:

.. code-block:: console

   $ jupyter lab
   (... Jupyter starts in a web browser)

You also need to be able to run Python from the command line (starting
on day 2).  For this, you can start the "terminal" application from
within JupyterLab, and do everything from there.  This is sufficient
for the course, so we recommend this if you don't normally use the
command line.

.. code-block:: console

   $ python3 -V
   Python 3.8.3



Text editor
-----------

For one portion of the course, you will need a text editor.  If you
don't know what to use, you can use the text editor that comes from
JupyterLab and it will do everything you need.

For other editors, see the `CodeRefinery instructions
<https://coderefinery.github.io/installation/editors/>`__.  You don't
exactly need a terminal editor - the graphical ones, such as VSCode or
whatever you use now, will work as well.



Shell
-----

If you can run JupyterLab, that is sufficient.  You should be able to
start the terminal from there.

TODO.  You can see the `CodeRefinery instructions
<https://coderefinery.github.io/installation/bash/>`__.


git
---

On the very last day, we use git.  See the `CodeRefinery instructions
<https://coderefinery.github.io/installation/git/>`__.

Verify:

.. code-block:: console

   $ git --version
   git version 2.17.1

Zoom
----

If this is an online workshop, it might use zoom.  You can see
`CodeRefinery instructions for it
<https://coderefinery.github.io/installation/zoom/>`__.
