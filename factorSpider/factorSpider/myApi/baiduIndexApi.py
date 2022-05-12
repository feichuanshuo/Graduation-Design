# 百度指数接口

import requests
import pandas as pd

def decrypt(t: str, e: str) -> str:
    """
    解密函数
    :param t:
    :type t:
    :param e:
    :type e:
    :return:
    :rtype:
    """
    n, i, a, result = list(t), list(e), {}, []
    ln = int(len(n) / 2)
    start, end = n[ln:], n[:ln]
    a = dict(zip(end, start))
    return "".join([a[j] for j in e])

def get_ptbk(uniqid: str, cookie: str) -> str:
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": cookie,
        'Cipher-Text': '1652338834776_1652340564888_hkI13Yn0yLUKwLROV9dYM4/ yCelaVT + hdNwcWLOU + ULT / P + hEkJDKCIXtlPTlgYnvNwcr0XECh + wuY + QU / w8Ev7Z + pr + LD7y0 + NPZSHEeGR0DqtDf2YjUpDJwWYH1DdpWgh4 + rvlccUDvuNB7SbyqFMIT7EdGt9po7UlIG + YO79vxsLhwnZMfVLH0BMcTpZ2sUq673Hg1nVTqZXeu + LFR138WQtUNquaZv / o2fW64m8tknhIEpzSZxTrtiZqZkzIEzGG5GHU6wEpoJqE + 8SQVEopHXKfpVFUzjEO84Ie0j + NMXV / wyUX3E6Nx26Jx3VJRkIHU + Tfm + +9IDGDT / 7NDhqKD6vki2P / mSForA9lKCEy4 / OR8bJFTDSfmVoxPkZu0eiYfqeWrBMIPMys5IrssDlgfwaWZkQR01ueu1yUZ8nFI674zaBJf2E2Y27vHvHp',
        "Host": "index.baidu.com",
        "Referer": "http://index.baidu.com/v2/main/index.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    session = requests.Session()
    session.headers.update(headers)
    with session.get(
        url=f"http://index.baidu.com/Interface/ptbk?uniqid={uniqid}"
    ) as response:
        ptbk = response.json()["data"]
        return ptbk

def baidu_search_index(word, start_date, end_date, cookie, type="all"):
    # 百度搜索数据
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate , br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": cookie,
            "Host": "index.baidu.com",
            'Cipher-Text':'1652338834776_1652340564888_hkI13Yn0yLUKwLROV9dYM4/ yCelaVT + hdNwcWLOU + ULT / P + hEkJDKCIXtlPTlgYnvNwcr0XECh + wuY + QU / w8Ev7Z + pr + LD7y0 + NPZSHEeGR0DqtDf2YjUpDJwWYH1DdpWgh4 + rvlccUDvuNB7SbyqFMIT7EdGt9po7UlIG + YO79vxsLhwnZMfVLH0BMcTpZ2sUq673Hg1nVTqZXeu + LFR138WQtUNquaZv / o2fW64m8tknhIEpzSZxTrtiZqZkzIEzGG5GHU6wEpoJqE + 8SQVEopHXKfpVFUzjEO84Ie0j + NMXV / wyUX3E6Nx26Jx3VJRkIHU + Tfm + +9IDGDT / 7NDhqKD6vki2P / mSForA9lKCEy4 / OR8bJFTDSfmVoxPkZu0eiYfqeWrBMIPMys5IrssDlgfwaWZkQR01ueu1yUZ8nFI674zaBJf2E2Y27vHvHp',
            "Referer": "http://index.baidu.com/v2/main/index.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
        }
        w = '{"name":"%s","wordType":1}' % word

        url = 'http://index.baidu.com/api/SearchApi/index?area=165&word=[[%s]]&startDate=%s&endDate=%s' % (w, start_date, end_date)

        r = requests.get(url=url, headers=headers)
        data = r.json()["data"]

        all_data = data["userIndexes"][0][type]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid, cookie)
        result = decrypt(ptbk, all_data).split(",")
        result = [int(item) if item != "" else 0 for item in result]
        temp_df_7 = pd.DataFrame(
                [pd.date_range(start=start_date, end=end_date), result],
                index=["date", word],
            ).T
        temp_df_7.index = pd.to_datetime(temp_df_7["date"])
        del temp_df_7["date"]
        return temp_df_7
    except Exception as e:
        return None

def baidu_info_index(word, start_date, end_date, cookie):
    # 百度资讯指数
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": cookie,
            'Cipher-Text': '1652338834776_1652340564888_hkI13Yn0yLUKwLROV9dYM4/ yCelaVT + hdNwcWLOU + ULT / P + hEkJDKCIXtlPTlgYnvNwcr0XECh + wuY + QU / w8Ev7Z + pr + LD7y0 + NPZSHEeGR0DqtDf2YjUpDJwWYH1DdpWgh4 + rvlccUDvuNB7SbyqFMIT7EdGt9po7UlIG + YO79vxsLhwnZMfVLH0BMcTpZ2sUq673Hg1nVTqZXeu + LFR138WQtUNquaZv / o2fW64m8tknhIEpzSZxTrtiZqZkzIEzGG5GHU6wEpoJqE + 8SQVEopHXKfpVFUzjEO84Ie0j + NMXV / wyUX3E6Nx26Jx3VJRkIHU + Tfm + +9IDGDT / 7NDhqKD6vki2P / mSForA9lKCEy4 / OR8bJFTDSfmVoxPkZu0eiYfqeWrBMIPMys5IrssDlgfwaWZkQR01ueu1yUZ8nFI674zaBJf2E2Y27vHvHp',
            "Host": "index.baidu.com",
            "Referer": "http://index.baidu.com/v2/main/index.html",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
        }
        w = '{"name":"%s","wordType":1}' % word

        url = 'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?area=0&word=[[%s]]&startDate=%s&endDate=%s' % (
        w, start_date, end_date)

        r = requests.get(url=url, headers=headers)
        data = r.json()["data"]
        all_data = data["index"][0]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid, cookie)
        result = decrypt(ptbk, all_data).split(",")
        result = [int(item) if item != "" else 0 for item in result]
        temp_df_7 = pd.DataFrame(
            [pd.date_range(start=start_date, end=end_date), result],
            index=["date", word],
        ).T
        temp_df_7.index = pd.to_datetime(temp_df_7["date"])
        del temp_df_7["date"]
        return temp_df_7
    except:
        return None

def baidu_media_index(word, start_date, end_date, cookie):
    # 百度媒体指数
    try:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": cookie,
            'Cipher-Text': '1652338834776_1652340564888_hkI13Yn0yLUKwLROV9dYM4/ yCelaVT + hdNwcWLOU + ULT / P + hEkJDKCIXtlPTlgYnvNwcr0XECh + wuY + QU / w8Ev7Z + pr + LD7y0 + NPZSHEeGR0DqtDf2YjUpDJwWYH1DdpWgh4 + rvlccUDvuNB7SbyqFMIT7EdGt9po7UlIG + YO79vxsLhwnZMfVLH0BMcTpZ2sUq673Hg1nVTqZXeu + LFR138WQtUNquaZv / o2fW64m8tknhIEpzSZxTrtiZqZkzIEzGG5GHU6wEpoJqE + 8SQVEopHXKfpVFUzjEO84Ie0j + NMXV / wyUX3E6Nx26Jx3VJRkIHU + Tfm + +9IDGDT / 7NDhqKD6vki2P / mSForA9lKCEy4 / OR8bJFTDSfmVoxPkZu0eiYfqeWrBMIPMys5IrssDlgfwaWZkQR01ueu1yUZ8nFI674zaBJf2E2Y27vHvHp',
            "Host": "index.baidu.com",
            "Referer": "http://index.baidu.com/v2/main/index.html",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
        }
        w = '{"name":"%s","wordType":1}' % word

        url = 'http://index.baidu.com/api/NewsApi/getNewsIndex?area=0&word=[[%s]]&startDate=%s&endDate=%s' % (w, start_date, end_date)

        r = requests.get(url=url, headers=headers)

        data = r.json()["data"]
        all_data = data["index"][0]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid, cookie)
        result = decrypt(ptbk, all_data).split(",")
        result = [int(item) if item != "" else 0 for item in result]
        temp_df_7 = pd.DataFrame(
            [pd.date_range(start=start_date, end=end_date), result],
            index=["date", word],
        ).T
        temp_df_7.index = pd.to_datetime(temp_df_7["date"])
        del temp_df_7["date"]
        return temp_df_7
    except:
        return None