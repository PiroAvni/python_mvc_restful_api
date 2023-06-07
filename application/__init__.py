from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from application import forms

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY']='91eaf8b20f28eaaf633f2217d77015ab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yabqzbvt:yefwOe3qoKVaVup0eNmlNCPecRbTP8l-@lucky.db.elephantsql.com/yabqzbvt'
db = SQLAlchemy(app)

from application import models


from application import routes

if __name__ == '__main__':
    app.run()