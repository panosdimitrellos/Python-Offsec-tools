#!/usr/bin/python3
import requests

target_IP = ""
URL = "http://target_IP/"
urlList = []
isFollowed = {}

def checkUrlList(URL):
   if URL in urlList:
       return True
   else:
       return False

def isFollowedCheck(URL):
   for entry in isFollowed.keys():
       if URL != entry:
           return False
       else:
           if isFollowed[URL] == "yes":
               return True
           else:
               return False

urlList.append(URL)

for URL in urlList:
   if isFollowedCheck(URL) != True:
       page = requests.get(URL)
       isFollowed[URL] = "yes"

       start = "http"
       for line in page.text.split("\n"):
           if "http" in line:
               if target_IP in line:
                   if "\">" in line:
                       end = "\">"
                   else:
                       end = "\" "
                   sliced = line[line.index(start):line.index(end)]
                   if "\"" in sliced:
                       end = "\""
                       parsedURL = sliced[sliced.index(start):sliced.index(end)]
                   else:
                       parsedURL = sliced
                   if checkUrlList(parsedURL) == False:
                       urlList.append(parsedURL)
                       isFollowed[parsedURL] = "no"

for URL in urlList:
   print(URL)

''' 
# --------> Second Way with BeautifulSoup <----------

import urllib3
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "your_url"
directory = "/your_direcory_to_start"
page = urlopen(url+directory).read()
soup = BeautifulSoup(page, features="html.parser")

all_urls = []

for link in soup.find_all('a'):
    links=link.get('href')
    all_urls.append(links)

for t_url in all_urls:
    print("Content of: "+t_url)
    response = requests.get(url+t_url)
    print(response.text)
'''
