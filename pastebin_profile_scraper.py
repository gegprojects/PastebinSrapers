import os
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests


print("Script to get all public pastes from a pastebin user's .html info")
filepath =input("\nEnter a file path for downloaded pastes: ")
if not os.path.exists(filepath):
    os.makedirs(filepath)

print("Downloading pastes to: " + filepath)

linkpath = input("\nEnter the url to the pastebin user profile: ")

getUser = linkpath.split("pastebin.com/u/")

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
else:
	print("Bad link, try again")		