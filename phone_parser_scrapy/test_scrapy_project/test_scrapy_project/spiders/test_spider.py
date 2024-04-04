import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OzonSpider(scrapy.Spider):
    name = 'ozon_spider'
    allowed_domains = ['ozon.ru']
    start_urls = ['https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating']

    def __init__(self):
        self.driver = webdriver.Chrome()  # Укажите путь к драйверу Chrome, если необходимо

    def parse(self, response):
        self.driver.get(response.url)

        # Ждем загрузки элементов страницы
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".widget-search-result-container"))
        )

        # Получаем HTML-код страницы через Selenium
        html = self.driver.page_source
        selector = Selector(text=html)

        # Извлекаем ссылки на страницы смартфонов
        smartphone_links = selector.css(".tile-hover-target i8t t8i::attr(href)").getall()

        for link in smartphone_links[:100]:
            # Переходим на страницу смартфона
            self.driver.get(response.urljoin(link))

            # Ждем загрузки информации о смартфоне
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "kl6"))
            )

            # Получаем HTML-код страницы смартфона через Selenium
            smartphone_html = self.driver.page_source
            smartphone_selector = Selector(text=smartphone_html)

            # Извлекаем информацию об операционной системе
            os_info = smartphone_selector.css("kl6 .e8r6::text").get()

            yield {
                'os': os_info
            }

        # Переходим на следующую страницу результатов поиска, если есть
        next_page = selector.css(".ui-k6 a.ui-k6::attr(href)").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def closed(self, reason):
        self.driver.quit()




# import scrapy
#
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
#
#
# class personSpider(CrawlSpider):
#     name = 'test_spider'
#     start_urls = ['https://minzdrav.tatarstan.ru/structure.htm']
#
#     rules = (
#         Rule(LinkExtractor(allow=('structure/\d+')), callback='parse_items')
#     )
#
#     def parse_items(self, response):
#         division = response.css('div.content__main h1.h1::text').get(default='').strip()
#         department = response.css('div.col-sm-4 div.person__dep::text').getall()
#         department = ' '.join(department).strip() if department else ''
#         name = response.css('div.col-sm-5 div.person__name::text').getall()
#         name = ' '.join(name).strip().split(' ') if name else []
#         last_name, first_name, patronymic = name + [''] * (3 - len(name))
#         post = response.css('div.col-sm-5 div.person__post::text').getall()
#         post = ' '.join(post).strip() if post else ''
#         phone_number = response.css('div.contacts__group div.contacts__data::text').getall()
#         phone_number = ' '.join(phone_number).strip() if phone_number else ''
#
#         yield {
#             'division': division,
#             'department': department,
#             'last_name': last_name,
#             'first_name': first_name,
#             'patronymic': patronymic,
#             'post': post,
#             'phone_number': phone_number,
#         }