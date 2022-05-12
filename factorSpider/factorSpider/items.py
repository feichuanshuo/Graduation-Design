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

class EnvironmentdataItem(scrapy.Item):
    year = scrapy.Field()
    hospital_num = scrapy.Field()
    doctor_num = scrapy.Field()
    cinema_num = scrapy.Field()
    traffic_noise = scrapy.Field()
    ambient_noise = scrapy.Field()

class DetailItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    plotRatio = scrapy.Field()
    greeningRate = scrapy.Field()
    busStop = scrapy.Field()
    subwayStations = scrapy.Field()
    kindergarten = scrapy.Field()
    primarySchool = scrapy.Field()
    middleSchool = scrapy.Field()
    hospital = scrapy.Field()
    CAhospital = scrapy.Field()
    shoppingMall = scrapy.Field()
    supermarket = scrapy.Field()
    park = scrapy.Field()
    emotionIndex = scrapy.Field()

class PoHpItem(scrapy.Item):
    date = scrapy.Field()
    price = scrapy.Field()
    baidu_search_index = scrapy.Field()
    baidu_info_index = scrapy.Field()
    baidu_media_index = scrapy.Field()