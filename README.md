# Metadata Scraper  
Check out the **automatically** [updated table](https://eo4geocourses.github.io/metadata_scraper/).  
To add, remove or rename Repositories, open and edit the **repo_links.csv** file.


This little script takes the EO4GEO course list and extracts the metadata for each course. The CSV file, table and index.html file are **automatically updated every night at 03:00am.**  The table this script produces can be used to assess any updates to which courses have already been changed from the template and which remain unchanged.
  
The index.html file contains a modified table of the csv in order to more quickly show which information is present. The extracted information itself is written into the metadata_presentations.csv file.
  
  
The following information is extracted per course:  

| Name of column        | Data Type           | Info  |
| ------------- |:-------------:| -----:|
| URL      | string | URL of hosted presentation |
| Public/Private  | Boolean String ("Public" or "Private")      |   Wether the presentation is currently accesible for the public or not |
| Added Metadata? | Boolean String ("True"/"False")      |   Wether the presentation contain Metadata or not |
|Title|String|Title of Presentation|
|Creator|List|List of credited creators|
|Publisher|String|Name of publishing institution|
|Abstract|String|Abstract of Presentation - Summary|
|Description|String|Specifying Learning outcomes|
|Language|String|ISO 639-1 Codes for languages, e.g. "EN" for english|
|Type|String|Specifying type of material, e.g. "teaching material","self-learning material", "webinar"|
|EQF|String|European Qualifications Framework code|
|Licnese|String|Link to license agreement, most commonly CC-BY-SA|
|Size ir Duration|String|Timeframe for coursework|
|Format|String|Presentation format, usually "html"|
|Contributors|List|List of contributors to learning material|
|Data created|YYYY-MM-DD|creation date of course material|
|Relation/s|list|containing string "eo4geo:" per entry in list to define the namespace and then the according BoK Code|
|BoK Links|list|permalinks to according BoK pages extracted from Relation/s tag|
|banner_link|string|Link to image used for displaying course tiles. Stored on Server, format: https://eo4geo.sbg.ac.at/banner/*course_title*/.png|
|graph_link|string|link to concept charts|
|Repo_URL|string|Lin to GitHub repository (not hosted pages link)|
    
## Documentation  
The Documentation can be found in the according folder. The documentation includes instructions on how to add new courses and how to set up the scraper. In case of questions, contact simon@donike.net.
