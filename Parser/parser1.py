import requests
from bs4 import BeautifulSoup as BS
def pars(txt):
    dol = 'https://aliexpress.ru/wholesale?SearchText=' + txt
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    full_page = requests.get(dol,headers=headers)
    soup = BS(full_page.content, 'html.parser')
    convert = soup.findAll('div', {"class":'product-snippet_ProductSnippet__name__lido9p'})


    return convert    


#это для авито 
# import requests
# import os
# from selenium import webdriver
# from selenium.webdriver.common.service import Service


# BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# CHROME_DRIVER_PATH = os.path.join(BASE_PATH, "chromedriver.exe")
# CHROME_SERVICE = Service(CHROME_DRIVER_PATH)


# class AvitoParsing:
#     def __init__(self, driver: webdriver.Chrome):
#         self.driver = driver

#     def run(self):
#         self._get_to_avito()

#     def _get_to_avito(self):
#         self.driver.get("https://avito.ru/")


# def main():
#     webdriver_chrome = webdriver.Chrome(service=CHROME_SERVICE)
#     ap = AvitoParsing(webdriver_chrome)
#     ap.run()