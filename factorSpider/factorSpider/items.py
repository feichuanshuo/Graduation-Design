import scrapy

class SupplydataItem(scrapy.Item):
    time = scrapy.Field()
    supply_num = scrapy.Field()
    supply_area = scrapy.Field()
    supply_price = scrapy.Field()
    floor_price = scrapy.Field()

class TransactiondataItem(scrapy.Item):
    time = scrapy.Field()
    transaction_num = scrapy.Field()
    transaction_area = scrapy.Field()
    transaction_price = scrapy.Field()
    floor_price = scrapy.Field()

class PopulationdataItem(scrapy.Item):
    year = scrapy.Field()
    population_num = scrapy.Field()
    average_wage = scrapy.Field()
    savings_balance = scrapy.Field()
    student_num = scrapy.Field()