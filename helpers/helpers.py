# requests can be installed by typing "pip install requests" in command line
# BeautifulSoup(bs4) can be downloaded from http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/
# matplotlib(pylab) can be downloaded from http://matplotlib.org/
from bs4 import BeautifulSoup
from dataTypes.Date import Date
from dataTypes.PageInfo import PageInfo
from pylab import *
import requests
import io
import re
import matplotlib.pyplot as plt

def getUrl(itemId):
	return "http://www.quickbid.com.tw/items/" + `itemId` + "/old"

def itemRange(start, end):
	if (start < 0 or end < 0):
		raise ValueError("item IDs must be positive")

	if start <= end:
		return range(start, end + 1) # include end
	else:
		tmp = range(end, start + 1)
		tmp.reverse()
		return tmp

def getDate(soup):
	# use print soup.encode('cp950') if you want to view the value of soup.
	timeText = soup.find('p').text
	year = timeText[6:10]
	month = timeText[11:13]
	day = timeText[14:16]
	return Date(year, month, day)

def getBidPrice(soup):
	return soup.find("span", { "id" : "bid_item_bid_price" }).text
	
def getItemPrice(soup):
	return soup.find("span", { "id" : "bid_item_price" }).text
	
def getPageInfo(itemId):
	print "Scraping item " + `itemId` + "..."
	targetUrl = getUrl(itemId)
	data = requests.get(targetUrl).text # type(data) == 'unicode'
	soup = BeautifulSoup(data)			# type(soup) == 'str'
	
	date = getDate(soup)
	bidPrice = int(getBidPrice(soup))
	itemPrice = int(getItemPrice(soup))
	pageInfo = PageInfo(date, bidPrice, itemPrice)
	return pageInfo

def outputTextData(infoByDay, begin, end):
	with io.open('report_' + begin + '_' + end + '.txt', 'w', encoding='utf8') as reportFile:
		reportFile.write(u"  Date      Bid Price\tItem Price\n")
		for i in infoByDay: 
			# each bid point equals 25 NT dollars
			reportFile.write(i.date.display() + ': ' + `int(i.bidPrice)*25` + '\t\t' + `i.itemPrice` + '\n')

def groupByDay(pageInfo):
	pageInfo.sort()
	infoByDay = []
	infoByDay.append(pageInfo[0])
	i = 1
	j = 0
	while(i < len(pageInfo)):
		tmp = pageInfo[i]
		if (infoByDay[j].date == tmp.date):
			infoByDay[j].bidPrice += int(tmp.bidPrice)
			infoByDay[j].itemPrice += int(tmp.itemPrice)
		else: # next day's data
			infoByDay.append(tmp)
			j += 1
		i += 1
	return infoByDay
			
def plotGraph(infoByDay):
	x = range(0, len(infoByDay))
	yBid = []
	for i in infoByDay:
		yBid.append(i.bidPrice*25)
	yItem = []
	for i in infoByDay:
		yItem.append(i.itemPrice)	
	
	
	fig, ax = plt.subplots()
	ax.plot(x, yBid, 'k', label='Bid Price')
	ax.plot(x, yItem, 'k:', label='Item Price')
	legend = ax.legend(loc='upper left', shadow=True)
	xlabel('Time (day)')
	ylabel('Bid Price')
	ax.set_title('Bid Price v.s. Item Price')
	grid(True)
	savefig("BidVSItem.png")
	plt.show()
	