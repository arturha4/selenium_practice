# -*- coding: cp1251 -*-
import json
import time
import pandas as pd
from pandas import json_normalize
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

domain = 'https://www.avito.ru'
service = Service(
    executable_path='C:\\Users\\Абдул\\PycharmProjects\\selenium_practice\\chromedriver\\yandexdriver.exe')

driver = uc.Chrome(service=service)
driver.get(
    'https://www.avito.ru/ekaterinburg/avtomobili/s_probegom/vaz_lada-ASgBAQICAUSGFMjmAQFA4LYNFMaZKA?f=ASgBAQICAkSGFMjmAfrwD~i79wIBQOC2DRTGmSg&radius=200&s=104&searchRadius=200')
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
cars_json = {
    "cars": [

    ]
}
cars = driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
for car in cars:
    name = car.find_element(By.CSS_SELECTOR,"[itemprop='name']").text
    url = domain + car.find_element(By.CSS_SELECTOR,"[itemprop='url']").get_attribute('href')
    try:
        description = car.find_element(By.CSS_SELECTOR,"[style='-webkit-line-clamp:4']").text
    except:
        print(f"error for {name}")
    finally:
        cars_json["cars"].append({"title":name, "url":url, "description": description})
res = json_normalize(cars_json["cars"])
res.to_csv('cars.csv')
#
# driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button/nextPage']").click()
# for link in soup.findAll('a', {"class": "iva-item-sliderLink-uLz1v"}):
#     cars_json["cars"].append({"title": link.get('title'), "link": link.get('href')})
# for car in cars_json["cars"]:
#     time.sleep(15)
#     driver.get(domain+car["link"])

#     print(driver.title)
# res = soup.findAll("meta", {"itemprop":"description"})
# print(res)
# res = json_normalize(cars_json["cars"])
driver.close()
driver.quit()
# title, href
