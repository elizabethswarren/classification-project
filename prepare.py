import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split




def prep_telco(df):
    ''' This function takes in raw telco data, removes duplicates, cleans the values for total_charges and changes to float,
        fills in null values in total_charges column, 
        removes the columns 'internet_service_type_id', 'contract_type_id', 'payment_type_id, and 'customer_id'
        and creates dummy variables for all columns that contain object data types.'''

    # gets rid of whitespace in columns    
    df.columns = df.columns.str.strip()

    # removes duplicate rows
    df = df.drop_duplicates()

    # drops unnecessary columns
    df = df.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id', 'customer_id'])

    # removes whitespace, replaces empty values with NaN values, changes dtype to float for total_charges column
    df['total_charges'] = df.total_charges.str.strip().replace('', np.nan, regex=True).astype(float)

    # replaces null values in total_charges with the median values
    df = df.fillna(df.total_charges.median())

    # creates a df of dummy values for categorical columns
    dummy_df = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service','multiple_lines', 'online_security', 'online_backup','device_protection', 'tech_support', 'streaming_tv', 'streaming_movies','paperless_billing', 'churn', 'payment_type','contract_type','internet_service_type']], drop_first=True)
    
    #remove spaces from dummy column names
    dummy_df.columns = dummy_df.columns.str.replace(' ', '_')
    
    # concats dummy_df to df
    df = pd.concat([df, dummy_df], axis=1)
    return df


def split_data(df,target):
    '''This function takes a dataframe and stratification target, splits the data into an approx 20, 30, 50 split,
       and returns the train, validate, and test dataframes.'''
    
    # initial split for test and train_validate datasets
    train_validate, test = train_test_split(df, test_size = .2, random_state=311, stratify=df[target])

    # splits train and validate datasets
    train, validate = train_test_split(train_validate, test_size = .3, random_state=311, stratify=train_validate[target])

    return train, validate, test