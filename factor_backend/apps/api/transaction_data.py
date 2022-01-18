from flask import Blueprint,request
from apps.models.models import Transaction_data
from libs.response import Success,ServerError

api = Blueprint('transaction_data',__name__,url_prefix='/transaction_data')

@api.route('',methods=['GET'])
def transaction_data_list():
    len = int(request.args.get('len'))
    data = []
    if Transaction_data.query.order_by(Transaction_data.time.desc()).all()[0:len]:
        result = Transaction_data.query.order_by(Transaction_data.time.desc()).all()[0:len]
        for item in result:
            element = {
                'time' : str(item.time),
                'transaction_num':item.transaction_num,
                'transaction_area':item.transaction_area,
                'transaction_price':item.transaction_price,
                'floor_price':item.floor_price
            }
            data.append(element)
        return Success(data)
    else:
        return ServerError()