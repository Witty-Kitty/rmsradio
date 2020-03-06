import argparse
import csv
import datetime
import re
import requests
from bs4 import BeautifulSoup
from url_parser import url_parser

parser = argparse.ArgumentParser()
parser.add_argument("station")
args = parser.parse_args()
station = args.station
d = datetime.datetime.today()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def content_extraction(url):
	r = requests.get(url, headers=headers)
	page_content = r.content

	soup = BeautifulSoup(page_content, features="xml")
	title = soup.find("title").contents[0].split("-")[0].strip()
	paragraph = soup.find("p").contents
	paragraph = ''.join(str(e) for e in paragraph)
	clean = re.compile('<.*?>')
	paragraph = re.sub(clean, '', paragraph)
	entry_date = soup.find("span", {"class": "entry-date"}).contents[0].split(":", 1)[1].strip()

	return [title, paragraph, entry_date, url]

with open(station + str(d.year) + '-' + str(d.month) + '-' + str(d.day) + '.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	with open(station + '_urls_dedup.csv', newline='') as file_in:
		reader = csv.reader(file_in)
		for row in reader:
			writer.writerow(content_extraction(row[0]))