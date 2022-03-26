from flask import Blueprint,request
from apps.models.models import Population_data
from libs.response import Success,ServerError

api = Blueprint('population_data',__name__,url_prefix='/population_data')

@api.route('',methods=['GET'])
def population_data_list():
    len = int(request.args.get('len'))
    data = []
    try:
        result = Population_data.query.order_by(Population_data.year.desc()).all()[0:len]
        for item in result:
            element = {
                'year': str(item.year),
                'population_num':item.population_num,
                'average_wage':item.average_wage,
                'savings_balance':item.savings_balance,
                'student_num':item.student_num
            }
            data.append(element)
        return Success(data)
    except Exception:
        return ServerError()