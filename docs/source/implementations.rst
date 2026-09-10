Implementations
===============

This section describes how the model works internally. It is not needed to
run INCHEM-Py, but it is useful when interpreting results or extending the
chemistry.

Time
----

INCHEM-Py works in local **solar time**: a 24-hour period dictated by the
position of the Sun, which depends only on the date and the latitude of the
location.

The date is used to calculate the declination angle of the Sun:

.. math::

   DEC = -23.45 \times \cos\left(\frac{360}{365.25}\times (d+10)\right)

where :math:`d` is the number of days since the start of the year. This
accounts for the Earth's orbit; the solar zenith angle then accounts for the
Earth's rotation.

The local hour angle (LHA), the angle between the meridian of the Sun and the
meridian of the modelled location, is calculated in radians as:

.. math::

   LHA = \left(1+\frac{t}{4.32\times10^{4}}\right)\times\pi

where :math:`t` is the time of day in seconds. The solar zenith angle
:math:`\theta` then follows from the spherical law of cosines, which
simplifies to:

.. math::

   \cos(\theta) = \sin(Lat)\sin(Dec)+\cos(Lat)\cos(Dec)\cos(LHA)

Outdoor concentrations and time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No longitude input is required, because local solar time is consistent across
longitudes. This means local outdoor measurements must be corrected to solar
noon before use. Tools such as `NOAA Solar Calculator
<https://gml.noaa.gov/grad/solcalc/>`_ give solar noon in local time, from
which the shift can be found.

For example, an office in York (latitude 53.94°, longitude −1.05°) had solar
noon at 11:48:24 local time on 12 November 2020, so measurements made in
local time on that day need to be shifted forward by 11 minutes 36 seconds
for consistency with the model's photolysis calculation. Model output is also
in solar time and needs the opposite shift to compare with local-time
measurements.

The outdoor fits for OH, HO\ :sub:`2`, CH\ :sub:`3`\ O\ :sub:`2` and HONO use
the cosine of the solar zenith angle and are therefore already in solar time.

The horizon
~~~~~~~~~~~

The model uses the astronomical horizon (90° to the zenith). Where the solar
declination plus the latitude exceeds 90° or falls below −90°, the Sun is
below the horizon and there is no sunlight. Since the declination reaches at
most ±23.45°, locations beyond ±66.55° (within the Arctic or Antarctic
circle) have no sunlight at certain times of year. Such locations can still
be simulated; they simply receive no sunlight.

Temperature
-----------

Two variables define the temperature. ``spline`` sets the method — a fixed
value, a linear interpolation, or a B-spline interpolation — and
``temperatures`` supplies the points to interpolate (ignored when ``spline``
is a fixed number).

Setting ``spline`` to a number (in Kelvin) fixes the temperature for the whole
simulation. Otherwise ``temperatures`` is a list of times (s) and
temperatures (K) joined by linear or B-spline interpolation, for example::

    temperatures = [[25200, 288.15], [50400, 294.15]]

When the given points do not cover the whole simulation, INCHEM-Py assumes a
repeating diurnal pattern, copying the last point onto the previous day and
the first point onto the next, so a temperature is always available.

The linear interpolation uses NumPy's ``interp``; the B-spline uses SciPy's
``BSpline``, with knots, coefficients and degree from ``splrep`` at a
smoothness of 0 (forcing the curve through the given points). Note that the
B-spline can "overfit" and may not give a consistent fit over a multi-day
simulation.

Integration
-----------

INCHEM-Py uses `scipy.integrate.ode
<https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html>`_,
which provides access to several numerical integrators. Because the system is
stiff and highly coupled, LSODA from the ODEPACK Fortran package is used.

The default integrator arguments are:

* ``atol = [1e-6]*num_species`` — absolute tolerance, where ``num_species``
  is the total number of species.
* ``rtol = 1e-6`` — relative tolerance.
* ``first_step = 1e-10`` — size of the first integration step to try (s).
* ``nsteps = 2000`` — maximum number of internal time steps.
* ``max_step = dt`` — the output interval from the settings file.

**Return code.** When the integrator stops it reports a return code:

* ``2`` — Integration successful.
* ``-1`` — Excess work done on this call.
* ``-2`` — Excess accuracy requested (tolerances too small).
* ``-3`` — Illegal input detected.
* ``-4`` — Repeated error test failures.
* ``-5`` — Repeated convergence failures (perhaps bad Jacobian or
  tolerances).
* ``-6`` — Error weight became zero.
* ``-7`` — Internal workspace insufficient to finish.

If only ``settings.py`` has been changed, the most likely cause of failure is
timed emissions producing very fast concentration changes that the integrator
cannot resolve within ``nsteps``. Remedies are to check whether the emission
rate is too high, to reduce ``dt``, or to "ramp up" the emission (for example,
1 s at 10% of the rate, then 1 s at 50%, then at 100%).

**Threading.** During integration the model uses multiple threads.
``threadpool_limits(limits=4)`` caps this at four threads; the limit can be
raised for faster machines.

Events
------

.. versionadded:: 1.3

The model integrates in continuous segments separated by **events**.
INCHEM-Py collects the indoor lighting on/off times and the start and end
times of any timed emissions, sorts them, and integrates from one boundary to
the next, **restarting the integrator at each one**.

Handling these discontinuities explicitly means the integrator never has to
absorb a sudden step change — a light switching on, or an emission starting or
stopping — part-way through a step. Each integrated period is therefore
continuous, which improves robustness and accuracy around events.

Outdoor concentrations
----------------------

Outdoor concentrations are set in one of two ways. Most simply, a constant
outdoor value can be set for a species. To add a new outdoor species, take
its name, append ``OUT``, and add an entry to the dictionary in
``outdoor_concentrations.py`` with a concentration in molecules cm\ :sup:`-3`.
A species not in the outdoor dictionary has an outdoor concentration of zero.

A diurnal profile can also be defined. For OH, HO\ :sub:`2`,
CH\ :sub:`3`\ O\ :sub:`2` and HONO, concentrations depend on the solar zenith
angle. Diurnal profiles for O\ :sub:`3`, NO\ :sub:`2`, NO and PM\ :sub:`2.5`
(TSPOUT) are fitted to measurements from four European locations; see
:doc:`outdoor_fits`. If both a constant average and a diurnal profile are
defined for a species, the diurnal profile takes precedence, as it is
calculated second.

Outdoor concentrations are inputs only: the model does not update outdoor
values based on transfer from indoors.

Photolysis
----------

Photolysis is calculated for both indoor light sources and sunlight entering
from outdoors; these are summed to give the total photolysis rate. The
absorption cross-section of a species is wavelength-dependent, so the
photolysis coefficients are calculated 1 m from the light source using the
wavelengths of the light sources and the transmission of the glass types.
Full details are in Wang et al. (2022).

INCHEM-Py calculates coefficients ``J1``–``J8``, ``J11``–``J24``,
``J31``–``J35``, ``J41``, ``J51``–``J57`` and ``J70``–``J78``, covering the
photolysis of ozone, hydrogen peroxide, the nitrogen oxides, carbonyls,
nitrates and the chlorine species.

The light types (with their ``light_type`` inputs), from Kowal et al. (2017),
are incandescent (``Incand``), halogen (``Halogen``), light-emitting diode
(``LED``), compact fluorescent (``CFL``), uncovered fluorescent tube
(``UFT``), covered fluorescent tube (``CFT``) and fluorescent tube (``FT``).

The glass types (with their ``glass`` inputs and wavelength ranges), from
Blocquet et al. (2018), are Glass C Sacht self-cleaning, 315–700 nm
(``glass_C``); low emissivity, 330–700 nm (``low_emissivity``); and low
emissivity with film, 380–700 nm (``low_emissivity_film``). Options for lights
off and no sunlight are also available.

Surface deposition
------------------

INCHEM-Py can treat surface deposition of H\ :sub:`2`\ O\ :sub:`2` and
O\ :sub:`3` separately from other species, where their deposition depends on
the surface and can produce surface emissions, by setting ``H2O2_dep`` or
``O3_dep`` to ``True``.

The surface-to-volume ratio (A/V, cm\ :sup:`-1`) is calculated from the
``volume`` and ``surface_area`` inputs. Within the surface dictionary the
deposition velocities are multiplied by A/V and fed to the ODE for each
species. Particles are assigned a deposition velocity of 0.004 cm s\ :sup:`-1`
(Carslaw et al., 2012). Species without a value in the surface dictionary do
not deposit. Deposition for a new species can be added in ``custom_input.txt``
as a reaction whose rate coefficient is the deposition velocity::

    0.016*AV : species1 =

When ``H2O2_dep`` or ``O3_dep`` is ``True``, INCHEM-Py uses surface-specific
deposition velocities, surface-specific A/V ratios, and the gas-phase
concentrations of H\ :sub:`2`\ O\ :sub:`2` and O\ :sub:`3` to calculate
surface losses, then applies known yields to calculate the emission of
species from each surface. Details are in Carter et al. (2023).

Breath emissions
----------------

INCHEM-Py can include breath emissions from adults and children (Carter et
al., 2023), set via ``adults`` and ``children`` in the settings file. The
function is in ``surface_dictionary.py``, where the emission rates can be
changed.

.. list-table:: Breath emissions (molecules cm\ :sup:`-3` s\ :sup:`-1`)
   :header-rows: 1

   * - Species
     - Adult rate
     - Child rate
   * - Acetone
     - 2.534×10\ :sup:`7`
     - 4.781×10\ :sup:`6`
   * - Ethanol
     - 1.98×10\ :sup:`7`
     - 3.009×10\ :sup:`6`
   * - Methanol
     - 8.512×10\ :sup:`6`
     - 3.108×10\ :sup:`6`
   * - Isopropanol
     - 3.862×10\ :sup:`6`
     - 6.593×10\ :sup:`5`
   * - Isoprene
     - 5.412×10\ :sup:`6`
     - 5.953×10\ :sup:`5`

.. versionchanged:: 1.3
   These measured rates (taken in a classroom of a known volume) are now
   automatically scaled to the room ``volume`` set in the settings file, so
   you no longer need to adjust them by hand for different room sizes.

Additional INCHEM reactions
---------------------------

To analyse varying indoor scenarios, additional mechanisms developed by
Carslaw and co-workers can be included by setting ``INCHEM_additional`` to
``True``. Unlike the MCM, these schemes are not fully explicit: they typically
take the rate coefficients from the literature for the first oxidation steps
and then map onto existing MCM species after a few steps, to limit
complexity. Species treated this way include linalool; octanal, nonanal and
decanal; chlorine; camphene, carene and terpinene; lactic acid; citronellol,
geraniol and geranial (citral); dihydromyrcenol; 2,5-DMBA; and α-terpinene,
α-phellandrene and terpinolene.

.. versionadded:: 1.3
   The following furan-family schemes have been added, from Coggon et al.
   (2019): **furan, methylfuran, dimethylfuran, furfural and
   methylfurfural**. A number of existing INCHEM chemistry reactions have
   also been corrected in this release.

This chemistry is in ``inchem_chemistry.py``. While careful modification is
possible, additional chemistry should preferably be added through
``custom_input.txt``. The chemistry is stored in the following formats.

**Peroxy radical species** (added to the RO\ :sub:`2` summation; not in the
MCM)::

    INCHEM_RO2 = ["species1", "species2"]

**Summations** (used in reactions or rate coefficients)::

    INCHEM_sums = [["sum_name", "species1 + species2 + species3"],
                   ["sum_name2", "species4 + species5 + species6"]]

**Rate coefficients**::

    INCHEM_rates = [
        ["name", "rate coefficient calculation"],
        ["name2", "rate coefficient calculation"],
    ]

**Reactions**::

    INCHEM_reactions = [
        ["rate coefficient calculation", "species1 + species2 = species3"],
        ["rate coefficient calculation", "species4 = species5 + species6"],
    ]

All generic rate coefficients, species and summations can be referenced in
reactions or summations added through ``custom_input.txt``.

Master array and Jacobian
-------------------------

The **master array** is a dictionary of species and their ODEs, processed by
the integrator. The ODEs are built from the MCM reactions, the INCHEM
chemistry, any custom reactions, and the gas-to-particle reactions.

To build the ODEs, each reaction (an equation plus a rate coefficient) is
parsed. For example:

.. math::

   \begin{aligned}
   y_1 + y_2 &\xrightarrow{k_1} y_3 + y_4\\
   y_2 + y_3 &\xrightarrow{k_2} y_1
   \end{aligned}

where :math:`y_n` is a species concentration. In the first reaction all
species change at a rate of :math:`y_1 y_2 k_1`, and in the second at
:math:`y_2 y_3 k_2`, positive for gain species and negative for loss species.
This gives:

.. math::

   \begin{aligned}
   \frac{dy_1}{dt} &= y_2 y_3 k_2 - y_1 y_2 k_1\\
   \frac{dy_2}{dt} &= -y_1 y_2 k_1 - y_2 y_3 k_2\\
   \frac{dy_3}{dt} &= y_1 y_2 k_1 - y_2 y_3 k_2\\
   \frac{dy_4}{dt} &= y_1 y_2 k_1
   \end{aligned}

Repeated for all reactions, this is the master array. Extra terms are added
for air change, surface deposition, and any timed emissions defined in the
settings file. The master array is saved to the output folder for analysis.

The **Jacobian** is built by parsing the master array: each ODE is
differentiated with respect to each species and saved as a compiled code
object, alongside its index positions in the Jacobian matrix.

.. note::

   In v1.3 this construction happens once when the model class is
   instantiated, before integration begins. See :doc:`whats_new`.

Timed emissions
---------------

Timed emissions are configured through ``timed_inputs`` in the settings file.
When the master array is written, every ODE includes a timed-emission term
that is zero unless specified. When specified, INCHEM-Py sets that term to the
given rate while the simulation time is between the user-entered start and end
times.

A typical use is to represent an emission event, such as cleaning. A single
limonene input::

    timed_inputs = {"LIMONENE": [[36720, 37320, 5e8]]}

Multiple species::

    timed_inputs = {"LIMONENE": [[36720, 37320, 5e8]],
                    "APINENE":  [[36720, 37320, 5e8]]}

A single species at multiple times::

    timed_inputs = {"LIMONENE": [[36720, 37320, 5e8], [39000, 39400, 5e8]]}

.. note::

   The start and end of each timed emission become integration boundaries in
   the v1.3 :ref:`implementations:Events` mechanism, so the integrator
   restarts cleanly at each one.

Reactivity and production
-------------------------

``reactivity.py`` calculates the total reactivity and total production rates
of selected species (by default, only OH). The total reactivity of a species
:math:`x` is the inverse of its lifetime, found by summing the reactivity of
all other species with :math:`x`. The production rate is the sum of all
reaction rates that create the species. Reactivity is in s\ :sup:`-1` and
production in molecules cm\ :sup:`-3` s\ :sup:`-1`.

Additional species can be added to the ``reactivity_species`` list in the
``reactivity_summation`` function::

    reactivity_species = ['OH']

Particles and HOMS
------------------

Particles are discussed in Pankow (1994) and Carslaw et al. (2012). **HOMS**
are highly oxygenated molecules that rapidly form secondary organic aerosol
(SOA) from terpenes.

.. versionadded:: 1.3
   HOMS chemistry has been added, following `Kruza et al. (2020)
   <https://doi.org/10.1016/j.atmosenv.2020.117784>`_.

All terpenes in the model can create particles through the HOMS reactions. The
terpenes that feed the scheme are specified in two files:

* **MCM terpenes** in ``modules/particle_input.py``.
* **INCHEM additional terpenes** in ``modules/inchem_chemistry.py``.

Both ``particles`` and ``INCHEM_additional`` must be ``True`` for the full
particle chemistry to be included; with ``INCHEM_additional`` set to
``False``, INCHEM-Py significantly under-predicts particle production. A
discussion of the particle implementation (though not HOMS) is given in Shaw
et al. (2023).
