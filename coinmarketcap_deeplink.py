import urllib.request
import os
import time
import pandas

if not os.path.exists("deeplink_files"):
	os.mkdir("deeplink_files")

df = pandas.read_csv("parsed_files/coinmarketcap_dataset.csv")

print(df)

