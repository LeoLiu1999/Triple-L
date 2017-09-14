import csv

with open('occupations.csv', 'rb') as csvfile:
	occreader = csv.reader(csvfile)
	for row in occreader:
		print row