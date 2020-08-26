#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:45:03 2020

@author: simondonike
"""

import requests
import pandas as pd
import time

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
"https://eo4geocourses.github.io/PLUS_EO_For_Natural_Hazards/",
]
"""Takes URL, returns HTML as string"""
def get_html(url):
    url_answer = requests.get(url)
    print(url_answer,"  received from GitHub Pages ->",url[32:])
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
"""Extracts string after dc:title, returns MAX 1 argument"""
def extract_title(metadata):
    metadata_short = metadata[metadata.find("dc:title ")+(len("dc:title ")+1):]
    title = metadata_short[:metadata_short.find('"')]
    return(title)

"""Extracts string after dc:creator, returns MAX 1 argument"""
def extract_creator(metadata):
    metadata_short = metadata[metadata.find("dc:creator ")+(len("dc:creator ")+1):]
    creator = metadata_short[:metadata_short.find('"')]
    return(creator)

"""Extracts string after dc:abstract, returns MAX 1 argument"""
def extract_abstract(metadata):
    metadata_short = metadata[metadata.find("dc:abstract ")+(len("dc:abstract ")+1):]
    abstract = metadata_short[:metadata_short.find('"')]
    return(abstract)

"""Extracts string after dc:description, returns MAX 1 argument"""
def extract_description(metadata):
    metadata_short = metadata[metadata.find("dc:description ")+(len("dc:description ")+1):]
    description = metadata_short[:metadata_short.find('"')]
    return(description)

"""Extracts string after dc:contributor, returns MAX 1 argument"""
def extract_contributor(metadata):
    metadata_short = metadata[metadata.find("dc:contributor ")+(len("dc:contributor ")+1):]
    contributor = metadata_short[:metadata_short.find('"')]
    return(contributor)

"""Extracts string after dc:created, returns MAX 1 argument"""
def extract_created(metadata):
    metadata_short = metadata[metadata.find("dc:created ")+(len("dc:created ")+1):]
    created = metadata_short[:metadata_short.find('"')]
    return(created)

"""Extracts string after dc:language, returns MAX 1 argument"""
def extract_language(metadata):
    metadata_short = metadata[metadata.find("dc:language ")+(len("dc:language ")+1):]
    language = metadata_short[:metadata_short.find('"')]
    return(language)

"""Extracts strings after dc:relations, returns LIST of arguments (relations)"""
def extract_relation(metadata):
    relation = []
    #Cycling through metadata while stil relation left, taking relation out of
    #string after appending to relation list
    while "dc:relation" in metadata:
        metadata_short = metadata[metadata.find("dc:relation")+(len("dc:relation ")):]
        temp = (metadata_short[:metadata_short.find(";")]).replace("eo4geo:","")
        
        # Checking for finish of last relation , either " " ";" or "."
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
item[9] = language
"""
def scrape(url_list):
    ls = []
    for url in url_list:
        item = []
        item.append(str(url))
        htmltext = get_html(url)
        metadata = extract_metadata(htmltext)
        #print(metadata)
        if extract_title(metadata) == "What is Copernicus?":
            #print("UNCHANGED",url)
            changed_metadata = False
            item.append(str(changed_metadata)) #status
            item.append("")             #title
            item.append("")             #creator
            item.append("")             #abstract
            item.append("")             #desctiption
            item.append("")             #contributor
            item.append("")             #created
            item.append("")             #relation
            item.append("")             #language
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
            #print("CHANGED",url)
            item.append(str(changed_metadata))               #status
            item.append(extract_title(metadata))        #title
            item.append(extract_creator(metadata))      #creator
            item.append(extract_abstract(metadata))     #abstract
            item.append(extract_description(metadata))  #description
            item.append(extract_contributor(metadata))  #contributors
            item.append(extract_created(metadata))      #created
            item.append(extract_relation(metadata))     #relation
            item.append(extract_language(metadata))     #language
            
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
print_status = False
start_time = time.time()
#turn resulting list from scrape into pd DataFrame
df = pd.DataFrame(scrape(url_list))
#Give df columns names
df.columns = ["URL","Added Metadata?","Title","Creator","Abstract","Description","Contributors","Date created","Relation/s","Language"]
#export to csv
df.to_csv("metadata_presentations.csv",index=False)
if print_status == True:
    print("Data sucessfully saved to 'metadata_presentations.csv'")
    print("Elapsed time in seconds: ", round(time.time()-start_time,2))
def write_html(meta_df):
    header = '''<p><span style="text-decoration: underline;"><strong><img style="float: left;" src="http://www.eo4geo.eu/wp-content/uploads/2018/03/logo_site_retina_22.png" alt="EO4GEO Logo" width="220" height="167" /></strong></span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4 style="text-align: left;">&nbsp;</h4>
<h4 style="text-align: left;">&nbsp;</h4>
<h4 style="text-align: left;">&nbsp;</h4>
<h4 style="text-align: left;"><span style="text-decoration: underline;"><strong><br />EO4GEO</strong> Course Material Metadata Status<br /></span></h4>
<p style="text-align: left;">This table is updated automatically to show the progress of metadata annotations of the slideshows hosted on <br />GitHub Pages/IO.&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<!--HTML TABLE START IN LINDE BELOW-->'''
    html = open("index.html","w")
    html.write(header)
    html.write(meta_df.to_html(index=False,bold_rows=True,justify='center'))

def format_html_table(df):
    import numpy as np
    df_2 = df.copy()
    #yes_icon = '<a href="https://www.w3schools.com"><img border="0" alt="https://www.eo4geo.sbg.ac.at/PLUS/Practice-Image-Processing/checkmark.png" width="100" height="100"></a>'
    #no_icon = '<a href="https://www.w3schools.com"><img border="0" alt="W3Schools" src="https://www.eo4geo.sbg.ac.at/PLUS/Practice-Image-Processing/icon-no.png" width="100" height="100"></a>'
    #Replacing missing titles with logo
    df["Title"] = df["Title"].replace("", "///")
    df["Creator"] = np.where(df["Creator"]!="", "Yes", "///")
    df["Abstract"] = np.where(df["Abstract"]!="", "Yes", "///")
    df["Description"] = np.where(df["Description"]!="", "Yes", "///")
    df["Contributors"] = np.where(df["Contributors"]!="", "Yes", "///")
    df["Date created"] = np.where(df["Date created"]!="", "Yes", "///")
    df["Relation/s"] = np.where(df["Relation/s"]!="", "Yes", "///")
    df["Language"] = df["Language"].replace("", "///")
    return df_2
df_2 = format_html_table(df)

write_html(format_html_table(df))