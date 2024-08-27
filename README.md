# us-city-to-metro-areas

This script is used to map cities to Metropolitan Statastical Areas (kinda). This script will accept a name of a city and return whether or not it belongs in Metro Area.

I couldn't find a direct correlation between an location and the MSA that it was in. Instead I hardcoded the coordinates for major cities and tried to get it as close to the offical MSAs as possible

It takes a location name, and then finds the closest major city to it. Right now, the goal is to get all locations to be less than 250 miles away from a major city.

# Running

## Set up Virtual Env (optional) & Install Dependencies

1. ```python3 -m venv ~/Desktop/MetroAreas```
2. ```source ~/Desktop/MetroAreas/bin/activate``` - this line activates the virtual environment so your Python will use an packages that are installed in it
3. ```which pip``` to verify what is being used (Should point to the one from the virtual environment)
4. ```~/Desktop/MetroAreas/bin/python3 -m pip install --upgrade pip```
5. ```pip install -r requirements.txt```
6. Add the CSV and name it `cities.csv`
7. `python main.py`

# Reference Files

- [Metropolitan and Micropolitan Statistical Areas of the United States and Puerto Rico](https://www2.census.gov/geo/maps/metroarea/us_wall/Mar2020/CBSA_WallMap_Mar2020.pdf)
- [Delineation Files](https://www.census.gov/geographies/reference-files/time-series/demo/metro-micro/delineation-files.html)
- [MSA County Reference](https://www2.census.gov/programs-surveys/cbp/technical-documentation/reference/metro-area-geography-reference/msa_county_reference22.txt)



