from flask import Blueprint,request
from libs.response import Success,ServerError
import gopup as gp
from libs.extend import handle_date
import time

# 当前时间的时间戳（毫秒为单位）
now_time = int(time.time())

api = Blueprint('public_sentiment',__name__,url_prefix='/public_sentiment')

baidu_cookie = 'BIDUPSID=9F13537D48E241A651EE89C72A039C1C; PSTM=1651053084; BDUSS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BDUSS_BFESS=XpCLVl2SDhWTWM3blJrdm5FQ1l-MDlIbElyNy1BcHZmOFlhQ2t0VGVZNDNuNUJpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcSaWI3EmliU; BAIDUID=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=9F13537D48E241A652F08D9BAB425DD8:SL=0:NR=10:FG=1; bdindexid=mrghbc6oscpaefgua6dgkkqts0; BA_HECTOR=0185a0a08l842g0gpr1h7nn0d0q; BDRCVFR[0oJJGm61Oos]=mk3SLVN4HKm; delPer=0; PSINO=6; H_PS_PSSID=31254_26350; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1652164034,1652258640,1652283401,1652340006; __yjs_st=2_NWE2NTc1MTIwZmFjOTRjMThhYTM2MjEwMTE0YTZhYmQ1YzA0MDNiMzZjOGI3NjdiOGY4MTJjMTRiZDFiMGE2YmY5NWI2OWZjOWJkNDc2NDEyNTliMDJkNGJiOTRkZTVmYTI0MGJkM2FlYWM2OTFhMGNmYjc3NTU4ODkxZjkwMmQ4YzE4MjUxZTg4NTQwZWZiODdjZWE0ZTAwMzJlYTBmZWE2YWFjYTc5YmE1Y2Y4YzVlYTQ1YTk3OTQ3OGYzYjhmXzdfYjQzZTg3YzA=; RT="z=1&dm=baidu.com&si=y9z5aimib7q&ss=l32okrua&sl=2&tt=164&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1652340021; ab_sr=1.0.1_MzczYWVhZjRkYjllZTQzNGYyMzc4MzhhNTIxNGQxNWZhYWFhZDAzZjExZTU5MjcwYjZlODM4NDYzZjIzNWRiNDJhY2NjMzhiNjE5NzFiZTdmMTM4ZDRhZWRlY2I3OWRlYjJiODk5MmUyODNjNWUzMzExZWQ4ZDFmNzgyYzZjNWNlNmEwMmI1NGRmMjkxNDFhZTFhNTBhMmJiM2IyZDM4OQ=='


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
