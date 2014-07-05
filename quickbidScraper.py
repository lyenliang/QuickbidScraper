# scrape target http://www.quickbid.com.tw/items/itemId/old
from helpers.helpers import *
from sys import argv
from dataTypes.Date import Date
from dataTypes.PageInfo import PageInfo
from multiprocessing import Pool

def scrapeInfo(begin, end):
	pool = Pool(processes=4)
	infoList = pool.map(getPageInfo, itemRange(int(begin), int(end)))
	return infoList

def genReport(pageInfo, begin, end):
	assert type(pageInfo) == list
	assert type(pageInfo[0]) == PageInfo
	
	infoByDay = groupByDay(pageInfo)
	outputTextData(infoByDay, begin, end)
	plotGraph(infoByDay)
	
def usage():
	return 'Please enter item ID for the program to scrape \n'\
	       'e.g., \"python.exe quickbidScraper.py 10473 10471\"'

def main(begin, end):
	pageInfo = scrapeInfo(begin, end)
	genReport(pageInfo, begin, end)
   
if __name__ == '__main__':
	if (len(argv) < 3):
		print usage()
		exit()
	main(argv[1], argv[2])