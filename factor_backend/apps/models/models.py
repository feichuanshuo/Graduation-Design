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