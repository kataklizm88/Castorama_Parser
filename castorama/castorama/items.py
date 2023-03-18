import scrapy
from itemloaders.processors import TakeFirst, Compose

""" Метод для обработки данных после парсинга в корректный вид"""


def clean_name(value: list):
    try:
        value = value[0].replace('\n', '').replace('  ', '')
    except Exception as e:
        print(f' Ошибка {e}')
        return value
    return value


class CastoramaItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(input_processor=Compose(clean_name), output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field()
    product_link = scrapy.Field()
