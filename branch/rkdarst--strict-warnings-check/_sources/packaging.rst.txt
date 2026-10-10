Packaging
=========

.. questions::

   - How to organize larger Python projects?
   - How can you make your Python functions most usable by your collaborators?
   - How to prepare your code to make a Python package?
   - How to publish your Python package?

.. objectives::

   - Learn to identify the components of a Python package
   - Learn to create a Python package
   - Learn to publish a Python package


Organizing Python projecs into modules
--------------------------------------

what is ``__init__.py`` and relative imports.


Best practices
--------------

- Add a license to your code (See `Software Licensing and Open source explained with cakes <https://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/social-coding/master/licensing-and-cakes.md/#1>`__)
- Write a `README.md` file

It is also recommended to `document your package <https://coderefinery.github.io/documentation/>`__.

Birds-eye view of PyPI, pip, and Conda
--------------------------------------


Python packages
---------------

.. challenge:: Packaging 1

  TODO: - Create a very simple Python package and make it pip-installable
        - Test to install it locally


Submit your package to PyPI
---------------------------

TODO:
- Show what is required. Remind about the importance of documentation, license, etc.
- Test-PyPI


Tools that simplify sharing via PyPI
------------------------------------

- poetry
- flit


Building a conda package and share it
-------------------------------------

.. callout:: Prerequisites
  
  To create a conda package, `conda-build` package is required. You may install it with **Anaconda Navigator** or from the command line::

    conda install conda-build
  

The simplest way for creating a conda package for your python script is to first publish it in `PyPI <https://pypi.org/>`__ following the steps explained above. 

Building a python package with conda skeleton pypi
***************************************************

Once build, the conda package can be installed locally. For this example, we will use `runtest <https://pypi.org/project/runtest/>`__. 
`runtest <https://github.com/bast/runtest>`__ is a numerically tolerant end-to-end test library for research software.

1. Create pypi skeleton::

      conda skeleton pypi runtest

   The command above will create a new folder called `runtest` containing a file `meta.yaml`, the conda recipe for `runtest`.

2. Edit `meta.yaml` and update requirements::

      requirements:
        host:
          - pip
          - python
          - flit
        run:
          - python
          - flit

   In the requirements above, we specified what is required for the `host <https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#host>`__ and for `running <https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html#run>`__  the package.

   .. callout:: Remark

      For pure python recipes, this is all you need for building a python package with conda.
      If your package needs to be built (for instance compilation), you would need additional files e.g. `build.sh` (to build on Linux/Mac-OSX) and `bld.bat` (to build on Windows systems). You can also add test scripts for testing your package. See `documentation <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html#writing-the-build-script-files-build-sh-and-bld-bat>`__ 
  

3. Build your package with conda

   Your package is now ready to be build with conda::

     conda-build runtest


   .. callout:: Conda package location

      Look at the messages produced while building. The location of the local conda package is given (search for `anaconda upload`)::

	~/anaconda3/conda-bld/win-64/runtest-2.2.1-py38_0.tar.bz2

      The prefix `~/anaconda3/` may be different on your machine and depending on your operating system (Linux, Mac-OSX or Windows) the sub-folder `win-64` differs too (for instance `linux-64` on Linux machines).

      The conda package we have created is specific to your platform (here `win-64`). It can be converted to other platforms using `conda convert <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html#converting-a-package-for-use-on-all-platforms>`__.

4. Check within new environment

   It is not necessary to create a new conda environment to install it but as explained in previous episode, it is good practice to have isolated environments.

   ::

      conda create -n local-runtest --use-local runtest

   We can then check `runtest` has been successfully installed in `local-runtest` conda environment. Open a new Terminal with `local-runtest` environment (either from the command line::

     conda activate local-runtest

   or via **Anaconda Navigator** (Open Terminal), import runtest and check its version::

     import runtest
     print(runtest.__version__)


.. callout:: Building a conda package from scratch

  It is possible to build a conda package from scratch without using conda skeleton. We recommend you to check the `conda-build documentation <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html>`__ for more information.

To be able to share and install your local conda package anywhere (on other platforms), you would need to upload it to a `conda channel <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>`__ (see below). 


  
Publishing a python package
****************************

- Upload your package to *Anaconda.org*: see instructions `here <https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs-skeleton.html#optional-uploading-packages-to-anaconda-org>`__. Please note that you will have to create an account on Anaconda.

- Upload your package to `conda-forge <https://conda-forge.org/>`__: conda-forge is a conda channel: it contains community-led collection of recipes, build infrastructure and distributions for the conda package manager. Anyone can public conda packages to conda-forge if certain `guidelines <https://conda-forge.org/docs/>`__ are respected.

- Upload your package to `bioconda <https://bioconda.github.io/>`_: bioconda is a very popular channel for the conda package manager specializing in bioinformatics software. As for conda-forge, you need to follow their `guidelines <https://bioconda.github.io/contributor/guidelines.html>`__ when building conda recipes.

You can also `create your own conda channel <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/create-custom-channels.html>`__ for publishing your packages.

Version pinning
---------------

When to pin and when not to pin.


.. keypoints::

   - Organize your code for publishing
   - Pypi
   - conda
