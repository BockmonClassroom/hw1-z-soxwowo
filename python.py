# Jitong Zou
# January 9th, 2025

import csv

# Open the CSV file
with open('data/Iris.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Loop through each row in the CSV
    for row in reader:
        print(row)
