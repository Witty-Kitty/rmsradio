import argparse
import csv
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("station")
args = parser.parse_args()
station = args.station

if station == 'mulembe':
	urls = ['https://rmsradio.co.ke/brands/mulembe-fm/']
if station == 'sulwe':
	urls = ['https://rmsradio.co.ke/brands/sulwe-fm/']
if station == 'vuuka':
	urls = ['https://rmsradio.co.ke/brands/vuuka-fm/']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def url_parser(url):
	r = requests.get(url, headers=headers)
	page_content = r.content

	soup = BeautifulSoup(page_content, features="xml")

	urls = []
	for a in soup.findAll('a', href=True):
		if "-" in a["href"]:
			urls.append(a['href'])

	return urls

with open(station + '_urls.csv', newline='') as file_in:
	reader = csv.reader(file_in)
	count = 0
	for row in reader:
		with open('urls/' + station + '_urls'+str(count)+'.csv', 'w', newline='') as file_out:
			writer = csv.writer(file_out)
			parsed_res = url_parser(row[0])
			for j in parsed_res:
				writer.writerow([j])
		count += 1
	
# for url in urls:
# 	with open(station + '_urls.csv', 'w', newline='') as file_out:
# 		writer = csv.writer(file_out)
# 		parsed_res = url_parser(url)
# 		for j in parsed_res:
# 			writer.writerow([j])

		