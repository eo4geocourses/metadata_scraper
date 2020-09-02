cd /home/simon/Git/metadata_scraper/;
echo "running scraper...";
python3 /home/simon/Git/metadata_scraper/raw_code.py;
sleep 5;
echo "scraping and writing to csvcomplete";
echo "commiting to GitHub and writ ing to log file"
echo "Run and push to repo successful" >> /home/simon/Git/metadata_scraper/log_file.txt;
date >>/home/simon/Git/metadata_scraper/log_file.txt;
echo "_______________________________" >> /home/simon/Git/metadata_scraper/log_file.txt;
sleep 10;
git status;
sleep 2;
git add *;
sleep 2;
git commit -m "automatic shell commit" >> /home/simon/Git/metadata_scraper/log_file.txt;
sleep 2;
git push origin master;
sleep 2;
echo "Run finished and pushed to Repo";
