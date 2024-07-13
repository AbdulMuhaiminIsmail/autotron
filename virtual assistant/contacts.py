import csv

# Path to the CSV file
file_path = "assets/contacts.csv"

# Dictionary to store the data
contacts = {}

# Open the CSV file
with open(file_path, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read each row in the CSV file and store it in the dictionary
    for row in csv_reader:
        key = row[0].lower()
        value = row[1]
        contacts[key] = value


