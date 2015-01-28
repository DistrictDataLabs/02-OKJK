import sys
import os
import csv
# print sys.version
import pandas as pd

###############################################################################
# Now that there are data files in fixtures, get the info that we want.
###############################################################################



def load_data(dir = '../fixtures/', file_name = 'all_states.txt', sep = '\t'):
	"""
	Given a directory, file_name, and seperator, load them into
	a pandas dataframe.

	Returns: a pandas dataframe.
	"""

	data = pd.read_table(dir+file_name, sep = sep)
	return data


def get_state_codes(state_file = '../fixtures/s_r_division.txt'):
	"""
	Uses the s_r_division text from the BLS website to 
	creates a dictionary which maps state codes to states.

	Returns: a dictionary, keys of state codes and values of states
	"""

	mapper = dict()
	with open(state_file) as f:
		reader = csv.DictReader(f, delimiter = '\t')
		for row in reader:
			mapper[row['srd_code']] = row[None][0]

	return mapper

def get_recent_data(data):
	"""
	Finds the most recent data in the data and subsets
	it only to return the data which is most recent. 

	Returns: a pandas dataframe.
	"""
	most_recent_year = max(data['year'].values)
	recent_data = data[data['year'] == most_recent_year]

	try:
		#M13 is used to denote a yearly average and should not be used
		most_recent_month = max(recent_data['period'].values.remove('M13'))
	except ValueError as ve:
		most_recent_month = max(recent_data['period'].values)

	recent_data = recent_data[recent_data['period'] == most_recent_month]

	return recent_data
 



def export_recent_data(data):

	data.to_csv('../fixtures/output.csv', sep = '\t', encoding = 'utf-8')

def main():
	##Load the state data
	data = load_data()

	## Subset it to only the most recent data
	data = get_recent_data(data)


	##get the state codes
	print get_state_codes()



	##Export the data
	# export_recent_data(data)



if __name__ == '__main__':
	print os.path.realpath(__file__)

	main()