from flask import Blueprint,request
from apps.models.models import Population_data,Environment_data
from libs.response import Success,ServerError

api = Blueprint('city_information',__name__,url_prefix='/city_information')

@api.route('',methods=['GET'])
def getCityInformation():
    len = int(request.args.get('len'))
    data = []
    try:
        result1 = Population_data.query.order_by(Population_data.year.desc()).all()[0:len]
        result2 = Environment_data.query.order_by(Environment_data.year.desc()).all()[0:len]
        for index in range(len):
            element = {
                'key': index,
                'year': str(result1[index].year),
                'population_num':result1[index].population_num,
                'average_wage':result1[index].average_wage,
                'savings_balance':result1[index].savings_balance,
                'student_num':result1[index].student_num,
                'hospital_num':result2[index].hospital_num,
                'doctor_num':result2[index].doctor_num,
                'traffic_noise':result2[index].traffic_noise,
                'ambient_noise':result2[index].ambient_noise,
            }
            data.append(element)
        return Success(data)
    except Exception:
        return ServerError()