Homework: 2D Ising model
========================

This homework exercise shares many similarities with the XY model
studied above.  The main difference is that in the 2D Ising model, the
spins are perpendicular to the plane, and can take only two values,
``+1`` and ``-1``. This model can be used to study the ferromagnetic
phase transition. Below the critical temperature ferromagnetic
domains, where the spins are aligned, form. Above the critical
temperature this order breaks down. In the Ising model the
configuration energy is defined as

.. math:: E = - J \sum_{i \ne j} \sigma_i \sigma_j - \mu H \sum_j \sigma_j,

where J is the exchange energy, :math:`\mu` is the magnetic moment of
the spins, and H is the external magnetic field in the direction
perpendicular to the plane. To simplify, you can set J and :math:`\mu`
to 1.

Implement a simulation program simulating the 2D Ising model. Use the
Metropolis-Hastings Monte Carlo algorithm. Visualize the results with
matplotlib. Run the simulation at different temperatures and with
different starting configurations (random vs. ordered), and see if you
can find the critical temperature by observing your visualizations.

If you find the above too easy, a few topics for further
exploration. Not needed to pass the course.

- Implement the Wolff algorithm, which flips whole clusters at a time
  instead of individual spins.  This helps avoid a phenomena called
  *critical slowing down* close to the critical temperature, which is
  problematic for algorithms such as the Metropolis algorithm that
  flip one spin at a time.

- Calculate and plot the net magnetization, the magnetic
  susceptibility, and the heat capacity of the system as a function of
  the temperature. How do they behave around the critical temperature?
