import sys
import os
import csv
# print sys.version
import pandas as pd

###############################################################################
# Now that there are data files in fixtures, get the info that we want.
###############################################################################



def load_data(dir = '../fixtures/', file_name = 'ap_current.txt', sep = '\t'):
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
	data['item_code'] = data['series_id'].str[-6:]


	data['area_code'] = data['series_id'].str[3:7]


	return data


def get_item_codes(series_file = '../fixtures/ap_item.txt'):
	"""
	Loads in the item codes regarding AP data.

	Returns: a dictionary with values as series explanations
	and keys as the corresponding item code.
	"""

	mapper = dict()
	with open(series_file) as f:
		reader = csv.DictReader(f, delimiter = '\t')
		for row in reader:
			mapper[row['item_code']] = row['item_name']

	return mapper

def get_area_codes(state_file = '../fixtures/ap_area.txt'):
	"""
	Uses the s_r_division text from the BLS website to 
	creates a dictionary which maps state codes to states.

	Returns: a dictionary, keys of state codes and values of states
	"""

	mapper = dict()
	with open(state_file) as f:
		reader = csv.DictReader(f, delimiter = '\t')
		for row in reader:
			mapper[row['area_code']] = row['area_name']
	return mapper

def subset_data_recent(data):
	"""
	Finds the most recent data in the data and subsets
	it only to return the data which is most recent. 

	Returns: a pandas dataframe.
	"""
	
	
	most_recent_year = max(data['year'].values)

	### First, only get the most recent year
	recent_data = data[data['year'] == most_recent_year]

	## Next, get only the most recent month
	try:
		#M13 is used to denote a yearly average and should not be used
		most_recent_month = max(recent_data['period'].tolist())

	except:
		pass
	if most_recent_month == 'M13':
		most_recent_month = 'M12'


	recent_data = recent_data[recent_data['period'] == most_recent_month]

	return recent_data
 
 
 

def subset_data_item(data, item_codes, desired_item):
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
	
	# print data.head

	######## Passing in the measure dictionary that is generated
	######## from get_measure_codes() allows us to get the 
	######## descriptions of each of the measures.
	data['item_name'] = data['item_code'].map(item_codes)

	data = data[data['item_name']==desired_item]

	return data



def subset_data_area(data, area_codes):
	"""


	"""
	data['area_name'] = data['area_code'].map(area_codes)
	
	data = data[data['area_name'].isin(['Northeast Region', 'Midwest urban',
				'South urban', 'West urban'])]

	return data


def export_clean_data(data):

	data.to_csv('../fixtures/clean_ap.csv', sep = '\t', encoding = 'utf-8')
	
	
	
def get_region_mapper():
	"""
	"""
	region_mapper = dict()
	# print os.getcwd()
	with open('../source/Clean/RegionMapper.txt') as f:
		for row in f.read().split(','):
			region_mapper[row.split(":")[0].strip('\n')] = row.split(":")[1]
	
	return region_mapper
	
	
	
	
def create_exportable_data(region_mapper, df):
	"""
	"""
	
	data_2 = pd.DataFrame.from_dict(region_mapper, orient = 'index')
	data_2['region'] = 1
	data_2.columns = ['region', 'dummy']
	
	data_2['state'] = data_2.index
	data_3 = data_2.merge(df, how = 'left', left_on = 'region', right_on = 'area_name')
	
	
	data_4 = data_3[['state', 'value']]
	
	data_5 = data_4.set_index('state')
	
	return data_5
	
def main():

	##Load the state data
	data = load_data()
	
	print 'Initial Load'
	# print data.info()
	## Subset it to only the most recent data
	data = subset_data_recent(data)
	print 'After Date Subset'
	print data.info()
	
	#load in the 'keys' from bls website as dictionaries
	item_codes = get_item_codes()
	area_codes = get_area_codes()
	region_mapper = get_region_mapper()

	data = subset_data_item(data, item_codes, 'Grapefruit, per lb. (453.6 gm)')
	print 'After Item Subset'
	print data.info()
	# data = subset_data_area(data, area_codes "Malt beverages, all types, all sizes, any origin, per 16 oz. (473.2 ml)")
	
	data = subset_data_area(data, area_codes)
	print 'After Area Subset'
	print data.info()
	
	data = create_exportable_data(region_mapper, data)

	#Export the data
	export_clean_data(data)



if __name__ == '__main__':

	main()