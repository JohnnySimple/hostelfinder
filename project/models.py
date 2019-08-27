from project import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from project import app


@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	user_posts = db.relationship('Posts', backref='pst')

	def __repr__(self):
		return format("User(" + self.username + "," + self.email + "," + str(self.phone) + ")")

class Posts(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	school = db.Column(db.String(60), nullable=False)
	hostel = db.Column(db.String(60), nullable=False)
	location = db.Column(db.String(60), nullable=False)
	rating = db.Column(db.Integer, nullable=False)
	imageName = db.Column(db.String(300))
	imageData = db.Column(db.LargeBinary)
	roomType = db.Column(db.Integer, nullable=False)
	phone = db.Column(db.String(10), nullable=False)
	price = db.Column(db.Float, nullable=False)
	userId = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return format("Post(" + self.hostel + "," + self.location + "," + self.roomType + ")")
