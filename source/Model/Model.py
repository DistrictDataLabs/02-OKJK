
###############################################################################
# This does the stuff you need to do.
#
#
#
#
#
###############################################################################

################################################################################
# Imports
################################################################################

import pandas as pd
import os
from os import path
import numpy as np

################################################################################
# Function Definitions
################################################################################


def find_clean_data(dir = '../fixtures'):
	"""
	Gets a list of all the clean 
	data sets that are ready to go
	"""


	fix_path = path.abspath(dir)


	load_me = list()

	for f in os.listdir(fix_path):
		ff = path.join(fix_path, f)

		if f.startswith('clean_'):
			load_me.append(ff)
	return load_me


def guess_delims(file_list):
	"""
	given a list of files, returns
	the likely delimiter of that file.

	file_list: a list of files to be loaded

	Returns: a dictionary. keys are the names
	of the file, and values are the guessed
	delimiter
	"""
	
	file_delims = dict()

	for f in file_list:
		with open(f, 'rb') as ff:

			text   = ff.read()

			delims = dict()

			delims[',']    = text.count(",")
			delims['\t']   = text.count("\t")
			delims[';']    = text.count(";")

			most_delim = 0
			for delim in delims.keys():
				if delims[delim] >= most_delim:
					most_delim = delims[delim]
					delim_of_choice = delim

		file_delims[f] = delim_of_choice

	return file_delims


def combine_data(loaded_files):
	"""
	make a single data frame from all of the cleaned data.

	loaded_files : a dictionary of file names and 
	loaded pandas dataframes

	returns: a single pandas dataframe with the state
	as the index and columns for each measure.
	"""

	#### Start with clean_laubs as a baseline, because
	#### I know exactly how it is structured
	for key in loaded_files.keys():
		short_key = path.basename(key)
		if short_key == 'clean_laubs.csv':
			df = loaded_files[key]


	#### We set the final "df" as clean_laubs
	#### and then change the index to be state-based

	df = df.set_index('state_name')
	for col in df.columns:
		if col != "value":
			df = df.drop(col, 1)

	#### Rename the initial 'value' column
	df = df.rename(columns = {'value': 'laubs'})
	

	#### Now merge all of them. It's a bit idiosynchratic,
	#### so we handle each one on its own
	for key in loaded_files.keys():
		short_key = path.basename(key)

		if short_key == 'clean_laubs.csv':
			pass

		elif short_key == 'clean_age.csv':
			df['age'] = loaded_files[key]['value']

	return df

		
def load_clean_data(files_and_delims):
	"""
	takes a list of files and their delimiters
	and loads them all into memory
	"""

	loaded_files = dict()

	for f in files_and_delims.keys():
		loaded_files[f] = pd.DataFrame.from_csv(f, sep = files_and_delims[f])


	return loaded_files


def export_data(df, export_dir = '../fixtures'):

	first_path = path.abspath(export_dir)

	file_name = 'final_data.tsv'

	full_path = path.join(first_path, file_name)

	print full_path
	# export_
	df.to_csv(full_path, encoding = 'utf-8', sep = '\t')


def normalize_data(df):
	"""
	given a df, normalize each column 
	to be scaled between 1 and 0.
	
	df : the dataframe to be normalized

	returns : a pandas dataframe with column 
	values between 0 and 1
	"""



	df = df.convert_objects(convert_numeric = True)
	df = df/df.max().astype(np.float64)

	df = 1-df

	return df

def fill_missing_values(df):
	"""
	given a df, replaces missing values with the average of 
	the dataset
	
	df : the dataframe to have missing values interpolated
	
	returns: a dataframe with interpolated values
	"""

	df = df.fillna(df.mean())

	return df

################################################################################
# Main Execution
################################################################################
def main():

	clean_data = find_clean_data()
	delims = guess_delims(clean_data)
	loaded = load_clean_data(delims)
	final_data = combine_data(loaded)
	final_data = normalize_data(final_data)
	final_data = fill_missing_values(final_data)
	export_data(final_data)

if __name__ == '__main__':
	main()