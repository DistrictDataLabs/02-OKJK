
###############################################################################
# Imports
###############################################################################



import requests



###############################################################################
# Global Configs
###############################################################################

base_url = 'http://api.census.gov/data/2010/sf1?key='
api_key  = '5a6a71e33855262413e837363928828d7c91f425'

# http://api.census.gov/data/2010/sf1?

try_me   = 'http://api.census.gov/data/2013/pep/stchar6?get=DATE,STNAME,POP&for=state:*&key={0}'.format(api_key)

validated = base_url+api_key+"&get="

census_keys = {
	"pop_sex_by_age" : "PCT012001"
}

def get_some_stuff(whatyouwant = "pop_sex_by_age"):
	start_here = base_url + api_key
	start_here += "&get={0}".format(census_keys[whatyouwant])


	example = 'http://api.census.gov/data/2013/pep/natstprc?get=DOM&for=state:02&DATE=6&key={0}'.format(api_key)
	r = requests.get(example)
	print start_here

	print r.json()
	# print r.status_code
# print validated


get_some_stuff()
