# 土地供应爬虫

import scrapy
import datetime
from factorSpider.items import SupplydataItem

class SupplydataSpider(scrapy.Spider):
    name = 'SupplydataSpider'
    allowed_domains = ['fdc.fang.com']

    # 当前时间
    now_time = datetime.datetime.now().strftime('%Y.%m')
    # 开始时间
    start_time = '2019.01'

    start_urls = ['https://fdc.fang.com/data/ajax/LandPicTable.aspx?DataType=1&LandType=&Locus=610100&Time=m&BeginTime='+start_time+'&EndTime='+now_time]



    def parse(self, response):
        tr_list = response.xpath('//table/tr')
        for i in range(3,len(tr_list)):
            #时间
            time = tr_list[i].xpath('./td[1]/text()').extract_first().replace('\n','').replace('\t','').replace(' ','').replace('\r','')+'-01'
            #供应宗数(块)
            supply_num = int(tr_list[i].xpath('./td[2]/text()').extract_first().replace('\n','').replace('\t','').replace(' ','').replace('\r',''))
            #供应面积(㎡)
            supply_area = float(tr_list[i].xpath('./td[3]/text()').extract_first().replace('\n','').replace('\t','').replace(' ','').replace('\r',''))
            #供应均价(元/㎡)
            supply_price = float(tr_list[i].xpath('./td[4]/text()').extract_first().replace('\n','').replace('\t','').replace(' ','').replace('\r',''))
            #楼面价(元 /㎡)
            floor_price = int(tr_list[i].xpath('./td[5]/text()').extract_first().replace('\n','').replace('\t','').replace(' ','').replace('\r',''))

            supplyData = SupplydataItem(time=time,supply_num=supply_num,supply_area=supply_area,supply_price=supply_price,floor_price=floor_price)

            yield supplyData