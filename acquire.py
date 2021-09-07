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
    '''
    This function gets my info from my env file and creats a connection url 
    
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

