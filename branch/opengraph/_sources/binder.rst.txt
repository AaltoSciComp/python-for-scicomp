Binder
======

.. questions::

   - Why sharing code alone may not be sufficient.
   - How to share a computational environment?
   - What is Binder?
   - How to binderize my Python repository?
   - How to publish my Python repository?

.. objectives::

   - Learn about reproducible computational environments.
   - Learn to create and share custom computing environments with Binder.
   - Learn to get a DOI from Zenodo for a repository.


Why is it sometimes not enough to share your code?
--------------------------------------------------

Before we work in groups,
let's take an example from geospatial
analysis where the first ``import`` in the code would be (please note that it is
not necessary to install any of the packages mentioned below)::

   from osgeo import ogr, osr, gdal

Depending on how you install this python package, it may be necessary to have
`libgdal` and its development headers already installed on your system; with
information on the version you have used, etc.


Exercise 1
~~~~~~~~~~

.. challenge:: Binder-1 (10 min)

   Lea is a PhD student in computational biology and after 2 years of intensive
   work, she is finally ready to publish her first paper. The code she has used
   for analyzing her data is available on GitHub but her supervisor who is an
   advocate of open science told her that sharing code is not sufficient.

   **Why is it possibly not enough to share "just" your code?
   What problems can you anticipate 2-5 years from now?**

   We form small groups (4-5 persons) and discuss in groups. If the workshop is
   online, each group will join a breakout room.
   If joining a group is not possible or practical, we use the shared document
   to discuss this collaboratively.

   Each group write a summary (bullet points) of the discussion in the workshop
   shared document (the link will be provided by your instructors).


Sharing a computing environment with Binder
-------------------------------------------

`Binder <https://mybinder.readthedocs.io/en/latest/>`__ allows you to create
custom computing environments that can be shared and used by many remote users.
It uses  `repo2docker <https://repo2docker.readthedocs.io/en/latest/>`__  to
create a container image (`docker <https://www.docker.com/>`__ image) of a
project using information contained in included configuration files.

Repo2docker is a standalone package that you can install locally on your laptop
but an `online Binder <https://mybinder.org/>`__ service is freely available.
This is what we will be using in the tutorial.

The main objective of this exercise is to learn to fork a repository and add a
requirement file to share the computational environment with Binder.

.. image:: https://opendreamkit.org/public/images/use-cases/reproducible_logbook.png

Credit: `Juliette Taka, Logilab and the OpenDreamKit project (2017) <https://opendreamkit.org/2017/11/02/use-case-publishing-reproducible-notebooks/>`_


Binder exercise/demo
~~~~~~~~~~~~~~~~~~~~

In an earlier episode (Data visualization with Matplotlib) we have created this notebook:

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt

   url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv"
   data = pd.read_csv(url)
   data_2007 = data[data["year"] == 2007]

   fig, ax = plt.subplots()

   ax.scatter(x=data_2007["gdpPercap"], y=data_2007["lifeExp"], alpha=0.5)

   ax.set_xscale("log")

   ax.set_xlabel("GDP (USD) per capita")
   ax.set_ylabel("life expectancy (years)")

We will now first share it via `GitHub <https://github.com/>`__ "statically",
then using `Binder <https://mybinder.org/>`__.

.. challenge:: Exercise/demo: Making your notebooks reproducible by anyone (15 min)

   Instructor demonstrates this:

   - Creates a GitHub repository
   - Uploads the notebook file
   - Then we look at the statically rendered version of the notebook on GitHub
   - Create a ``requirements.txt`` file which contains::

       pandas==1.2.3
       matplotlib==3.4.2

   - Commit and push also this file to your notebook repository.
   - Visit https://mybinder.org and copy paste the code under "Copy the text below ..." into your `README.md`:

     .. image:: img/binder/binder.jpg

   - Check that your notebook repository now has a "launch binder"
     badge in your `README.md` file on GitHub.
   - Try clicking the button and see how your repository is launched
     on Binder (can take a minute or two). Your notebooks can now be expored and executed in the cloud.
   - Enjoy being fully reproducible!


How can I get a DOI from Zenodo?
---------------------------------

`Zenodo <https://about.zenodo.org/>`__ is a general purpose open-access
repository built and operated by `CERN <https://home.cern/>`__ and `OpenAIRE
<https://www.openaire.eu/>`__ that allows researchers to archive and get a
`Digital Object Identifier (DOI) <https://www.doi.org/>`__ to data that they
share.

.. challenge:: Binder-3 (optional)

  **Everything you deposit on Zenodo is meant to be kept (long-term archive).
  Therefore we recommend to practice with the Zenodo "sandbox" (practice/test area)
  instead: https://sandbox.zenodo.org**

  1. **Link GitHub with Zenodo**:

    - Go to https://sandbox.zenodo.org (or to https://zenodo.org for the real upload later, after practicing).
    - Log in to Zenodo with your GitHub account. Be aware that you may need to
      authorize Zenodo application (Zenodo will redirect you back to GitHub for
      Authorization).
    - Choose the repository webhooks options.
    - From the drop-down menu next to your email address at the top of the page, select GitHub.
    - You will be presented with a list of all your Github repositories.

  2. **Archiving a repo**:

    - Select a repository you want to archive on Zenodo.
    - Toggle the "on" button next to the repository ou need to archive.
    - Click on the Repo that you want to reserve.
    - Click on Create release button at the top of the page. Zenodo will redirect you back to GitHub’s repo page to generate a release.

  3. **Trigger Zenodo to Archive your repository**

    - Go to GitHub and create a release. Zenodo will automatically download a .zip-ball of each new release and register a DOI.
    - If this is the first release of your code then you should give it a
      version number of v1.0.0. Add description for your release then click the
      Publish release button.
    - Zenodo takes an archive of your GitHub repository each time you create a new Release.

  4.  **To ensure that everything is working**:

    - Go to https://zenodo.org/account/settings/github/ (or the corresponding
      sandbox at https://sandbox.zenodo.org/account/settings/github/), or the
      Upload page (https://zenodo.org/deposit), you will find your repo is
      listed.
    - Click on the repo, Zenodo will redirect you to a page that contains a DOI for your repo will the information that you added to the repo.
    - You can edit the archive on Zenodo and/or publish a new version of your software.
    - It is recommended that you add a description for your repo and fill in other metadata in the edit page. Instead of editing metadata
      manually, you can also add a ``.zenodo.json`` or a ``CITATION.cff`` file to your repo and Zenodo will infer the metadata from this file.
    - Your code is now published on a Github public repository and archived on Zenodo.
    - Update the README file in your repository with the newly created zenodo badge.


Create a Binder link for your Zenodo DOI
----------------------------------------

Rather than specifying a GitHub repository when launching binder, you can instead use a Zenodo DOI.

.. challenge:: Binder-4 (10 min)

  We will be using an existing Zenodo DOI `10.5281/zenodo.3886864 <https://doi.org/10.5281/zenodo.3247652>`_ to start Binder:

    - Go to `https://mybinder.org <https://mybinder.org>`__ and fill information using Zenodo DOI (as shown on the animation below):

    .. image:: https://miro.medium.com/max/1050/1*xOABVY2hNtVmjV5-LXreFw.gif

    - You can also get a Binder badge and update the README file in the
      repository. It is good practice to add both the Zenodo badge and the
      corresponding Binder badge.

.. keypoints::

   - Sharing reproducible computational environments
   - Binder
   - Zenodo DOI
