from flask import Blueprint,request
from apps.models.models import Supply_data
from libs.response import Success,ServerError

api = Blueprint('supply_data',__name__,url_prefix='/supply_data')

@api.route('',methods=['GET'])
def getSupplyData():
    len = int(request.args.get('len'))
    data = []
    try:
        result = Supply_data.query.order_by(Supply_data.time.desc()).all()[0:len]
        for index in range(len):
            element = {
                'key' : index,
                'time' : str(result[index].time)[0:7],
                'supply_num':result[index].supply_num,
                'supply_area':result[index].supply_area,
                'supply_price':result[index].supply_price,
                'floor_price':result[index].floor_price
            }
            data.append(element)
        return Success(data)
    except Exception:
        return ServerError()