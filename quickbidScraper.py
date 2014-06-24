# scrape target http://www.quickbid.com.tw/items/itemId/old
from helpers import *
import io
from sys import argv

def scrapeInfo(begin, end):
	infoList = []
	for itemId in itemRange(int(begin), int(end)):
		print "Scraping item " + `itemId` + "..."
		info = getPageInfo(itemId)
		infoList.append(info)
	return infoList

def genReport(pageInfo):
	with io.open('report.txt', 'w', encoding='utf8') as reportFile:
		reportFile.write(u"  Date      Bid Price\tItem Price\n")
		for i in pageInfo: 
			# each bid point equals 25 NT dollars
			reportFile.write(i['time'].display() + ': ' + `int(i['bidPrice'])*25` + '\t\t' + i['itemPrice'] + '\n')

def usage():
	return 'Please enter item ID for the program to scrape \n'\
	       'e.g., \"python.exe quickbidScraper.py 10473 10471\"'

if __name__ == '__main__':
	if (len(argv) < 3):
		print usage()
		exit()
	pageInfo = scrapeInfo(argv[1], argv[2])
	genReport(pageInfo)