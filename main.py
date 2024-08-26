import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_msa_name(city, state):
    # Step 1: Get the Wikipedia page
    url = f"https://en.wikipedia.org/wiki/{city},_{state}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 2: Find the FIPS code
    fips_code = None
    for table in soup.find_all('table', class_='infobox'):
        for row in table.find_all('tr'):
            if 'FIPS code' in row.text:
                fips_code = row.find('td').text.strip()
                break
        if fips_code:
            break

    if not fips_code:
        return "FIPS code not found"

    # Extract the first two digits of the FIPS code
    fips_prefix = fips_code[:2]

    # Step 3: Search the CSV file
    df = pd.read_csv('msa_geography_reference.csv')  # Replace with your actual CSV file name
    
    # Convert state_fips to string and ensure it has leading zeros
    df['state_fips'] = df['state_fips'].astype(str).str.zfill(2)

    # Find matching rows
    matching_rows = df[df['state_fips'] == fips_prefix]

    if matching_rows.empty:
        return "No matching MSA found"

    # Return the first matching MSA name
    return matching_rows.iloc[0]['msa_name']

# Example usage
# city = "Chicago"
# state = "IL"
city = "Oshkosh"
state = "WI"
msa_name = get_msa_name(city, state)
print(f"The MSA for {city}, {state} is: {msa_name}")