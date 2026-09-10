reactions_analyser.py
=====================

``reactions_analyser.py`` uses ``master_array.pickle``, ``out_data.pickle``,
``reactions.pickle`` and ``surface_dictionary.py`` to produce a CSV of the
production or loss rate of a species due to each specific reaction.

Like the extractor, this is not part of INCHEM-Py itself but a tool for making
use of its outputs. It lets users with no prior Python knowledge assess
reaction rates at specific times in a simulation, and is intended to be
modified for specific needs. The lines to modify are near the top of the
script.

.. note::

   ``reactions.pickle`` is only written when ``reactions_output`` is ``True``
   in the settings file, so run the simulation with that enabled before using
   this tool.

output_folder
-------------
::

    output_folder = "reaction_rates_output_folder"

The name of the folder to save the CSV of reaction rates to.

out_directory
-------------
::

    out_directory = 'INCHEM-Py_output_folder'

The name of the INCHEM-Py output folder containing the model outputs to
analyse.

species
-------
::

    species = "HCHO"

The species for which reaction rates should be calculated, in MCM format.

time_index
----------
::

    time_index = 120

The time (seconds) at which to analyse the reaction rates. This must be an
output time point of the simulation being analysed.

surface_dict_path
-----------------
::

    surface_dict_path = 'modules/surface_dictionary.py'

Path to the surface dictionary. This must be from the same version of the
model as the simulated data.

timed_emissions and timed_inputs
--------------------------------
::

    timed_emissions = True   # or False
    timed_inputs = {"species":  [[start, end, rate]],
                    "species2": [[start, end, rate], [start, end, rate]]}

Whether timed emissions were used in the simulation, and — if so — the same
``timed_inputs`` dictionary used in that simulation's ``settings.py``.

H2O2_dep and O3_dep
-------------------
::

    H2O2_dep = True   # or False
    O3_dep = True     # or False

Whether O\ :sub:`3` or H\ :sub:`2`\ O\ :sub:`2` surface-specific deposition
was included in the simulation being analysed. These must match the
simulation's settings.
