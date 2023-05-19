# Weather Forecasting

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
![Dependencies
](https://img.shields.io/badge/dependencies-none-brightgreen.svg?style=flat)

In this project, we'll predict tomorrow's temperature and weather using python and historical data. We'll start by downloading a dataset of local weather by BMKG.

Then, we'll clean the data and get it ready for machine learning. We'll build a system to make historical predictions, and add more predictors to improve the model.  We'll end with how to make next-day predictions.


Weather related information is one of the things that is very important and has a big influence on all kinds of life
activities such as in public safety, socio-economics, agriculture, aviation, and especially when stargazing activity.

## Installation

Requires a recent version of python (either 2 or 3 should work).

The following should work on any unix-ish environment:
```sh
wget https://raw.githubusercontent.com/ .. soon
python file.py -h
```


## Details

This repository contains datasets which mining from 
DATA ONLINE Application - DATABASE CENTER - BMKG is a data service application for users, 
both for internal BMKG circles and external groups consisting of Universities, Institutions of 
Ministries/Agencies, Private and Community MKKuG data users.
[source](https://dataonline.bmkg.go.id/home)

One of the most important factors in model development is weather and climate parameters in a waters. 
Weather and climate greatly affect the pattern of water circulation and the process of transferring heat from the air to the sea surface. 
Therefore, measurement of weather field data is needed to find out the characteristics of the weather in certain waters. 
Weather data that has been collected over a long period of time will provide information on climate conditions in these waters and produce climatological data. 
These weather and climate data are needed as boundary conditions in modeling where current generating forces and energy transfer between the air and the water surface are important.

### Features

Acquisition of weather and climate field measurement data using equipment with an integrated system. All sensors used are installed in a series of tools and recorded automatically. The data recording time interval can be set and the process of averaging or summing can be done for a certain time unit.

The weather forecast models the following features as parameters:
  * Wind
  * Air Temperature
  * Rainfall or Precipitation
  * Air Humidity
  * Sun Intensity

There are several limitations:
  1) this project happen to find out more about forecasting and how it can be used to help astronomers and stargazers plan when to get the best views of the night sky.
  2) There's using BMKG data that provide weather time-series periode that happen in one-hour increments.

### Parameters

Included parameters:
  * Required:

| Name                  | Short | Long                    | Description                                | Default |
|-----------------------|-------|-------------------------|--------------------------------------------|---------|
| Latitude              | -la   | --latitude              | -90 to 90; plus for north, minus for south | N/A     |
| Longitude             | -lo   | --longitude             | -180 to 180; plus for east, minus for west | N/A     |
| Day                   | -da   | --day_of_year           | Julian day of year; 1 to 365               | N/A     |
| Surface temperature   | -st   | --surface_temp          | Initial surface air temperature (F or C)   | N/A     |
| Ground temperature    | -gt   | --ground_temp           | Ground reservoir temperature (F or C)      | N/A     |
| Percent net radiation | -pr   | --percent_net_radiation | Percent net radiation (0 to 1)             | N/A     |
| Degrees               | -de   | --degrees               | Temperatures in Celsius or Fahrenheit      | N/A     |

  * Optional:

| Name                    | Short | Long               | Description                                                     | Default |
|-------------------------|-------|--------------------|-----------------------------------------------------------------|---------|
| Hour                    | -ho   | --hour             | Initial hour of day; 0 to 24                                    | 12      |
| Minute                  | -mi   | --minute           | Initial minute of hour; 0 to 59                                 | 59      |
| Albedo                  | -al   | --albedo           | Albedo; 0 to 1                                                  | 0.3     |
| Cloud fraction          | -cf   | --cloud_fraction   | Cloud fraction; 0 to 1                                          | 0       |
| Solstice                | -ds   | --day_of_solstice  | Day of solstice; 172 or 173                                     | 173     |
| UTC offset              | -uo   | --utc_offset       | UTC offset in hours; -12 to 12                                  | 0       |
| Forecast minutes        | -fm   | --forecast_minutes | Forecast minutes ahead; 1 to 1440 (24 * 60)                     | 60      |
| Report period           | -rp   | --report_period    | Report period in minutes (including write to CSV file); 1 to 60 | 60      |
| Transmissivity          | -tr   | --transmissivity   | Atmospheric transmissivity; greater than 0                      | 0.8     |
| Emissivity              | -em   | --emissivity       | Surface emissivity; 0.9 to 0.99                                 | 0.95    |
| Bowen ratio             | -br   | --bowen_ratio      | Bowen ratio; -10 to 10                                          | 0.9     |
| Precipitable water      | -pw   | --precip_water     | Precipitable water in cm; greater than 0                        | 1.0     |
| Resistance to heat flux | -rh   | --resistance       | EXPERIMENTAL Resistance to heat flux (m s^-1)                   | 0       |
| File name               | -fn   | --filename         | File name for comma separated value output                      | N/A     |
| Help                    | -h    | --help             | Show this help message and exit                                 | N/A     |
| Verbose                 | -v    | --verbose          | Print additional information                                    | N/A     |

  * Mutually exclusive option group 1 parameters:
    * Choose --cloud_temp_constant or --cloud_temp_adjust but not both

| Name                         | Short | Long                  | Description                                                  | Default             |
|------------------------------|-------|-----------------------|--------------------------------------------------------------|---------------------|
| Cloud temperature constant   | -ct   | --cloud_temp_constant | Temperature of the base of the cloud constant                | Surface temperature |
| Cloud temperature adjustment | -tc   | --cloud_temp_adjust   | EXPERIMENTAL Temperature of the base of the cloud adjustment | 0                   |


The notebooks directory contains the
[plot_temperature_and_fluxes.ipynb](https://github.com/makeyourownmaker/ParametricWeatherModel/blob/master/notebooks/plot_temperature_and_fluxes.ipynb)
notebook which will plot the data.csv file.
In addition to [Jupyter](https://jupyter.org/) it requires the following packages to run locally:
  * [pandas](https://pandas.pydata.org/)
  * [matplotlib](https://matplotlib.org/)

Alternatively, check notebook(s) remotely:
  * [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/makeyourownmaker/ParametricWeatherModel/blob/master/notebooks/plot_temperature_and_fluxes.ipynb) - editable
  * [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://mybinder.org/v2/gh/makeyourownmaker/ParametricWeatherModel/master?filepath=notebooks%2Fplot_temperature_and_fluxes.ipynb) - editable
  * View on [NBViewer](https://nbviewer.jupyter.org/github/makeyourownmaker/ParametricWeatherModel/blob/master/notebooks/plot_temperature_and_fluxes.ipynb)
  * View on [GitHub](https://github.com/makeyourownmaker/ParametricWeatherModel/blob/master/notebooks/plot_temperature_and_fluxes.ipynb)

## Contributing

Pull requests are welcome.  For major changes, please open an issue first to discuss what you would like to change.
