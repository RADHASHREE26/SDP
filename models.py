from app import db

class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'
    __table_args__ = {"schema":"dbo"}
    user_id = db.Column(db.String(300), primary_key = True)
    user_pw = db.Column(db.String(300))
    created_on = db.Column(db.DateTime)
    updated_on = db.Column(db.DateTime)

class UserDetails(db.Model):
    __tablename__ = 'user_account_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer)
    user_id = db.Column(db.String(300), primary_key = True)
    username = db.Column(db.String(300))
    contact_number = db.Column(db.Integer)
    contact_email = db.Column(db.String(300))
    address = db.Column(db.String)
    created_on = db.Column(db.DateTime)
    updated_on = db.Column(db.Datetime)