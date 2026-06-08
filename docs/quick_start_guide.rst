Quick Start Guide
=================

If you’re new to Python then the following guide will take you through a quick way to download the model, run the model and access the outputs.

#. Download Anaconda 3 from https://www.anaconda.com/products/individual

#. Install Anaconda 3 with default settings. This is both your Python install as well as all of the required packages.

#. Download INCHEM-Py from https://github.com/DrDaveShaw/INCHEM-Py

#. Extract INCHEM-Py to the folder you would like to run it from.

#. Open Anaconda Navigator and "Launch" Spyder. If the "Launch" button says "Install" then you need to install it first.

   .. image:: _static/images/Spyder.png
      :alt: image
      :width: 40.0%

#. Spyder can be used to run INCHEM-Py. First navigate to the folder where INCHEM-Py was extracted by clicking the folder icon in the top right of Spyder. Browse to the INCHEM-Py directory. Select the INCHEM-Py folder.

   .. image:: _static/images/folder.png
      :alt: image
      :width: 1.5cm

#. At the bottom of the top right window in Spyder, click the "Files" tab. This will show the contents of the INCHEM-Py folder in this window.

   .. image:: _static/images/files.png
      :alt: image
      :width: 5cm

8. Double click on "settings.py" to open this file in the window on the left.

9. To run INCHEM-Py click the green arrow in the Spyder tool bar.

   .. image:: _static/images/run.png
      :alt: image
      :width: 3cm

   Progress will be shown in the console in the bottom right. It is normal for the first iteration to take a long time.

   .. image:: _static/images/progress.png
      :alt: image
      :width: 90.0%

   The output folder will also have been created in the INCHEM-Py directory with the current date and time, shown in the top right window. With default settings the model will take around 30 minutes.

   The default plot of ozone (O\ :math:`_3`, O3 in the model) and O\ :math:`_{3,outdoors}` (O3OUT in the model) can be seen in the Plots tab of the top right window, it is also saved in the created output folder as "graph.png" with these concentrations saved in csv format as "output.csv".

   .. image:: _static/images/example_out.png
      :alt: image
      :width: 90.0%

10. The full output is saved in "out_data.pickle". To extract other species concentrations to a csv file for analysis in other software the "inchem_extractor.py" file is used. Double click on this file to open it in the left hand window.

    The following variables can be changed to extract different outputs. Full details of these variables and how to change them can be found in appendix `10 <#inchem_extractor.py>`__.

    .. image:: _static/images/extractor.png
       :alt: image
       :width: 70.0%

11. To extract data from the model run that has just completed the "out_directories" variable must be changed. The output folder in this example is "20210302_114556_Bergen_urban" but will be slightly different for you. This name should be put into the "output_directories" variable.

    .. image:: _static/images/out_directories_variable.png
       :alt: image
       :width: 50.0%

12. To run the extractor, the same green arrow in the Spyder toolbar should be pressed.

    .. image:: _static/images/run.png
       :alt: image
       :width: 3cm

    The folder "extracted_outputs" is created and contains graphs for concentrations, reactivity, production rates, and photolysis of the default species in the extractor script. It also contains a csv file of all of these values from the simulation.
