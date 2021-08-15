# Documentation  
This file explains the workings of the metadata scraping process.

## Which Metadata is Extracted?
The metadata is extracted from the DublinCore-Type annotations within the HTML code of the presentations' web pages. The following information is extracted in the following order:  

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
|License|String|Link to license agreement, most commonly CC-BY-SA|
|Size ir Duration|String|Timeframe for coursework|
|Format|String|Presentation format, usually "html"|
|Contributors|List|List of contributors to learning material|
|Data created|YYYY-MM-DD|creation date of course material|
|Relation/s|list|containing string "eo4geo:" per entry in list to define the namespace and then the according BoK Code|
|BoK Links|list|permalinks to according BoK pages extracted from Relation/s tag|
|banner_link|string|Link to image used for displaying course tiles. Stored on Server, format: https://eo4geo.sbg.ac.at/banner/*course_title*.png|
|graph_link|string|link to concept charts|
|Repo_URL|string|Lin to GitHub repository (not hosted pages link)|

## Structure  

![Structure Image](/documentation/scraper_schema.png?raw=True "Schema")

The process of scraping the metadata consits of 4 files:
1. **run_scraper_commit_log.sh**
  * Bash file, used to start the whole process. It runs the python file, writes the log file and commits to GitHub.
2. **raw_code.py**
  * Containing all the python code. Running this file starts the scraping process, including the creation of output files.
3. ** graphs/graphs.py**
  * Python program being run by the bash script, creating a JSON file that contains the metadata information in a specific format. This file is being used to create interactive graphs.
4. **repo_links.txt**
  * Text file, containing a list of all presentation links (GitHub Pages links). This file is read as an input for the scraping proces of the python file.
  
The scraping process creates the following outputs:
1. **meatadata_presentations.csv**
  * Output table, containing the extracted metadata from the html files of the input presentation links.
2. **index.html**
  * HTML file that is automatically created in order to visualize the same information as the metadata_presentation.csv file as a webpage in GitHub Pages
3. **graphs/metadata_presentations.json**
  * JOSN, holding Information on content type tags. It is used to create visualizations on an external webpage.
4. **log_file.txt**
  * automatically logs infomration on when and how the program was run. Does not contain a delete function, so currently it is growing at a rate of 300kb/year.

## Commiting to GitHub
In order to commit to GitHub, the local repository must be properly set up. this includes the creation of a SSH key, since authentication via username/password is not supported any longer via the command line. If properly set up, running the bash file will first finish all the processing and saving, followed by commiting the local changes to the repository. 

## Cronjob
The run_scraper_comit_log.sh file should be ran periodically (nightly or weekly). This should be accomplished via a cronjob, with the following settings (for nightly):  
0 3 * * * /absloutePathtoBash /abolutePathTorepo/run_scraper_commit_log.sh

## Instructions to add a new Course
1. Add link to hosted (GitHub Pages) presentation to repo_links.txt
2. Upload representative picture in .png file format at via SFTP at the server in the folder 'banner'. File name must be identical to repository name of course.
3. Check the next day if the scraper worked, alternatively manually run the scaper by running the shell file with bash.

## How to set up the scraper
1. Pull this rreository onto the server
2. Authenticate on GitHub via SSH key
3. Edit bash script to change file paths to the correct python file locations (No need to change paths internally in the scripts since they are all relative)
4. Set up cronjob as instructed in "Commiting to GitHub"
