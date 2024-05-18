from flask import Flask, render_template, request, url_for, flash, redirect
from flask import send_from_directory
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, PasswordField,
                                         RadioField)
from wtforms.validators import InputRequired, Length
from flask_argon2 import argon2

# ...
#from flask import Flask, render_template
class RegisterForm(FlaskForm):
        username = StringField('Username', validators=[InputRequired(),
                                                                                         Length(min=10, max=32)])
        email = StringField('Email', validators=[InputRequired(),
                                                                                         Length(min=10, max=64)])
        password = PasswordField('Password', validators=[InputRequired(),
                                                                                         Length(min=10, max=64)])
        
 


app = Flask(__name__,
        static_url_path='', 
        static_folder='static',)

messages = [{'title': 'Proof of Concept Test App',
                         'content': 'andriod/ios authentication backe'},
                        {'title': 'Login Status',
                         'content': 'True/False'}
                        ]

@app.route('/')
def index():
        return render_template('index.html', messages=messages)

@app.route('/login/', methods=('GET', 'POST'))
def login():
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
        
                messages.append({'username': username, 'password': password })
                 
                return redirect(url_for('index'))
        return render_template('login.html')

@app.route('/register/', methods=('GET', 'POST'))
def register():
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                email = request.form['email'] 
                messages.append({'username': username, 'password': password,
                                'email' : email,})
                return redirect(url_for('index'))
        return render_template('register.html')


#@app.route('/css/<path:path>')
#def static_css(path):
#    reurn send_from_directory('css', path)
    
