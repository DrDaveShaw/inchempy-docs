INCHEM-Py overview
==================

The INdoor CHEMical model in Python (INCHEM-Py) is an open source box model
that creates and solves a system of coupled ordinary differential equations
(ODEs) to provide predicted concentrations of indoor air pollutants through
time. It is a refactor of the indoor detailed chemical model developed by
Carslaw (2007), with improvements in form, function, and accessibility.

INCHEM-Py uses the Master Chemical Mechanism (MCM), a near-explicit mechanism
developed for atmospheric chemistry, together with additional chemical
mechanisms developed specifically for indoor air. These include gas-to-particle
partitioning for three commonly encountered indoor terpenes (limonene and
alpha- and beta-pinene), an improved photolysis parameterisation, indoor–outdoor
air change, and deposition to surfaces.

Typical usage of INCHEM-Py is either alongside experiment, where it can be used
to gain deeper insight into the chemistry through its ability to track a vast
array of species concentrations, or as a standalone method of investigating
chemical events that occur indoors over a range of conditions. INCHEM-Py is
open source, has no black-box processes, and all inputs can be tracked through
the model, allowing for a complete understanding of the system.

A wide array of outputs can be accessed, including species concentrations,
species reactivity and production rates, photolysis values, rate coefficients,
and summations such as the total peroxy radical concentration. Custom reactions
and summations can also be added by users to tailor the model to specific
indoor scenarios.

INCHEM-Py will continue to be developed, and new versions will be publicly
released alongside peer-reviewed literature.

Licensing and citation
-----------------------

INCHEM-Py is free software, released under the GNU General Public License
v3.0. A copy of the licence is included in the repository.

Because it is a scientific code, the developers ask that you show professional
courtesy when using it:

* Since you benefit from work on INCHEM-Py, please submit any improvements you
  make back to the project by opening a pull request. Report problems using the
  issue tracker.
* If you use INCHEM-Py results in a paper or professional publication, please
  include an appropriate reference. In most cases, if one or more of the
  INCHEM-Py team are involved in preparing results, they should appear as
  co-authors.
* The INCHEM-Py logo is included with the model and may optionally be used in
  oral or poster presentations.

Getting help
------------

Please contact the development team if you require any support:

* David Shaw — david.shaw@york.ac.uk
* Nicola Carslaw — nicola.carslaw@york.ac.uk
