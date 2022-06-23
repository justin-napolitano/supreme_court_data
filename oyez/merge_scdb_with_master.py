#merging.python
from doctest import master
import os
import pandas as pd
from pprint import pprint
import json

def read_json(file_path):
    with open(file_path) as f: 
        dict = json.load(f)
    return dict

    
def nodify_list(lst,node_name):
    return_list=[]
    for item in lst: 
        dict = {node_name: item}
        return_list.append(dict)
    return return_list


def convert_citation(x):
    x = x.split(" ")
    try:
        padding = 3
        page = x[2]
        volume = x[0]
        page = str(page).zfill(padding)
        volume = str(volume).zfill(padding)
        
        x = 'usrep' + volume + page
    except:
        x = pd.nan
    return x

def nodify(x):
    keys = x.keys()
    dct = {}
    for key in keys:
        #print(key)
        #print(x[key])
        dct[key] = x[key]
        #pprint(dct)
    #pprint(dct)
    return dct


def to_file_path(x):
    outpath = os.sep.join([os.getcwd(),"scdb_nodes"])
    x = x +".json"
    pprint(x)
    x = os.sep.join([outpath,x])

    
    return x

def to_json(x):
    #pprint(x.outpath)
    file_list = []
    with open(x["outpath"], "w") as f: 
        json.dump(x,f, indent = 6)
        file_list.append("outpath")
    return file_list
    
    

def main():
    json_list = []
    # outpath fo the current file
    inpath = "/Users/jnapolitano/Projects/supreme_court_transcripts/oyez/scdb_case_files.csv"
    outpath = 'final_json_data'
    
    #Create a df from the case_files.csv file
    master_df = pd.read_csv(inpath)
    #master_df.usCite = master_df.usCite.dropna()


    #pprint(master_df.usCite)
    for index, row in master_df.iterrows():
            
        oyez_dict = read_json(row["Path"])
        loc_dict = read_json(row['Path_1'])
        #pprint(loc_dict)

        for key in loc_dict:
            key_name = "scdb_" + key
            oyez_dict[key_name] = loc_dict[key]


        outfile = os.sep.join([outpath,oyez_dict['simple_citation']])
        outfile = outfile + ".json"

        with open(outfile, "w") as f: 
            json.dump(oyez_dict,f, indent = 6)
        

    #pprint(oyez_dict)
if __name__ == "__main__":
    main()