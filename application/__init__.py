from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://akcuzyce:Jr4aIrJrQ8rtedjAPbe9ONUpiYC4s1Lp@lucky.db.elephantsql.com/akcuzyce'
db = SQLAlchemy(app)

from application import models


from application import routes

if __name__ == '__main__':
    app.run()