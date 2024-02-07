import pandas as pd
from datetime import datetime
import requests 
from bs4 import BeautifulSoup
import numpy as np
import sqlite3

table_attr = ['Name', 'MC_USD_Billion']
csv_filename = 'Largest_banks_data.csv'
database = 'banks.db'
log_file = 'code_log.txt'
table_name = 'Largest_banks'



def log_progress(message):
    timestamp = datetime.now()
    with open(log_file , 'a') as f:
        f.write(f'{timestamp} : {message}\n')


def extract():

    df = pd.DataFrame(columns = table_attr)
    
    response = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')
    
    soup = BeautifulSoup(response.text,'html.parser')
    
    all_tables = soup.find_all('table')
    
    req_table = all_tables[0]
    
    rows = req_table.find_all('tr')
    
    for i in range(1,len(rows),1):
        cols = rows[i].find_all('td')
        data_dic = {'Name' : cols[1].text.strip('\n'),
                    'MC_USD_Billion' : cols[2].text.strip('\n')}
        df1 = pd.DataFrame(data_dic, index = [0])
        df = pd.concat([df, df1], ignore_index=True)

    return df


def transform(df):
    exchange_rate = pd.read_csv('exchange_rate.csv')
    
    # Creating a dictionary from the exchange_rate DataFrame
    exchange_rate_dict = exchange_rate.set_index('Currency')['Rate'].to_dict()
    print(exchange_rate_dict)
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)

    # Using the dictionary to convert values in 'MC_USD_Billion' to GBP,EUR,INR
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate_dict['GBP'],2) for x in df['MC_USD_Billion']]
    
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate_dict['EUR'],2) for x in df['MC_USD_Billion']]
    
    df['MC_INR_Billion'] = [np.round(x*exchange_rate_dict['INR'],2) for x in df['MC_USD_Billion']]

    print(df['MC_EUR_Billion'][4])

    return df


def load_to_csv(df):
    try: 
        df.to_csv(csv_filename, index = False)
        print('----------------------------------')
        print(' Data Sucessfully loaded to CSV.')
        print('----------------------------------')
    except:
        print('----------------------------------')
        print(' Error while loading data to CSV!')
        print('----------------------------------')

def load_to_db(df, sql_connection,table):
    try:
        df.to_sql(table, sql_connection , if_exists ='replace' , index = False)
        print('----------------------------------')
        print('  Data Sucessfully loaded to DB.')
        print('----------------------------------')
    except:
        print('----------------------------------')
        print(' Error while loading data to DB.')
        print('----------------------------------')

def run_query(query, sql_connection):
    print('Query Statement : ' , query)
    output = pd.read_sql(query,sql_connection)
    print('Query Output : ')
    print(output)




log_progress('Preliminaries complete. Initiating ETL process')

df = extract()

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)

log_progress('Data transformation complete. Initiating Loading process')

load_to_csv(df)

log_progress('Data saved to CSV file')

conn = sqlite3.Connection(database)

log_progress('SQL Connection initiated')

load_to_db(df, conn, table_name)

log_progress('Data loaded to Database as a table, Executing queries')

run_query('SELECT * FROM Largest_banks', conn)

run_query('SELECT AVG(MC_GBP_Billion) FROM Largest_banks',conn)

run_query('SELECT Name from Largest_banks LIMIT 5', conn)

log_progress('Process Complete')

conn.close()

log_progress('Server Connection closed')