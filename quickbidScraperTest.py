import unittest
from dataTypes.Date import Date
from dataTypes.PageInfo import PageInfo
import requests
import io
from bs4 import BeautifulSoup
from helpers.helpers import *
from quickbidScraper import *

class TestQucikBidScraper(unittest.TestCase):

	def setUp(self):
		self.itemID = 10545
		self.testUrl = "http://www.quickbid.com.tw/items/" + `self.itemID` + "/old"
		data = requests.get(self.testUrl).text 
		self.soup = BeautifulSoup(data)
		
		self.date0 = Date('2014', '01', '02')
		self.date1 = Date('2014', '01', '03')
		self.pageInfo0 = PageInfo(self.date0, 25, 100)
		self.pageInfo1 = PageInfo(self.date0, 30, 120)
		self.pageInfo2 = PageInfo(self.date1, 40, 110)
		self.pageInfoL = [self.pageInfo0, self.pageInfo1, self.pageInfo2]
		
	def test_getUrl(self):
		result = getUrl(123)
		expected = "http://www.quickbid.com.tw/items/123/old"
		self.assertEqual(result, expected)

	def test_itemRange_up(self):
		result = itemRange(1,4)
		expected = [1, 2, 3, 4]
		self.assertEqual(result, expected)
	
	def test_itemRange_down(self):
		result = itemRange(4, 1)
		expected = [4, 3, 2, 1]
		self.assertEqual(result, expected)
		
	def test_itemRange_neg(self):
		with self.assertRaises(ValueError):
			itemRange(-1, -9)
	
	def test_getDate(self):
		result = getDate(self.soup)
		expected = Date('2014', '06', '27')
		self.assertEqual(result, expected)
	
	def test_getBidPrice(self):
		result = int(getBidPrice(self.soup))
		expected = 71
		self.assertEqual(result, expected)
		
	def test_getItemPrice(self):
		result = int(getItemPrice(self.soup))
		expected = 2580
		self.assertEqual(result, expected)
	
	def test_getPageInfo(self):
		result = getPageInfo(self.itemID)
		d = Date('2014', '06', '27')
		bidPrice = 71
		itemPrice = 2580
		expected = PageInfo(d, bidPrice, itemPrice)
		self.assertEqual(result, expected)
	
	def test_scrapeInfo(self):
		result = scrapeInfo('10473', '10472')
		self.assertEqual(len(result), 2)
		self.assertEqual(result[0].date, '2014-06-22')
		self.assertEqual(result[0].bidPrice, 18)
		self.assertEqual(result[0].itemPrice, 1680)
		
	def test_groupByDay(self):
		result = groupByDay(self.pageInfoL)
		self.assertEqual(result[0].bidPrice, 25 + 30)
		self.assertEqual(result[0].itemPrice, 100 + 120)
		self.assertEqual(result[1].bidPrice, 40)
		self.assertEqual(result[1].itemPrice, 110)
		
if __name__ == '__main__':
    unittest.main()