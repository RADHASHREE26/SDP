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
    user_id = db.Column(db.String(300), primary_key = True)
    username = db.Column(db.String(300))
    contact_number = db.Column(db.Integer)
    contact_email = db.Column(db.String(300))
    address = db.Column(db.String)
    created_on = db.Column(db.DateTime)
    updated_on = db.Column(db.Datetime)

class AdminDetails(db.Model):
    __tablename__ = 'admin_details'
    __table_args__ = {"schema":"dbo"}
    admin_id = db.Column(db.String(300), primary_key = True)
    admin_pw = db.Column(db.String(300))
    admin_email = db.Column(db.String(300))

class EquipmentDetails(db.Model):
    __tablename__ = 'equipment_details'
    __table_args__ = {"schema":"dbo"}
    equipment_id = db.Column(db.String(300))
    user_id = db.Column(db.String(300))
    equipment_name = db.Column(db.String(300))
    equipment_type = db.Column(db.String(300))
    equipment_description = db.Column(db.String(300))
    age = db.Column(db.Integer)
    location = db.Column(db.String(300))
    rent = db.Column(db.Integer)
    availability = db.Column(db.String(300))
    payment_id = db.Column(db.String(300))

class EquipmentReviews(db.Model):
    __tablename__ = 'equipment_reviews'
    __table_args__ = {"schema":"dbo"}
    equipment_id = db.Column(db.String(300))
    belongs_to = db.Column(db.String(300))
    review_by = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    review = db.Column(db.String(300))
    reviewed_on = db.Column(db.Datetime)

class UserPurchaseDetails(db.Model):
    __tablename__ = 'user_purchase_details'
    __table_args__ = {"schema":"dbo"}
    user_id = db.Column(db.String(300))
    equipment_rented = db.Column(db.String(300))