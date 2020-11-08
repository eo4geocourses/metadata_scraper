#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:45:03 2020

@author: simondonike
"""

import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
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
"https://eo4geocourses.github.io/FSU-Jena_SAR-Data-for-Flood-Mapping/",
"https://eo4geocourses.github.io/ROSA_Change-Detection-in-optical-Data/",
"https://eo4geocourses.github.io/UNIBAS_Remote-Sensing-Environment/",
"https://eo4geocourses.github.io/UNIBAS_Methods-Techniques-EO/",
"https://eo4geocourses.github.io/UJI_Introduction-to-Programming/",
"https://eo4geocourses.github.io/UJI_Reproducible-Research-Practices-in-Geosciences/",
"https://eo4geocourses.github.io/UJI_AgroMonitoring-with-Geospatial-Data/",
"https://eo4geocourses.github.io/PLUS_EO_For_Natural_Hazards/",
"https://eo4geocourses.github.io/PLUS_OBIA-Introduction/"
]

"""repositories to be added later: "https://eo4geocourses.github.io/FSU-Jena_Persistent-Scaterrer-Interferometry/","""


"""Takes URL, returns HTML as string"""
def get_html(url):
    url_answer = requests.get(url)
    print(url_answer,"  received from GitHub Pages ->",url[32:])
    htmltext = url_answer.text
    return(htmltext)


"""Takes URL, returns if Repo is status 404 or 200"""
def get_html_code(url):
    url_answer = requests.get(url)
    if str(url_answer) == "<Response [404]>":
        return("Private")
    if str(url_answer) == "<Response [200]>":
        return("Public")
    else:
        return("UNKNOWN")
    


"""ORDER OF RETURN LIST:
        1. URL
        2. Changed Boolean
        3. Title
        4. Creator
        5. Abstract
        6. Description
        7. Contributor(s)
        8. Created
        9. Relation(s)
        10. Language
"""
def scrape_BS(url,htmltext):
    
    
    url_repo = ""
    sizeOrDuration = ""
    format_tag = ""
    license_tag = ""
    soup = BeautifulSoup(htmltext,features="lxml")
    ret_ls = []             #Resetting return list
    # Setting empty variables to fill by meta tags
    title = ""
    changed = ""
    creator = []
    abstract = ""
    description = ""
    contributor = []
    created = ""
    relation = []
    language = []
    education_level = ""
    content_type = ""
    publisher = ""
   
    
    for tag in soup.find_all("meta"):
        
        
        """Check for validity of Metadata/changed state by comparing and adding True/False attribute"""
        if tag.get("property", None) == "dc:title":
            if tag.get("content", None) == "What is Copernicus?":
                changed = (False)
            if tag.get("content", None) != "What is Copernicus?":
                changed = (True)
                
        
        if tag.get("property", None) == "dc:title":
            #ret_ls.append(tag.get("content", None))
            title = (tag.get("content", None))
            
        elif tag.get("property", None) == "dc:creator":
            #ret_ls.append(tag.get("content", None))
            creator.append(tag.get("content", None))

        elif tag.get("property", None) == "dc:publisher":
            #ret_ls.append(tag.get("content", None))
            publisher = tag.get("content", None)
            
            
#        elif tag.get("property", None) == "dc:subject":
#            print(tag.get("content", None))
    
        elif tag.get("property", None) == "dc:abstract":
            #ret_ls.append(tag.get("content", None))
            abstract = tag.get("content", None)
            
#        elif tag.get("property", None) == "dc:tableOfContents":
#            print(tag.get("content", None))
            
        elif tag.get("property", None) == "dc:description":
            #ret_ls.append(tag.get("content", None))
            description = tag.get("content", None)
            
        elif tag.get("property", None) == "dc:contributor":
            #tag.get("content", None)
            #print("pass")
            #ret_ls.append(tag.get("content", None))
            #ret_ls_contributors.append(tag.get("content", None))
            contributor.append(tag.get("content", None))

            
        elif tag.get("property", None) == "dc:created":
            #ret_ls.append(tag.get("content", None))
            created = tag.get("content", None)
            
        elif tag.get("property", None) == "dc:type":
            #print(tag.get("content", None))
            content_type = tag.get("content", None)
            
        elif tag.get("property", None) == "dc:format":
#            print(tag.get("content", None))
            format_tag = tag.get("content", None)
            
        elif tag.get("property", None) == "dc:language":
            #ret_ls.append(tag.get("content", None))
           language = tag.get("content", None)
            
        elif tag.get("property", None) == "dc:SizeOrDuration":
#            print(tag.get("content", None))
            sizeOrDuration = tag.get("content", None)
            
#        elif tag.get("property", None) == "dc:audience":
#            print(tag.get("content", None))
            
#        elif tag.get("property", None) == "dc:audience":
#            print(tag.get("content", None))
            
        elif tag.get("property", None) == "dc:educationLevel":
            #print(tag.get("content", None))
            education_level = tag.get("content", None)
            
#        elif tag.get("property", None) == "dc:source":
#            print(tag.get("content", None))
            
#        elif tag.get("property", None) == "dc:rightsHolder":
#            print(tag.get("content", None))
    
        elif tag.get("property", None) == "dc:license":
#            print(tag.get("content", None))
            license_tag = tag.get("content", None)
        
        #Extra list for individual relation tags
#        elif tag.get("property", None) == "dc:relation":
#            relation.append(tag.get("content", None))

#        elif tag.get("link", None) == "dc:relation":
#            relation.append(tag.get("content", None))
#            print(relation)


    # Add URL to unhosted Repo to list
    url_repo = "https://github.com/eo4geocourses/" + url[32:]

    for link in soup.find_all('link', href=True):
        if "eo4geo:" in link['href']:
            relation.append(link['href'])

    
    #append extracted MD information in corect order
    ret_ls.append(url)
    ret_ls.append(get_html_code(url_repo)) # Getting HTML answer code from Repo
    ret_ls.append(changed)
    ret_ls.append(title)

    #making sure not to append empty contributor list
    if len(creator) == 0:
        ret_ls.append("")
    if len(creator) != 0 and len(creator[0]) == 0:
           ret_ls.append("")
    if len(creator) != 0 and creator[0] != "" and len(creator[0])!=0:
        ret_ls.append(creator)
    
    ret_ls.append(publisher)
    ret_ls.append(abstract)
    ret_ls.append(description)
   
       #making sure not to append empty language list
    if len(language) == 0:
        ret_ls.append("")
    if len(language) != 0 and len(language[0]) == 0:
           ret_ls.append("")
    if len(language) != 0 and language[0] != "" and len(language[0])!=0:
        ret_ls.append(language)
   
    ret_ls.append(content_type)
    ret_ls.append(education_level)
    
    ret_ls.append(license_tag)
    ret_ls.append(sizeOrDuration)
    ret_ls.append(format_tag)
    
    #making sure not to append empty list
    if len(contributor) == 0:
        ret_ls.append("")
    if len(contributor) != 0 and len(contributor[0]) == 0:
           ret_ls.append("")
    if len(contributor) != 0 and contributor[0] != "" and len(contributor[0])!=0:
        ret_ls.append(contributor)
        
    ret_ls.append(created)
    
    # Making sure not to append empty relations list
    # Making sure not to add list with only eo4geo: inside
    if len(relation) == 0:
        ret_ls.append("")
    if len(relation) != 0 and relation[0] == "eo4geo:":
        ret_ls.append("")
    if len(relation)!=0 and relation[0]!="eo4geo:":
        ret_ls.append(relation)
    
    
    # Creating list of BoK Links
    # Makin sure not to append empty list
    bok_links = []
    for i in relation:
        bok_links.append("https://bok.eo4geo.eu/" + str(i[7:]))
    if len(bok_links)==0:
        ret_ls.append("")
    else:
        ret_ls.append(bok_links)
    # Append URL Repo last
    ret_ls.append(url_repo)
    return(ret_ls)
    
    
    

# Running Scraper
list_of_metadata = []
for url in url_list:
    list_of_metadata.append(scrape_BS(url,get_html(url)))



"""
____________________________________________________________________________
"""



"""Extracts MetaData part ftom full HTML text, removes formating characters"""
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
        if extract_title(metadata) == "What is Copernicus?" and extract_created(metadata) == "2020-06-20" and extract_creator(metadata) == "Stefan Lang, University of Salzburg" : 
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



"""
DF creation for comment MD scraping
"""

"""
#turn resulting list from scrape into pd DataFrame
df = pd.DataFrame(scrape(url_list))
df = pd.DataFrame()
#Give df columns names
df.columns = ["URL","Added Metadata?","Title","Creator","Abstract","Description","Contributors","Date created","Relation/s","Language"]
#export to csv
df.to_csv("metadata_presentations.csv",index=False)
"""


"""
DF creation for new RDFa method
"""
# Creating DF from List
df = pd.DataFrame.from_records(list_of_metadata)
# Giving column names
df.columns = ["URL","Public/Private","Added Metadata?","Title","Creator","Publisher","Abstract","Description",
              "Language","Type", "EQF", "License", "Size or Duration","Format","Contributors","Date created","Relation/s","BoK Links", "Repo_URL"]





# Adding Banner links to DF
# empty list to hold links in correct order
banner_list = []
#Cycling through URL list of DF
for url in df["URL"]:
    # Adding URL prefix of server
    # Extracting Name of course from link
    # ending with png for file ending
    banner_list.append("https://eo4geo.sbg.ac.at/banner/"+url[32:-1]+".png")

# Adding Graph links to DF
# empty list to hold links in correct order
graph_list = []
for url in df["URL"]:
    # Adding URL prefix of server
    # Extracting Name of course from link
    # ending with URL for graph
    graph_list.append("https://eo4geocourses.github.io/ConceptChart/ConceptChart.html?id="+url[32:-1])
        
#Appending Link to Banner image
df["banner_link"] = banner_list
#Appending Link to Banner image
df["graph_link"] = graph_list


# Rearrange Order
df = df[["URL","Public/Private","Added Metadata?","Title","Creator","Publisher","Abstract","Description",
              "Language","Type", "EQF", "License", "Size or Duration","Format","Contributors","Date created","Relation/s",
              "BoK Links","banner_link","graph_link", "Repo_URL"]]



"""
HTML table Stuff
_____________________________________________________________________________

"""
def format_html_table(df):
    import numpy as np
    df_2 = df.copy()
    df_2["Title"] = df_2["Title"].replace("", "///")
    df_2["Creator"] = np.where(df_2["Creator"]!="", "Yes", "///")
    df_2["Abstract"] = np.where(df_2["Abstract"]!="", "Yes", "///")
    df_2["Description"] = np.where(df_2["Description"]!="", "Yes", "///")
    df_2["Contributors"] = np.where(df_2["Contributors"] != "" , "Yes", "///")
    df_2["Date created"] = np.where(df_2["Date created"]!="", "Yes", "///")
    df_2["Relation/s"] = np.where(df_2["Relation/s"]!="", "Yes", "///")
    df_2["Language"] = df_2["Language"].replace("", "///")
    return df_2


def write_html(meta_df):
    header = '''<p><span style="text-decoration: underline;"><strong><img style="float: left;" src="https://eo4geo.sbg.ac.at/PLUS/EO4GEO_logo.png" alt="EO4GEO Logo" width="220" height="167" /></strong></span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h4 style="text-align: left;">&nbsp;</h4>
<h4 style="text-align: left;">&nbsp;</h4>
<h4 style="text-align: left;">&nbsp;</h4>
<h4 style="text-align: left;"><span style="text-decoration: underline;"><strong><br />EO4GEO</strong> Course Material Metadata Status<br /></span></h4>
<p style="text-align: left;">This table is updated automatically to show the progress of RDFa compliant metadata annotations of the slideshows hosted on <br />GitHub Pages/IO.&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<!--HTML TABLE START IN LINDE BELOW-->'''
    html = open("index.html","w")
    html.write(header)
    html.write(meta_df.to_html(index=False,bold_rows=True,justify='center'))


#Cleaning up table for hmtl writing
df_html = format_html_table(df)
#writing cleaned up table to html
write_html(df_html)





print_status = False
if print_status == True:
    print(df.head(5),"\n\n")
    print("Data sucessfully saved to 'metadata_presentations.csv'")
    print("Elapsed time in seconds: ", round(time.time()-start_time,2))
del start_time, print_status









"""
Cleaning DF of Private Repositories
"""
indexNames = df[df['Public/Private'] == "Private"].index
df.drop(indexNames , inplace=True)

"""
Export of final pandas dataframe to csvs
"""
# Export to final output csv
df.to_csv("metadata_presentations.csv",index=False)
 #put copy in graph subfolder
df.to_csv("graphs/metadata_presentations.csv",index=False)
#print(df)
