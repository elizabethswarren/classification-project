import pandas as pd
import os
from env import get_db_url


def get_telco_data():
    ''' This function checks to see if a csv with the telco data exists, and if not,
        runs a SQL query to pull from database and save it in a new csv file.'''
    filename = 'telco.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)

    else:
        sql = '''SELECT *
                FROM customers
                JOIN payment_types USING (payment_type_id)
                JOIN contract_types USING (contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id);
                '''

        df = pd.read_sql(sql, get_db_url('telco_churn'))

        df.to_csv(filename, index=False)

        return df