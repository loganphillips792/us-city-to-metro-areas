import csv

csv_file_path = "user_metro_counts.csv"

def generate(city_data):
    # Writing to the CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Value"])
        
        for city, value in city_data.items():
            writer.writerow([city, value])
    print(f"CSV file '{csv_file_path}' created successfully.")