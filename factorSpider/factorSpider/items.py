import scrapy


class SupplydataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    supply_num = scrapy.Field()
    supply_area = scrapy.Field()
    supply_price = scrapy.Field()
    floor_price = scrapy.Field()

class TransactiondataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    transaction_num = scrapy.Field()
    transaction_area = scrapy.Field()
    transaction_price = scrapy.Field()
    floor_price = scrapy.Field()