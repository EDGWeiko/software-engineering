from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
import time
import mysql.connector



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

all_url=[]

for i in range(1,2):
    driver.get(f'http://dbxinshipin.sy.foodvip.net/home/index/index.html?num=30&catid=0&title=&ldtitle=&&page={i}')
    driver.maximize_window()
    html = driver.page_source
    bs = etree.HTML(html)
    lis = bs.xpath('/html/body/div/div/table/tbody/tr')
    for link in lis:
        url = link.xpath('./td[7]/a/@href')[0]
        url1 = 'http://dbxinshipin.sy.foodvip.net/' + url
        all_url += [url1]
        time.sleep(1)
    time.sleep(2)

for i in all_url:
    driver.get(i)
    time.sleep(2)
    html = driver.page_source
    bs = etree.HTML(html)
    lis = bs.xpath('/html/body/div/div/table/tbody')
    for link in lis:
        name = link.xpath('./tr[2]/td[2]/text()')[0]
        english_name = link.xpath('./tr[3]/td[2]/text()')[0]
        print(name,english_name)