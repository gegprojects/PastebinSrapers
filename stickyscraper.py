import os
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests

print("Script to download all pastebin paste and user profile links in a txt file to a user specified directory.\nIf the directory does not exist, then this script will create it")
print("There can only be one pastebin file per line in the links file.\nNo other formatting of the links file is neccesary.\nThis scrapper will not scrape pastebin links that are inside a downloaded pastebin file")

filepath =input("\nEnter a folder path to download pastes at: ")
if not os.path.exists(filepath):
    os.makedirs(filepath)
print("Downloading pastes to: " + filepath)

listpath = input("\nEnter the file path to the links file: ")
if not os.path.exists(listpath):
	print("Path does not exit")
	exit()
print("link path: " + listpath)

file = open(listpath,'r')

while True:
	line = file.readline()
	if not line: 
		break
	#grab user pastes from file
	getUser = line.split("pastebin.com/u/")
	
	if len(getUser) == 2:

		authorStoryIDs = []
		title_count = 0;
		titles = []
		getUserFinal = ''.join(getUser[1].split())

		profile_link = "https://pastebin.com/u/"+getUserFinal
		print(profile_link)

		URL = profile_link
		try:
			content = requests.get(URL)
			soup = BeautifulSoup(content.text, 'html.parser')
			contentTable  = soup.find('table', { "class" : "maintable"})
			rows = contentTable.find_all('a', href=True)
			#titles
			for row in rows:
				authorStoryIDs.append(str(row['href']))
				#print( row.get_text())
				title = row.get_text()
				title = ''.join(e for e in title if e.isalnum())
				titles.append(title)
		except:
			print("Error scrapping " + profile_link)
		if not os.path.exists(filepath+"/"+getUserFinal):
			os.makedirs(filepath+"/"+''.join(getUserFinal.split()))
			
		for i in range(len(authorStoryIDs)):
			print("Attemping to download https://pastebin.com/raw"+authorStoryIDs[i])
			try:
				urllib.request.urlretrieve("https://pastebin.com/raw"+authorStoryIDs[i], filename=filepath+"/"+getUserFinal+"/"+titles[i]+".txt")
				print("Success!")
			except HTTPError as err:
				print("https://pastebin.com/raw"+authorStoryIDs[i]+" gives error code: "+ str(err.code))
	#else if just a regular paste then download in root of download directory
	else:
		getID = line.split("pastebin.com/")
	
		if len(getID) == 2:
			getIDFinal = getID[1][0:8]
			print("Attemping to download https://pastebin.com/raw/"+getIDFinal)
			try:
				urllib.request.urlretrieve("https://pastebin.com/raw/"+getIDFinal, filename=filepath+"/"+getIDFinal+".txt")
				print("Success!")
			except HTTPError as err:
				print("https://pastebin.com/raw/"+getIDFinal+" gives error code: "+ str(err.code))
			