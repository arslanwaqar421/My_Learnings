import pandas as pd
from bs4 import BeautifulSoup
import requests as request
from datetime import datetime
import sqlite3 as sql
import numpy as np

csv_file = 'countries_by-gdp.csv'
table_attrs= ['Country', 'GDP_USD_Billions']
table_name  = 'countries_by_gdp'
URL = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

def extract_data(url):
    '''Extract the data from the given URL'''
    country = []
    gdp = []
    response = request.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        table_tags = soup.find_all('table')
        req_table_tag = table_tags[2]
        body_tag = req_table_tag.find('tbody')
        rows = body_tag.find_all('tr')
        for i in range(3,216,1):
            data = rows[i].find_all('td')
            country.append(data[0].text.strip())
            try:
                gdp.append(data[2].text)
            except Exception as e:
                gdp.append('')
    print(len(country))
    print(len(gdp))
    df = pd.DataFrame({'Country' : country,
                         'GDP_USD_Billions': gdp})    
    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
    
    # Remove commas and convert to float
    df['GDP_USD_Billions'] = df["GDP_USD_Billions"].str.replace(',', '').replace('—', 'NaN').astype(float)
    
    # Divide by 1000 and round to 2 decimal places
    df['GDP_USD_Billions'] = (df['GDP_USD_Billions'] / 1000).round(2)
    
    print(df.dtypes)

    return df

def load_to_csv(filename, df):

    '''This function loads the given dataframe to a csv file'''
    df.to_csv(filename, index = False)
    print('-------------------------------------')
    print("   Data Successfully loaded to CSV")
    print('-------------------------------------')




df = extract_data(URL)
print(df)
df = transform(df)
print(df)
load_to_csv(csv_file,df)
