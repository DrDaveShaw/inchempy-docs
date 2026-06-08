Model set-up
============

INCHEM-Py consists of a number of input files and a single settings file in which the model options can be specified. The files themselves are all commented, but a description is also provided below.

Naming conventions
------------------

All species names are in the format given by the MCM download. There is no guide to these but they are self explanatory in most cases. If you are unsure of a species name, then check using `the MCM website <mcm.york.ac.uk>`__ and search for the species using its MCM name or SMILES string.

When using custom inputs it is important that any new species do not share a name with any of the existing species, including those used in the inchem_chemistry file inputs.

Other names are assigned within INCHEM-Py. The following naming conventions are used:

-  ``J1, J2, J3, etc...`` - photolysis rates, combining indoor artificial lighting and attenuated sunlight according to the selected conditions

-  ``O3OUT, HONOOUT, NOOUT, etc...`` - outdoor concentrations. Not all species have outdoor concentrations and the majority are constants. The specified outdoor concentrations are listed in the outdoor_concentrations.py module

-  ``TSP`` - total suspended particles (molecules cm\ :math:`^{-3}`) and ``TSPx`` - total suspended particles in :math:`\mu`\ g/m\ :math:`^3`, if particles are used

-  ``OH_reactivity, OH_production, etc...`` - the reactivity and production rates of species specified in the reactivity.py module

-  ``RO2`` - the sum of all organic peroxy radical concentrations

settings.py
-----------

The settings file provides inputs for all of the current model variables and runs the model. All species names must be in the MCM format. The following variables are used in the model and can be adjusted. Each must have a value even if unused.

| ``"mcm.fac"``
| The file name for the download of the MCM from the MCM website. The format and placement of the file within the file structure is detailed earlier in this document.

|  ``True or False``
| Set to True to include gas-to-particle partitioning for limonene, alpha-pinene and beta-pinene within the simulation and to False to exclude particle formation. Details of how particles are implemented can be found in Carslaw et al. (2012), which is based on the methodology of Pankow (1994) (Nicola Carslaw et al. 2012; Pankow 1994).

| ``True or False``
| Set as True to use the inchem_chemistry.py module which includes additional reaction mechanisms developed specifically for indoor air chemistry.

| ``True or False``
| Set as True to use a custom input file to include user set reactions that are not included in the MCM. Set as False to not use any custom inputs.

| ``"custom_input.txt"``
| Any .txt filename can be used, allowing for multiple custom input files to be saved in the INCHEM-Py directory. The formatting of this file is detailed within the file itself and also within the custom_input.txt section of this document.

| ``293., "Linear" or "BSpline"``
| Method for setting the temperature. For a constant temperature, in degrees Kelvin, a numerical value can be set, the default is 293 K. For a variable temperature a linear or zero-degree B-Spline interpolation can be used to interpolate between temperatures at given time points using the "temperatures" variable.

| ``[[time (s), temperature (K)],[time (s), temperature (K)]]``
| Temperatures at given times. This is only used when the spline variable is set to "Linear" or "BSpline". Times are times of day in seconds, temperatures are in Kelvin. Each time must increase from the previous time and may or may not extend beyond the time of the simulation. If not enough time points are given then the model will duplicate points to cover the entire simulation, details are given in the temperature section of this document.

| ``50``
| Relative humidity as a percentage. Set to 50% as default value.

| ``2.51e+19``
| Number density of air in the simulated environment in molecules cm\ :math:`^{-3}`.

| ``{’species’ : number density in molecules cm``\ :math:`^{-3}`\ ``}``
| Dictionary of species or values that should remain constant throughout the simulation. There is no limit to the number of species that can be included in this way and the code will remove them from the integration. O\ :math:`_2` (0.2095\ :math:`\times`\ M) and N\ :math:`_2` (0.7809\ :math:`\times`\ M) should always be included as the MCM does not include them as outputs in reactions due to their abundance in the atmosphere.

|  ``{time (s) : air change rate (s``\ :math:`^{-1}`\ ``),``
| ``time (s) : air change rate (s``\ :math:`^{-1}`\ ``),``
| ``time (s) : air change rate (s``\ :math:`^{-1}`\ ``)}``
| A dictionary of times and Air Change Rates (ACRate) per second. The air change rate will be set at the specified time and will remain at that value until the next specified time. The first time value must be before or at t0. The ACRate is the number of times the volume of air in the room is fully changed with the air from outside. The default value for the first day of the simulation is a typical value of 0.5 h\ :math:`^{-1}` which is divided by 3600 to adjust to s\ :math:`^{-1}`. For reference, 0.2 h\ :math:`^{-1}` is considered to be a reasonable value for a very well insulated building, 2.0 h\ :math:`^{-1}` would be considered reasonable for a very loosely built building (Weschler 2000).

| ``True or False``
| Set as True to include diurnal outdoor concentrations and as False to use constant values. Diurnally varying concentrations are given for OH and HO\ :math:`_2` radicals, NO, NO\ :math:`_2`, TSPOUT, O\ :math:`_3` and HONO. Both the diurnal equations and the constant values can be adjusted in the outdoor_concentrations.py file within the modules folder.

| ``"London_urban", "London_suburban", "Bergen_urban",``
| ``or "Milan_urban_Aug2003"``
| The model comes with four preset outdoor fits to measured concentrations for O\ :math:`_3`, NO\ :math:`_2`, NO, and PM\ :math:`_{2.5}` (assumed to be TSPOUT). Three of these are daily average fits over the three month period of July - September for urban London, suburban London, and urban Bergen, in 2018. The Milan concentrations are fits taken from a particularly polluted two week period in Milan in August 2003 from Terry et al. (2014) (Terry et al. 2014). The full details of the locations and data can be found in the outdoor concentrations section of this manual. Although we do provide this data for use in the model it is clear that the outdoor concentrations can have a major effect on indoor air chemistry, therefore, we advise that tailored outdoor fits are produced for any specific location.

| ``"21-06-2020"``
| The day of the simulation in the format "DD-MM-YYYY" as a string. The model will use this date for all days simulated and it is used for the photolysis calculations to work out the angle of the Sun.

| ``45``
| The latitude of the simulation location.

| ``"Incand", "Halogen", "LED", "CFL", "UFT", "CFT", "FT", or "off"``
| The type of indoor lighting used within the simulation as a string. "Incand" for incandescent, "Halogen" for halogen, "LED" for light emitting diodes, "CFL" for compact fluorescent lighting, "UFT" for uncovered fluorescent tubes, "CFT" for covered fluorescent tubes, and "FT" for fluorescent tubes. The values used for these are included in the photolysis.py module and are taken from work done by Wang and Carslaw (2021) (Wang 2021). "off" sets the attenuation factors of indoor lights to 0 and, therefore, removes indoor lighting from the simulation.

| ``[[light on time (h), light off time (h)],[light on time (h), light off time (h)]]``
| A list of times at which the indoor lights are turned on and turned off. These times are in hours from 00:00 on the first day of the simulation. E.g. an input of 7 would be 7 AM on the first day and an input of 31 would be 7 AM on the second day. These are irrespective of the time at which the simulation starts, if the simulation is set to start at 8 am and the lights are set to come on at 7 AM, then the simulation would start with the lights on. Decimals can be used to fine tune the times, e.g. 7.5 as an input would equate to 7:30 AM on the first day.

| ``"glass_C", "low_emissivity", "low_emissivity_film",``
| ``or "no_sunlight"``
| Type of window glass used for the attenuation of outdoor light by wavelength range, given by a string. The values are given in the photolysis.py module and are based on the paper by Blocquet et al., (2018) (Blocquet et al. 2018). "no_sunlight" sets all window attenuation factors to 0 and therefore no light enters from outdoors.

| ``2.97e7``
| Volume of simulated space (cm\ :math:`^{3}`). It is used with the surface areas (below) to calculate the surface to volume ratios of individual surfaces and the total surface to volume ratio. This dictates the rate of surface deposition of species within the model, including H\ :math:`_2`\ O\ :math:`_2` and O\ :math:`_3` which can cause surface emissions. Individual species deposition rates can be adjusted in the surface_dictionary.py file in the modules folder. Volume is also used to adjust breath emissions to correctly dilute into the room, if on. To turn surface deposition off then the total surface areas should be set to 0 to avoid a division by 0 from setting the volume to 0.

| ``’SOFT’ : 10.42e4, # soft furnishings``
| ``’PAINT’ : 33.76e4, # painted surfaces``
| ``’WOOD’ : 18.23e4, # wood``
| ``’METAL’ : 7.46e4, # metal``
| ``’CONCRETE’ : 0.391e4, # concrete``
| ``’PAPER’ : 1.89e4, # paper``
| ``’LINO’ : 0, # linoleum``
| ``’PLASTIC’ : 14.18e4, # plastic``
| ``’GLASS’ : 2.61e4, # glass``
| ``’HUMAN’ : 0, # humans, does not automatically include breath emissions``
| ``’OTHER’: 0 # other surfaces, no emissions``
| A dictionary of surface areas for different surfaces in the indoor environment. The default values given are an average from all three rooms given in (Carter et al. 2023). These are summed to give a total surface area which is used in the calculation of the surface to volume ratios. Surface areas of individual surfaces are only important for H\ :math:`_2`\ O\ :math:`_2` and O\ :math:`_3` deposition and subsequent emissions.

| ``True or False``
| ``True or False``
| Deposition for H\ :math:`{_2}`\ O\ :math:`{_2}` and O\ :math:`{_3}` on (True) or off (False). If either of these are set to True then the volume and the surface_area dictionary is used to calculate surface deposition of hydrogen peroxide and/or ozone and subsequent VOC emission. Development of this system is given in (Carter et al. 2023), with some discussion in `7.6 <#surface_dictionary.py>`__.

| ``0``
| ``0``
| The number of adults and children present in the room for the calculation of breath emissions. Emission rates for acetone, ethanol, methanol, isopropanol and isoprene in breath are given by values calculated in (Carter et al. 2023). The function for this is in the surface_dictionary.py file.

|  ``True or False``
| Initial gas concentrations are either provided by a text file (when "initials_from_run" = False and "initial_conditions_gas" is provided with the name of a text file) or by an output file from a previous run (when "initials_from_run" = True and providing an input as detailed below).

The benefit of using an output file from a previous run is that the model will change the initial values depending on the start time of the simulation. E.g. if you set your model to run from 3600 seconds then by using "initials_from_run" the initial species concentrations will be from the 3600 second mark of the input file. The initial integration steps will be faster and require less time to equilibrate. This is especially useful if there is an event within the model, such as a timed input, which you are varying on multiple model runs and wish only to run the model over the short period where that event is occurring.

To use data from a previous run for initialising species concentrations, the out_data.pickle file from the run must be copied into the main folder of the model and renamed to in_data.pickle with "initials_from_run" set to True. The in_data.pickle file must contain values for all species used in the current model run.

| ``"initial.txt"``
| The string file name of the text file containing the initial species concentrations in molecules cm\ :math:`^{-3}`, the format of this file is detailed later in this document. If a species concentration is not given then the model will assume it is 0. To use this file, "initials_from_run" must be set to False.

|  ``True or False``
| Set as False to not include additional emissions and True to include additional emissions. Emissions can be added at specific points in time during the simulation. The times and emission rates are set using "timed_inputs".

| ``{"species":[[start time, end time, rate]],``
| ``"species2":[[start time, end time, rate],[start time, end time, rate]]}``
| A dictionary of species, times (s) and emissions rates (molecules cm\ :math:`^{-3}` s\ :math:`^{-1}`), for use when "timed_emissions" is set to True. The user needs to define the emission rates and times of emissions for their particular scenario in this file. In the above example, species2 emits at two different times at two different rates. It is important that the start and end times of the emissions are divisible by dt so that the integrator does not skip the emission start or end.

As many species can be input this way as required. The model will still calculate changes in concentration to these species over time during this input period, i.e. the total gain/loss rate will simply have the emission added to it. More details and examples are given later in this document.

| ``120``
| Time between outputs in seconds.

| ``0``
| The time of day, in seconds from midnight, to start the simulation.

| ``86400``
| The length of the model run in seconds, starting at t0. Arithmetic is accepted here so a simple way to run for four hours would be to input ``3600*4``.

| ``"string"``
| String that is added to the end of the output folder name to make output folders easier to find and identify.

| ``True or False``
| True to produce a graph of selected species (output_species) and write it to file as "graph.png" in the output folder, False to not produce a graph. The species chosen will also have their concentrations saved in a csv format in the output folder in molecules cm\ :math:`^{-3}`.

| ``[’species 1’,’species 2’,’species 3’]``
| A list of string names of species to be plotted on a graph if "output_graph" is set to True.

.. _custom_input.txt:

custom_input.txt (optional)
---------------------------

A file for inputting rates, reactions, additional peroxy radical species for the RO\ :math:`_2` summation, as well as additional organic nitrate and PAN-type species for the summations of these that are not already included in the model. To use this file then custom in settings.py must be set to True. This allows users to add custom mechanisms. A description of how to format the file is included here and within the file itself. Any species that are not already in the MCM download but that do appear in any of the additional custom equations will be automatically added to the species list. The user must be careful to spell the species names correctly. The user also needs to check that any new species formed on the right-hand side of a reaction, also appears on the left-hand side of at least one other reaction. Otherwise, the species would play no other part in the chemistry once formed. Finally, the user should be careful not to include species or reactions that are already in the model mechanism and should check against the species and reactions in the MCM and inchem_chemistry.py carefully (it is possible to search the MCM by molecular weight and smiles string at http://mcm.york.ac.uk/).

The format of any calculations (e.g. for rate coefficients) should be acceptable for Python and fit with the conventions used within INCHEM-Py, such as ’temp’ for temperature or "e" for the exponent. Any additional photolysis rates must be added in the appropriate module file and not here.

This file can be uniquely names to allow for multiple custom input files to be saved. Only one file can be imported by the model per run.

Rate coefficients in this file are common ones that might be used in multiple reactions within the file (e.g. KRO2NO for each time that a peroxy radical reacts with NO). These are simply entered as

::

       name = coefficient calculation

Reactions in this file are species reactions with their rate coefficients. The rate coefficients can include calculations, constants, common values included in the MCM (see previous section), additional values within this file, or a combination of these. The form that reactions should take is

::

       rate coefficient : species + species = species + species
       rate2 coefficient : species + species = species

The code uses the colon and the mathematical symbols to parse the input so it is important that these are correct. There doesn’t have to be a species on both sides of the reaction, pure loss or gain reactions are both valid, for example:

::

       rate of loss coefficient : species = 
       rate of gain : = species

The model uses RO\ :math:`_2` as a summation of all organic peroxy radicals. New user-defined peroxy radical species need to be added to the file where shown. This is a single line within the file of the format

::

       peroxy_radicals = species, species, species

To add summations of species that are to be used in custom scenarios in this file (e.g. the sum of all terpene species), then they should be added as

::

       sum : name_of_summation = species+species+species
       sum : name_of_second_summation = species+species+species

where the word ``sum`` is used by the model to parse this line as a summation.

.. _initial_concentrations.txt:

initial_concentrations.txt (optional)
-------------------------------------

The file setting the starting concentrations of species within the model when "initials_from_run" is used and is set to False. The name of this file must match the name given in settings.py for "initial_conditions_gas". This text file is a list of species and their concentrations in molecules cm\ :math:`^{-3}`. The format of the list is

::

       species = concentration ;
       species2 = concentration ;

If a species that exists in the model does not have a concentration given in this file, the default value of 0 will be applied.
