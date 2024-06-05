from app import db

class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(300))
    user_pw = db.Column(db.String(300))
    created_on = db.Column(db.DateTime)
    updated_on = db.Column(db.DateTime)

class UserDetails(db.Model):
    __tablename__ = 'user_account_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(300))
    username = db.Column(db.String(300))
    contact_number = db.Column(db.Integer)
    contact_email = db.Column(db.String(300))
    address = db.Column(db.String)
    created_on = db.Column(db.DateTime)
    updated_on = db.Column(db.DateTime)

class AdminDetails(db.Model):
    __tablename__ = 'admin_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    admin_id = db.Column(db.String(300))
    admin_pw = db.Column(db.String(300))
    admin_email = db.Column(db.String(300))

class EquipmentDetails(db.Model):
    __tablename__ = 'equipment_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    equipment_id = db.Column(db.String(300))
    belongs_to = db.Column(db.String(300))
    equipment_name = db.Column(db.String(300))
    equipment_type = db.Column(db.String(300))
    equipment_description = db.Column(db.String(300))
    age = db.Column(db.Integer)
    location = db.Column(db.String(300))
    rent = db.Column(db.Integer)
    availability = db.Column(db.String(300))
    image_file = db.Column(db.LargeBinary)
    payment_id = db.Column(db.String(300))

class EquipmentReviews(db.Model):
    __tablename__ = 'equipment_reviews'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    equipment_id = db.Column(db.String(300))
    belongs_to = db.Column(db.String(300))
    review_by = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    review = db.Column(db.String(300))
    reviewed_on = db.Column(db.DateTime)

class UserPurchaseDetails(db.Model):
    __tablename__ = 'user_purchase_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(300))
    equipment_rented = db.Column(db.String(300))
    rented_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    amount_spent = db.Column(db.Integer)

class UserSaleDetails(db.Model):
    __tablename__ = 'user_sale_details'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(300))
    equipment_lended = db.Column(db.String(300))
    rented_to = db.Column(db.String(300))
    lend_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    earning = db.Column(db.Integer)

class PlatformReview(db.Model):
    __tablename__ = 'platform_review'
    __table_args__ = {"schema":"dbo"}
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    updated_on = db.Column(db.DateTime)