# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:16:33 2021

@author: Satish Narasimhan
"""

import csv
import json


# Function to convert a CSV file at a filepath to JSON
def csv_json(csvFile, jsonFile):
	
	# Instantiate a dictionary
	data = {}
	
	# Open the csv reader - DictReader in csv package
	with open(csvFile, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Each row into the dictionary
		for rows in csvReader:
			
			# Column 'Id' is the primary key
			key = rows['Id']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFile, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
        
# Provide the file path
sourcePath = '<<>>' 
csvFileName = 'csvOutliers.csv'
csvFile = (sourcePath+csvFileName) 


jsonFileName = 'jsonOutliers.json'
jsonFile = (sourcePath+jsonFileName)
# Call the make_json function
csv_json(csvFile, jsonFile)

# Read JSON data from file and pretty print it
with open(jsonFile, "r") as read_file:
    # Convert JSON file to Python Types
    obj = json.load(read_file)

    pretty_json = json.dumps(obj, indent=4)
    print(pretty_json)


