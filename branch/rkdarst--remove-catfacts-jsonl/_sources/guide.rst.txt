Instructor's guide
==================

Learner personas
----------------

A is a early career PhD researcher who has been using Python a bit,
but is not sure what they know or don't know.  They want to be able to
do their research more efficiently and make sure that they are using
the right tools.  A may know that numpy exists, etc. and could
theoretically read some about it themselves, but aren't sure if they
are going in the right direction.

A2 can use numpy and pandas, but have learned little bits here and
there and hasn't had a comprehensive introduction.  They want to
ensure they are using best practices.  (Baseline of high-level
packages)

B is a mid-to-late undergraduate student who has used Python in some
classes.  They have possibly learned the syntax and enough to use it
in courses, but in a course-like manner where they are expected to
create everything themselves.


Prerequisites:
- Knowing basic Python syntax
- Watch the command line crash course, if you aren't familiar.

Not prerequisites:
- Any external libraries, e.g. numpy
- Knowing how to make scripts or use Jupyter



About each section
------------------

In general, "Python for Scientific Computing could be a multi-year
course.  We can't even pretend to really teach even a small fraction
of it.  We can, however, introduce people to things that can very
easily be missed in the typical academic career path.

* **Python intro:** We can't really replace a Python tutorial, but
  here we try to outline some of the main points.  We don't go over
  this in the course.

* **Jupyter:** Jupyter is somewhat useful, but the main reason we go
  over it is that it provides a convenient user interface for the
  other programming lessons (it's easier to spend a bit of time with
  Jupyter than expect people to be able to use some
  editor/IDE/shell/etc).  So, we do start from the beginning, so that
  people can do the other lessons, but also try to teach some advanced
  tips and tricks.

* **Numpy:** The basic of much of the rest of scipy, so we need to
  cover it.  We try to get the main principles out, but if someone
  already knows it this can be a bit boring.  We try to make sure
  everyone comes out with an appreciation for vectorization and
  broadcasting.

* **Pandas:** A lot of similar goals to the Numpy section, especially
  the concepts behind Dataframes that one needs to know in order to
  read other documentation.

* **Visualization:** Matplotlib is getting a bit old, but is still the
  backbone of other plotting packages.  We try to get forth the ideas
  of the matplotlib API that can be seen in other packages and the
  importance of scripted plots.

* **Data formats:** Input/output/storage is a common task, and can
  easily either be a bottleneck or a huge mess.  This lessons tries to
  show some best practices with data formats and, as usual, get the
  idea to not "do it yourself".  Pandas is used as a common framework,
  but we should point out there are plenty of other options.

* **Scripts:** The most important lesson here is to break out of
  Jupyter/run buttons of editors.  If you can't make actual programs
  with an actual interface, you can't scale up.

  * This is the first lesson to introduce the command line.  We
    recommend being as simple as possible: at least demonstrate the
    JupyterLab terminal and discuss the bigger picture behind what it
    means and why.

  * This is also the first lesson to use non-Jupyter code editor.  We
    recommend again being simple: use the JupyterLab code editor to
    start off, and carefully explain what is going on.

* **Scipy:** We don't cover much here (this is super short), but the
  point is scipy exists and the concept of wrapping existing C/fortran
  libraries and so on.

* **Library ecosystem:** This was an overview of the types of packages
  available in the "scipy ecosystem", which is a large and ill-defined
  thing.  But there is another point: choosing what to use.  Do you
  trust a half-done thing published on someone's personal webpage?  If
  it's on Github?  How do you make your code more reusable?  When
  coming from academic courses, you get a "build it yourself" idea,
  which isn't sustainable in research.

* **Parallel programming:**

* **Dependencies:** The main point here is environments, another thing
  you often don't learn in courses.

  * There is a lot of material here.  Consider what you will demo,
    what will be done as exercises, and what is advanced/optional.
    However, it is the fourth-day lesson that is most interactive, so
    it is OK if it take a while to go through everything.

  * If someone else installs Anaconda for a user (e.g. admin-managed
    laptop), the conda environment creations (with ``--name``,
    possibly with ``--prefix`` too?) may not work.  Be prepared for
    this and mention it.  You don't need to solve the problem but
    acknowledge that the lesson becomes a demo.  The virtualenv part
    should hopefully work for them.

* **Binder:** Binder exists and can help make code
  reproducible/reusable by others.

* **Packaging:** How to make your code reusable by others.  By the
  time we get here, people are tired and the topics get involved.  We
  more explicitly say "you might want to watch and take this as a
  demo".

