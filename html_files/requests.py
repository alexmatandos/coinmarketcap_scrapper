from bs4 import BeautifulSoup
import requests

html_text = requests.get('http://coinmarketcap.com/').text
#it will only print the request status, thus, add '.text' at end above!
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('tbody')
print(table)