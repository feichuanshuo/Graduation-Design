from flask_sqlalchemy import SQLAlchemy
import json
import time

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy()

def handle_date(data):
    result = []
    data = json.loads(data.to_json(date_unit='s'))
    data_dict = data[list(data.keys())[0]]
    for key in data_dict:
        result.append({
            'Date': time.strftime("%Y-%m-%d",time.localtime(int(key))),
            'index': data_dict[key]
        })
    return result

