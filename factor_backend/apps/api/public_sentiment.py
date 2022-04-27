from flask import Blueprint,request
from libs.response import Success,ServerError
import gopup as gp
from libs.extend import handle_date
import time

# 当前时间的时间戳（毫秒为单位）
now_time = int(time.time())

api = Blueprint('public_sentiment',__name__,url_prefix='/public_sentiment')

baidu_cookie = 'BIDUPSID=9F13537D48E241A651EE89C72A039C1C; PSTM=1651053084; BA_HECTOR=812ka12k8g0h21208a1h6i4gu0r; BDUSS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BDUSS_BFESS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BAIDUID=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; BAIDUID_BFESS=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=36309_31254_34812_35915_36166_34584_36120_36074_35801_36344_26350_36300_36061; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1651053961; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; bdindexid=mobrumnq9ocnesndja0gieitu6; __yjs_st=2_ZmEyNzI4NGE4NGUyOThmNWVhYTNlYmMxOWQzZGFmNDY4Nzk5YWNhMDkyMGQ1YzRjMWY3OWYzZjJkNjQ3NGU3YTliNDVjMjJkNTk0M2MxZmMzODE4YmMwMTMxNjAyNGQ1YzA3OWRhYjBiZTRjNzY0NGY4YTQ1YWM5NWM0YTJmNmQ0ZDllM2RmMzA1M2Y5ZWJiMDJhMjRlNWFmZTQ5ZjJmYWYzYjQ3ODM3M2E0YzhmYmJmZWU0OWNhM2M1NGRjZDYwXzdfNDk4YTRkNmQ=; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc='+ str(now_time) +'; ab_sr=1.0.1_OWY3ZTcxM2YwODFiNTkzOTIwZGQ2ZDY4MmMwNjI5ZTY5MmQ1MWRkNzg2ZGVjODEwZTEyMmFhZmM4ZDRiOGZjMTk1YzdmZmMzOGMxMzkxMGM2ODViODViMWU3Y2QyODk3MTA4NDkwNDkzNzczMGYwY2I2NzBiMmY4M2JlMzRlMzRmNzJhZmE1Y2M5MTNiYTExNjlhZDFiMDg4MGRjZGM4Zg==; RT="z=1&dm=baidu.com&si=gtnn70brlet&ss=l2hewdex&sl=4&tt=2v9&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=c48"'


@api.route('/baidu_index',methods=['GET'])
def getBaiduIndex():
    try:
        word = request.args.get('word')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        search_index = gp.baidu_search_index(word=word, start_date=start_date, end_date=end_date, cookie=baidu_cookie)
        info_index = gp.baidu_info_index(word=word, start_date=start_date, end_date=end_date, cookie=baidu_cookie)
        media_index = gp.baidu_media_index(word=word, start_date=start_date, end_date=end_date, cookie=baidu_cookie)
        data = {
            'search_index':handle_date(search_index),
            'info_index':handle_date(info_index),
            'media_index':handle_date(media_index)
        }
        return Success(data)
    except BaseException:
        return ServerError()
