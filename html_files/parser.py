#importing beautifulsoup library, from the library folder ('bs4'):
from bs4 import BeautifulSoup
import requests
#request library allows you to get info from any website:

#accessing the html file and describing what action to take (in this case, just reading 'r'):
with open('coinmarket.html', 'r') as html_file:
		content = html_file.read()
		#using the beautifulsoup library to prettify the html code:
		soup = BeautifulSoup(content, 'lxml')
		table = soup.find('tbody')
		prices = table.find_all('a', class_ = 'cmc-link')
		print(prices)