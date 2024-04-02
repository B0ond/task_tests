from typing import Any

import scrapy
from selenium import webdriver
import pandas as pd

class OzonSpider(scrapy.Spider):
    name = 'ozon'
    allowed_domains = ['ozon.ru']
    start_urls = ['https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating']

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        phones = self.driver.find_elements_by_css_selector('.tile-card__title')
        for phone in phones[:100]:
            link = phone.find_element_by_css_selector('a').get_attribute('href')
            yield scrapy.Request(url=link, callback=self.parse_phone)

    def parse_phone(self, response):
        self.driver.get(response.url)
        try:
            os_version = self.driver.find_element_by_xpath(
                "//div[contains(text(), 'Версия iOS') or contains(text(), 'Версия OS')]/following-sibling::div").text
            yield {'OS version': os_version}
        except Exception as e:
            print(f"Error: {e}")
            yield {'OS version': 'Нет информации'}

    def closed(self, reason):
        self.driver.quit()

# # Запуск паука
# scrapy crawl ozon -o phones.csv

# Чтение данных из CSV файла
data = pd.read_csv('phones.csv')

# Построение распределения
os_distribution = data['OS version'].value_counts().sort_index(ascending=False)
print(os_distribution)
