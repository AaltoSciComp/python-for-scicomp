Software installation
=====================

This page contains instructions for installing the required software
on your computer.  
Please make sure before the course that you have all the required software
installed or in any other way access to it.

For example, the workshop could be done with a remote Jupyter
server, as long as you can use the terminal from the Jupyter (you need
to be able to access the command line sometime).


List of software needed during the course
------------------------------------------

* Zoom (not needed for 'non interactive' people following the workshop on Twitch)
* Pyhton 3 (Anaconda is suggested)
   * numpy
   * pandas
   * scipy
   * matplotlib
* Jupyter lab
* Text editor
* git


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


Command line
~~~~~~~~~~~~

There are different ways to start the command line.

* From the Anaconda Navigator:

  .. figure:: img/installation/anaconda-prompt.png
     :class: with-border

     From the Anaconda Navigator, you can select "environments" on the
     left, then click on one, then the arrow, then "Open terminal".

* You can try from the Jupyter terminal.



Verify the installation
~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Watch the video

   See this `verification in video form
   <https://youtu.be/OEX1ss_HCHc>`__ - if you can do this, you are
   ready to go for day one.

You should be able to start JupyterLab.  You can do this from the
`Anaconda Navigator <https://docs.anaconda.com/anaconda/navigator/>`__ (recommended if you have it), or from the command
line like this:

.. code-block:: console

   $ jupyter lab
   (... Jupyter starts in a web browser)

To verify command line usage:

.. code-block:: console

   $ python -V
   Python 3.8.3

   ## Or python3...
   $ python3 -V
   Python 3.8.3

Any version of Python 3 through Anaconda should work for the course.


Text editor
-----------

For one portion of the course, you will need a text editor.  If you
don't know what to use, you can use the text editor that comes from
JupyterLab and it will do everything you need.

For other editors, see the `CodeRefinery instructions
<https://coderefinery.github.io/installation/editors/>`__.  You don't
exactly need a terminal editor - the graphical ones, such as VSCode or
whatever you use now, will work as well.



Command line
------------

See above under "command line".

TODO.  You can see the `CodeRefinery instructions
<https://coderefinery.github.io/installation/bash/>`__ for more
advanced ways of doing things.


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
