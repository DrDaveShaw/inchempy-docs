Model set-up
============

INCHEM-Py consists of a number of input files and a single settings file in
which the model options are specified. The files themselves are all
commented, but a description is also provided below.

Naming conventions
------------------

All species names are in the format given by the MCM download. There is no
guide to these, but they are self-explanatory in most cases. If you are
unsure of a species name, check using `the MCM website
<https://mcm.york.ac.uk/>`_ and search for the species using its MCM name or
SMILES string.

When using custom inputs it is important that any new species do not share a
name with any existing species, including those used in the
``inchem_chemistry.py`` inputs.

Other names are assigned within INCHEM-Py. The following naming conventions
are used:

* ``J1, J2, J3, ...`` — photolysis rates, combining indoor artificial
  lighting and attenuated sunlight according to the selected conditions.
* ``O3OUT, HONOOUT, NOOUT, ...`` — outdoor concentrations. Not all species
  have outdoor concentrations, and the majority are constants. The specified
  outdoor concentrations are listed in ``outdoor_concentrations.py``.
* ``TSP`` — total suspended particles (molecules cm\ :sup:`-3`) and
  ``TSPx`` — total suspended particles in µg m\ :sup:`-3`, if particles are
  used.
* ``OH_reactivity, OH_production, ...`` — the reactivity and production
  rates of species specified in ``reactivity.py``.
* ``RO2`` — the sum of all organic peroxy radical concentrations.

settings.py
-----------

The settings file provides inputs for all of the current model variables and
runs the model. All species names must be in the MCM format. The following
variables can be adjusted; each must have a value even if unused.

filename
~~~~~~~~
``"mcm.fac"``

The file name of the MCM download from the MCM website. The format and
placement of the file are detailed in :doc:`dependencies`.

particles
~~~~~~~~~
``True`` or ``False``

Set to ``True`` to include gas-to-particle partitioning for limonene,
alpha-pinene and beta-pinene, and to ``False`` to exclude particle
formation. Details of how particles are implemented can be found in Carslaw
et al. (2012), based on the methodology of Pankow (1994). See
:ref:`implementations:Particles and HOMS`.

INCHEM_additional
~~~~~~~~~~~~~~~~~~
``True`` or ``False``

Set to ``True`` to use the ``inchem_chemistry.py`` module, which includes
additional reaction mechanisms developed specifically for indoor air
chemistry. See :ref:`implementations:Additional INCHEM reactions`.

custom
~~~~~~
``True`` or ``False``

Set to ``True`` to use a custom input file for user-defined reactions that
are not in the MCM. Set to ``False`` to not use any custom inputs.

custom_filename
~~~~~~~~~~~~~~~
``"custom_input.txt"``

Any ``.txt`` filename can be used, allowing multiple custom input files to
be saved in the INCHEM-Py directory. The format is detailed in
:ref:`model_setup:custom_input.txt (optional)`.

spline
~~~~~~
``293.``, ``"Linear"`` or ``"BSpline"``

Method for setting the temperature. For a constant temperature, in Kelvin, a
numerical value can be set (the default is 293 K). For a variable
temperature, a linear or zero-degree B-spline interpolation can be used
between the points given in ``temperatures``.

temperatures
~~~~~~~~~~~~
``[[time (s), temperature (K)], [time (s), temperature (K)]]``

Temperatures at given times, used only when ``spline`` is ``"Linear"`` or
``"BSpline"``. Times are times of day in seconds and temperatures are in
Kelvin. Each time must increase from the previous one. If not enough points
are given to cover the simulation, the model duplicates points; see
:ref:`implementations:Temperature`.

rel_humidity
~~~~~~~~~~~~
``50``

Relative humidity as a percentage. The default value is 50%.

M
~
``2.51e+19``

Number density of air in the simulated environment, in
molecules cm\ :sup:`-3`.

const_dict
~~~~~~~~~~
``{'species': number density in molecules cm⁻³}``

A dictionary of species or values that should remain constant throughout the
simulation. There is no limit on the number of species, and the model
removes them from the integration. O\ :sub:`2` (0.2095 × M) and
N\ :sub:`2` (0.7809 × M) should always be included, as the MCM does not
include them as products in reactions owing to their abundance.

ACRate
~~~~~~
``{time (s): air change rate (s⁻¹), ...}``

A dictionary of times and air change rates (per second). The air change rate
is set at the specified time and remains until the next specified time. The
first time value must be at or before ``t0``. The air change rate is the
number of times per second the room air volume is fully exchanged with
outdoor air. The default value for the first day is a typical
0.5 h\ :sup:`-1`, divided by 3600 to convert to s\ :sup:`-1`. For reference,
0.2 h\ :sup:`-1` is reasonable for a very well insulated building and
2.0 h\ :sup:`-1` for a very loosely built one.

diurnal
~~~~~~~
``True`` or ``False``

Set to ``True`` to include diurnally varying outdoor concentrations and to
``False`` to use constant values. Diurnal profiles are given for OH and
HO\ :sub:`2` radicals, NO, NO\ :sub:`2`, TSPOUT, O\ :sub:`3` and HONO. Both
the diurnal equations and the constant values can be adjusted in
``outdoor_concentrations.py``.

city
~~~~
``"London_urban"``, ``"London_suburban"``, ``"Bergen_urban"`` or
``"Milan_urban_Aug2003"``

The model comes with four preset outdoor fits to measured concentrations of
O\ :sub:`3`, NO\ :sub:`2`, NO and PM\ :sub:`2.5` (assumed to be TSPOUT).
Three are daily-average fits over July–September 2018 for urban London,
suburban London and urban Bergen. The Milan fit is from a particularly
polluted two-week period in August 2003 (Terry et al., 2014). Full details
are given in :doc:`outdoor_fits`. Because outdoor concentrations strongly
affect indoor chemistry, tailored outdoor fits are advised for any specific
location.

date
~~~~
``"21-06-2020"``

The day of the simulation in the format ``"DD-MM-YYYY"`` as a string. The
model uses this date for all simulated days; it drives the photolysis
calculation of the Sun's angle.

lat
~~~
``45``

The latitude of the simulation location.

light_type
~~~~~~~~~~
``"Incand"``, ``"Halogen"``, ``"LED"``, ``"CFL"``, ``"UFT"``, ``"CFT"``,
``"FT"`` or ``"off"``

The type of indoor lighting, as a string: incandescent, halogen,
light-emitting diode, compact fluorescent, uncovered fluorescent tube,
covered fluorescent tube and fluorescent tube respectively. Values are in
``photolysis.py`` and taken from Wang and Carslaw (2021). ``"off"`` sets the
indoor light attenuation factors to zero, removing indoor lighting.

light_on_times
~~~~~~~~~~~~~~
``[[light on (h), light off (h)], [light on (h), light off (h)]]``

A list of times at which indoor lights turn on and off, in hours from 00:00
on the first day of the simulation. For example, 7 is 7 a.m. on the first
day and 31 is 7 a.m. on the second. These are independent of the simulation
start time. Decimals can be used, so 7.5 is 07:30.

glass
~~~~~
``"glass_C"``, ``"low_emissivity"``, ``"low_emissivity_film"`` or
``"no_sunlight"``

Type of window glass used for the attenuation of outdoor light by wavelength
range. Values are in ``photolysis.py`` and based on Blocquet et al. (2018).
``"no_sunlight"`` sets all window attenuation factors to zero, so no light
enters from outdoors.

volume
~~~~~~
``2.97e7``

Volume of the simulated space (cm\ :sup:`3`). It is used together with the
surface areas below to calculate the surface-to-volume ratios of individual
surfaces and the total surface-to-volume ratio, which set the rate of
surface deposition — including for H\ :sub:`2`\ O\ :sub:`2` and O\ :sub:`3`,
whose deposition can cause surface emissions. The volume is also used to
dilute breath emissions correctly into the room.

.. versionchanged:: 1.3
   The settings file now takes physical surface areas and a room volume
   directly, rather than pre-computed surface-to-volume ratios. INCHEM-Py
   derives the ratios internally, and breath emissions are automatically
   scaled to this volume.

surface_area
~~~~~~~~~~~~
A dictionary of surface areas (cm\ :sup:`2`) for the different surfaces in
the indoor environment::

    surface_area = {          # (cm2)
        'SOFT'     : 10.42e4,  # soft furnishings
        'PAINT'    : 33.76e4,  # painted surfaces
        'WOOD'     : 18.23e4,  # wood
        'METAL'    : 7.46e4,   # metal
        'CONCRETE' : 0.391e4,  # concrete
        'PAPER'    : 1.89e4,   # paper
        'LINO'     : 0,        # linoleum
        'PLASTIC'  : 14.18e4,  # plastic
        'GLASS'    : 2.61e4,   # glass
        'HUMAN'    : 0,        # humans (does not include breath emissions)
        'OTHER'    : 0}        # other surfaces, no emissions

The default values are an average across the three rooms in Carter et al.
(2023). They are summed to give a total surface area used in the
surface-to-volume calculation. Individual surface areas matter specifically
for H\ :sub:`2`\ O\ :sub:`2` and O\ :sub:`3` deposition and the resulting
emissions.

.. tip::

   To turn surface deposition off, set the surface areas to zero rather than
   setting the volume to zero — this avoids a division by zero.

H2O2_dep and O3_dep
~~~~~~~~~~~~~~~~~~~~
``True`` or ``False``

Deposition schemes for H\ :sub:`2`\ O\ :sub:`2` and O\ :sub:`3`. When either
is ``True``, the volume and ``surface_area`` dictionary are used to calculate
surface deposition of that species and the subsequent VOC emission.
Development of this system is given in Carter et al. (2023); see
:ref:`implementations:Surface deposition`.

adults and children
~~~~~~~~~~~~~~~~~~~~
``0``

The number of adults and children (aged 10) present in the room, for the
calculation of breath emissions. Emission rates for acetone, ethanol,
methanol, isopropanol and isoprene are from Carter et al. (2023). The
function is in ``surface_dictionary.py``.

.. versionchanged:: 1.3
   Breath emissions are now automatically scaled to the room ``volume``, so
   the emission rates no longer need to be adjusted by hand when the room
   size changes.

initials_from_run
~~~~~~~~~~~~~~~~~~
``True`` or ``False``

Initial gas concentrations are provided either by a text file (when
``initials_from_run = False`` and ``initial_conditions_gas`` names a text
file) or by an output file from a previous run (when
``initials_from_run = True``).

The benefit of using a previous run is that the model takes the initial
values from the time point closest to ``t0`` in the input, so the initial
integration steps are faster and require less time to equilibrate. This is
especially useful when repeatedly running the model over a short window
around an event, such as a timed input.

To use data from a previous run, copy that run's ``out_data.pickle`` into
the main folder, rename it to ``in_data.pickle``, and set
``initials_from_run = True``. The file must contain values for all species
used in the current run.

.. versionadded:: 1.3
   Initial concentrations can also be supplied as a pandas **DataFrame in
   memory** rather than a pickle file on disk, via the model class's
   ``initial_dataframe`` argument. This is convenient for scripted or batch
   studies that chain runs together. See :doc:`whats_new`.

initial_conditions_gas
~~~~~~~~~~~~~~~~~~~~~~~
``"initial.txt"``

The name of the text file containing initial species concentrations in
molecules cm\ :sup:`-3`. Its format is detailed in
:ref:`model_setup:initial_concentrations.txt (optional)`. Any species
without a given concentration is assumed to be zero. To use this file,
``initials_from_run`` must be ``False``.

timed_emissions
~~~~~~~~~~~~~~~
``True`` or ``False``

Set to ``True`` to include additional emissions at specific points in time.
The times and rates are set using ``timed_inputs``.

timed_inputs
~~~~~~~~~~~~
``{"species": [[start (s), end (s), rate]], ...}``

A dictionary of species, times (s) and emission rates
(molecules cm\ :sup:`-3` s\ :sup:`-1`), used when ``timed_emissions`` is
``True``. A species can emit at more than one time. It is important that the
start and end times are divisible by ``dt`` so the integrator does not skip
the emission boundary. See :ref:`implementations:Timed emissions`.

dt
~~
``120``

Time between outputs in seconds. Also used as the maximum step for the
integrator. See :ref:`implementations:Integration`.

t0
~~
``0``

The time of day, in seconds from midnight, at which the simulation starts.

seconds_to_integrate
~~~~~~~~~~~~~~~~~~~~~
``86400``

The length of the run in seconds, starting at ``t0``. Arithmetic is
accepted, so four hours can be written ``3600*4``.

custom_name
~~~~~~~~~~~
``"string"``

A string appended to the output folder name to make runs easier to find and
identify.

reactions_output
~~~~~~~~~~~~~~~~
``True`` or ``False``

INCHEM-Py calculates the rate constant for each reaction at every time point.
Setting this to ``True`` saves all reactions and their assigned constants to
``reactions.pickle`` and adds all calculated reaction rates and surface
deposition rates to ``out_data.pickle``. This substantially increases the
output size.

output_graph
~~~~~~~~~~~~
``True`` or ``False``

``True`` to produce a graph of the selected species (``output_species``),
written to ``graph.png`` in the output folder, with the concentrations also
saved as CSV in molecules cm\ :sup:`-3`.

output_species
~~~~~~~~~~~~~~
``['species 1', 'species 2', 'species 3']``

A list of species names to plot when ``output_graph`` is ``True``.

custom_input.txt (optional)
---------------------------

A file for inputting rate coefficients, reactions, additional peroxy radical
species for the RO\ :sub:`2` summation, and additional organic nitrate and
PAN-type species for those summations, where they are not already in the
model. To use it, set ``custom = True`` in the settings file.

Any species not in the MCM download but appearing in the custom equations are
added to the species list automatically, so spelling matters. Any new species
formed on the right-hand side of a reaction should also appear on the
left-hand side of at least one other reaction, or it plays no further part in
the chemistry once formed. Take care not to duplicate species or reactions
already in the MCM or ``inchem_chemistry.py``.

Calculations (for example, rate coefficients) must be valid Python and follow
INCHEM-Py conventions, such as ``temp`` for temperature. Additional photolysis
rates must be added in the appropriate module, not here.

**Rate coefficients** — common coefficients used across multiple reactions
(for example ``KRO2NO``)::

    name = coefficient calculation

**Reactions** — species reactions with their rate coefficients::

    rate coefficient : species + species = species + species
    rate2 coefficient : species + species = species

A reaction need not have species on both sides; pure loss or gain reactions
are valid::

    rate of loss coefficient : species =
    rate of gain : = species

**Peroxy radicals** — new user-defined peroxy radical species to add to the
RO\ :sub:`2` summation, on a single line::

    peroxy_radicals = species, species, species

**Summations** — sums of species for use in custom scenarios::

    sum : name_of_summation = species+species+species
    sum : name_of_second_summation = species+species+species

The word ``sum`` tells the model to parse the line as a summation.

initial_concentrations.txt (optional)
-------------------------------------

Sets the starting concentrations of species when ``initials_from_run`` is
``False``. The file name must match ``initial_conditions_gas``. It is a list
of species and concentrations in molecules cm\ :sup:`-3`::

    species = concentration ;
    species2 = concentration ;

Any species in the model without a concentration here defaults to zero.

Constrained inputs (optional)
-----------------------------

.. versionadded:: 1.3
   Constrained inputs allow the model to be driven directly by
   time-dependent chemical measurements.

A CSV file can be used to constrain the concentrations of indoor and outdoor
species, J values, and rates over time. Configure it with the
``constrained_file`` setting:

* ``constrained_file = None`` (the default) — no constrained input.
* ``constrained_file = 'filename.csv'`` — use the named file.

The CSV must have the **time of day (in seconds)** as its first column. Each
subsequent column is headed with the name of the species or variable to
constrain, with concentrations or values beneath (molecules cm\ :sup:`-3`
for species concentrations). ``example_constraints.csv`` in the repository
shows the required format.

When a constrained file is used, the constrained species are removed from
the integration and held to the interpolated measured values, and the start
and end of the simulation are set to the first and last times in the CSV. If
you want to see decay from a constrained species, run one simulation with the
constrained file and then a second using ``initials_from_run`` (see
:ref:`model_setup:initials_from_run`).
