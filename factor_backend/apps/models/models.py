from libs.extend import db

class Supply_data(db.Model):
    # 定义表名
    __tablename__ = 'supply_data'
    # 定义字段
    time = db.Column(db.Date, primary_key=True, autoincrement=False)
    supply_num = db.Column(db.Integer)
    supply_area = db.Column(db.Float)
    supply_price = db.Column(db.Float)
    floor_price = db.Column(db.Integer)

class Transaction_data(db.Model):
    # 定义表名
    __tablename__ = 'transaction_data'
    # 定义字段
    time = db.Column(db.Date, primary_key=True, autoincrement=False)
    transaction_num = db.Column(db.Integer)
    transaction_area = db.Column(db.Float)
    transaction_price = db.Column(db.Float)
    floor_price = db.Column(db.Integer)

class Population_data(db.Model):
    # 定义表名
    __tablename__ = 'population_data'
    # 定义字段
    year = db.Column(db.Date, primary_key=True, autoincrement=False)
    population_num = db.Column(db.Float)
    average_wage = db.Column(db.Integer)
    savings_balance = db.Column(db.Float)
    student_num = db.Column(db.Float)

class Environment_data(db.Model):
    # 定义表名
    __tablename__ = 'environment_data'
    # 定义字段
    year = db.Column(db.Date, primary_key=True, autoincrement=False)
    hospital_num = db.Column(db.Integer)
    doctor_num = db.Column(db.Float)
    cinema_num = db.Column(db.Integer)
    traffic_noise = db.Column(db.Float)
    ambient_noise = db.Column(db.Float)

class Detail_data(db.Model):
    # 定义表名
    __tablename__ = 'detail_data'
    # 定义字段
    name = db.Column(db.String(30), primary_key=True, autoincrement=False)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    plotRatio = db.Column(db.Float)
    greeningRate = db.Column(db.Integer)
    busStop = db.Column(db.Integer)
    subwayStations = db.Column(db.Integer)
    kindergarten = db.Column(db.Integer)
    primarySchool = db.Column(db.Integer)
    middleSchool = db.Column(db.Integer)
    hospital = db.Column(db.Integer)
    CAhospital = db.Column(db.Integer)
    shoppingMall = db.Column(db.Integer)
    supermarket = db.Column(db.Integer)
    park = db.Column(db.Integer)
    emotionIndex = db.Column(db.Float)

class Sentiment_data(db.Model):
    # 定义表名
    __tablename__ = 'sentiment_data'
    # 定义字段
    month = db.Column(db.Date,primary_key=True,autoincrement=False)
    price = db.Column(db.Integer)
    word_1 = db.Column(db.Integer)
    word_2 = db.Column(db.Integer)
    word_3 = db.Column(db.Integer)
    word_4 = db.Column(db.Integer)
    word_5 = db.Column(db.Integer)