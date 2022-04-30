from flask import Blueprint,request
from apps.models.models import Transaction_data
from libs.response import Success,ServerError

api = Blueprint('transaction_data',__name__,url_prefix='/transaction_data')

@api.route('',methods=['GET'])
def getTransactionData():
    len = int(request.args.get('len'))
    data = []
    try:
        result = Transaction_data.query.order_by(Transaction_data.time.desc()).all()[0:len]
        for index in range(len):
            element = {
                'key':index,
                'time' : str(result[index].time),
                'transaction_num':result[index].transaction_num,
                'transaction_area':result[index].transaction_area,
                'transaction_price':result[index].transaction_price,
                'floor_price':result[index].floor_price
            }
            data.append(element)
        return Success(data)
    except Exception as e:
        return ServerError()