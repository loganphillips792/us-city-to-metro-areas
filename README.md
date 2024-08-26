# us-city-to-metro-areas

This script is used to map cities to Metropolitan Statastical Areas. This script will accept a name of a city and return whether or not it belongs in Metro Area

# Running

## Set up Virtual Env (optional) & Install Dependencies

1. ```python3 -m venv ~/Desktop/MetroAreas```
2. ```source ~/Desktop/MetroAreas/bin/activate``` - this line activates the virtual environment so your Python will use an packages that are installed in it
3. ```which pip``` to verify what is being used (Should point to the one from the virtual environment)
4. ```~/Desktop/MetroAreas/bin/python3 -m pip install --upgrade pip```
5. ```pip install -r requirements.txt```

# Reference Files

[Metropolitan and Micropolitan Statistical Areas of the United States and Puerto Rico](https://www2.census.gov/geo/maps/metroarea/us_wall/Mar2020/CBSA_WallMap_Mar2020.pdf)

[Delineation Files](https://www.census.gov/geographies/reference-files/time-series/demo/metro-micro/delineation-files.html)


# How it works