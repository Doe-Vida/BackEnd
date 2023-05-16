from flask_app import  db, jwt__
from flask import jsonify, request
from flask_app.models import Donation_order, Hospitals, User
from flask_app.utils import check_and_update_hospitals, check_hospital_db
from flask_jwt_extended import jwt_required, get_jwt_identity, create_refresh_token, create_access_token

def get_app():
    from flask_app import app
    return app

app = get_app()

@app.route("/donations_orders")
def get_donations_orders():
  donations_orders = Donation_order.query.all()
  return jsonify(donations_orders=[donation_order.to_dict() for donation_order in donations_orders]), 200

@app.route("/donations_orders/<int:donation_order_id>")
def get_donation_order_by_id(donation_order_id):
  donation_order = Donation_order.query.get(donation_order_id)
  if donation_order is None:
    return jsonify({"error": "Donation order not found"}), 404
  else:
    return jsonify(donation_order.to_dict()), 200
  
@app.route("/donations_orders", methods=["POST"])
def post_donation_order():
  patient_name = request.json["patient_name"]
  blood_type = request.json["blood_type"]
  description = request.json["description"]
  qty_bags = request.json["qty_bags"]
  hospital = request.json["hospital"]
  requester = request.json["requester"]
  city_name = request.json["city_name"]
  state = request.json["state"]

  if check_hospital_db(hospital, city_name, state) == False:
    new_hospital = Hospitals(hospital_name=hospital, city_name=city_name, state=state)
    db.session.add(new_hospital)
    db.session.commit()

  hospital = Hospitals.query.filter_by(hospital_name=hospital).first()
  requester = User.query.get(requester)

  new_donation_order = Donation_order(
    patient_name=patient_name,
    blood_type=blood_type,
    description=description,
    qty_bags=qty_bags,
    hospitals=hospital,
    user=requester
  )

  db.session.add(new_donation_order)
  db.session.commit()

  return jsonify(new_donation_order.to_dict()), 200