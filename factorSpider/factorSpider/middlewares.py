# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class FactorspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class FactorspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class SeleniumMiddleware:


    def process_request(self, request, spider):
        if spider.name == 'DetailSpider':
            global browser
            option = ChromeOptions()
            option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            browser = webdriver.Chrome(chrome_options=option)


            # 小区详情页url列表
            hrefList = []


            # 反防爬
            browser.get(request.url)
            time.sleep(1)
            browser.get(request.url)
            url = browser.current_url
            body = browser.page_source
            with open('url.txt','r') as f:
                listStr = f.read()
                if listStr:
                    hrefList = eval(listStr)

            if hrefList == []:
                # 获取小区详情页url
                plotList = browser.find_elements(By.CLASS_NAME,'plotListwrap')
                for item in plotList:
                    hrefList.append(item.find_element(By.TAG_NAME,'a').get_attribute('href'))
                while(browser.find_element(By.CLASS_NAME,'fanye').find_elements(By.TAG_NAME,'a')[-2].text== '下一页'):
                    browser.find_element(By.CLASS_NAME,'fanye').find_elements(By.TAG_NAME,'a')[-2].click()
                    plotList = browser.find_elements(By.CLASS_NAME, 'plotListwrap')
                    for item in plotList:
                        hrefList.append(item.find_element(By.TAG_NAME, 'a').get_attribute('href'))
                    time.sleep(2)
                with open('url.txt','w') as f:
                    f.write(str(hrefList))

            #数据填补
            # xiaoqvList = ['太白山唐镇','西安恒大雅苑','水岸花城','新城悦隽公园里','中南春溪集','开远半岛广场','龙江国际城','南飞鸿蓝庭序','天正花园','西市佳郡','泾渭馨佳苑','陕汽泾渭国际城','铁一局后村小区','华尔兹花园','后卫馨佳苑','景辰家园','锦绣新苑','曲江大观园','乾基九境城','石化厅家属院','天沣园','新城玺樾骊府别墅','逸景佲居','车城温泉花园','嘉园馨苑','龙泉花园','泽星雅龙湾','翠华路小学小区','长乐小区','东屿枫舍','东仓门小区','电力医院家属院','电力职业大学家属院','枫禾苑小区','福乐家属院','高尔夫花园','广天国际公寓','冠诚鼎和国际','高科尚都摩卡','公安未央分局西院家属院','海纳观景园','华浮宫桂园','宏府向荣新区','翰怡苑','海红佳苑','翰林新苑','华宇东原阅境','海红小区(长安)','佳和苑','金源皇家园林','假日国际公寓','嘉泰隆花园','金桂苑','开发住宅小区二区','空军西安南郊干休所','绿园小区','莲湖区地税局家属院','劳动公园家属院','绿地骊山花城别墅','美林星公寓','煤炭工业西安设计研究院住宅区','庆阳观邸','曲江明翰花园','山海丹家属楼','盛豪小区','唐品A+','天玺龙景','五龙汤花园','文华阁','西雅图翡翠城','小寨家属院','徐家湾小区','西安光机所北生活区','西安市天燃气总公司住宅小区','馨苑新世纪','雅苑东方','雅荷四季城','怡园洋房','永乐小区','远洋落子栖','雁泊台','兆丰家园','紫晶大厦']

            # if hrefList == []:
            #     plotList = browser.find_elements(By.CLASS_NAME, 'plotListwrap')
            #     for item in plotList:
            #         aTag = item.find_element(By.TAG_NAME, 'dd').find_element(By.TAG_NAME,'a')
            #         print(aTag.text)
            #         print(xiaoqvList.count(aTag.text))
            #         print(xiaoqvList.count(aTag.text) != 0)
            #         if xiaoqvList.count(aTag.text) != 0:
            #             hrefList.append(aTag.get_attribute('href'))
            #     while (browser.find_element(By.CLASS_NAME, 'fanye').find_elements(By.TAG_NAME, 'a')[-2].text == '下一页'):
            #         browser.find_element(By.CLASS_NAME, 'fanye').find_elements(By.TAG_NAME, 'a')[-2].click()
            #         plotList = browser.find_elements(By.CLASS_NAME, 'plotListwrap')
            #         for item in plotList:
            #             aTag = item.find_element(By.TAG_NAME, 'dd').find_element(By.TAG_NAME,'a')
            #             if xiaoqvList.count(aTag.text) != 0:
            #                 hrefList.append(aTag.get_attribute('href'))
            #         time.sleep(2)
            #     with open('url.txt', 'w') as f:
            #         f.write(str(hrefList))

            request.meta['hrefList'] = hrefList
            request.meta['browser'] = browser
            return HtmlResponse(url=url, body=body, request=request, encoding='utf-8', status=200)


