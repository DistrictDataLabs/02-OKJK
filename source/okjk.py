
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

################################################################################
# Function Definitions
################################################################################


def get_all_data():
	"""
	Just a wrapper to run all the necessary bins
	"""


def find_clean_data():
	"""
	Gets a list of all the clean 
	data sets that are ready to go
	"""

	#### TODO: get this away from relative paths.
	os.chdir('../fixtures')


	load_me = list()

	for file in os.listdir(os.getcwd()):
		if file.startswith('clean'):
			load_me.append(file)
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

	for file in file_list:
		with open(file, 'rb') as f:

			text   = f.read()

			delims = dict()
			delims[','] = text.count(",")
			delims['\t']   = text.count("\t")
			delims[';']   = text.count(";")

			most_delim = 0
			for delim in delims.keys():
				if delims[delim] >= most_delim:
					most_delim = delims[delim]
					delim_of_choice = delim

		file_delims[file] = delim_of_choice

	return file_delims


def combine_data(loaded_files):
	"""
	make a single data frame from all of the cleaned data.

	"""

	#### Start with clean_laubs as a baseline, because
	#### I know exactly how it is structured

	df = loaded_files['clean_laubs.csv']

	for each_key in loaded_files.keys():
		if each_key == 'clean_laubs.csv':
			pass
		else:
			try:
				df = pd.merge(left = df, right = loaded_files[each_key],
					left_on = 'state_name', right_on = 'state')
				print 'hello'
			except:
				print 'broke'
	
	print df.info()
	return df


def combine_data(loaded):
	"""

	"""

	# First, load in clean_laubs as a baseline
	df = loaded['clean_laubs.csv']

	# Then join em all!
	for f in loaded.keys():
		if f == 'clean_laubs.csv':
			pass
		else:
			try:
				df = pd.merge(left = df, right = f, 
				left_on = 'state_name', right_on ='state',
				how = 'left')

			except TypeError as te:

	return df
		
def load_clean_data(files_and_delims):
	"""
	takes a list of files and their delimiters
	and loads them all into memory
	"""

	loaded_files = dict()

	for file in files_and_delims.keys():
		loaded_files[file] = pd.DataFrame.from_csv(file, sep = files_and_delims[file])


	return loaded_files

################################################################################
# Main Execution
################################################################################
def main():

	clean_data = find_clean_data()
	delims = guess_delims(clean_data)
	loaded = load_clean_data(delims)
	combine_data(loaded)

if __name__ == '__main__':
	main()