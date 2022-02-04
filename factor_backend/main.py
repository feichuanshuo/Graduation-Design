from flask import Flask
from config import setting
from apps.api import supply_data,transaction_data,population_data
from libs.extend import db

app = Flask(__name__)
app.config.from_object(setting)
app.register_blueprint(supply_data.api)
app.register_blueprint(transaction_data.api)
app.register_blueprint(population_data.api)
db.init_app(app)



if __name__ == '__main__':
    app.run()