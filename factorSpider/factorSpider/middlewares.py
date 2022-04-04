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

            # 返回数据
            result = []

            # 反防爬
            browser.get(request.url)
            time.sleep(1)
            browser.get(request.url)
            url = browser.current_url
            body = browser.page_source

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

            # 获取小区攻略页面数据
            for href in hrefList:
                browser.get(href)
                btn = browser.find_element(By.ID,'orginalNaviBox').find_elements(By.TAG_NAME,'li')[2]
                if(btn.find_element(By.TAG_NAME,'a').text == '小区攻略'):
                    detailData = {
                        'name': '',
                        'address': '',
                        'plotRatio': 0.0,
                        'greeningRate': 0,
                        'busStop': 0,
                        'subwayStations': 0,
                        'kindergarten':0,
                        'primarySchool': 0,
                        'middleSchool': 0,
                        'hospital': 0,
                        'CAhospital': 0,
                        'shoppingMall': 0,
                        'supermarket': 0,
                        'park': 0
                    }
                    detailData['name'] = browser.find_element(By.CLASS_NAME,'title_village').find_element(By.TAG_NAME,'h3').text
                    time.sleep(1)
                    btn.click()
                    detailData['address'] = browser.find_elements(By.CLASS_NAME,'flextable')[0].find_elements(By.TAG_NAME,'p')[4].text

                    boxList = browser.find_elements(By.CLASS_NAME,'bg_box_in')
                    for box in boxList:
                        boxTag =  box.find_element(By.TAG_NAME,'h3').text
                        if boxTag == '容积率':
                            detailData['plotRatio'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text
                        elif boxTag == '绿化率':
                            detailData['greeningRate'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text
                        elif boxTag == '交通配置':
                            detailData['busStop'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text
                            detailData['subwayStations'] = box.find_elements(By.CLASS_NAME,'num_score')[1].text
                        elif boxTag == '教育配置':
                            detailData['kindergarten'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text
                            detailData['primarySchool'] = box.find_elements(By.CLASS_NAME,'num_score')[1].text
                            detailData['middleSchool'] = box.find_elements(By.CLASS_NAME,'num_score')[2].text
                        elif boxTag == '医疗配套':
                            detailData['hospital'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text
                            detailData['CAhospital'] = box.find_elements(By.CLASS_NAME,'num_score')[1].text
                        elif boxTag == '购物配套':
                            detailData['shoppingMall'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text
                            detailData['supermarket'] = box.find_elements(By.CLASS_NAME,'num_score')[1].text
                        elif boxTag == '休闲配套':
                            detailData['park'] = box.find_elements(By.CLASS_NAME,'num_score')[0].text

                    time.sleep(2)
                    result.append(detailData)

            browser.close()
            request.meta['result'] = result
            return HtmlResponse(url=url, body=body, request=request, encoding='utf-8', status=200)


