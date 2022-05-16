# 舆情和房价爬虫

import scrapy
from ..myApi.baiduIndexApi import baidu_search_index
import calendar
import json
import time
from ..items import PoHpItem


cookie = 'BIDUPSID=9F13537D48E241A651EE89C72A039C1C; PSTM=1651053084; BAIDUID=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; BAIDUID_BFESS=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; BDUSS=ZFRlVEbUVzSmxyYmlyRWFBWGJMcUgzM0o5aGplejVKSHVRY3YtY05ibHNPcWhpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGytgGJsrYBidW; BDUSS_BFESS=ZFRlVEbUVzSmxyYmlyRWFBWGJMcUgzM0o5aGplejVKSHVRY3YtY05ibHNPcWhpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGytgGJsrYBidW; __yjs_st=2_ZmEyNzI4NGE4NGUyOThmNWVhYTNlYmMxOWQzZGFmNDY0NjEzYjFhNWYxOTc3N2IxMjgyZTE1ZWM0Y2EyZjk4MWRmOWVhYjAxY2YyNGMwZTAyNGM2ZGI2ODNjMzg5ZjFjODU4YjczZDlkNDc0ODlkOGE0OTFhNDM3M2ZlNDFhYThlYjRlNTI1YjE1NWE1NGY3YzAyOWI4MDkyY2U0MzdiZjBjNDY3NjU0NmQxMzU5MjAwMDZmOGNjYzdmMzBiNWJhXzdfYTk2NjU4ZmQ=; bdindexid=b3mli213jp38lmmqsrtk8avij1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1652594718,1652613140,1652696783,1652715689; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1652715695; ab_sr=1.0.1_ZjlmYzY0NWY3ZTgyOTNlY2Y5OTQ0MzBjZWExZjI0NTIwZTIyZTUxMmNkZDQwYTk2YjNhOTU3YWVkOGNhOGMzODIxYzFlNGUxZWZkYjNhMzA2ODNkZTJmMTUwOGQ2YTM1Nzg4NDZmNGJmOWRhYjE4ZmY2MWZkMGIxMzBjZTY3MmM0NTYwMWU3MTg5ZDU0ODNmODAwMDg3ZjVkYjJhYmI0NQ==; RT="sl=7&ss=l38w8yj7&tt=3ih&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=s1sfz5vw0hj&ld=11ta"'


wordList = [
    '房价',
    '房价上涨',
    '房价下跌',
    '房产税',
    '房贷'
]


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

class PoHpSpider(scrapy.Spider):
    name = 'PoHpSpider'

    start_urls = ['http://xa.cityhouse.cn/market/chartsdatanew.html?city=xa&proptype=11&district=allsq1&town=&sinceyear=5&flag=1&based=price&dtype=line']

    def parse(self, response):
        res = eval(response.text)[0]['rows']
        print(res)
        for item in res:
            wordSearchIndexList = []
            tempMonth = item['month'].split('-')
            year = tempMonth[0]
            month = handleMonth(int(tempMonth[1]))
            start_date = year + '-' + month + '-01'
            end_date = year + '-' + month + '-' + str(calendar.monthrange(int(year), int(month))[1])
            date = start_date
            price = item['data']
            for word in wordList:
                SearchIndex = handle_data(baidu_search_index(word=word,cookie=cookie,start_date=start_date,end_date=end_date))
                print(SearchIndex)
                baiduSearchIndex = 0
                for item in SearchIndex:
                    if item['index'] != None:
                        baiduSearchIndex = baiduSearchIndex + item['index']
                baiduSearchIndex = int(baiduSearchIndex/len(SearchIndex))
                wordSearchIndexList.append(baiduSearchIndex)
            pohpItem = PoHpItem(
                month=date,
                price=price,
                word_1=wordSearchIndexList[0],
                word_2=wordSearchIndexList[1],
                word_3=wordSearchIndexList[2],
                word_4=wordSearchIndexList[3],
                word_5=wordSearchIndexList[4]
            )
            time.sleep(2)
            yield pohpItem
