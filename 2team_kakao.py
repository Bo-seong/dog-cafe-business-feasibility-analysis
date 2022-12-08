import re
import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import insertDB

import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
list=[]


url = "https://map.kakao.com/"

#현재파일에 있는 크롬 드라이버를 가져와서 열기
options = webdriver.ChromeOptions() # 크롬 브라우저 옵션
# options.add_argument('headless') # 브라우저 안 띄우기
options.add_argument('lang=ko_KR') #  KR 언어


options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
driver = webdriver.Chrome(options=options)


# 1. 카카오 지도로 이동
driver.get(url)
searchloc = input("찾고싶은 검색어 : ")


#2. 음식점 입력 후 찾기 버튼 클릭 xpath활용
search_area = driver.find_element(By.XPATH,'//*[@id="search.keyword.query"]') # 검색 창
search_area.send_keys("'"+searchloc+"'")  # 검색어 입력
driver.find_element(By.XPATH,'//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  # Enter로 검색

time.sleep(2)
#3 장소 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER) 

title = []
address = []

def storeNamePrint():
    

    time.sleep(3)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    nameEl = soup.select('#info\.search\.place\.list > li > div.head_item.clickArea > strong > a.link_name')
    addressEl = soup.select('#info\.search\.place\.list > li > div.info_item > div.addr > p')

    for a in nameEl:
        # print(a.text)
        title.append(a.text)
        print(title)
        

    for idx, p in enumerate(addressEl):
        if idx % 2 == 1:
            continue
        address.append(' '.join(p.attrs['title'].split()[:2])) #광주광역시 광산구
        p.attrs['title'].split(maxsplit=1)
        print(address)



   


#페이지 수를 넘기면서 크롤링
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
page = 1
page2 = 1
print(soup.select('#info\.search\.place\.cnt'))
maxPage = math.ceil(int(soup.select_one('#info\.search\.place\.cnt').text) / 15)
print(maxPage)

for i in range(maxPage):  

    #페이지 넘어가며 출력 
    try:
        print("page:",page2)

        if i > 0:
            driver.find_element(By.XPATH,f'//*[@id="info.search.page.no{page}"]').send_keys(Keys.ENTER)           
        storeNamePrint()

        if page % 5 == 0:
            driver.find_element(By.XPATH,'//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page = 0

        page+=1
        page2+= 1
    except Exception as e:
        print("오류", e)
        break

print(len(title))

list_name_addr = []
for i in range(len(title)):
    lis = []
    lis.append("동물미용업")
    lis.append(address[i])
    lis.append(title[i])
    list_name_addr.append(lis)

print(list_name_addr)

import insertDB

conDB = insertDB.connectDB('root', '1234')
query = "INSERT INTO crawling.analysis_element (category, gu, element_name) VALUES (%s, %s, %s)"
conDB.insert_many_sql(query, list_name_addr)
conDB.close_db()
print("완료")
