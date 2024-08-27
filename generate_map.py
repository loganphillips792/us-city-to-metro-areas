import pandas as pd
from geopy.geocoders import Nominatim
import folium

def generate():
    # Load the data
    data = pd.read_csv('user_metro_counts.csv')

    # Initialize the geocoder
    geolocator = Nominatim(user_agent="us-city-to-metro-areas")

    # Geocode function
    def geocode_city(city):
        location = geolocator.geocode(city, timeout=None)
        return (location.latitude, location.longitude) if location else (None, None)

    # Apply geocoding
    data['Coordinates'] = data['City'].apply(geocode_city)

    # Initialize the map
    m = folium.Map(location=[data['Coordinates'].iloc[0][0], data['Coordinates'].iloc[0][1]], zoom_start=5)

    # Add markers
    for index, row in data.iterrows():
        folium.Marker(location=row['Coordinates'], popup=row['Value']).add_to(m)

    # Save map to HTML
    m.save('users_map.html')
