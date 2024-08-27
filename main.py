import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import string
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import sys
import os
import json
import pprint
from generate_map import generate as generate_map
from generate_csv import generate as generate_csv

def load_metro_areas(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'r') as f:
        return json.load(f)

def get_coordinates(city, state):
    geolocator = Nominatim(user_agent="closest_metro_finder")
    location = geolocator.geocode(f"{city}, {state}, USA", timeout=None)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def find_closest_metro(coordinates, metro_areas):
    closest_metro = min(metro_areas.items(), key=lambda x: geodesic(coordinates, x[1]).miles)
    return closest_metro[0], geodesic(coordinates, closest_metro[1]).miles

def process_csv_file():
    data = pd.read_csv('cities.csv')
    metro_areas = load_metro_areas('metro-areas.json')
    final_city_count = {}

    df = pd.DataFrame(data, columns=['ip_location', 'is_confirmed', 'created_at', 'unsubscribed'])

    new_data = []
    for index, row in df.iterrows():
        st1 = row['ip_location']
        new_data.append(st1)

    for city_and_state in new_data:
        # split the string by comma and then take the first 2 elements
        city = city_and_state.split(',')[0].strip()
        state = city_and_state.split(',')[1].strip()

        coordinates = get_coordinates(city, state)
        if coordinates:
            closest_metro, distance = find_closest_metro(coordinates, metro_areas)
            # print(f"The closest metro area to {city},{state} is {closest_metro}, approximately {distance:.2f} miles away.")
            if distance > 250.00:
                print(f"The closest metro area to {city},{state} is {closest_metro}, approximately {distance:.2f} miles away.")
            if closest_metro in final_city_count:
                final_city_count[closest_metro] += 1
            else:
                final_city_count[closest_metro] = 1
        else:
            print(f"Could not find coordinates for {city},{state}. Please check the input and try again.")
    return final_city_count
    

# only generate the csv file if it does not exists
if not os.path.isfile('./user_metro_counts.csv'):
    final_city_count_map = process_csv_file()
    pprint.pp(dict(sorted(final_city_count_map.items(), key=lambda item: item[1], reverse=True)))
    generate_csv(final_city_count_map)
generate_map()