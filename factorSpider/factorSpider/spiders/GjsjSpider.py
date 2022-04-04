import scrapy
from scrapy import Request
import json
from factorSpider.items import PopulationdataItem,EnvironmentdataItem
import time

class GjsjSpider(scrapy.Spider):
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
        # 噪声检测
        'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=csnd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"610100"}]&dfwds=[{"wdcode":"zb","valuecode":"A0A"},{"wdcode":"sj","valuecode":"LAST20"}]&k1='+str(now_time)+"&h=1",
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
            # 普通本专科学生(万人)
            student_num = float(data_list[i]['data']['data'])
            populationData = PopulationdataItem(year=year,student_num=student_num)
            yield populationData
            # 医院数(个)
            hospital_num = int(data_list[i+20]['data']['data'])
            # 执业(助理)医师数(万人)
            doctor_num = float(data_list[i+40]['data']['data'])
            # 剧场、影剧院数(个)
            cinema_num = int(data_list[i+60]['data']['data'])

            environmentData = EnvironmentdataItem(year=year,hospital_num=hospital_num,doctor_num=doctor_num,cinema_num=cinema_num)

            yield environmentData


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
            savings_balance = float(data_list[i+40]['data']['data'])

            populationData = PopulationdataItem(year=year,savings_balance=savings_balance)

            yield populationData

        yield Request(
            self.urls_list[3],
            self.parse_noise
        )


    # 爬取噪声检测
    def parse_noise(self,response):
        data_list = json.loads(response.text)['returndata']['datanodes']

        for i in range(0,20):
            year = data_list[i]['code'].split('.')[3]
            # 道路交通等效声级dB(A)
            traffic_noise = float(data_list[i]['data']['data'])
            # 环境噪声等效声级dB(A)
            ambient_noise = float(data_list[i+20]['data']['data'])

            environmentData = EnvironmentdataItem(year=year, traffic_noise=traffic_noise, ambient_noise=ambient_noise)

            yield environmentData