'''
Brian Leung
+
Leo Liu
'''
import csv, random

def random_job(jobdict):
	total = 0.0
	for key in jobdict:
		total += jobdict[key]
	print total*10

def make_dict(csv_in):
	csv_dict = {}
	with open(csv_in, 'rb') as csvfile:
		occreader = csv.reader(csvfile)
		#This part eliminates the "Job Class, Percentage"
		#It also makes the dictionary
		for row in occreader:
			try:	
				csv_dict[row[0]] = float(row[1])
			except:
				pass
	#This removes 'Total'
	del csv_dict['Total']
	return csv_dict

job_dict = make_dict('occupations.csv')
print(job_dict)
random_job(job_dict)
