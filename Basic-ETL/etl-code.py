import pandas as pd

import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"

def extract_from_csv(filename):
    return pd.read_csv(filename)


def extract_from_json(filename):
    return pd.read_json(filename,lines=True)


def extract_from_xml(filename):
    df = pd.DataFrame(columns=["name","height","weight"])
    tree = ET.parse(filename)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        df = pd.concat([df,pd.DataFrame([{"name": name, "height":height, "weight": weight}])],ignore_index=True)
    return df


def extract():
    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

    for csvfile in glob.glob("*.csv"):
        data = extract_from_csv(csvfile)
        if data is not None and not data.empty:
            extracted_data = pd.concat([extracted_data, data], ignore_index=True)

    for jsonfile in glob.glob("*.json"):
        data = extract_from_json(jsonfile)
        if data is not None and not data.empty:
            extracted_data = pd.concat([extracted_data, data], ignore_index=True)

    for xmlfile in glob.glob("*.xml"):
        data = extract_from_xml(xmlfile)
        if data is not None and not data.empty:
            extracted_data = pd.concat([extracted_data, data], ignore_index=True)

    return extracted_data



def transform(data):
    '''Convert the inches to meters and round off to two decimals 1 inch is 0.0254 meters'''
    data['height'] = round(data.height*0.0254, 2)

    data['weight'] = round(data.weight*0.45359237,2)

    return data


def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 


# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 

 

# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended")
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 