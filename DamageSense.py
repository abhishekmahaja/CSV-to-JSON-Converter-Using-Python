import csv
import json
from datetime import datetime, timedelta

# Function to convert HH:MM:SS to total seconds
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

# Function to convert total seconds back to HH:MM:SS
def seconds_to_time(seconds):
    return str(timedelta(seconds=seconds))

# Starting time
start_time = "17:00:00"
current_seconds = time_to_seconds(start_time)

# Specify your CSV file name here
csv_file_name = 'CSV data/Exapmle csv data.csv'

# Specify your output JSON file name here
json_file_name = 'Exapmle converted data.json'

# When enter the csv file path and json file name then run command 
# python.exe .\DamageSense.py 


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
            new_key = k.lower().split()[-1]  # Taking the last word and making it lowercase
            try:
                new_row[new_key] = float(v) if '.' in v else int(v)
            except ValueError:
                new_row[new_key] = v

        data.append(new_row)

# Write the data to a JSON file
with open(json_file_name, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data from '{csv_file_name}' has been successfully written to '{json_file_name}' in JSON format.")
