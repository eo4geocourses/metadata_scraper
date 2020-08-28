echo "running scraper...";
python3 /home/simon/Git/metadata_scraper/raw_code.py;
sleep 5;
echo "scraping and writing to csvcomplete";
echo "commiting to GitHub and writing to log file"
echo "Run and push to repo successful" >> /home/simon/Git/metadata_scraper/log_file.txt;
date >>/home/simon/Git/metadata_scraper/log_file.txt;
echo "_______________________________" >> /home/simon/Git/metadata_scraper/log_file.txt;
git status;
sleep 2;
git add *;
sleep 2;
git commit -m "automatic shell commit";
sleep 2;
git push origin master;
sleep 5;
echo "Run finished and pushed to Repo";
