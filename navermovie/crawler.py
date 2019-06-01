from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

class Navermovie:
    def __init__(self, url):
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        soup =BeautifulSoup(driver.page_source, 'html.parser')
        # 한 줄 코딩 driver. 컨트롤 스페이스
        print(soup)
        