import scrapy
from factorSpider.items import DetailItem

class DetailSpider(scrapy.Spider):
    name = 'DetailSpider'
    # allowed_domains = ['www.cc.com']
    # start_urls = ['https://xian.esf.fang.com/housing/__0_3_0_0_1_0_0_0/']

    def start_requests(self):
        urls = [
            'https://xian.esf.fang.com/housing'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for item in response.request.meta['result']:
            # 小区名称
            name = item['name']
            # 小区地址
            address = item['address']
            # 小区容积率
            plotRatio = item['plotRatio']
            # 小区绿化率
            greeningRate = item['greeningRate']
            # 小区公交站数
            busStop = item['busStop']
            # 小区地铁站数
            subwayStations = item['subwayStations']
            # 小区幼儿园数
            kindergarten = item['kindergarten']
            # 小区小学数
            primarySchool = item['primarySchool']
            # 小区中学数
            middleSchool = item['middleSchool']
            # 小区医院数
            hospital = item['hospital']
            # 小区三甲医院数
            CAhospital = item['CAhospital']
            # 小区购物中心数
            shoppingMall = item['shoppingMall']
            # 小区超市数
            supermarket = item['supermarket']
            # 小区公园数
            park = item['park']

            detailData = DetailItem(
                name = name,
                address = address,
                plotRatio = float(plotRatio),
                greeningRate = int(greeningRate),
                busStop = int(busStop),
                subwayStations = int(subwayStations),
                kindergarten = int(kindergarten),
                primarySchool = int(primarySchool),
                middleSchool = int(middleSchool),
                hospital = int(hospital),
                CAhospital = int(CAhospital),
                shoppingMall = int(shoppingMall),
                supermarket = int(supermarket),
                park = int(park)
            )

            yield detailData


