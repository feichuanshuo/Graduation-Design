from flask import Blueprint,request
from libs.response import Success
import gopup as gp
from libs.extend import handle_data

api = Blueprint('public_sentiment',__name__,url_prefix='/public_sentiment')

baidu_cookie = 'BIDUPSID=7AED0A72C52D47D4F142F30255C32729; PSTM=1645587989; __yjs_duid=1_dea6428a3dde06fa02a54beebf5772cb1645605965773; BDUSS=pwbGp4SktrRWF6VWhQclhvSmdIOEdpZWdmazU4YU92aXhKZUJHVUpVYUlnVDFpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIj0FWKI9BViTk; BDUSS_BFESS=pwbGp4SktrRWF6VWhQclhvSmdIOEdpZWdmazU4YU92aXhKZUJHVUpVYUlnVDFpRVFBQUFBJCQAAAAAAAAAAAEAAACIK3fWt8e0q8u1NjI0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIj0FWKI9BViTk; BAIDUID=7CC442BDB341E2F6A3601CD21C61B75F:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%223598134152%22%2C%22scope%22%3A1%7D%7D; bdindexid=qiid3mhjiq6533s9utpa1h0b45; BAIDUID_BFESS=7CC442BDB341E2F6A3601CD21C61B75F:FG=1; BDRCVFR[0oJJGm61Oos]=mk3SLVN4HKm; delPer=0; PSINO=6; H_PS_PSSID=31253_26350; BA_HECTOR=2k2ga18g8ga0agak7u1h30dic0r; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1647245527,1647326797; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1647326798; __yjs_st=2_NWE2NTc1MTIwZmFjOTRjMThhYTM2MjEwMTE0YTZhYmRkMzcxOWYxZjIzYTFjMjk4YmFlZmE0Nzk4NDYwZWJmZWIzNjcyMmNhMDBkNWMzMWMyZGUwMmJiMjUxMzNhYWZiNWI2ODZhZGM0MDVmMjY1YzI2MGNmMWJhNGViMTdjYTIzM2VhMDE1OGZjZDIyZmM2ZTAzYjkwMDhkMDU4MGU2NzRhMjgyODk3NDQyNzU2ZjM1N2ExYTNjNmMyYWFlNTIzXzdfNzExYTcxZmQ=; ab_sr=1.0.1_NDQyMDRlN2RkMzkyNTI1MDJhYTc3MmExMjIzMjBkZTU3MDY4MDdjYjEwMjY4ZTE3NjExZmRlZmE2MWQwOWU1M2Q4NTEzZjZmZjc3ZWU2NjRhNTg2Y2U3NDFhZmFkZWI1MGJkNThlNDlmMTA3YjM2YTdhN2M3YzZjOTcwOGI2ZDI4NGJlMzI4ZTJmNzBhZjM5NGIxZWVmMTU0NjRiZTUzMA==; RT="z=1&dm=baidu.com&si=ardpbaouf5&ss=l0rrubrs&sl=3&tt=1dy&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"'

@api.route('/baidu_index',methods=['GET'])
def getBaiduIndex():
    word = request.args.get('word')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    search_index = gp.baidu_search_index(word=word, start_date=start_date, end_date=end_date, cookie=baidu_cookie)
    info_index = gp.baidu_info_index(word=word, start_date=start_date, end_date=end_date, cookie=baidu_cookie)
    media_index = gp.baidu_media_index(word=word, start_date=start_date, end_date=end_date, cookie=baidu_cookie)
    data = {
        'word': word,
        'search_index':handle_data(search_index),
        'info_index':handle_data(info_index),
        'media_index':handle_data(media_index)
    }
    return Success(data)