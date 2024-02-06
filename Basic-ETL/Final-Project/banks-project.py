import pandas as pd
from datetime import datetime
import requests 
from bs4 import BeautifulSoup

table_attr = ['Name', 'MC_USD_Billion']
csv_filename = 'Largest_banks_data.csv'
database = 'banks.db'
log_file = 'code_log.txt'
table_name = 'Largest_banks'



def log_progress(message):
    timestamp = datetime.now()
    with open(log_file , 'a') as f:
        f.write(f'{timestamp} : {message}')


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
    
    print(df)
    return 
    


extract()