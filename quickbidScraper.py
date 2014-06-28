# scrape target http://www.quickbid.com.tw/items/itemId/old
from helpers.helpers import *
from sys import argv
from dataTypes.Date import Date
from dataTypes.PageInfo import PageInfo

def scrapeInfo(begin, end):
	infoList = []
	for itemId in itemRange(int(begin), int(end)):
		print "Scraping item " + `itemId` + "..."
		info = getPageInfo(itemId)
		infoList.append(info)
	return infoList

def genReport(pageInfo):
	assert type(pageInfo) == list
	assert type(pageInfo[0]) == PageInfo
	
	infoByDay = groupByDay(pageInfo)
	outputTextData(infoByDay)
	plotGraph(infoByDay)
	
def usage():
	return 'Please enter item ID for the program to scrape \n'\
	       'e.g., \"python.exe quickbidScraper.py 10473 10471\"'

def main(begin, end):
	pageInfo = scrapeInfo(begin, end)
	genReport(pageInfo)
   
if __name__ == '__main__':
	if (len(argv) < 3):
		print usage()
		exit()
	main(argv[1], argv[2])