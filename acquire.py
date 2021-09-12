# acquire zillow data for regression-project

# imports

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

from env import host, user, password # I already added my env to .gitignore first and then to my repository

# establishing get_connection function
def get_connection(db, user=user, host=host, password=password):

    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


    
def new_zillow_data():
    sql_query = '''select * from properties_2017
    join predictions_2017 using(parcelid)
    where transactiondate between "2017-05-01" and "2017-08-31"
    and propertylandusetypeid in (260, 261, 262, 263, 264, 265, 266, 273, 275, 276, 279)'''
    
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df 



def get_zillow_data():
    if os.path.isfile('zillow.csv'):
        df = pd.read_csv('zillow.csv', index_col=0)
    
    else:
        df = new_zillow_data()
        df.to_csv('zillow.csv')
    
    return df
    
    
    
    
def clean_zillow(df):
    #select features for df, took these features from my acquire exercise
    features = ['parcelid', 'calculatedfinishedsquarefeet', 'bathroomcnt', 'bedroomcnt', 'taxvaluedollarcnt','yearbuilt','taxamount','fips']
    df = df[features]

    #rename columns for easier use
    df = df.rename(columns={
                            'parcelid': 'parcel_id',
                            'calculatedfinishedsquarefeet': 'sqft',
                            'bathroomcnt': 'baths',
                            'bedroomcnt': 'beds',
                            'taxvaluedollarcnt':'tax_value',
                            'yearbuilt':'year_built',
                            'taxamount': 'tax_amount'
        
    })
    
    #set index
    df = df.set_index('parcel_id')
    #drop nulls
    df = df.dropna(subset=['sqft','tax_value'])
    
    return df