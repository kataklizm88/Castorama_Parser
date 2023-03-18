import scrapy
from scrapy.http import HtmlResponse
from items import CastoramaItem
from scrapy.loader import ItemLoader


URL = 'https://www.castorama.ru'


class CastoPSpider(scrapy.Spider):
    name = "casto_p"
    allowed_domains = ["castorama.ru"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://www.castorama.ru/{kwargs.get('section')}/{kwargs.get('category')}/"]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(URL + next_page, callback=self.parse)
        product_links = response.xpath("//a[@class='product-card__img-link']/@href").getall()
        for link in product_links:
            yield response.follow(URL + link, callback=self.parse_page)

    def parse_page(self, response: HtmlResponse):
        loader = ItemLoader(item=CastoramaItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photo', "//ul[@class='swiper-wrapper']/li[1]/span/@content")
        loader.add_xpath('price', "//span[@class='price']/span/span/text()")
        loader.add_value('product_link', response.url)
        yield loader.load_item()
