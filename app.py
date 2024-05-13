import datetime
import json
import pymssql
from sqlalchemy import and_, desc, or_
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
                setattr(self, x.name, p_dict.get(x.name))c

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
    # else:
    #     data = json.loads(request.data)
    #     user_id = data['user_id']
    #     db_entry = db.session.query(UserDetails).filter(UserDetails.user_id == user_id).first()


@app.route('/equipment_lending/<user_id>', methods=['GET','POST'])
def equipment_lending(user_id):
    if request.method == 'POST':
        data = json.loads(request.data)
        user_id = data['user_id']
        new_equiment_id = 0
        db_entry = db.session.query(EquipmentDetails).filter(EquipmentDetails.user_id == user_id).order_by(desc(EquipmentDetails.equipment_id)).first()
        if db_entry:
            last_equiment_id = db_entry.equipment_id
            number_part = int(last_equiment_id[1:])
            new_number_part = number_part + 1
            new_equiment_id = "E" + str(new_number_part)
        else:
            new_equiment_id = "E1"
            db_entry = EquipmentDetails()
            db_entry.equipment_id = new_equiment_id
            db_entry.belongs_to = user_id
            db_entry.equipment_name = data['equipment_name']
            db_entry.equipment_type = data['equipment_type']
            db_entry.equipment_description = data['equipment_description']
            db_entry.age = data['age']
            db_entry.location = data['location']
            db_entry.rent = data['rent']
            db_entry.availability = data['availability']
            db_entry.payment_id = None
            db.session.add(db_entry)
            db.session.commit()
    else:
        db_entry = db.session.query(EquipmentDetails).filter(EquipmentDetails.belongs_to == user_id).all()
        equipments_list = []
        for i in db_entry:
            c = {}
            c = {
                "equipment_id": i.equipment_id,
                "equipment_name": i.equipment_name,
                "equipment_type": i.equipment_type,
                "equipment_description": i.equipment_description,
                "age": i.age,
                "location": i.location,
                "rent": i.rent,
                "availability": i.availability
            }
            equipments_list.append(c)
        return equipments_list
    
@app.route('/product_details/<user_id>/<equipment_id>', methods = ['GET','POST'])
def product_details(user_id, equipment_id):
    db_entry = db.session.query(EquipmentDetails).filter(and_(EquipmentDetails.equipment_id == equipment_id, EquipmentDetails.belongs_to == user_id, EquipmentDetails.availability == 'Y')).first()
    if db_entry:
        c = {}
        c = {
            "equipment_id": db_entry.equipment_id,
            "equipment_name": db_entry.equipment_name,
            "equipment_type": db_entry.equipment_type,
            "equipment_description": db_entry.equipment_description,
            "age": db_entry.age,
            "location": db_entry.location,
            "rent": db_entry.rent,
            "availability": db_entry.availability
        }
        return c
    else:
        return jsonify({"status":"product information not found"})
    
@app.route('/search_product', methods = ['GET','POST'])
def search_product():
    if request.method == 'POST':
        data = json.loads(request.data)
        match_word = data['word']
        db_entry = db.session.query(EquipmentDetails).filter(or_(EquipmentDetails.equipment_type == match_word, EquipmentDetails.equipment_description.like(f"%{match_word}%")), EquipmentDetails.equipment_name.like(f"%{match_word}")).all()
        equipments_list = []
        for i in db_entry:
            c = {}
            c = {
                "equipment_id": i.equipment_id,
                "equipment_name": i.equipment_name,
                "equipment_type": i.equipment_type,
                "equipment_description": i.equipment_description,
                "age": i.age,
                "location": i.location,
                "rent": i.rent,
                "availability": i.availability
            }
            equipments_list.append(c)
        return equipments_list
        

if __name__ == '__main__':
    app.run()