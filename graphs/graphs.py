#removes all non capitalized letters, 
def strip_string(string):
	import re
	return(re.sub(r"[^A-Z,]", '', string))

def URL_to_name(string):
	return(string[32:-1])

def count_unique(ls):
	from collections import Counter
	#Counter(ls).keys() # equals to list(set(words))
	#Counter(ls).values() # counts the elements' frequency
	count_dict = dict(Counter(ls).items())
	return(count_dict)

def split_list(string):
	ls = string.split(",")
	return(ls)

# Importing csv as pd.df
import pandas as pd
import numpy as np
df = pd.read_csv("metadata_presentations.csv")
# transfering to new df_clean
df_clean = df[['URL', 'Relation/s']]
# dropping all courses where Relation is undefined
df_clean = df_clean.dropna()


#Clean up name of courses
url_names_ls = []
for entry in df_clean["URL"]:
	url_names_ls.append(URL_to_name(entry))
df_clean["names"] = url_names_ls

# Adding column "rel_tags" of relations with only string w/ relations
meta_relations_tags = []
for entry in df_clean["Relation/s"]:
	meta_relations_tags.append(strip_string(entry))
df_clean["rel_tags"] = meta_relations_tags




#setting all entries to NaN where relation was incorrectly filled out
df_clean = df_clean.replace("",np.NaN)
#dropping those incorrect relations from df
df_clean = df_clean.dropna()
# dropping "Relation/s" column from list
df_clean = df_clean.drop(["URL","Relation/s"], axis = 1)


#splitting list information and appending to df column
rel_ls = []
for i in df_clean["rel_tags"]:
	rel_ls.append(split_list(i))
df_clean["rel_ls"] = rel_ls


#getting unique count dict and appending to list
ls_dicts = []
for i in df_clean["rel_ls"]:
	ls_dicts.append(count_unique(i))
    
	
# Append ls_dicts list with names of courses
df_clean["rel_dicts"] = ls_dicts
for names,dicts in zip(df_clean["names"],ls_dicts):    
    dicts["ID"]=names
    
#getting rid of useless variables
#del names, dicts, entry, i, meta_relations_tags, url_names_ls, df, rel_ls


df_clean["rel_dicts"] = ls_dicts




"""USE df_clean HERE FOR NEW FORMAT OF OUTPUT JSON"""
#print(df_clean)


#Define empty list to hold new lists
barbaras_list = []


# Empty list that will be appended
final_list = []

#Go through both names and rel lists
for a,b in zip(df_clean["names"],df_clean["rel_ls"]):
    # Eliminating empty lists
    if b[0] != "":
        # calling count unique method, passing rel_list, returns dict with counts
        unique_dict = (count_unique(b))
        # iterating over dict by key(concept) and value(count)
        for key in unique_dict:
            # a = names
            # key = code (concept), unique
            # unique_dict[key] = count of code (key)
            
            #appending empty list with one entry per concept and course w/ appended count
            final_list.append({"ID":a,"code":key,"count":unique_dict[key]})
        




"""
        #For every list entry per course name
        #print(b)
        for x in b:
            #append to list of rel lists
            # x = unique concept entries
            # a = name of course
            # b = list of relations w/ multiple entries
            
            d = {}
            d = {"ID":a, "code":x}
            
            barbaras_list.append(d)
            
"""





#dump to JSON string
import json
json_str = json.dumps(final_list)

#write list to JSON file in same dict
with open('meatadata_presentations.json', 'w') as json_file:
    json.dump(final_list, json_file)




"""PIE CHARTS STANDARD"""


"""

# library
import matplotlib.pyplot as plt
 
# create data
size_of_groups=[12,11,3,30]
 
# Create a pieplot
plt.pie(size_of_groups)
#plt.show()
 
# add a circle at the center
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
 
plt.show()
"""