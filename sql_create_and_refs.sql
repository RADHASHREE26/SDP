
use farming_rental

create table admin_details(
	id int IDENTITY(1,1),
	admin_id varchar(max),
	admin_pw varchar(max),
	admin_email varchar(max)
)

create table user_credentials(
	id int IDENTITY(1,1),
	[user_id] varchar(max),
	user_pw varchar(max),
	created_on datetime,
	updated_on datetime
)

create table user_details(
	id int IDENTITY(1,1),
	[user_id] varchar(max),
	username varchar(max),
	contact_number int,
	contact_email varchar(max),
	[address] varchar(max),
	created_on datetime,
	updated_on datetime
)

create table equipment_details(
	id int IDENTITY(1,1),
  equipment_id varchar(max),
  belongs_to varchar(max),
  equipment_name varchar(max),
  equipment_type varchar(max),
  equipment_description varchar(max),
  age integer,
  [location] varchar(max),
  rent integer,
  [availability] varchar(max),
  payment_id varchar(max)
)

create table equipment_reviews(
	id int IDENTITY(1,1),
  equipment_id varchar(max),
  belongs_to varchar(max),
  review_by varchar(max),
  rating varchar(max),
  review varchar(max),
  reviewed_on datetime
)

create table payment_details(
	id int IDENTITY(1,1),
  payment_for varchar(max),
  payment_id varchar(max),
  payment_amount integer,
  payment_mode varchar(max),
  delivery_id varchar(max),
)

create table delivery_details(
	id int IDENTITY(1,1),
  delivery_id varchar(max),
  deliver_to varchar(max),
  collect_from varchar(max),
  drop_to varchar(max),
  delivery_partner varchar(max),
  delivery_executive varchar(max),
  delivery_fees integer,
  estimated_delivery_date datetime,
  actual_delivery_date datetime
)

create table address_book(
	id int IDENTITY(1,1),
  address varchar(max),
  pincode integer,
  city varchar(max),
  state varchar(max),
  country varchar(max),
)

create table user_purchase_details(
	id int IDENTITY(1,1),
  user_id varchar(max),
  equipment_rented varchar(max),
  rented_date datetime,
  return_date datetime,
  amount_spent integer
)

create table user_sale_details(
	id int IDENTITY(1,1),
  user_id varchar(max),
  equiment_lended varchar(max),
  rented_to varchar(max),
  lend_date datetime,
  return_date datetime,
  earning integer
)

create table platform_review(
	id int IDENTITY(1,1),
  user_id varchar(max),
  rating integer,
  review varchar(max),
  updated_on varchar(max),
)
