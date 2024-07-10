# In this script convert data 
# based on Angle, Time, Lat, Long

import csv
import json
from datetime import datetime, timedelta
import random

# Function to convert HH:MM:SS to total seconds
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

# Function to convert total seconds back to HH:MM:SS
def seconds_to_time(seconds):
    return str(timedelta(seconds=seconds))

# Starting time
start_time = "09:00:00"
current_seconds = time_to_seconds(start_time)

# Specify your CSV file name here
csv_file_name = 'Csv-data/demo.csv'

# Specify your output JSON file name here
json_file_name = 'demo2376674_left.json'

# Function to generate random latitude and longitude
def generate_random_lat_long():
    # Latitude: -90 to 90
    lat = round(random.uniform(-90, 90), 6)
    # Longitude: -180 to 180
    long = round(random.uniform(-180, 180), 6)
    return lat, long

# Read the CSV and add data to a dictionary
data = []
with open(csv_file_name, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        # New row with timestamp
        new_row = {'timestamp': seconds_to_time(current_seconds)}
        current_seconds += 1  # Increment time by one second

        # Convert and rename keys
        for k, v in rows.items():
            if k.strip():  # Check if k is not empty or whitespace
                new_key = k.lower().split()[-1]  # Taking the last word and making it lowercase
            else:
                new_key = k.lower()  # If k is empty or whitespace, use it as is
            
            try:
                new_row[new_key] = float(v) if '.' in v else int(v)
            except ValueError:
                new_row[new_key] = v
        
        # Add random lat and long
        lat, long = generate_random_lat_long()
        new_row['lat'] = lat
        new_row['long'] = long

        data.append(new_row)

# Write the data to a JSON file
with open(json_file_name, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data from '{csv_file_name}' has been successfully written to '{json_file_name}' in JSON format.")
