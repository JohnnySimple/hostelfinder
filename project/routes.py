from flask import render_template, flash, url_for,redirect, request, send_from_directory
from project import app
from project import db, mail
from project.forms import signUpForm, loginForm, postForm, contactForm
from project.models import Users, Posts
import os
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user, logout_user
from flask_mail import Message

UPLOAD_FOLDER = 'D:/personalWebsite/projs/hostelFinder/project/static/post_imgs'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
	rooms = Posts.query.all()
	form = contactForm()
	return render_template("index.html", rooms=rooms, form=form)

@app.route('/signUp', methods=['GET','POST'])
def signUp():
	signupform = signUpForm()
	form = contactForm()
	if signupform.validate_on_submit():
		new_user = Users(username=signupform.username.data, email=signupform.email.data, password=signupform.password.data)
		db.session.add(new_user)
		db.session.commit()

		return redirect('login')

	return render_template("signup.html",signupform=signupform, form=form)

@app.route('/login', methods=['GET','POST'])
def login():
	loginform = loginForm()
	form = contactForm()

	if loginform.validate_on_submit():
		user = Users.query.filter_by(email=loginform.email.data).first()
		if user and user.password == loginform.password.data:
			login_user(user)
			return redirect('dashboard')
		else:
			flash('Username or password incorrect!', 'danger')

	return render_template("login.html",loginform=loginform, form=form)

@app.route('/dashboard')
def dashboard():
	form = postForm()
	mailForm = contactForm()
	# user = Users.query.all()
	myposts = Posts.query.all()

	return render_template("dashboard.html", form=form, myposts=myposts, mailForm=mailForm)


def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['GET', 'POST'])
def upload():
	form = postForm()

	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(url_for('posts_page'))
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(url_for('posts-page'))
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			new_post = Posts(school= form.school.data, hostel= form.hostel.data, location=form.location.data, 
				rating=int(form.rating.data), roomType=form.room_type.data, 
				phone=form.phone.data, price=float(form.price.data), imageName=file.filename, imageData=file.read(),
				userId=current_user.id)
			db.session.add(new_post)
			db.session.commit()
		
			return redirect(url_for('uploaded_file', filename=filename))

	return 'successful'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


@app.route('/delete_post/<postid>', methods=['GET', 'POST'])
def delete_post(postid):
	post = Posts.query.filter_by(id=postid).delete()
	db.session.commit()
	flash('One post deleted', 'danger')
	return redirect(url_for('dashboard'))


#route for user to contact us
@app.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
	form = contactForm()
	msg = Message(form.email.data, sender='obengboatengjohnson@gmail.com', recipients=['obengjohnsonboateng@gmail.com'])
	msg.body = form.message.data
	mail.send(msg)
	return 'Email Sent!'


# @app.route('/layout')
# def layout():
# 	form = contactForm()
# 	return render_template("layout.html")

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))