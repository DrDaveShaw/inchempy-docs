Dependencies
============

INCHEM-Py relies on a number of Python packages. If you use Anaconda, then the current version at time of writing (Anaconda 2022.10) includes all of the packages required and no further downloads or installs are required.

If you have opted to not use Anaconda, are using an older version, or you have opened a new environment without the default packages, then the following packages need to be installed:

============= =====================
Package       Known working version
============= =====================
numpy         1.21.5
numba         0.56.3
pandas        1.4.4
tqdm          4.64.1
scipy         1.9.1
threadpoolctl 2.2.0
matplotlib    3.5.2
============= =====================

INCHEM-Py saves some serial outputs to a pickle file. When importing the pickle file for analysis you may find that you get an error which is likely due to a mismatch or lack of compatibility between the version of the packages used when creating the file and the version of packages used when unpickling. This is a known issue which will be fixed in later versions.

INCHEM-Py is available for download from https://github.com/DrDaveShaw/INCHEM-Py and should be extracted to the directory within the computer from which it will be run. This can be anywhere on the hard drive where there is sufficient space and where you have write permission. Each run of the model will save between 100 MB to 3 GB of data, depending on output options.

A version of the MCM is included in the INCHEM-Py download and is up-to-date as of February 2021 (checked April 2023), but should be updated if/when the MCM is updated.

The Master Chemical Mechanism (MCM) can be downloaded from `the MCM website <http://mcm.york.ac.uk/home.htt>`__.

INCHEM-Py has been designed to run with the full MCM mechanism.

In order to download a mechanism it first must be chosen via the `"browse" <http://mcm.york.ac.uk/roots.htt>`__ tab on the MCM website by checking the required subsets. "Check all" can be used to select everything, which INCHEM-Py has been designed to use. "Add Selection to Mark List" must then be used to add the checked subsets to your selection. Then the `"extract" <http://mcm.york.ac.uk/extract.htt>`__ tab can be used to download the mechanism or subset mechanism in the required format. This is the "FACSIMILE input format, suitable for inserting into a FACSIMILE model", also selecting the inclusion of inorganic reactions if required and the generic rate coefficients. Selecting "Extract" will download the required .fac file.

The following files show the folder structure of INCHEM-Py after extraction. If the model does not run, it could be due to missing files, please check that they are all downloaded and extracted correctly.
