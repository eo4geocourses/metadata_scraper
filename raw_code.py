#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:45:03 2020

@author: simondonike
"""

import requests
import pandas as pd
import time
start_time = time.time()


url_list = [
"https://eo4geocourses.github.io/PLUS_Practice-Image-Processing/",
"https://eo4geocourses.github.io/VITO_TerraScope_TrainingPack_Application_Example/",
"https://eo4geocourses.github.io/VITO_Data_Access_In_Terrascope/",
"https://eo4geocourses.github.io/VITO_Cloud_Infrastructure/",
"https://eo4geocourses.github.io/GISIG_Introduction_to_EO4GEO/",
"https://eo4geocourses.github.io/SpaSe_OBIA-for-Operations-Copernicus-Service-Challenge-Practical-Example/",
"https://eo4geocourses.github.io/GEOF_Understanding-the-concept-of-EO-time-series/",
"https://eo4geocourses.github.io/GEOF_Basic-GIS-knowledge-vector-and-raster-data/",
"https://eo4geocourses.github.io/GEOF_Copernicus-Service-Land/",
"https://eo4geocourses.github.io/GEOF_EO-Data-sources/",
"https://eo4geocourses.github.io/GEOF_Validation-of-EO-products/",
"https://eo4geocourses.github.io/GEOF_Preprocessing-of-EO-data/",
"https://eo4geocourses.github.io/GEOF_Legal-issues-in-EO-GI/",
"https://eo4geocourses.github.io/UT-ITC_Satellite_Data_Classification_Random_Forests/",
"https://eo4geocourses.github.io/UT-ITC_Satellite_Data_Classification_Decision_Trees/",
"https://eo4geocourses.github.io/UNEP-GRID_Introduction-to-GIS/",
"https://eo4geocourses.github.io/KULeuven_Technical-Introduction-to-SDI/",
"https://eo4geocourses.github.io/KULeuven_Management-View-on-SDI/",
"https://eo4geocourses.github.io/KULeuven_Introduction-CitizenScience-in-GI-and-EO/",
"https://eo4geocourses.github.io/IGIK_Sentinel2-Data-and-Vegetation-Indices/",
"https://eo4geocourses.github.io/IGIK_Introduction-to-Remote-Sensing/",
"https://eo4geocourses.github.io/ClimateKIC_Copernicus-Service-Climate-Change/",
"https://eo4geocourses.github.io/ClimateKIC_Copernicus-Service-Atmosphere/",
"https://eo4geocourses.github.io/IES_EO-for-Managers/",
"https://eo4geocourses.github.io/FSU-Jena_Persistent-Scaterrer-Interferometry/",
"https://eo4geocourses.github.io/FSU-Jena_SAR-Data-for-Flood-Mapping/",
"https://eo4geocourses.github.io/ROSA_Change-Detection-in-optical-Data/",
"https://eo4geocourses.github.io/UNIBAS_Remote-Sensing-Environment/",
"https://eo4geocourses.github.io/UNIBAS_Methods-Techniques-EO/",
"https://eo4geocourses.github.io/UJI_Introduction-to-Programming/",
"https://eo4geocourses.github.io/UJI_Reproducable-Research-Practices-in-Geosciences/",
"https://eo4geocourses.github.io/UJI_AgroMonitoring-with-Geospatial-Data/",
"https://eo4geocourses.github.io/PLUS_Practice-Image-Processing/",
"https://eo4geocourses.github.io/PLUS_EO_For_Natural_Hazards/",
]



"""Takes URL, returns HTML as string"""
def get_html(url):
    url_answer = requests.get(url)
    print(url_answer,"  received from:  ",url[8:])
    htmltext = url_answer.text
    return(htmltext)


"""Extracts MetaData part ftom full HTML text, removes formatiing characters"""
def extract_metadata(htmltext):
    metadata_start = htmltext[htmltext.find("AUTHORS: DEFINE METADATA FOR WHOLE SLIDESET HERE:"):]
    metadata_end = metadata_start[:metadata_start.find("-->",50)]
    metadata = metadata_end
    #removing new line and tab characters
    metadata = metadata.replace("\n","")
    metadata = metadata.replace("\t","")
    
    return(metadata)


"""Exxtracts string after dc:title, returns MAX 1 argument"""
def extract_title(metadata):
    metadata_short = metadata[metadata.find("dc:title ")+(len("dc:title ")+1):]
    title = metadata_short[:metadata_short.find('"')]
    return(title)

"""Exxtracts string after dc:creator, returns MAX 1 argument"""
def extract_creator(metadata):
    metadata_short = metadata[metadata.find("dc:creator ")+(len("dc:creator ")+1):]
    creator = metadata_short[:metadata_short.find('"')]
    return(creator)

"""Exxtracts string after dc:abstract, returns MAX 1 argument"""
def extract_abstract(metadata):
    metadata_short = metadata[metadata.find("dc:abstract ")+(len("dc:abstract ")+1):]
    abstract = metadata_short[:metadata_short.find('"')]
    return(abstract)

"""Exxtracts string after dc:description, returns MAX 1 argument"""
def extract_description(metadata):
    metadata_short = metadata[metadata.find("dc:description ")+(len("dc:description ")+1):]
    description = metadata_short[:metadata_short.find('"')]
    return(description)

"""Exxtracts string after dc:contributor, returns MAX 1 argument"""
def extract_contributor(metadata):
    metadata_short = metadata[metadata.find("dc:contributor ")+(len("dc:contributor ")+1):]
    contributor = metadata_short[:metadata_short.find('"')]
    return(contributor)

"""Exxtracts string after dc:created, returns MAX 1 argument"""
def extract_created(metadata):
    metadata_short = metadata[metadata.find("dc:created ")+(len("dc:created ")+1):]
    created = metadata_short[:metadata_short.find('"')]
    return(created)

"""Exxtracts strings after dc:relations, returns LIST of relations"""
def extract_relation(metadata):
    relation = []
    #Cycling through metadata while stil relation left, taking relation out of
    #string after appending to relation list
    while "dc:relation" in metadata:
        "WIP"
        metadata_short = metadata[metadata.find("dc:relation")+(len("dc:relation ")):]
        temp = (metadata_short[:metadata_short.find(";")]).replace("eo4geo:","")
        
        #Checking for finish of last relation , either " " ";" or "."
        # in order to slice string after last relation
        if " " in temp:
            temp = temp[:temp.find(" ")]
        if "." in temp:
            temp = temp[:temp.find(".")]
        
        relation.append(temp)
        metadata = metadata_short[metadata_short.find(";"):]
    
    return(relation)

"""Takes List, returns list of metadata.
for each item in list:
item[0] = URL
item[1] = changed? True/False
item[2] = title
item[3] = creator
item[4] = abstract
item[5] = description
item[6] = contributors
item[7] = created
item[8] = relation
"""
def scrape(url_list):
    ls = []
    for url in url_list:
        item = []
        item.append(str(url))
        htmltext = get_html(url)
        metadata = extract_metadata(htmltext)
        
        if extract_title(metadata) == "What is Copernicus?":
            print("UNCHANGED",url)
            changed_metadata = False
            item.append(str(changed_metadata)) #status
            item.append("")             #title
            item.append("")             #creator
            item.append("")             #abstract
            item.append("")             #desctiption
            item.append("")             #contributor
            item.append("")             #created
            item.append("")             #relation
            """
            dict_meta = {}
            dict_meta["title"] = ""
            dict_meta["creator"] = ""
            dict_meta["abstract"] = ""
            dict_meta["description"] = ""
            dict_meta["contributor"] = ""
            dict_meta["created"] = ""
            dict_meta["relation"] = ""
            item.append(dict_meta)
            """
        else:
            changed_metadata = True
            print("CHANGED",url)
            item.append(str(changed_metadata))               #status
            item.append(extract_title(metadata))        #title
            item.append(extract_creator(metadata))      #creator
            item.append(extract_abstract(metadata))     #abstract
            item.append(extract_description(metadata))  #description
            item.append(extract_contributor(metadata))  #contributors
            item.append(extract_created(metadata))      #created
            item.append(extract_relation(metadata))     #relation
            """
            dict_meta = {}
            dict_meta["title"] = extract_title(metadata)
            dict_meta["creator"] = extract_creator(metadata)
            dict_meta["abstract"] = extract_abstract(metadata)
            dict_meta["description"] = extract_description(metadata)
            dict_meta["contributor"] = extract_contributor(metadata)
            dict_meta["created"] = extract_created(metadata)
            dict_meta["relation"] = extract_relation(metadata)
            item.append(dict_meta)
            """
        ls.append(item)
    return(ls)




#turn resulting list from scrape into pd DataFrame
df = pd.DataFrame(scrape(url_list))
#Give df columns names
df.columns = ["URL","Added Metadata?","Title","Creator","Abstract","Description","Contributors","Date created","Relation/s"]
#export to csv
df.to_csv("metadata_presentations.csv",index=False)
#print results
print("\n\n",df,"\n\n")
print("Data sucessfully saved to .csv")
print("Elapsed time in seconds: ", round(time.time()-start_time,2))