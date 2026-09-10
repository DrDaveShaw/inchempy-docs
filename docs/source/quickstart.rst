Quick start guide
=================

If you are new to Python, this guide takes you through a quick way to
download the model, run it, and access the outputs. Nothing needs to be
edited to get a first result — INCHEM-Py runs with its default settings.

Install and run
---------------

#. Download Anaconda 3 from https://www.anaconda.com/download and install
   it with the default settings. This provides both Python and all of the
   packages INCHEM-Py requires.

#. Download INCHEM-Py from https://github.com/DrDaveShaw/INCHEM-Py and
   extract it to the folder you would like to run it from. You must have
   write permission to this folder, as each run creates an output
   directory there.

#. Open Anaconda Navigator and launch **Spyder**. If the button says
   "Install" rather than "Launch", install Spyder first.

   .. image:: _static/images/Spyder.png
      :alt: Launching Spyder from Anaconda Navigator
      :width: 40%

#. In Spyder, set the INCHEM-Py directory as your working directory using
   the folder icon in the top right. Then click the **Files** tab at the
   bottom of that top-right pane to list the contents of the folder.

#. Double-click ``settings.py`` to open it in the editor pane on the left.

#. Run the model by clicking the green arrow in the Spyder toolbar (or
   press :kbd:`F5`).

   Progress is shown in the console at the bottom right. It is normal for
   the first iteration to take a long time while the mechanism is compiled.
   With default settings the run takes roughly 30 minutes.

   A new output folder, named with the current date and time, is created
   in the INCHEM-Py directory.

#. The default plot of ozone (``O3``) and outdoor ozone (``O3OUT``) appears
   in the **Plots** tab. It is also saved in the output folder as
   ``graph.png``, with the plotted concentrations saved as ``output.csv``.

   .. image:: _static/images/example_out.png
      :alt: Example default output plot of indoor and outdoor ozone
      :width: 90%

Extract further results
-----------------------

The complete run is saved in ``out_data.pickle``. To pull other species out
to CSV for analysis in other software, use ``inchem_extractor.py``:

#. Open ``inchem_extractor.py`` in Spyder.

#. Set the ``output_directories`` variable to the name of the output folder
   you just created (for example ``20240302_114556_Bergen_urban``; yours
   will differ).

#. Run the extractor with the green arrow.

   A folder called ``extracted_outputs`` is created containing graphs of
   concentration, reactivity, production rate, and photolysis for the
   default species, together with a CSV of those values.

Full details of every extractor option are given in :doc:`extractor`.
