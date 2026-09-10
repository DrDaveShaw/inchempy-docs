Running INCHEM-Py
=================

A :doc:`quickstart` guide is included at the start of this documentation.

Once you are happy with the input files, the model is run via ``settings.py``.
Two methods, both using Anaconda, are shown here. If you would like to edit
and run the code within a single environment, we recommend the Spyder IDE. If
you are comfortable running Python from the command line, that is also
described.

You may wish to run INCHEM-Py in a virtual environment; see
https://docs.python.org/3/tutorial/venv.html. Detailed instructions for
Anaconda are at https://docs.anaconda.com/.

Spyder
------

INCHEM-Py was written using the Spyder IDE. Spyder can be installed with
Anaconda or from the Anaconda Navigator.

Set the INCHEM-Py directory as your working directory using the folder icon
in the top right. Then, from the **Files** tab at the bottom of that pane,
double-click ``settings.py`` (or any file you wish to edit) to open it in the
editor on the left.

Run the model by opening ``settings.py`` and either clicking the green arrow
in the toolbar or pressing :kbd:`F5`. The model runs in the console at the
bottom right.

Only one simulation can run at a time in a single console, but multiple
consoles can be opened. Because a simulation uses substantial resources,
running several at once may not be any faster than running them in sequence.

Anaconda prompt or terminal
---------------------------

Assuming Python was installed via Anaconda, INCHEM-Py can be run from the
Anaconda prompt on Windows, or the terminal on macOS or Linux. Navigate to
the INCHEM-Py directory with ``cd`` and run ``settings.py``::

    cd C:/Directory/AnotherDirectory/INCHEM-Py/
    python settings.py

This can also be done in one command::

    python C:/Directory/AnotherDirectory/INCHEM-Py/settings.py

Be aware that this will not work if there are spaces in any directory name in
the path.

Batch runs
----------

``settings.py`` can be modified to produce batch runs across multiple
variable changes. It is a script that sets the input variables and then calls
INCHEM-Py; the model runs each time it is imported and writes a new output
folder. By changing variables between imports, a batch of runs can be
completed.

This method cannot change variables that are set inside the INCHEM-Py modules
rather than the settings file (for example, the outdoor concentrations);
changing those requires modifying the module.

.. tip::

   The v1.3 class-based engine makes advanced scripted workflows easier,
   because the mechanism can be built once and then integrated repeatedly
   with different conditions — including initial concentrations supplied as a
   DataFrame in memory. See :doc:`whats_new`.

Checking model function
-----------------------

When first running the model, you can confirm the default download behaves
as intended. A copy of a working default run (``default_output.csv``,
containing O\ :sub:`3` and outdoor O\ :sub:`3` with time) is in the
``test_files`` folder. After running the model with default values, the
``output.csv`` produced can be compared with ``default_output.csv`` to
confirm the run is valid.

``inchem_test.py`` (in the ``modules`` folder) tests the functions that
manipulate input data into the formats used internally. It uses preset
inputs from ``test_files``.

When entering new species or mechanisms via ``custom_input.txt``, take care
that names are correct and reactions are not duplicated: the model does not
test for duplicate or new species, as both are valid inputs. The
``master_array`` can be viewed to validate reactions, and the Jacobian is
saved for a similar purpose. Any user-entered mechanisms are saved alongside
those provided by the INCHEM-Py team.

Example usage
-------------

INCHEM-Py runs with no changes to the inputs, as downloaded. A simple test of
model behaviour is to adjust the air change rate (``ACRate``), which changes
the concentrations of all indoor species. Typical household values lie
between 0.2 h\ :sup:`-1` and 2 h\ :sup:`-1`.
