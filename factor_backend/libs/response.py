def Success(data):
    return {
        'code':200,
        'data':data,
        'msg':'success'
    }

def ServerError():
    return {
        'code': 500,
        'data': [],
        'msg': 'sorry, we made a mistake (*￣︶￣)!'
    }