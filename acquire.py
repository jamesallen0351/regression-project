# acquire zillow data for regression-project

# imports

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

from env import host, user, password
from env import host, user, password # I already added my env to .gitignore first and then to my repository

# establishing get_connection function
def get_connection(db, user=user, host=host, password=password):

    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# getting zillow data for single unit properties from codeup database    
def new_zillow_data():
    sql_query = '''select * from properties_2017
    join predictions_2017 using(parcelid)
    where transactiondate between "2017-05-01" and "2017-08-31"
    and propertylandusetypeid in (260, 261, 262, 263, 264, 265, 273, 275, 279)'''
    
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df 



def get_zillow_data():
    if os.path.isfile('zillow.csv'):
        df = pd.read_csv('zillow.csv', index_col=0)
    
    else:
        df = new_zillow_data()
        df.to_csv('zillow.csv')
    
    return df


# cleaning up the zillow data to use for regression project, dropping columns and nulls and renaming remaining columns
def clean_zillow(df):
    
    # selecting features needed for zillow project
    features = ['parcelid', 'calculatedfinishedsquarefeet', 'bathroomcnt', 'bedroomcnt', 'taxvaluedollarcnt','yearbuilt','fips']
    df = df[features]

    
    # renaming my columns to make them easier to use and read
    df = df.rename(columns={
                            'parcelid': 'parcel_id',
                            'calculatedfinishedsquarefeet': 'sqft',
                            'bathroomcnt': 'baths',
                            'bedroomcnt': 'beds',
                            'taxvaluedollarcnt':'tax_value',
                            'yearbuilt':'year_built'
        
    })
    
    # setting my index
    df = df.set_index('parcel_id')
    
    # dropping all nulls 
    df = df.dropna(subset=['sqft','tax_value', 'year_built'])
    
    return df
    