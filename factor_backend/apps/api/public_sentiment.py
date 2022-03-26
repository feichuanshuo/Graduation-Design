from flask import Blueprint,request
from libs.response import Success,ServerError
import gopup as gp
from libs.extend import handle_date

api = Blueprint('public_sentiment',__name__,url_prefix='/public_sentiment')

baidu_cookie = 'BIDUPSID=7AED0A72C52D47D4F142F30255C32729; PSTM=1645587989; __yjs_duid=1_dea6428a3dde06fa02a54beebf5772cb1645605965773; BDUSS=pwbGp4SktrRWF6VWhQclhvSmdIOEdpZWdmazU4YU92aXhKZUJHVUpVYUlnVDFpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIj0FWKI9BViTk; BDUSS_BFESS=pwbGp4SktrRWF6VWhQclhvSmdIOEdpZWdmazU4YU92aXhKZUJHVUpVYUlnVDFpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIj0FWKI9BViTk; BAIDUID=7CC442BDB341E2F6A3601CD21C61B75F:FG=1; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=7CC442BDB341E2F6A3601CD21C61B75F:FG=1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1647396564,1647444654,1647590939,1647694357; bdindexid=5fbgumocn0evoes042t6pic6c0; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1647694421; ab_sr=1.0.1_OWZiYjA4NDE5NzVhNTA0NTc4Njc2YmU5MDFiYTVhMDIzZGI1YTFlOTdiODA1YThiYjg3YzFmY2JkNDU2NzVhNjM4N2JhZmQ3OTJmYWNjNGMxNjRiYmZmNWViMDU3MTQ5YjlmMzU0NTUxODk1MmM1ZmVlNDY5M2JlNThhZTkzZGI2ZGNiNTNmZWIxYTBhMzRjMjA2YWI2MDYwNTc3NmQzZg==; __yjs_st=2_NWE2NTc1MTIwZmFjOTRjMThhYTM2MjEwMTE0YTZhYmRlOWJhMzk4Y2U1NmIxYTBmMWRiYmE1ZDhjYzlmZDdlZTMxNWIwNDdjM2U0MmRhMGY2MDUyYWM5MGU3MmJmYmJjYmNhNThhMzE0YTRhYmU4NGZhZTg1ZDM2ZDBmZGY2Y2I5NDRkZDVmY2NhMmQ3YTcwODBkMmZkOTVmMzQwZjVlM2UyMGJhM2IyOTQ2NzJhOWZjYWM0Mzk5ZjZkMjYzZWY2XzdfZDkyZjQ3YTY=; RT="z=1&dm=baidu.com&si=h04dh3bsdmp&ss=l0xuodv2&sl=7&tt=4s0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1lcj"'

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
