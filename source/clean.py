import sys
import os
# print sys.version
import pandas as pd

###############################################################################
# Now that there are data files in fixtures, get the info that we want.
###############################################################################



def load_data(dir = '../fixtures/'):

	data = pd.read_table(dir+'all_states.txt', sep = '\t')

	return data



def get_recent_data(data):

	recent_data = data[data['year']=='2014']
	recent_data = recent_data[recent_data['period'] == 'M11']

	return recent_data

def main():
	data = load_data()
	print get_recent_data(data)
	# print load_data().info()



if __name__ == '__main__':
	print os.path.realpath(__file__)

	main()