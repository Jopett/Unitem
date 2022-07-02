import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

# Query
plusUrl = "아이폰"
# bunjang newest items
baseUrl = "https://m.bunjang.co.kr/search/products?order=date&q="

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
url = baseUrl + plusUrl
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html , "html.parser")

items = soup.select('#root > div > div > div:nth-child(4) > div > div.sc-bbkauy.ckBMEw > div > div')
# name price imgUrl itemUrl location
for i in items:
    title =  i.select_one('a > div.sc-cooIXK.eRiVOY > div.sc-fcdeBU.iVCsji').text
    itemUrl =  i.select_one('a')["href"]
    imgUrl =  i.select_one('a > div.sc-kxynE.hRMUEo > img')["src"]
    price = i.select_one('a > div.sc-cooIXK.eRiVOY > div.sc-RcBXQ.CFZut > div:nth-child(1)').text
    location =  i.select_one('a > div.sc-kZmsYB.eylVEY').text
    ## SQL Insert
    ##

