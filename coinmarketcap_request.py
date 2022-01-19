	#importing the library to request the html
import urllib.request
#importing functionalities from windows to python
import os
#importing time-functionalities library
import time
#library to write the current time into filename
import datetime
#to avoid creating the same folder multiple times:

if not os.path.exists("html_files"):
	os.mkdir("html_files")

#identation is mandatory (i.e. the 'shift' space)

#to open file use, now for 5 interations (0 to 4, every 30 seconds, i.e. totalling 150 seconds) the script returns the html script for each of the five:
#instead of indexing with 'i', why not index by the time in which you retrieved the files?
for i in range(5):
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time)
	f = open("html_files/coinmarketcap"+current_time+".html", "wb")
	response = urllib.request.urlopen("http://coinmarketcap.com/")
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(30)

#thus we created a file containing the html file from "http://coinmarketcap.com/"
