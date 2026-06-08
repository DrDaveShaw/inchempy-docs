reactions_analyser.py
=====================

reactions_analyser.py uses the master_array.pickle, out_data.pickle, reactions.pickle and the surface_dictionary.py to give a csv file containing the actual rates of production or loss rate of a species due to a specific reaction.

This is not a part of INCHEM-Py, but is a tool that is useful for making use of the INCHEM-Py outputs. It is provided so that users with no prior Python knowledge can quickly assess the reaction rates at specific times within a simulation, and is intended to be modified for the specific needs of users.

The lines that need modifying are between lines 162 and 196 in the reactions_analyser.py script.

::

   output_folder = "reaction_rates_output_folder"

The name of the folder to save the csv of reaction rates to.

::

   out_directory = 'INCHEM-Py_output_folder'

The name of the folder created by INCHEM-Py when running the model that contains the outputs from the model.

::

   species="HCHO"

Name of the species for which reaction rates should be calculated, in MCM format.

::

   time_index = 120

The time, in seconds, for which to analyse the reaction rates. This needs to be an output time point of the simulation being analysed.

::

   surface_dict_path = 'modules/surface_dictionary.py'

String path to the surface dictionary of INCHEM-Py. This needs to be from the same version of the model as the simulated data.

::

   timed_emissions = True or False

Boolean, whether timed emissions were used in the INCHEM-Py simulation being analysed.

::

   timed_inputs = {"species":[[start time, end time, rate]],
                   "species2":[[start time, end time, rate],
                   [start time, end time, rate]]}}

The timed_inputs dictionary specified in the settings.py file of the simulation of interest needs to be repeated here for the reactions analyser.

::

   H2O2_dep = True or False

::

   O3_dep = True or False

Specify whether O\ :math:`_3` or H\ :math:`_2`\ O\ :math:`_2` surface-specific deposition was included in the simulation being analysed. This needs to be the same as in the INCHEM-Py simulation settings.py file.