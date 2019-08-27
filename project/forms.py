from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField,FileRequired
from project.models import Users

# form class for signing up
class signUpForm(FlaskForm):
	username = StringField('USERNAME',
		validators=[DataRequired(), Length(min=2, max=100)])
	email = StringField('EMAIL',
		validators=[DataRequired(), Email()])
	password = PasswordField('PASSWORD',
		validators=[DataRequired()])
	confirm_password = PasswordField('CONFIRM PASSWORD',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('SIGN UP')

	# function to throw an error if student username already exists
	def validate_username(self, username):
		check = Users.query.filter_by(username=username.data).first()
		if check:
			raise ValidationError('The username already exists! Please choose another name.')

	# function to throw an error if student email already exists
	def validate_username(self, email):
		check = Users.query.filter_by(email=email.data).first()
		if check:
			raise ValidationError('The email already exists! Please choose another email.')

# form class for logging in
class loginForm(FlaskForm):
	email = StringField('EMAIL',
		validators=[DataRequired(), Email()])
	password = PasswordField('PASSWORD',
		validators=[DataRequired()])
	submit = SubmitField('LOGIN')

# form class for posts
class postForm(FlaskForm):
	school = SelectField('SCHOOL',
		validators=[DataRequired()], choices=[('KNUST','KNUST'), ('LEGON','LEGON'), ('UDS','UDS'), ('UPSA','UPSA'), ('UEW','UEW'), ('UCC','UCC')])
	hostel = StringField('HOSTEL',
		validators=[DataRequired()])
	location = StringField('LOCATION',
		validators=[DataRequired()])
	rating = SelectField('RATING',
		validators=[DataRequired()], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	image = FileField(validators=[FileRequired()])
	room_type = SelectField('ROOM TYPE',
		validators=[DataRequired()], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
	phone = StringField('PHONE',
		validators=[DataRequired()])
	price = StringField('PRICE',
		validators=[DataRequired()])
	submit = SubmitField('POST')


class contactForm(FlaskForm):
	name = StringField('NAME',
		validators=[DataRequired(), Length(min=2, max=200)])
	email = StringField('EMAIL',
		validators=[DataRequired(), Email()])
	message = StringField('MESSAGE',
		validators=[DataRequired()], widget=TextArea())
	submit = SubmitField('MAIL ME')
