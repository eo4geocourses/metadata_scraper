#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:45:03 2020

@author: simondonike
"""




#READ AS STRING
import requests
url_list = [
"https://eo4geocourses.github.io/PLUS_Practice-Image-Processing/",
"https://eo4geocourses.github.io/VITO_TerraScope_TrainingPack_Application_Example/",
"https://eo4geocourses.github.io/VITO_Data_Access_In_Terrascope/",
"https://eo4geocourses.github.io/VITO_Cloud_Infrastructure/",
"https://eo4geocourses.github.io/GISIG_Introduction_to_EO4GEO/"
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
    url = requests.get(url)
    htmltext = url.text
    return(htmltext)


"""Extracts MetaData part ftom full HTML text"""
def extract_metadata(htmltext):
    metadata_start = htmltext[htmltext.find("AUTHORS: DEFINE METADATA FOR WHOLE SLIDESET HERE:"):]
    metadata_end = metadata_start[:metadata_start.find("-->",50)]
    metadata = metadata_end
    return(metadata)

"""Exxtracts string after dc:title, returns MAX 1 argument"""
def extract_title(metadata):
    metadata_short = metadata[metadata.find("dc:title ")+(len("dc:title ")+1):]
    title = metadata_short[:metadata_short.find(";")-1]
    return(title)

"""Exxtracts string after dc:creator, returns MAX 1 argument"""
def extract_creator(metadata):
    metadata_short = metadata[metadata.find("dc:creator ")+(len("dc:creator ")+1):]
    creator = metadata_short[:metadata_short.find(";")-1]
    return(creator)

"""Exxtracts string after dc:abstract, returns MAX 1 argument"""
def extract_abstract(metadata):
    metadata_short = metadata[metadata.find("dc:abstract ")+(len("dc:abstract ")+1):]
    abstract = metadata_short[:metadata_short.find(";")-1]
    return(abstract)

"""Exxtracts string after dc:description, returns MAX 1 argument"""
def extract_description(metadata):
    metadata_short = metadata[metadata.find("dc:description ")+(len("dc:description ")+1):]
    description = metadata_short[:metadata_short.find(";")-1]
    return(description)

"""Exxtracts string after dc:contributor, returns MAX 1 argument"""
def extract_contributor(metadata):
    metadata_short = metadata[metadata.find("dc:contributor ")+(len("dc:contributor ")+1):]
    contributor = metadata_short[:metadata_short.find(";")-1]
    return(contributor)

"""Exxtracts string after dc:created, returns MAX 1 argument"""
def extract_created(metadata):
    metadata_short = metadata[metadata.find("dc:created ")+(len("dc:created ")+1):]
    created = metadata_short[:metadata_short.find(";")-1]
    return(created)

"""Exxtracts string after dc:relations, returns MAX 1 argument"""
def extract_relation(metadata):
    while "dc:relation" in metadata:
        "WIP"
        relation = []
        metadata_short = metadata[metadata.find("dc:relation ")+(len("dc:relation ")):]
        relation.append(metadata_short[:metadata_short.find(";")-1])
        print("HERE",metadata_short)
        metadata = metadata_short[metadata_short.find(";"):]
    
    return(relation)
    

for url in url_list:
    htmltext = get_html(url)
    metadata = extract_metadata(htmltext)
    
    
    title = extract_title(metadata)
    creator = extract_creator(metadata)
    abstract = extract_abstract(metadata)
    description = extract_description(metadata)
    contributor = extract_contributor(metadata)
    created = extract_created(metadata)
    #relation = extract_relation(metadata)
    
    print("COURSE: ",title,"\n",creator,"\n",abstract,"\n",description,"\n",
          contributor,"\n",created,"\n","RELATION PLACEHOLDER\n","____________________\n\n\n\n")
