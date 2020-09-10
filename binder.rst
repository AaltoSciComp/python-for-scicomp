Binder
======

.. questions::

   - Why sharing code is not sufficient?
   - How to share computational environment?
   - What is Binder?
   - How to binderize my python repository?

.. objectives::

   - Learn about reproducible computational environments
   - Learn to create and share custom computing environments with myBinder



Why isn't enough to share your code?
------------------------------------

Before we work in group and write our thoughts on why we need more than sharing our codes for reproducible research, let's take an example from geospatial analysis where the first `import` in the code would be: 


::

   from osgeo import ogr, osr, gdal


Depending on how you install this python package, it may be necessary to have `libgdal` and its development headers already installed on your system; with information on the version you have used, etc. 


.. challenge::

   Lea is a PhD student in computational biology and after 2 years of intensive work, she is finally ready to publish her first paper. The code she has used for analyzing her data is available on github but her supervisor who is an advocate of Open Science told her that sharing code is not sufficient.

   1. Why isn't enough to share your code?

   We form small groups (4-5 persons) and discuss in groups. If the workshop is online, each group will join a breakout room.

   Each group write a summary (bullet points) of the discussion in the workshop shared document (the link will be provided by your instructors).


Binder
------

`Binder <https://mybinder.readthedocs.io/en/latest/>`_ allows you to create custom computing environments that can be shared and used by many remote users. It uses  `repo2docker <https://repo2docker.readthedocs.io/en/latest/>`_  to create a container image (`docker <https://www.docker.com/>`_ image) of a project using information contained in included configuration files.

Repo2docker is a standalone package that you can install locally on your laptop but an `online Binder <https://mybinder.org/>`_ service is freely available. This is what we will be using in the tutorial.

How can I share my computing environment with myBinder?
-------------------------------------------------------

The main objective of this exercise is to learn to fork a repository and add a requirement file to share the computational environment with myBinder.


..image:: https://opendreamkit.org/public/images/use-cases/reproducible_logbook.png

Credit: `Juliette Taka, Logilab and the OpenDreamKit project (2017) <https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/>`_


.. challenge::

   1. Fork `the following github repository
<https://github.com/coderefinery/binder-exercise>`_. In the top-right corner of the page, click Fork.

.. image:: https://docs.github.com/assets/images/help/repository/fork_button.jpg

   2. Follow instruction given `here <https://coderefinery.github.io/jupyter/06-sharing/#exercise-making-your-notebooks-reproducible-by-anyone-via-binder>`_ to share the forked repository via `Binder <https://mybinder.org/>`_.


.. keypoints::

   - Sharing reproducible computational environments
   - myBinder
