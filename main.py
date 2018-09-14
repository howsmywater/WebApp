from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "219nv8438vncjkxjfg9904jkcod4niv90"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Might be needed included only for development side, once launched can remove this as it should be https
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

@app.route('/')
@app.route('/home')
def check():
    print("went into and running")
    

if __name__ == '__main__':
    app.run(debug=True)
