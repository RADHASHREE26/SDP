from app import db

class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer)
    user_id = db.Column(db.String(300), primary_key = True)
    user_pw = db.Column(db.String(300))

class UserAccountDetails(db.Model):
    __tablename__ = 'user_account_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer)
    user_id = db.Column(db.String(300), primary_key = True)
    # username = db.Column(db.)