# requests can be installed by typing "pip install requests" in command line
# BeautifulSoup(bs4) can be downloaded from http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/
from bs4 import BeautifulSoup
from Date import Date
import requests

def getUrl(itemId):
	return "http://www.quickbid.com.tw/items/" + `itemId` + "/old"

def itemRange(start, end):
	if (start < 0 or end < 0):
		print "Item ID can't be negative."
		exit()
	if start <= end:
		return range(start, end + 1) # include end
	else:
		tmp = range(end, start + 1)
		tmp.reverse()
		return tmp

def getDate(soup):
	# use print soup.encode('cp950') if you want to view the value of soup.
	timeText = soup.find("div", { "class" : "item_original_end_at" }).text
	year = timeText[5:9]
	month = timeText[10:12]
	day = timeText[13:15]
	return Date(year, month, day)

def getBidPrice(soup):
	return soup.find("span", { "id" : "bid_item_bid_price" }).text
	
def getItemPrice(soup):
	return soup.find("span", { "id" : "bid_item_price" }).text

def getPageInfo(itemId):
	targetUrl = getUrl(itemId)
	data = requests.get(targetUrl).text # type(data) == 'unicode'
	soup = BeautifulSoup(data)			# type(soup) == 'str'
	info = {}
	info['time'] = getDate(soup)
	info['bidPrice'] = getBidPrice(soup)
	info['itemPrice'] = getItemPrice(soup)
	return info
	