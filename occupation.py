'''
Brian Leung
+
Leo Liu
'''
import csv, random

def random_job(jobdict):
    '''
    Select a random job based on the provided percentages.

    Select a random job based on percentage in jobdict by calculating total employment rate, generate random number within the range [0,employment rate). Go through all occupations, subtracting the percentage of each from the previously generated random number, until that number is less than the percentage. That job is selected.

    Arg:
    jobdict(dictonary) contains job sectors as keys, and their respective percentages as values.

    Ret:
    str the selected job
    '''
    total = 0.0
    for key in jobdict:
        total += jobdict[key]
    print total * 10
    
    random_counter = random.random() * total
    for key in jobdict:
        job_percentage = jobdict[key]
        if (random_counter <= job_percentage):
            return key
        else:
            random_counter -= job_percentage

def make_dict_from_csv(csv_in):
	'''
	Read in csv and generate a dictionary from it.

	Arg:
	csv_in(filename) : File to be read

	Ret:
	dictionary : Contains job class and percentage.
	'''
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


job_dict = make_dict_from_csv('occupations.csv')
print(job_dict)
print(random_job(job_dict))
