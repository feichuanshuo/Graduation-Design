import scrapy
from scrapy import Request
import json
from factorSpider.items import PopulationdataItem
import time

class GjsjspiderSpider(scrapy.Spider):
    name = 'GjsjSpider'
    allowed_domains = ['data.stats.gov.cn']

    # 当前时间的时间戳（毫秒为单位）
    now_time = int(round(time.time() * 1000))

    urls_list = [
        # 人口和就业
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A02"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+str(now_time)+"&h=1",
        # 教育、卫生、文化
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A08"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+str(now_time)+"&h=1",
        # 财政和金融
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A04"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+str(now_time)+"&h=1",
        # 运输和邮电
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22610100%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22sj%22%2C%22valuecode%22%3A%22LAST20%22%7D%5D&k1=1641963243449',
        # 噪声监测
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22610100%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0A%22%7D%5D&k1=1641963330197&h=1'
    ]

    start_urls = [urls_list[0]]


    # 爬取人口和就业数据
    def parse(self, response):
        data_list = json.loads(response.text)['returndata']['datanodes']
        for i in range(0,20):
            year = data_list[i]['code'].split('.')[3]
            # 年末总人口(万人)
            population_num = float(data_list[i]['data']['data'])
            #在岗职工平均工资(元)
            average_wage = int(data_list[i+20]['data']['data'])

            populationData = PopulationdataItem(year=year,population_num=population_num,average_wage=average_wage)

            yield populationData

        yield Request(
            self.urls_list[1],
            self.parse_ehc
        )

    # 爬取教育、卫生、文化
    def parse_ehc(self,response):

        data_list = json.loads(response.text)['returndata']['datanodes']

        for i in range(0,20):
            year = data_list[i]['code'].split('.')[3]
            student_num = data_list[i]['data']['data']
            populationData = PopulationdataItem(year=year,student_num=student_num)
            yield populationData

        # for i in range(20,40):
        #     year = data_list[i]['code'].split('.')[3]
        #     hospital_num = data_list[i]['data']['data']
        #
        # for i in range(40,60):
        #     year = data_list[i]['code'].split('.')[3]
        #     doctor_num = data_list[i]['data']['data']
        #
        #
        # for i in range(60,80):
        #     year = data_list[i]['code'].split('.')[3]
        #     cinema_num = data_list[i]['data']['data']

        yield Request(
            self.urls_list[2],
            self.parse_finance
        )

    # 爬取财政和金融
    def parse_finance(self,response):
        data_list = json.loads(response.text)['returndata']['datanodes']

        for i in range(0,20):
            year = data_list[i]['code'].split('.')[3]
            # 城乡居民储蓄年末余额(亿元)
            savings_balance = data_list[i+40]['data']['data']

            populationData = PopulationdataItem(year=year,savings_balance=savings_balance)

            yield populationData