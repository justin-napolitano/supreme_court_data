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

def main():

    # outpath fo the current file
    inpath = "/Users/jnapolitano/Projects/supreme_court_db_integration/data/SCDB_2021_01_caseCentered_LegalProvision.csv"
    #inpath = os.sep.join([os.getcwd(),"case_files.csv"])
    outpath = os.sep.join([os.getcwd(),"scdb_nodes"])
    
    #Create a df from the case_files.csv file
    master_df = pd.read_csv(inpath)
    pprint(master_df)
    #for index, row in master_df.iterrows():
            
    #    oyez_dict = read_json(row["Path"])
    #    loc_dict = read_json(row['Path_1'])
    #    oyez_dict['loc_id'] = loc_dict['id']
    ##    oyez_dict['loc_url'] = loc_dict['id']
    #    oyez_dict['simple_citation'] = loc_dict['loc_id']
    #    oyez_dict['shelf_id'] = loc_dict['shelf_id']
    #    oyez_dict['title'] = loc_dict['title']
    #    oyez_dict['issues'] = nodify_list(loc_dict['subject'],'issue')
    #    try:
    #        oyez_dict['major_topics'] = nodify_list(loc_dict['subject_major_case_topic'], 'major_topic')
    #    except:
    #        oyez_dict['major_topics'] = [""]
    #    oyez_dict['loc_pdf'] = loc_dict['resources'][0]['pdf']#

    #    outfile = os.sep.join([outpath,oyez_dict['simple_citation']])
    #    outfile = outfile + ".json"

    #    with open(outfile, "w") as f: 
    #        json.dump(oyez_dict,f, indent = 6)
        


    #pprint(oyez_dict)
if __name__ == "__main__":
    main()