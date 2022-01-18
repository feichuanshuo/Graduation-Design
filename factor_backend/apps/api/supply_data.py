from flask import Blueprint,request
from apps.models.models import Supply_data
from libs.response import Success,ServerError

api = Blueprint('supply_data',__name__,url_prefix='/supply_data')

@api.route('',methods=['GET'])
def supply_data_list():
    len = int(request.args.get('len'))
    data = []
    if Supply_data.query.order_by(Supply_data.time.desc()).all()[0:len]:
        result = Supply_data.query.order_by(Supply_data.time.desc()).all()[0:len]
        for item in result:
            element = {
                'time' : str(item.time),
                'supply_num':item.supply_num,
                'supply_area':item.supply_area,
                'supply_price':item.supply_price,
                'floor_price':item.floor_price
            }
            data.append(element)
        return Success(data)
    else:
        return ServerError()