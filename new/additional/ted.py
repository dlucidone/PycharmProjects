from bs4 import BeautifulSoup
import requests
import re
import sys
from subprocess import call

def getDownloadLink(url):
			print(url)
			request = requests.get(url)
			# remove en for the language list option
			prog = re.compile("http://download.ted.com/talks/[^\"]*480p-en.mp4")
			result = prog.findall(request.text)
			# take the best result (low,medium,high)
			return result[-1]

r = requests.get(sys.argv[2])
soup = BeautifulSoup(r.text)

talks = set()
for talk in soup.find_all("a",{"class":"playlist-talks__play"},href=True):
	    talks.add(talk['href'])


file_des = None
if sys.platform == "win32":
			file_des = open("download.bat","w")
else:
			file_des = open("download.sh", "w")

for url in talks:
			complete_url = "http://www.ted.com" + url
			download_link = getDownloadLink(complete_url)
			download_name = download_link[download_link.rfind("/")+1:]
			file_des.write('wget -c -O \"%s\" \"%s\"\n' % (download_name, download_link))

file_des.close()
if sys.platform == "win32":
			call(["download.bat"])