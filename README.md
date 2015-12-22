QuickbidScraper
=================================

A web scraper for scraping [QuickBid](http://www.quickbid.com.tw/)'s data(including item price, bid price, and date) using BeautifulSoup.

#### Usage

`python quickbidScraper.py 10602 10500` for scraping the data from
http://www.quickbid.com.tw/items/10602/old
to
http://www.quickbid.com.tw/items/10500/old


Because the program accumulates the prices in each day, please make sure that your input parameters cover the whole day.


#### 用法
例如當你想抓http://www.quickbid.com.tw/items/10602/old 到 http://www.quickbid.com.tw/items/10500/old
的紀錄時，你可以輸入`python quickbidScraper.py 10602 10500`

由於程式會把一天內價格累加起來，所以請確保輸入的參數剛好能抓到一整天的範圍。
