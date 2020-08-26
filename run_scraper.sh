echo "running scraper...";
python3 raw_code.py;
sleep 5;
echo "scraping and writing to csvcomplete";
echo "commiting to GitHub"
git status;
sleep 2;
git add *;
slep 2;
git commit -m "automatic shell commit";
sleep 2;
git push origin master;
sleep 5;
echo "Run finished and pushed to Repo";
