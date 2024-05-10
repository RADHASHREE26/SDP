import json
from sqlalchemy import and_
from flask import Flask, render_template, request, Response, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import sqlalchemy
from models import *

app = Flask(__name__)

db_string = "mssql+pymssql://"+ 'Bose01' + ":" + 'Bose01' + "@" + 'Radhashree' + "/" + 'farming_rental'
app.config['SQLALCHEMY_DATABASE_URI'] = db_string


db = SQLAlchemy(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
sh.setFormatter(formatter)
logger.addHandler(sh)


conn = sqlalchemy.create_engine(db_string)

@app.route('/user_login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        data = json.loads(request.data)
        user_id = data['user_id']
        user_pw = data['user_pw']
        db_entry = db.session.query(UserCredentials).filter(and_(UserCredentials.user_id == user_id, UserCredentials.user_pw == user_pw)).first()
        if db_entry:
            return jsonify({'status':'valid user'})
        else:
            return jsonify({'status':'invalid user'})
        
@app.route('/user_signup', methods = ['GET','POST'])
def user_signup():
    if request.method == 'POST':
        data = json.loads(request.data)
        username = data['username']
        address = data['address']
        email = data['email']
        contact_number = data['contact_number']
        user_id = data['user_id']
        user_pw = data['user_pw']
        db_entry = UserCredentials()
        db_entry.user_id = user_id
        db_entry.user_pw = user_pw
        db.session.add(db_entry)
        db.session.commit()

        db_entry = UserAccountDetails()
        db_entry.user_id = user_id
        db_entry.contact_number = contact_number
        db_entry.contact_email = email
        db_entry.address = address


if __name__ == '__main__':
    app.run()