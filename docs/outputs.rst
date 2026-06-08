Outputs
=======

Multiple files are produced by INCHEM-Py during a model run. The output folder is named automatically using the current date and time in the format ``YYYYMMDD_hhmmss``, and an additional custom title can be set within the settings.py file ("custom_name"). The main output files are listed below:

.. _settings.py-1:

settings.py
-----------

A copy of the settings.py file used to run the model.

MCM.fac
-------

A copy of the MCM download used to run the model.

out_data.pickle
---------------

This is the main output of the INCHEM-Py model. This file is a compressed data frame (table) of all of the species concentrations with time. This method (as opposed to outputting all data in the csv format) is used because the data is saved more efficiently and can be opened again in Python for analysis, while retaining the functionality of the data frame when it was saved. Concentrations of species are all in molecules cm\ :math:`^{-3}` and follow the naming conventions detailed earlier in this manual.

Included within the output are as follows:

-  All species concentrations, unless they have been set as constants

-  The peroxy radical summation "RO2"

-  Photolysis J values "J1", "J2" etc...

-  Outdoor concentrations

-  Reactivity and production rates of species set in reactivity.py

If optional settings are also used, then the following are also included in the output:

-  INCHEM additional chemistry summations (e.g. "TOTPAN" and "TOTORGNO3")

-  Custom summations

-  Particle concentrations

To analyse the output data, there are two approaches. The first is to use inchem_extractor.py (included in the INCHEM-Py download) which requires little/no working knowledge of Python. The second is to manually extract data from the out_data.pickle file. Both approaches are outlined below and the choice of which to use depends on the level of analysis required.

A main aim for producing this model was to improve accessibility for use across a wide audience. Therefore, included in the INCHEM-Py download is the inchem_extractor.py. This provides an easy method of extracting required outputs from model runs that requires little/no prior knowledge of Python. Using this script, all output elements can be extracted from multiple out_data.pickle files into .csv files and will be plotted for initial assessment of results. A description of this file and its usage is given in appendix `10 <#inchem_extractor.py>`__.

For more detailed analysis of the output data, manipulation of the out_data.pickle file is required. Example commands to import and export the data are shown below. These are necessary if you wish to analyse the data further within Python.

::

   import pickle
   with open("out_data.pickle","rb") as handle:
       out_data=pickle.load(handle)

::

   species_to_export = ["species1", "species2", "species3"]
   out_data.to_csv("output.csv", columns = species_to_export)

Although all the data can be exported to a .csv file, the file size will be roughly double that of the equivalent pickle file.

.. _initial_concentrations.txt-1:

initial_concentrations.txt
--------------------------

A text file of initial concentrations of all species within the model run at t0.

INCHEM_inputs.txt
-----------------

Lists of species, summations, rate coefficents, and reactions included within the additional "INCHEM_chemistry" input file. This file provides a record of the additional indoor reactions used for a particular model run for future reference.

master_array.pickle
-------------------

A copy of the master array of ordinary differential equations for all species within the model run. The pickle module in Python can be used to open this to check the build of the ODEs and to investigate the mechanism if required. An example script to load the master array is

::

   import pickle
       
   with open("master_array.pickle", "rb") as handle:
       master_array = pickle.load(handle)

integration_times.csv
---------------------

A CSV of time stamps tracking the time from the start of the model to the start of each integration step.

output.csv (optional)
---------------------

A csv table of output species concentrations with time for the species specified in the "output_species" variable of settings.py if the "output_graph" variable is set to True.

graph.png (optional)
--------------------

A graph of species concentrations with time for the species specified in the "output_species" variable of settings.py. This is only produced if "output_graph" = True.

reactions.pickle (optional)
---------------------------

| reactions.pickle is a dictionary of all of the rate constants of all of the individual reactions included in the model. They are saved in the form of a dictionary as
| ``{reaction number:[rate equation, reaction]}``
| where the reaction number is an assigned number of the form "r1". reactions.pickle, out_data.pickle, master_array.pickle and surface_dictionary.py can be used to extract the reaction rate of any reaction at any time within a model run. A script to extract these rates is included additionally in the INCHEM-Py download as reactions_analyser.py, the variables of this script are described in appendix `11 <#reactions_analyser.py>`__. It is saved when "reactions_output" in settings.py is set to True.

The output from the reactions_analyser.py is a csv of rate numbers, the reaction rate at a specific time in molecules cm\ :math:`^{-3}` s\ :math:`^{-1}`, the equation of the rate coefficient and the reaction occurring at the calculated rate.
