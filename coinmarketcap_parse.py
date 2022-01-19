from bs4 import BeautifulSoup
import pandas

import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pandas.DataFrame()

#doing the "for" loop for executing the below for
#every file within the folder in quotations:
for file_name in glob.glob("html_files/*.html"):

	#file_name = "html_files/coinmarketcap20210927181055.html"
	scrape_time = os.path.basename((file_name).replace("coinmarketcap", "").replace(".html",""))
	f = open(file_name, "r")
	#file_content = f.read()

	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	tbody = soup.find("tbody")
	currency_rows = tbody.find_all("tr")

	#crypto_row = currency_rows[0]

	#currency_columns = crypto_row.find_all("td")

		#finds bitcoin price at 6:10pm of 09/27/2021, by
		#going to the <tbody></tbody> section of the webpage
		#inside the <tr></tr> tag; within <td></td>, in the
		#fourth column, with the tag <a></a>; bitcoin's tag,
		#BTC, on the other hand is located in the third column,
		#thus (disclaimer: remind yourself to properly identify the
		#tag through specifying its class in curly brackets)...
	#print("Tag:")
	#print(currency_columns[2].find("p", {"class":"sc-1eb5slv-0 gGIpIK coin-item-symbol"}).text)
	#print("Price:")
	#print(currency_columns[3].find("a").text)

		#for finding the market cap (located in the seventh column) you need to further specify that
		#within the "p" there's a "span" tag and then describe its class
	#print("Market Cap:")
	#print(currency_columns[6].find("p").find("span",{"class": "sc-1ow4cwt-1 ieFnWP"}).text)

	#print("Further Info:")
	#print(currency_columns[2].find("a")["href"])

	#now, we create a for loop going through each and every row within
	#<tbody></tbody>...
	#probably, while running the "for" loop, some element within the html
	#file won't match the script, and, thus, it will halt the process

	for crypto_row in currency_rows:
		currency_columns = crypto_row.find_all("td")
		if len(currency_columns)>5:
			#print(scrape_time)
			#print("Tag:")
			currency_name = currency_columns[2].find("p", {"class":"sc-1eb5slv-0 gGIpIK coin-item-symbol"}).text
			#print("Price:")
			currency_price = currency_columns[3].find("a").text.replace("$", "").replace(",", "")

			#for finding the market cap (located in the seventh column) you need to further specify that
			#within the "p" there's a "span" tag and then describe its class
			#print("Market Cap:")
			currency_marketcap = currency_columns[6].find("p").find("span",{"class": "sc-1ow4cwt-1 ieFnWP"}).text.replace("$", "").replace(",", "")

			#print("Further Info:")
			currency_link = currency_columns[2].find("a")["href"]
			#adding the data into the dataframe with "append"
			#and then add all the inputs between "({})"
			df = df.append({
				'time': scrape_time,
				'crypto': currency_name,
				'price': currency_price,
				'marketcap': currency_marketcap,
				'more info': currency_link
				}, ignore_index = True)

df.to_csv("parsed_files/coinmarketcap_dataset.csv")

#making a github repository, first make sure you're inside the correct folder in
#the command prompt ('pwd'), thus, containing the parse and request py files and parsed and html files;
#in the cmd, use 'git init' only once for every project
#uploading has three stages ('untracked', 'added', and 'committed')
#from 'untracked'(first stage) to 'added' use the command 'git add .'
#from 'added' to the 'committed' use the command 'git commit -m "(description of what the files and data actually do)"'
#use 'git status' to check the status of the files
#to finally upload use 'git push origin master'
#when uploading from github's website, we need to generate an ssh key through cmd prompt
#'cd .ssh', then 'ssh-keygen'; you can copy the repository of others into your computer
#use 'git clone' and add the https address