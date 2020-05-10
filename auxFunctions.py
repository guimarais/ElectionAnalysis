import pandas as pd
import json
from pandas.io.json import json_normalize

def readExportToPd(file='./Files/export.json'):
    """
    Reads an export file and returns a pandas dataframe.
    """
    
    with open(file) as f:
        data = json.load(f)
        
    ## Ignore the first two hierarchical layers
    tempj = data['campaign-markers']['data']
    
    #To flatten the remaining json and convert it into a pandas dataframe (easier to manipulate, imo)
    data = pd.json_normalize(tempj)
    
    ## Cleanup the d.parameters.campaign column a little bit. Add a new column called campaign which is the cleaned version. Remove trailing and leading chars we might not want
    data['campaign'] = data['d.parameters.campaign']
    data['campaign'] = data['campaign'].astype('str')
    data['campaign'] = data['campaign'].map(lambda x: x.lstrip('[').rstrip(']'))
    data['campaign'] = data['campaign'].map(lambda x: x.lstrip('\'').rstrip('\''))
    
    return data