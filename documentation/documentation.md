# Documentation  
This file explains the workings of the metadata scraping process.
## Structure  
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
  * automatically logs infomration on when and how the program was run. Does not contain a delete function, so currently it is growing day by day.
