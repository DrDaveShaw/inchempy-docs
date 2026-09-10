What's new in v1.3
==================

Version 1.3 introduces a substantial internal rewrite of the model engine
along with several new capabilities and chemistry schemes. This page
summarises the changes and highlights anything that affects existing
``settings.py`` files.

.. contents:: On this page
   :local:
   :depth: 1

Settings file changes you need to know about
--------------------------------------------

Most existing settings carry over unchanged. The one change that affects
older input files is how the room geometry is specified.

**Surface areas and volume instead of surface-to-volume ratios.**
The settings file now takes physical **surface areas** (in cm\ :sup:`2`)
and a room **volume** (in cm\ :sup:`3`) directly, rather than pre-computed
surface-to-volume ratios. INCHEM-Py calculates the individual and total
surface-to-volume ratios internally. A useful side effect is that
**breath emissions are now automatically scaled** to the room volume, so
you no longer need to adjust emission rates by hand when you change the
size of the modelled space. See :ref:`model_setup:surface_area` and
:ref:`model_setup:volume` for the current inputs.

If you are migrating a v1.2.x ``settings.py``, replace any surface-to-volume
ratio inputs with the ``surface_area`` dictionary and ``volume`` value used
in the current default settings file.

New model engine (class-based)
------------------------------

The procedural ``run_inchem`` main routine has been reorganised around a
model **class**, ``InChemPyMainClass`` (in
``modules/inchem_main_class.py``). Constructing the object builds the
species list, reaction set, master array, and Jacobian once; calling its
``run`` method then performs the integration.

For the great majority of users nothing changes: you still edit and run
``settings.py`` exactly as before. The benefit of the class-based design is
that the expensive set-up step (building the mechanism) is separated from
the integration step, which makes it far easier to script advanced
workflows — for example, building the model once and running it repeatedly
with different initial conditions.

Subsets of the MCM can now be used
----------------------------------

Previously INCHEM-Py was designed to run only with the full MCM mechanism.
The model now **detects undefined species and assigns them a concentration
of zero**, which means you can supply a subset of the MCM rather than the
complete mechanism.

This is useful when you are interested in a limited set of chemistry and
want faster set-up and smaller outputs. Note the usual caveat about
particles still applies: particle and total-suspended-particle (TSP)
calculations require the relevant species to be present, so particle
modelling should still be run with the full mechanism.

Initialise from a DataFrame in memory
-------------------------------------

In addition to reading initial concentrations from a text file, or from a
previous run's ``out_data.pickle`` written to disk, the model's ``run``
method now accepts an optional pandas **DataFrame** of initial
concentrations passed directly in memory (the ``initial_dataframe``
argument).

This avoids the round-trip of writing a pickle to disk and reloading it,
which is particularly convenient in batch or scripted studies where one
run feeds the next.

Events mechanism for continuous integration periods
---------------------------------------------------

An **events** mechanism has been added. INCHEM-Py collects the indoor
lighting on/off times and the start and end times of any timed emissions,
and uses them to break the run into segments, **restarting the integrator
at each boundary** so that every integrated period is continuous.

Handling these discontinuities explicitly avoids the integrator having to
absorb a sudden step change (a light switching on, or an emission
beginning or ending) part-way through a step, which improves the
robustness and accuracy of the solution around those events.

HOMS (highly oxygenated molecules)
----------------------------------

Highly oxygenated molecule (HOMS) chemistry has been added, following the
mechanism of `Kruza et al. (2020)
<https://doi.org/10.1016/j.atmosenv.2020.117784>`_. HOMS rapidly form
secondary organic aerosol (SOA) from terpenes.

The terpenes that feed the HOMS scheme are specified in two places:

* **MCM terpenes** are specified in the particle input file
  (``modules/particle_input.py``).
* **INCHEM additional terpenes** are specified in the INCHEM chemistry
  file (``modules/inchem_chemistry.py``).

As before, both ``particles`` and ``INCHEM_additional`` must be set to
``True`` in the settings file for the full particle chemistry to be
included. See :ref:`implementations:Particles and HOMS`.

Constrain inputs from time-dependent measurements
-------------------------------------------------

A **constrained input file** can now be supplied to drive the model
directly with time-dependent chemical measurements. The file is a CSV in
which the first column is the time of day (in seconds) and each subsequent
column is named for the species, J value, or rate to constrain, with the
measured values beneath.

When a constrained file is used, the constrained species are removed from
the integration and instead held to the interpolated measured values, and
the start and end of the simulation are set to the start and end times in
the CSV. This is configured through the ``constrained_file`` setting; see
:ref:`model_setup:Constrained inputs (optional)`.

New and updated chemistry schemes
---------------------------------

The following furan-family schemes have been added, from Coggon et al.
(2019):

* Furan
* Methylfuran
* Dimethylfuran
* Furfural
* Methylfurfural

In addition, a number of the existing INCHEM additional chemistry
reactions have received **corrections and fixes** in this release.
