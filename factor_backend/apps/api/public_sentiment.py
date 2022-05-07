from flask import Blueprint,request
from libs.response import Success,ServerError
import gopup as gp
from libs.extend import handle_date
import time

# 当前时间的时间戳（毫秒为单位）
now_time = int(time.time())

api = Blueprint('public_sentiment',__name__,url_prefix='/public_sentiment')

baidu_cookie = 'BIDUPSID=9F13537D48E241A651EE89C72A039C1C; PSTM=1651053084; BDUSS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BDUSS_BFESS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BAIDUID=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; BAIDUID_BFESS=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1651053961,1651634611; bdindexid=f0ns22labmlv68k84k2hd326h2; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc='+str(now_time)+'; __yjs_st=2_NWE2NTc1MTIwZmFjOTRjMThhYTM2MjEwMTE0YTZhYmQxZjQyZGVjMjI0ZjkwMjNjYzAzYWQyZWRlZGQ0MWY4ZTBhMDc2MmVlZTYxNGVjZDg4ZGNjNTdjMTVkN2FhNWI1MWViMmFmZWY1Mzg4MzBlNjI0N2Y2NmQ4Yjc0ODQ3NTU4ZTFlNjFjMGUyZTQ2NzUyZGFhM2M3YzEyMjVjZWM0MmJiMDA0MDJkODk0Y2M4Yjk0MTM3NmZkYzBlMWI1MzMyXzdfMDA1NDk4OGM=; ab_sr=1.0.1_NzA5MThiMzdhMmNhYzQyN2U5ZThiMjMxMmI4YTJiYmRmZWI0Yzc4OGQxMTE1MWQ5M2NmMjdjMjJjOGU3MzRiMjBkMjdhMzY0OTYzMzExYjFjMmI1MWZlNmZmZTgzNzRjNGZiNGY5ZTNlZjU3Zjg2NzY5OTkxMTEzMjFjY2QyMWQ1Mzg1ZmYwNDI4MjRhOTQxNWU0MzE1YzVjMjI5MmQxMQ==; RT="z=1&dm=baidu.com&si=ihlz6s8tts&ss=l2r0lp2t&sl=6&tt=49x&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=m62"'

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
