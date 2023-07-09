import re
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import matplotlib.pyplot as plt
service = Service(executable_path='C:\\Users\\Абдул\\PycharmProjects\\selenium_practice\\chromedriver\\yandexdriver.exe')
driver = webdriver.Chrome(service=service)

url = "http://www.sberbank.ru/ru/person"
sber_urls = []
another_urls= []
netlocs = ['www.sberbank.ru','www.sberbank.com', 'sberbank.com', 'sberbank.ru']
try:
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for link in soup.findAll('a'):
        if link.get('href')[:1] == 'h':
            if urlparse(link.get('href')).netloc in netlocs:
                sber_urls.append(link.get('href'))
            else:
                another_urls.append(link.get('href'))
    CLEANR = re.compile('<.*?>')
    print(re.sub(CLEANR, '', soup.text))
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
    # print(len(another_urls))
    # fig, ax = plt.subplots()
    # bar_labels = ['Сбербанк', 'Другие']
    # bar_colors = ['tab:red', 'tab:blue']
    # ax.bar(['URL в доменной зоне сбербанка', 'Другие домены'], [len(sber_urls), len(another_urls)], label=bar_labels, color = bar_colors)
    # ax.set_ylabel('Количество url-путей')
    # ax.set_title('Соотнощение путей')
    # ax.legend(title='URLS')
    # plt.show()

