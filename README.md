# PastebinSrappers
Two scripts for scrapping pastebin without needing the api

pastebin_profile_scraper.py will scrape all public pastes from a user profile. 
It will prompt for a directory to dowload the files in and the url of the pastebin profile i.e. https://pastebin/u/anon
It scrapes all the pastes from the profile and downloads them to the specified directory. Titles are saved.

stickyscraper.py scrapes all pastebin direct links and user profile links in a user provided txt file. It will scrape any included user profile links just like the profile scrapper. It will not scrape pastebin links inside of a downloaded paste file, so ensure that you also scrape/save the nested pastebin links seperatley when using the script. Do not put pastebin.com/raw/ links in the input text file, the script automatically converts them. Direct pastebin links will have their 8 character pastebin id as a title so formatting is needed if you want to know what each txt file is. 

Both scripts will create a new directory pointing to the user's inputed folder path if the directory the user provides does not exist.
Both scripts will create a subdirectory with the pastebin profile name and download the files to the subdirectory if a user profile is inputted

Both scripts require requests, BeautifulSoup4, urllib, and os packages in your python environment to run. To run, open a terminal in the same directory the scripts are downloaded at. Run python3 scriptname.py and follow the script's prompts.

Not tested on windows. 
Optimizations coming. I can easily double the speed and reduce the code clutter.
