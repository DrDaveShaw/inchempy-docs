inchem_extractor.py
===================

``inchem_extractor.py`` extracts data from the ``out_data.pickle`` files
produced by INCHEM-Py and saves the species concentrations, or other specified
outputs, to CSV. Multiple output files can be read at once, and comparison
plots are saved to an output folder for quick comparison between runs.

This script is not part of the model itself: it is an addition to improve
accessibility for users who are not comfortable with Python. It is intended
for quick access to data rather than detailed analysis.

All values a user should change are at the top of the file.

out_directories
---------------
::

    out_directories = ['directory1', 'directory2', 'directory3']

A list of the INCHEM-Py output folder names to read (created in the format
``YYYYMMDD_hhmmss_custom``). These are folder names, not full paths; the
script expects to sit one directory above them.

species_to_extract
------------------
::

    species_to_extract = ['species1', 'species2', 'species3']

A list of output variables to extract and plot. The script distinguishes
between concentrations, reactivity, production rates and photolysis
coefficients, and plots each type on a separate graph with the correct axis
labels.

start_time and end_time
-----------------------
::

    start_time = 0
    end_time = 86400

The time range (seconds) over which to plot. This does not affect the data
written to CSV — the full simulation range is always extracted.

scale
-----
::

    scale = "hours"

Sets the time axis on the plots: ``"hours"``, ``"minutes"`` or ``"seconds"``.
This does not affect the CSV.

output_folder
-------------
::

    output_folder = "folder_name"

The name of the folder (existing or to be created) where the CSVs and plots
are saved.

log_plot
--------
::

    log_plot = True

``True`` for a logarithmic y-axis, ``False`` for a linear y-axis.
