# 舆情和房价爬虫

import scrapy
from ..myApi.baiduIndexApi import baidu_search_index
import calendar
import json
import time


cookie = 'BIDUPSID=9F13537D48E241A651EE89C72A039C1C; PSTM=1651053084; BDUSS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BDUSS_BFESS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BAIDUID=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=31254_26350; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1652258640,1652283401,1652340006,1652340558; BAIDUID_BFESS=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; delPer=0; PSINO=6; BA_HECTOR=0k01ak8k2kal2gagva1h7pgnu0r; BDRCVFR[0oJJGm61Oos]=mk3SLVN4HKm; __yjs_st=2_NWE2NTc1MTIwZmFjOTRjMThhYTM2MjEwMTE0YTZhYmQ1YzA0MDNiMzZjOGI3NjdiOGY4MTJjMTRiZDFiMGE2YmY5NWI2OWZjOWJkNDc2NDEyNTliMDJkNGJiOTRkZTVmYTI0MGJkM2FlYWM2OTFhMGNmYjc3NTU4ODkxZjkwMmQ3ZDQ5MGRkZDgyNDQwZjM0M2NlMTU4ZWY2NjZmMTRjMWEyMWM3NGE4MDQwMzQzN2FkMDRhNDA2MzFlZDJlNDBmXzdfZDhlMjJlOGU=; bdindexid=5c6ahvetgot2c9b06ue5moo445; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1652349516; ab_sr=1.0.1_YjNiNjU3ZTM4ODFlNzBiMGE0ZjVmNTMxMWYzM2Y0YTVlNjNjMDM1ODNmYWFkMjZmYjhjNDk3NWU4ZDU0ZjZjYTg0ZDkxMDYxMDhkZTMxOTI5ODVhMzZhNmI3Nzk1NDBlZTJkNTM3ZDNiY2ZlNDRhMjJkZWY3ODc1OTk5MjkwNjQ2NDdjZDZiNzBlNzk1Zjc3MGM1YjcyMDU5ZTViMWEyNg==; RT="z=1&dm=baidu.com&si=beyv9n1gr5o&ss=l32u8iom&sl=5&tt=2f6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=az3"'

def handleMonth(month):
    if month > 9:
        return str(month)
    else:
        return '0' + str(month)

def handle_data(data):
    result = []
    data = json.loads(data.to_json(date_unit='s'))
    data_dict = data[list(data.keys())[0]]
    for key in data_dict:
        result.append({
            'Date': time.strftime("%Y-%m-%d",time.localtime(int(key))),
            'index': data_dict[key]
        })
    return result

class SupplydataSpider(scrapy.Spider):
    name = 'PoHpSpider'

    start_urls = ['http://xa.cityhouse.cn/market/chartsdatanew.html?city=xa&proptype=11&district=allsq1&town=&sinceyear=5&flag=1&based=price&dtype=line']

    def parse(self, response):
        res = eval(response.text)[0]['rows']
        for item in res:
            tempMonth = item['month'].split('-')
            year = tempMonth[0]
            month = handleMonth(int(tempMonth[1]))
            start_date = year + '-' + month + '-01'
            end_date = year + '-' + month + '-' + str(calendar.monthrange(int(year), int(month))[1])
            date = start_date
            price = item['data']
            SearchIndex = handle_data(baidu_search_index(word='二手房',cookie=cookie,start_date=start_date,end_date=end_date))
            baiduSearchIndex = 0
            for item in SearchIndex:
                baiduSearchIndex = baiduSearchIndex + item['index']
            baiduSearchIndex = int(baiduSearchIndex/len(SearchIndex))


            print(date,price,baiduSearchIndex)
        pass