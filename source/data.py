import random
import pandas as pd
import os

################################################################################
#
# Just hosts the final data set so that app.py 
# can load it and route it as json to an endpoint
#
################################################################################


df_states = pd.DataFrame.from_csv('fixtures/final_data.tsv', sep='\t', header = 0)
