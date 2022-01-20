def Success(data):
    return {
        'code':10000,
        'data':data,
        'msg':'success'
    }

def ServerError():
    return {
        'code': 500,
        'data': [],
        'msg': 'sorry, we made a mistake (*￣︶￣)!'
    }