import scrapy
class DetailspiderSpider(scrapy.Spider):
    name = 'detailSpider'
    # allowed_domains = ['www.cc.com']
    # start_urls = ['https://xian.esf.fang.com/housing/__0_3_0_0_1_0_0_0/']

    def start_requests(self):
        urls = [
            'https://xian.esf.fang.com/housing'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # hrefList = response.xpath('//div[@class="houseList"]//dl/dt/a/@href').extract()
        # print(hrefList)
        print(response.request.meta['result'])

        # pass
        # print(response.text)
    #     # htm = response.xpath('//html').extract_first()
    #     # # with open('test.html', 'w') as f:
    #     # #     f.write(htm)
    #     # dt_list = response.xpath('//div[@class="houseList"]')
    #     # print(dt_list)
    #     # for dt in dt_list:
    #     #     print('执行')
    #     #     url = dt.xpath('./a[1]/@href').extract_first()
    #     #     print(url)