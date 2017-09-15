'''
Brian Leung
+
Leo Liu
'''
import csv, random

def random_job():

def make_dict(csv_in):
	csv_dict = {}	
	with open(csv_in, 'rb') as csvfile:
		occreader = csv.reader(csvfile)
		for row in occreader:
			if (row[0] == 'Job Class') or (row[0] == 'Total'):
				continue
			csv_dict[row[0]] = float(row[1])
	return csv_dict

job_dict = make_dict('occupations.csv')
print(job_dict)
