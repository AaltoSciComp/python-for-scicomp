Binder
======

.. questions::

   - Why sharing code is not sufficient?
   - How to share computational environment?
   - What is Binder?
   - How to binderize my python repository?
   - How to publish my python repository?

.. objectives::

   - Learn about reproducible computational environments
   - Learn to create and share custom computing environments with myBinder
   - Learn to get a DOI from zenodo for a repository.



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

How can I get a DOI from Zenodo?
---------------------------------

`Zenodo <https://about.zenodo.org/>`_ is a general purpose open-access repository built and operated by `CERN <https://home.cern/>`_ and `OpenAIRE <https://www.openaire.eu/>`_ that allows researchers to archive and get a `Digital Object Identifier (DOI) <https://www.doi.org/>`_ to data that they share.

1. Link GitHub with Zenodo:

- Go to `https://zenodo.org <https://zenodo.org>`_
- Log in to Zenodo with your GitHub account. Be aware that you may need to authorize Zenodo application (Zenodo will redirect you back to GitHub for Authorization)
- Choose the repository webhooks options
- From the drop-down menu next to your email address at the top of the page, select GitHub.
- You will be presented with a list of all your Github repositories

2. Archiving a repo:

- Select a repository you want to archive on Zenodo.
- Toggle the "on" button next to the repository ou need to archive.
- Click on the Repo that you want to reserve.
- Click on Create release button at the top of the page. Zenodo will redirect you back to GitHub’s repo page to generate a release 

3. Trigger Zenodo to Archive your repository
- Go to GitHub and create a release. Zenodo will automatically download a .zip-ball of each new release and register a DOI. 
- If this is the first release of your code then you should give it a version number of v1.0.0. Add description for your release then click the Publish release button.
- Zenodo takes an archive of your GitHub repository each time you create a new Release

4.  To ensure that everything is working:

- Go to https://zenodo.org/account/settings/github/,  or the Upload page (https://zenodo.org/deposit), you will find your repo is listed 
- Click on the repo, Zenodo will redirect you to a page that contains a DOI for your repo will the information that you added to the repo. 
- You can edit the archive on Zenodo and/or publish a new version of your software.
- It is recommended that you add a description for your repo and fill in other metadata in the edit page. 
- Your code is now published on a Github public repository and archived on Zenodo. 
- Update the README file in your repository with the newly created zenodo badge.

How to create a Binder link for your Zenodo DOI?
-------------------------------------------------

We use the same recipe as in our previous exercise:

- Go to `https://mybinder.org <https://mybinder.org>`_ and fill information using Zenodo DOI (as shown on the figure below)

.. image:: https://miro.medium.com/max/1050/1*xOABVY2hNtVmjV5-LXreFw.gif

- Get your Binder badge and update the README file in your repository. It is good practice to add both the zenodo badge and the corresponding binder badge.


.. keypoints::

   - Sharing reproducible computational environments
   - myBinder
