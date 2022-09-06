import os
from flask import Flask
from application.database import db
import sqlite3
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.schema import ForeignKey

cdir=os.path.abspath(os.path.dirname(__file__))
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+ os.path.join(cdir,"app.db")
db.init_app(app)
api=Api(app)
app.app_context().push()
from application.controllers import *

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',debug='True',port=8100)
