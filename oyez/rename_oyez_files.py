from ast import Num
import glob
import os
import json
import numpy as np
from pprint import pprint
import re

def get_cwd():
    cwd = os.getcwd()
    return cwd

def load_json_data(file):
    f = open (file, "r")
  
    # Reading from file
    data = json.loads(f.read())
    return data

def get_paths(cwd =os.getcwd(), input_directory = 'cases'):
    
    path = os.sep.join([cwd,input_directory])
    path_list= [f for f in glob.glob(path + "**/*.json", recursive=True)]

  
    return path_list

def get_files(path_list):
    for path in path_list:
        file = path.split(os.sep)
        print(file)


def output_files(file_list):
    for file in file_list:
        print(file)

    
def load_json_data(file):
    f = open(file, "r")
  
    # Reading from file
    data = json.loads(f.read())
    return data


if __name__ == "__main__":
    #neo_applified = instantiate_neo_model_api()
    cwd = get_cwd()
    path_list = get_paths(cwd = cwd)
    outpath = os.sep.join([cwd,'oyez_cited'])
    for path in path_list:
        data = load_json_data(path)
        try:
            citation = data['citation']
        except:
            continue
        try:
            padding = 3
            page = citation['page']
            volume = citation['volume']
            page = str(page).zfill(padding)
            volume = str(volume).zfill(padding)
            
            data['loc_id'] = 'usrep' + volume + page
        except:
            continue
        try:
            outfile = data['loc_id'] + '.json'
            outfile = os.sep.join([outpath,outfile])
            pprint(outfile)
            with open(outfile, 'w') as f:
                json.dump(data, f)
        except:
            raise
        
    #file_list = get_files(path_list)

    #output_files = output_files(file_list)