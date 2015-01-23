import sys
import os
import csv
# print sys.version
import pandas as pd

###############################################################################
# Now that there are data files in fixtures, get the info that we want.
###############################################################################



def load_data(dir = '../fixtures/', file_name = 'all_states.txt'):
	data = pd.read_table(dir+file_name, sep = '\t')
	return data

def get_state_codes(state_file = '../fixtures/s_r_division.txt'):
	mapper = dict()
	with open(state_file) as f:
		reader = csv.DictReader(f, delimiter = '\t')
		for row in reader:
			mapper[row['srd_code']] = row[None][0]

	return mapper

def get_recent_data(data):

	recent_data = data[data['year'] == 2014]
	recent_data = recent_data[recent_data['period'] == 'M11']
	return recent_data


def export_recent_data(data):

	data.to_csv('../fixtures/output.csv')

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