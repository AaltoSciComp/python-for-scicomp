Demo application
================

To demonstrate how to make a simple simulation program, here the
lecturer will 'live-code' a small simulation program.  For a suitable
model, lets choose a suitably fascinating problem that can be
simulated with a relatively simple model. First, some background.

Topological phase transitions
-----------------------------

Historically, for a long time we believed there were two, and only
two, kinds of phase transitions in nature.  So-called discontinous, or
first-order, transitions which are characterized by the presence of a
latent heat (mathematically, a discontinuity in the first derivative
of the free energy with respect to some thermodynamic parameter),
whereas continuous phase transitions are characterized by a
discontinuity in the second or higher derivative of the free energy.

However, in the 1970'ies, some experiments on ultrathin films of
superfluid Helium-3 were made which produced data that existing
theories could not describe.  Eventually Kosterlitz and Thouless (and
independently Berezinskii in the then Soviet Union) were able to
describe what was happening.  What they had discovered was an entirely
new kind of phase transition which defied the existing classification
schemes. Namely, there is *NO* discontinuity in any free energy
derivative. So in a way, it's an *infinite*-order phase transition.

What is happening is that *topological defects* (vortices in this
case) in the system change how they interact with each other at the
critical temperature. At low temperatures below the transition
temperature the correlation function between spins decays as a power
law, whereas above the transition temperature the correlation decays
exponentially. This results in vortex-antivortex pairs at low
temperature, and a *vortex unbinding* transition at the transition
temperature with free vortices at higher temperatures.

This work eventually resulted in the 2016 Nobel Prize in Physics. See
the `scientific background for the 2016 physics prize
<https://www.nobelprize.org/uploads/2018/06/advanced-physicsprize2016-1.pdf>`_.

The XY model
------------

Topological phase transitions can be studied with a XY model (also
called the planar model, or rotor model). Take a lattice with spins
rotating in the plane. Each spin interacts with its neighbors, and the
configuration energy of the system is given by

.. math:: E = -J \sum_{i \ne j} s_i s_j,

where the sum is over nearest neighbor spins.

In this case we can ignore the constant J which determines the
interaction strength. Also, since the spin vectors are all of equal
lengths the dot product can be simplified, so we have

.. math:: E = - \sum_{i \ne j} \cos(\theta_i - \theta_j).


The Metropolis-Hastings Monte Carlo algorithm
---------------------------------------------

The Metropolis-Hastings algorithm is a Markov chain Monte Carlo method
that can be used for sampling a probability distribution.  In this
case, the basic idea is that for each spin ``s`` we do a *trial move*,
to change the spin. We then calculate a random trial spin ``s'``, and
calculate an acceptance probability

.. math:: A = min(1, \frac{P(s')}{P(s)}).

In this case the probability density is the
Boltzmann distribution

.. math:: P(s) = \frac{1}{Z} exp(-\beta E(s)) ,


where :math:`\beta` is the thermodynamic beta, or

.. math:: \beta = \frac{1}{k_B T} ,

where :math:`k_B` is the Boltzmann constant. For this simulation we
can set it to 1 and ignore it hereafter. :math:`\beta` is thus just
the inverse of the temperature.

Thus the quotient

.. math:: \frac{P(s')}{P(s)}

can be calculated as

.. math:: exp(-\beta (E' - E)).

Then finally, calculate a uniform random number ``r`` in the interval
``[0,1)``.  If :math:`r \le A` the new state is accepted. Repeating
this for all the spins constitutes a single Monte Carlo step in the
algorithm.
