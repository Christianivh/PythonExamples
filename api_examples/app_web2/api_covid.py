from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

class Country(Resource):
    def get(self, country_name):
        df = pd.read_csv("/Users/chvasquez/PycharmProjects/API_Example/covid19.csv")
        df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
        df = df[(df['country']==country_name)]
        max_date = max(df['date'])
        return df[df['date']==max_date].to_csv()

class CountryDate(Resource):
    def get(self, country_name, date_str):
        df = pd.read_csv("/Users/chvasquez/PycharmProjects/API_Example/covid19.csv")
        df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
        df = df[(df['country']==country_name)]
        return df[df['date']==date_str].to_csv()

api.add_resource(Country, '/<country_name>')

api.add_resource(CountryDate, '/<country_name>/<date_str>')

if __name__ == '__main__':
    app.run(debug=True)
