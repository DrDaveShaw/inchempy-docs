inchem_extractor.py
===================

inchem_extractor.py will extract data from the out_data.pickle files produced by INCHEM-Py and save the species concentrations, or other outputs that are specified, to a csv file. Multiple output files can be read at a time. Plots comparing results from any files input will be saved to an output folder to get quick and easy comparisons between model runs.

This script is not part of INCHEM-Py but is an addition to give greater accessibility to any users that are not comfortable with Python. It is intended to provide quick access to data, not as a tool for further analysis.

All elements that should be changed by the user are at the top of the file.

::

   out_directories = ['directory1','directory2','directory3']

A list of output folder names that inchem_extractor will take output data from. These are created by INCHEM-Py when it is run in the format YYYYMMDD_hhmmss_custom and should be listed here. These names are not the full file path as this script expects to be one directory above these.

::

   species_to_extract = ['species1','species2','species3']

A list of output variables to extract and plot. The script will differentiate between concentrations, reactivity, production rates and photolysis coefficients (if entered) and plot them on separate graphs with the correct axes labels.

::

   start_time = 0
   end_time = 86400

Time in seconds between which to plot the graphs. This does not change the data extracted to .csv files, the full simulation time range will always be extracted.

::

   scale = "hours"

String to change the scale of the time axis on the plots. The options are "hours", "minutes", or "seconds". This does not change the data extracted to the .csv

::

   output_folder = "folder_name"

String name of output folder, that either exists already or is to be created, where the .csv files and plots are saved.

::

   log_plot = True

Can be True or False. True to set the y axis to a log scale, False to set the y axis to a linear scale.
