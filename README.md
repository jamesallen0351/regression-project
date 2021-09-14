# Regression Project: Estimating Home Value

# Zillow Data Science Team

## Executive Summary

- Single Unit Properties: Linear Regression model to predict property values using 2017 data

- Baseline: $363,349
- Prediction: $269,196

### Counties and Tax %:
- Los Angeles: 1.38 %
- Orange: 1.20 %
- Ventura: 1.19%

## Project Overview

- This project will be working with the Zillow data and create a model to predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.

- We would like to know what states and counties these are located in. We'd also like to know the distribution of tax rates for each county.

## Business Goals

- Predict the value of single unit properties duirng May - August, 2017
- Identify states and counties of the properties and the distribution of tax rates
- Presentation about findings to Zillow Data Science Team 

## Deliverables

1. A report in the form of a presentation, verbal supported by slides.

    - The report/presentation slides should summarize your findings about the drivers of the single unit property values. This will come from the analysis you do during the exploration phase of the pipeline. In the report, you should have visualizations that support your main points.

    - The presentation should be no longer than 5 minutes.

2.  A github repository containing your work. 'regression-project'

    - This repository should contain one clearly labeled final Jupyter Notebook that walks through the pipeline, but, if you wish, you may split your work among 2 notebooks, one for exploration and one for modeling. In exploration, you should perform your analysis including the use of at least two statistical tests along with visualizations documenting hypotheses and takeaways. In modeling, you should establish a baseline that you attempt to beat with various algorithms and/or hyperparameters. Evaluate your model by computing the metrics and comparing.

    - Make sure your notebook answers all the questions posed in the email from the Zillow data science team.

    - The repository should also contain the .py files necessary to reproduce your work, and your work must be reproducible by someone with their own env.py file.

## Data Dictionary

| Column Name                  | Renamed   | Info                                            |
|------------------------------|-----------|-------------------------------------------------|
| parcelid                     | N/A       | ID of the property (unique)                     |
| bathroomcnt                  | baths     | number of bathrooms                             |
| bedroomcnt                   | beds      | number of bedrooms                              |
| calculatedfinishedsquarefeet | sqft      | number of square feet                           |
| fips                         | N/A       | FIPS code (for county)                          |
| propertylandusetypeid        | N/A       | Type of property                                |
| yearbuilt                    | N/A       | The year the property was built                 |
| taxvaluedollarcnt            | tax_value | Property's tax value in dollars                 |
| taxamount                    | tax_amount| amount of tax on property                       |
| tax_rate                     | N/A       | tax_rate on property                            |


## Data Science Pipeline

- Project Planning
    - Goal: leave this section with (at least the outline of) a plan for the project documented in your README.md file.

- Acquire
    - Goal: leave this section with a dataframe ready to prepare.
    - Create an acquire.py file the reproducible component for gathering data from a database using SQL and reading it into a pandas DataFrame.

- Prepare
    - Goal: leave this section with a dataset that is split into train, validate, and test ready to be analyzed. Make sure data types are appropriate and missing values have been addressed, as have any data integrity issues.
    - Create a prep.pyfile as the reproducible component that handles missing values, fixes data integrity issues, changes data types, scales data, etc.

- Data Exploration
    - Goal: The findings from your analysis should provide you with answers to the specific questions your customer asked that will be used in your final report as well as information to move forward toward building a model.
        - Run at least 1 t-test and 1 correlation test.

        - Make sure to summarize your takeaways and conclusions. 


- Modeling
    - Goal: develop a regression model that performs better than a baseline.
    - feature engineering
        - Which features should be included in your model?



## Key Findings and Takeaways

- The number of bedrooms is positively related to property value

- The number of bathrooms is positively related to property value

- The Linear Regression test data outperformed the baseline in predicting property value

- Counties and Tax include:
    - Los Angeles : 1.38 %
    - Orange : 1.21 %
    - Ventura : 1.19 %

## Next steps

- With more time I would like to:

    - a. Explore the year built and age of propety compared to property value
    
    - b. Refine my models with different parameters and run additional tests
    
    - c. Map out county locations and run models on specific counties

## To Recreate my project

- Create your own .env file with your own username/password/host to use the get_connection function in my acquire.py in order to access the Zillow database.

- Make a copy of my acquire and prepare files to use the functions within the files.

- Make a copy of my final notebook, run each cell, and adjust any parameters as desired.
