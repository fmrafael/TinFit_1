from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

from flask_bootstrap import Bootstrap
import smtplib
import requests


#OWN_EMAIL = YOUR OWN EMAIL ADDRESS
#OWN_PASSWORD = YOUR EMAIL ADDRESS PASSWORD

#API_KEY  

class LoginForm(FlaskForm):
  email = StringField()
  submit = SubmitField(label='Cadastrar email')

app = Flask(__name__)
app.secret_key = "teste-key"
Bootstrap(app)


@app.route('/')
def home():
  login_form = LoginForm()
  return render_template('index.html',form=login_form)
  



@app.route('/login.html',methods=["GET","POST"])
def login():
  return render_template("success.html")
  

  
 


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8000)