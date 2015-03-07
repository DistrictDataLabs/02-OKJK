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

	Also, creates state_code and measure_code columns built from the
	original 'series_id' code.

	Returns: a pandas dataframe.
	"""


	data = pd.read_table(dir+file_name, sep = sep)

	######## From the series id, we can grab a few more features
	######## out of the data
	#### There's a lot of whitespace in series_id, so we strip it
	data['series_id'] = data['series_id'].str.strip()

	#### The last two digits of series id refer to particular measure
	#### We seperate this for conveneiences sake.
	data['measure_code'] = data['series_id'].str[-2:]


	data['state_code'] = data['series_id'].str[5:7]


	return data


def get_measure_codes(series_file = '../fixtures/measure.txt'):
	"""
	Loads in the series codes regarding LAUS data.

	Returns: a dictionary with values as series explanations
	and keys as the corresponding laus code.
	"""

	mapper = dict()
	with open(series_file) as f:
		reader = csv.DictReader(f, delimiter = '\t')
		for row in reader:
			mapper[row['measure_code']] = row['measure_text']

	return mapper

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

def subset_data_recent(data):
	"""
	Finds the most recent data in the data and subsets
	it only to return the data which is most recent. 

	Returns: a pandas dataframe.
	"""
	most_recent_year = max(data['year'].values)

	######## First, only get the most recent year
	recent_data = data[data['year'] == most_recent_year]

	print set(recent_data['period'].tolist()).remove('M13')
	######## Next, get only the most recent month
	try:
		#M13 is used to denote a yearly average and should not be used
		most_recent_month = max(recent_data['period'].tolist().discard('M13'))

	except ValueError as ve:
		most_recent_month = max(recent_data['period'].values)

	recent_data = recent_data[recent_data['period'] == most_recent_month]

	return recent_data
 

def subset_data_measure(data, measure_codes, desired_measure):
	"""
	Given the all_states data format from the BLS and a dictionary
	which maps measures to normal english-language names, 
	returns only the requested normal english-language name. 
	only return the data series that is the unemployment rate

	data            : a pandas dataframe to be subsetted
	measure_codes:  : a dictionary structured like {measure_code : measure_name}
	desired_measure : a list of english-language measures you want

	Returns: a pandas dataframe.
 
	"""

	######## Passing in the measure dictionary that is generated
	######## from get_measure_codes() allows us to get the 
	######## descriptions of each of the measures.
	data['measure_name'] = data['measure_code'].map(measure_codes)

	data = data[data['measure_name']==desired_measure]

	return data



def subset_data_state(data, state_codes):
	"""


	"""
	data['state_name'] = data['state_code'].map(state_codes)

	return data


def export_clean_data(data):

	data.to_csv('../fixtures/clean_laubs.csv', sep = '\t', encoding = 'utf-8')

def main():


	##Load the state data
	data = load_data()
	
	print 'Initial Load:'
	print data.info()

	## Subset it to only the most recent data
	data = subset_data_recent(data)

	print 'After Date Subset:'
	print data.info()

	#load in the 'keys' from bls website as dictionaries
	measure_codes = get_measure_codes()
	state_codes = get_state_codes()

	data = subset_data_measure(data, measure_codes, 'unemployment rate')
	data = subset_data_state(data, state_codes)
	print 'After Measures Subset:'
	print data.info()


	#Export the data
	export_clean_data(data)



if __name__ == '__main__':
	print os.path.realpath(__file__)

	main()