# In this script convert data 
# based on Angle, Time, Lat, Long

import csv
import json

# Specify your CSV file name here
csv_file_name = 'CSV data/demo.csv'

# Specify your output JSON file name here
json_file_name = 'demo2376674_left.json'

# Read the CSV and add data to a dictionary
data = []
with open(csv_file_name, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for rows in csv_reader:
        # New row without timestamp
        new_row = {}
        
        # Convert and rename keys
        for k, v in rows.items():
            if k.strip():  # Check if k is not empty or whitespace
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