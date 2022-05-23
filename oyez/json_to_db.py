
import pandas as pd
import glob
import os
import json
import numpy as np
from pprint import pprint
import re
#from neoModelAPI import NeoNodes as nn




    

def get_cwd():
    cwd = os.getcwd()
    return cwd

def get_files(cwd =os.getcwd(), input_directory = 'loc_cases'):
    
    path = os.sep.join([cwd,input_directory])
    file_list= [f for f in glob.glob(path + "**/*.json", recursive=True)]
  
    return file_list



def load_json_data(file):
    f = open (file, "r")
  
    # Reading from file
    data = json.loads(f.read())
    return data

def citation_output(file_list,cwd):
    outpath = os.sep.join([cwd,'loc_cited'])
    for file in file_list:
        
        data = load_json_data(file=file)
        data = data['results']
        #data = create_citation(data)
        for result in data:
            split = result['id'].split('/')
            result['loc_id'] = split[4]
            outfile = split[4] + '.json'
            outfile = os.sep.join([outpath,outfile])
            
            pprint(outfile)
            with open(outfile, 'w') as f:
                json.dump(result, f)



if __name__ == "__main__":
    #neo_applified = instantiate_neo_model_api()
    cwd = get_cwd()
    file_list = get_files(cwd = cwd)
    output_files = citation_output(file_list,cwd)

    

    
    




    
    