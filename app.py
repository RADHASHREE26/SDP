import datetime
import json
import pymssql
from sqlalchemy import and_
from flask import Flask, render_template, request, Response, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
import sqlalchemy
from models import *

app = Flask(__name__)

db_string = "mssql+pymssql://Bose01:Bose01@Radhashree:1433/farming_rental"
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

# conn = pymssql.connect(server='Radhashree', user='Bose01', password='Bose01', database='farming_rental')

def from_dict(self, p_dict):
    for x in self.__table__.columns:
        if x.name in p_dict.keys():
            if isinstance(x.type, db.DateTime):
                setattr(self, x.name, datetime.strptime(
                    p_dict.get(x.name), '%Y-%m-%d %H:%m:%S'))
            elif isinstance(x.type, db.Data):
                setattr(self, x.name, datetime.strptime(
                    p_dict.get(x.name), '%Y-%m-%d'))
            else:
                setattr(self, x.name, p_dict.get(x.name))

@app.route('/user_login', methods = ['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        data = json.loads(request.data)
        var_user_id = data['user_id']
        var_user_pw = data['user_pw']
        print(data)
        db_entry = db.session.query(UserCredentials).filter(and_(UserCredentials.user_id == var_user_id, UserCredentials.user_pw == var_user_pw)).first()
        print(db_entry)
        if db_entry:
            return jsonify({'status':'valid user'})
        else:
            return jsonify({'status':'invalid user'})
    return jsonify({"status":"ok"}), 200
        
@app.route('/user_signup', methods = ['GET','POST'])
def user_signup():
    if request.method == 'POST':
        print(request.data)
        data = json.loads(request.data)
        username = data['username']
        address = data['address']
        email = data['email']
        contact_number = data['contact_number']
        user_id = data['user_id']
        user_pw = data['user_pw']
        created_on = datetime.now()

        db_entry = UserCredentials()
        db_entry.user_id = user_id
        db_entry.user_pw = user_pw
        db_entry.created_on = created_on
        db.session.add(db_entry)
        db.session.commit()

        db_entry = UserDetails()
        db_entry.user_id = user_id
        db_entry.username = username
        db_entry.contact_number = contact_number
        db_entry.contact_email = email
        db_entry.address = address
        db_entry.created_on = created_on
        db.session.add(db_entry)
        db.session.commit()

    return jsonify({"status": "created"}), 201


@app.route('/account_update', methods = ['GET','POST'])
def credentials_update():
    if request.method == 'POST':
        data = request.get_json()
        user_id = data['user_id']
        db_entry = db.session.query(UserDetails).filter(UserDetails.user_id == user_id).first()
        from_dict(db_entry, data)
        db_entry.updated_on = datetime.now()
        db.session.commit()
        return jsonify({"status":"User Details updated"}), 201
        


if __name__ == '__main__':
    app.run()