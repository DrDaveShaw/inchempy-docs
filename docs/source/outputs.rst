Outputs
=======

Multiple files are produced during a model run. The output folder is named
automatically using the current date and time in the format
``YYYYMMDD_hhmmss``, with an additional custom title set by ``custom_name``.
The main output files are listed below.

settings.py
-----------

A copy of the ``settings.py`` file used to run the model.

MCM.fac
-------

A copy of the MCM download used to run the model.

out_data.pickle
---------------

This is the main output. It is a compressed DataFrame of all species
concentrations with time. Storing it this way is more efficient than a CSV
and preserves the DataFrame for later analysis in Python. Concentrations are
in molecules cm\ :sup:`-3` and follow the naming conventions in
:ref:`model_setup:Naming conventions`.

The output always includes:

* All species concentrations, unless set as constants.
* The peroxy radical summation ``RO2``.
* Photolysis J values ``J1``, ``J2``, etc.
* Outdoor concentrations.
* Reactivity and production rates of species set in ``reactivity.py``.

If the corresponding optional settings are used, it also includes:

* INCHEM additional chemistry summations (for example ``TOTPAN`` and
  ``TOTORGNO3``).
* Custom summations.
* Particle concentrations.

There are two ways to analyse the output. The first is
``inchem_extractor.py`` (see :doc:`extractor`), which requires little or no
Python knowledge. The second is to work with ``out_data.pickle`` directly.

**Importing the pickle**::

    import pickle
    with open("out_data.pickle", "rb") as handle:
        out_data = pickle.load(handle)

**Exporting selected species to CSV**::

    species_to_export = ["species1", "species2", "species3"]
    out_data.to_csv("output.csv", columns=species_to_export)

Exporting everything to CSV produces a file roughly double the size of the
pickle.

initial_concentrations.txt
--------------------------

A text file of the initial concentrations of all species at ``t0``.

INCHEM_inputs.txt
-----------------

Lists of species, summations, rate coefficients and reactions included from
the additional INCHEM chemistry input. This provides a record of the
additional indoor reactions used for a run.

master_array.pickle
-------------------

A copy of the master array of ODEs for all species in the run. It can be
loaded to inspect the ODE build and investigate the mechanism::

    import pickle
    with open("master_array.pickle", "rb") as handle:
        master_array = pickle.load(handle)

See :ref:`implementations:Master array and Jacobian`.

integration_times.csv
---------------------

A CSV of time stamps tracking the time from the start of the model to the
start of each integration step.

output.csv (optional)
---------------------

A CSV of output species concentrations with time, for the species in
``output_species``, produced when ``output_graph`` is ``True``.

graph.png (optional)
--------------------

A graph of species concentrations with time for the species in
``output_species``. Produced only when ``output_graph`` is ``True``.

reactions.pickle (optional)
---------------------------

A dictionary of the rate constants of all individual reactions, in the form::

    {reaction number: [rate equation, reaction]}

where the reaction number is of the form ``"r1"``. Together with
``out_data.pickle``, ``master_array.pickle`` and ``surface_dictionary.py``,
this can be used to extract the rate of any reaction at any time.
``reactions_analyser.py`` (see :doc:`reactions_analyser`) does exactly this.
It is saved when ``reactions_output`` is ``True``.
