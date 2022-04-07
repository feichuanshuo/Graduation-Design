import scrapy
from factorSpider.items import DetailItem
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium import webdriver

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

        global browser
        browser = response.request.meta['browser']
        hrefList = response.request.meta['hrefList']

        # 获取小区攻略页面数据
        flag = 0
        for href in hrefList:
            if flag >= 200:
                browser.close()
                option = ChromeOptions()
                option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
                browser = webdriver.Chrome(chrome_options=option)
                flag = 0
            browser.get(href)
            btnList = browser.find_element(By.ID,'orginalNaviBox').find_elements(By.TAG_NAME,'li')
            btn = None
            for b in btnList:
                if b.find_element(By.TAG_NAME,'a').text == '小区攻略':
                    btn = b
                    break
            if(btn != None):
                detailData = DetailItem(
                    name = '',
                    price = 0,
                    address = '',
                    plotRatio = 0.0,
                    greeningRate = 0,
                    busStop = 0,
                    subwayStations = 0,
                    kindergarten = 0,
                    primarySchool = 0,
                    middleSchool = 0,
                    hospital = 0,
                    CAhospital = 0,
                    shoppingMall = 0,
                    supermarket = 0,
                    park = 0
                )
                detailData['name'] = browser.find_element(By.CLASS_NAME,'title_village').find_element(By.TAG_NAME,'h3').text
                price = browser.find_element(By.CLASS_NAME,'num_price').find_element(By.TAG_NAME,'b').text
                if price != '暂无':
                    detailData['price'] = price
                time.sleep(1)
                btn.click()
                flextableLi = browser.find_elements(By.CLASS_NAME, 'flextable')[0].find_elements(By.TAG_NAME, 'li')
                for li in flextableLi:
                    if li.find_element(By.TAG_NAME, 'span').text == '小区地址':
                        detailData['address'] = li.find_element(By.TAG_NAME, 'p').text
                        break

                # 小区攻略页面数据爬取
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
                yield detailData
            flag = flag + 1
        browser.close()

