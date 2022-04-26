from flask import Blueprint,request
from apps.models.models import Detail_data
from libs.response import Success,ServerError
from libs.neuralNetwork.main import get_estimated_data

api = Blueprint('detail',__name__,url_prefix='/detail')

# 获取小区详情的接口
@api.route('/detail_data',methods=['GET'])
def getDetailData():
    # 小区名
    name = request.args.get('name')
    try:
        result = Detail_data.query.filter_by(name=name).first()
        estimated_price = None
        if result.price != 0 and result.plotRatio!=0 and result.greeningRate!=0:
            estimated_price = get_estimated_data([[
                result.plotRatio,
                result.greeningRate,
                result.busStop,
                result.subwayStations,
                result.kindergarten,
                result.primarySchool,
                result.middleSchool,
                result.hospital,
                result.shoppingMall,
                result.supermarket,
                result.park
            ]])
        data = {
            'name':result.name,
            'address':result.address,
            'price':result.price,
            'estimated_price':estimated_price,
            'plotRatio':result.plotRatio,
            'greeningRate':result.greeningRate,
            'busStop':result.busStop,
            'subwayStations':result.subwayStations,
            'kindergarten':result.kindergarten,
            'primarySchool':result.primarySchool,
            'middleSchool':result.middleSchool,
            'hospital':result.hospital,
            'shoppingMall':result.shoppingMall,
            'supermarket':result.supermarket,
            'park':result.park,
        }
        return Success(data)
    except Exception:
        return ServerError()

# 获取包含指定关键字的小区列表
@api.route('/search_hint',methods=['GET'])
def getSearchHint():
    # 关键字
    keyword = request.args.get('keyword')
    # 返回的数据
    data = []
    try:
        result = Detail_data.query.filter(Detail_data.name.like('%'+keyword+'%')).all()
        for item in result:
            data.append(item.name)
        return Success(data)
    except Exception:
        return ServerError()