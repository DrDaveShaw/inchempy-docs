INCHEM-Py overview
==================

The INdoor CHEMical model in Python (INCHEM-Py) is an open source box model that creates and solves a system of coupled Ordinary Differential Equations (ODEs) to provide predicted concentrations of indoor air pollutants through time. It is a refactor of the indoor detailed chemical model, developed by Carslaw (Nicola Carslaw 2007), with improvements in form, function, and accessibility.

INCHEM-Py uses the Master Chemical Mechanism (MCM) (Michael E. Jenkin, Saunders, and Pilling 1997; Saunders et al. 2003; Bloss et al. 2005; M. E. Jenkin et al. 2012; M. E. Jenkin, Young, and Rickard 2015), a near explicit mechanism developed for atmospheric chemistry, with additional chemical mechanisms developed specifically for indoor air. These include gas-to-particle partitioning for three of the commonly encountered terpenes indoors (limonene and alpha- and beta-pinene), improved photolysis parameterisation, indoor-outdoor air change, and deposition to surfaces.

Typical usage of INCHEM-Py is either alongside experiment, where it can be used to gain a deeper insight into the chemistry through its ability to track a vast array of species concentrations; or as a standalone method of investigating chemical events that occur indoors over a range of conditions. INCHEM-Py is open source, has no black box processes, and all inputs can be tracked through the model allowing for complete understanding of the system.

A wide array of outputs from the model can be accessed, including species concentrations, species reactivity and production rates, photolysis values, rate coefficients and summations such as the total peroxy radical concentration. Custom reactions and summations can also be added by users to tailor the model to specific indoor scenarios.

INCHEM-Py will continue to be developed into the future and new versions will be publicly released alongside peer reviewed literature.
