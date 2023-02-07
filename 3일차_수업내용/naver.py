# naver.com 사이트 제어 및 데이터 수집하기
# 모듈 불러오기
from selenium import webdriver
import chromedriver_autoinstaller as ca
import time

query_text = '가을여행'

# 웹사이트 접속하기
driver = webdriver.Chrome(ca.install())

address = "https://search.naver.com/search.naver?where=blog&sm=tab_viw.blog&query="
driver.get(address + query_text + '&nso=')
time.sleep(2) ; driver.maximize_window()

# 웹사이트 닫기
time.sleep(5) ; driver.close()
