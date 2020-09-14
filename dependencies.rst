Dependency management
=====================

.. questions::

   - How can my collaborators get the same results?
   - How can my collaborators easily install my codes with all the necessary dependencies?
   - How can make it easy for my colleagues to reproduce my results?

.. objectives::

   - Record dependencies
   - Simplify usage of my codes



Installing Packages for your project
-------------------------------------

The idea is to start thinking about identifying the list of packages for a given project.

--> Create an environment

- virtualenv 
- pipenv
- conda 


Dependencies
------------

https://coderefinery.github.io/reproducible-research/03-dependencies/#dependencies

.. challenge:: dependencies 1

  Maybe reuse example from preceding episode and ask learners to make the list of dependencies. Does everyone has the exact same version for each package?
  Create a requirements.txt for this project.

  Could be nice to have an example that requires a version > Y for a package (such ad matplotlib (3D plotting?).


Other Tools for Application Dependency Management
-------------------------------------------------

- poetry
- micropipenv

.. keypoints::

   - Conda, pip, Virtualenv, Pipenv, pyenv, Poetry, requirements.txt 
