import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("station")
args = parser.parse_args()
station = args.station

if station == 'bahari' or 'chamgei' or 'egesa' or 'inooro' or 'mulembe' or 'musyi' or 'muuga' or 'ramogi' or 'sulwe' or 'vuuka' or 'wimwaro':
	blacklist = ["https://rmsradio.co.ke/category/" + station + "-fm/", "https://rmsradio.co.ke/brands/" + station + "-fm/"]

url_list = []
with open(station + '_urls.csv', newline='') as file_in:
	reader = csv.reader(file_in)
	for row in reader:
		url_list.append(row[0])

for count in range(len(url_list)):
	with open('urls/' + station + '_urls'+str(count)+'.csv', newline='') as file_in:
		reader = csv.reader(file_in)
		for row in reader:
			url_list.append(row[0])

newlist = list(dict.fromkeys(url_list))

with open(station + '_urls_dedup.csv', 'w', newline='') as file_out:
			writer = csv.writer(file_out)
			for url in newlist:
				if url not in blacklist:
					writer.writerow([url])