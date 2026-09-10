Dependencies
============

Installing Python
-----------------

INCHEM-Py relies on a number of Python packages. If you use a recent
Anaconda distribution, all of the required packages are already included
and no further installation is needed.

If you are not using Anaconda, are using an older version, or have created
a new environment without the default packages, the following packages are
required:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Package
     - Known working version
   * - numpy
     - 1.21.5
   * - numba
     - 0.56.3
   * - pandas
     - 1.4.4
   * - tqdm
     - 4.64.1
   * - scipy
     - 1.9.1
   * - threadpoolctl
     - 2.2.0
   * - matplotlib
     - 3.5.2

.. note::

   INCHEM-Py saves some outputs as pickle files. When reloading a pickle
   for analysis you may see an error caused by a mismatch between the
   package versions used to create the file and those used to read it.
   Reading a pickle back with the same environment that produced it avoids
   this.

Downloading INCHEM-Py
---------------------

INCHEM-Py is available from https://github.com/DrDaveShaw/INCHEM-Py and
should be extracted to the directory from which it will be run. This can be
anywhere on the drive where there is sufficient space and where you have
write permission. Each run saves between roughly 100 MB and 3 GB of data,
depending on the output options selected.

A copy of the MCM is included in the download. It should be updated if and
when the MCM itself is updated.

Downloading the MCM
-------------------

The Master Chemical Mechanism can be downloaded from the
`MCM website <https://mcm.york.ac.uk/>`_.

To download a mechanism, first choose it via the "browse" tab on the MCM
website by checking the required subsets ("Check all" selects everything).
Use "Add Selection to Mark List" to add the checked subsets to your
selection, then use the "extract" tab to download the mechanism in the
**FACSIMILE input format**, optionally including inorganic reactions and
the generic rate coefficients. Selecting "Extract" downloads the ``.fac``
file.

.. note::

   As of v1.3, INCHEM-Py can also run with a **subset** of the MCM.
   Species that appear in reactions but are not defined are detected
   automatically and assigned a concentration of zero. Particle modelling
   still requires the full mechanism. See :doc:`whats_new`.

Folder structure
----------------

After extraction, the INCHEM-Py directory has the following structure. If
the model does not run, check that all of these files are present::

    INCHEM-Py/
    ├── modules/
    │   ├── test_files/
    │   │   ├── custom_input_test.txt
    │   │   ├── in_data.pickle
    │   │   ├── chemistry_test.py
    │   │   ├── initial_test.txt
    │   │   ├── jacobian_test.pickle
    │   │   └── mcm_parse_test.fac
    │   ├── constraints.py
    │   ├── inchem_chemistry.py
    │   ├── inchem_import.py
    │   ├── inchem_main.py
    │   ├── inchem_main_class.py
    │   ├── inchem_test.py
    │   ├── initial_dictionaries.py
    │   ├── outdoor_concentrations.py
    │   ├── particle_input.py
    │   ├── photolysis.py
    │   ├── reactivity.py
    │   └── surface_dictionary.py
    ├── custom_input.txt
    ├── example_constraints.csv
    ├── inchem_extractor.py
    ├── INCHEMPY_logo.png
    ├── INCHEMPY_logo.svg
    ├── initial_concentrations.txt
    ├── LICENSE
    ├── mcm_v331.fac
    ├── reactions_analyser.py
    ├── README.md
    └── settings.py

.. note::

   ``modules/inchem_main_class.py`` (the model class) and
   ``modules/constraints.py`` (constrained inputs) are part of the v1.3
   engine described in :doc:`whats_new`.
