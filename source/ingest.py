#! usr/bin/env python


import requests
import os
import csv

###############################################################################
# This module gets all of the data from urls listed in urls.txt
# and exports them as txt files in the /fixtures dir.
#
# Some of this isn't data--it's supporting documentation that
# explains what the data is, etc. Load them judiciously! 
###############################################################################




def get_urls(url_file = './urls.txt'):
	"""
	Right now, simply returns a dictionary of predefined
	urls. Later, might load from a seperate resource

	Returns: dictionary of {"description" : "url"} pairs
	"""

	urls = dict()

	with open(url_file, 'rb') as f:
		for each_item in f.read().split(','):
			key   = each_item.split(' : ')[0].strip()
			value = each_item.split(' : ')[1].strip()
			urls[key] = value

	return urls


def get_data(urls, export_dir = os.path.realpath(__file__)):
	"""
	Given a dictionary where the values are urls,
	gets the resource listed at each url and dumps it 
	into a directory of the user's chosing.
	"""
	
	for url in urls.keys():
		r = requests.get(urls[url])
		try:
			r.raise_for_status()
		except requests.exceptions.HTTPError as e:
			print url, "failed", e

		print 'writing to {0}.txt'.format(url)
		with open(export_dir+"{0}.txt".format(url), 'wb') as f:
			f.write(r.text)

def main():
	urls = get_urls()
	get_data(urls, export_dir = '../fixtures/')


if __name__ == '__main__':
	main()
