# scrape target http://www.quickbid.com.tw/items/itemId/old
import argparse
from helpers.helpers import *
from sys import argv
from dataTypes.Date import Date
from dataTypes.PageInfo import PageInfo
from multiprocessing import Pool

def scrapeInfo(begin, end):
	pool = Pool(processes=4)
	infoList = pool.map(getPageInfo, itemRange(int(begin), int(end)))
	infoList = [x for x in infoList if x is not None] # filter out none values
	return infoList

def genReport(pageInfo, begin, end):
	assert type(pageInfo) == list
	assert type(pageInfo[0]) == PageInfo

	infoByDay = groupByDay(pageInfo)
	outputTextData(infoByDay, begin, end)
	plotGraph(infoByDay)

def main(begin, end):
	pageInfo = scrapeInfo(begin, end)
	genReport(pageInfo, begin, end)

def initArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("beginId", type=int, help="the begin ID of the range of items you want to fetch")
    parser.add_argument("endId", type=int, help="the end ID of the range of items you want to fetch")
    return parser.parse_args()

if __name__ == '__main__':
    args = initArgs()
    main(args.beginId, args.endId)