from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostelfinder.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['postgres://tixzqghxamvlqb:098bf3ec80eb9e7e3fedfd883e4ba0093592fc51e662d05f173b139d132c3ce2@ec2-107-20-230-70.compute-1.amazonaws.com:5432/dbqa66b5uv87ic']

db = SQLAlchemy(app)
login_manager = LoginManager(app)


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ('obengboatengjohnson')
app.config['MAIL_PASSWORD'] = ('johnny@1998')

mail = Mail(app)


from project import routes