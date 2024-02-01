import pandas as pd
from bs4 import BeautifulSoup
import requests as request
from datetime import datetime
import sqlite3 as sql
import numpy as np

csv_file = 'countries_by-gdp.csv'
table_attrs= ['Country', 'GDP_USD_billions']
table_name  = 'countries_by_gdp'
URL = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

def extract_data(url):
    '''Extract the data from the given URL'''

    df = pd.DataFrame(table_attrs)

    response = request.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        table_tags = soup.find_all('table')
        req_table_tag = table_tags[2]
        body_tag = req_table_tag.find('tbody')
        rows = body_tag.find_all('tr')







extract_data(URL)
