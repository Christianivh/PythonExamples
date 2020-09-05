from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

class CovidPeru(Resource):
    def get(self):
        df = pd.read_csv("/Users/chvasquez/PycharmProjects/API_Example/covid19.csv")
        df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
        df = df[(df['country']=='Peru') & (df['date'] == '2020-09-02')]
        return df.to_csv()

api.add_resource(CovidPeru, '/')

if __name__ == '__main__':
    app.run(debug=True)

