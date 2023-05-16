import re
import jwt
from flask import jsonify, request
from functools import wraps
from . import app
from flask_app.models import Hospitals

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('Token')

        print(request.url)
        print(token)

        if not token:
            return jsonify({'mensagem': 'Token ausente!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'mensagem': 'Token inválido!'}), 403

        return f(*args, **kwargs)

    return decorated


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_username(email):
    if len(email) > 80:
        return {"Erro": "Seu email precisa ter menos que 80 caracteres."}
    if email is None or len(email) == 0:
        return {"Erro": "O campo e-mail não pode estar vazio."}
    if is_valid_email(email) == False:
        return {"Erro": "O e-mail não é válido."}
    return None

def check_and_update(user, **json_data):
    if json_data.get('first_name') is not None:
        user.first_name = json_data['first_name']
    if json_data.get('last_name') is not None:
        user.last_name = json_data['last_name']
    if json_data.get('birthdate') is not None:
        user.birthdate = json_data['birthdate']
    if json_data.get('blood_type') is not None:
        user.blood_type = json_data['blood_type']
    if json_data.get('phone') is not None:
        user.phone = json_data['phone']
    if json_data.get('sex') is not None:
        user.sex = json_data['sex']
    if json_data.get('qty_donations') is not None:
        user.qty_donations = json_data['qty_donations']
    if json_data.get('date_last_donation') is not None:
        user.date_last_donation = json_data['date_last_donation']
    if json_data.get('state') is not None:
        user.state = json_data['state']
    if json_data.get('city') is not None:
        user.city = json_data['city']
    return user

def check_and_update_hospitals(hospital, **json_data):
  if json_data.get('hospital_name') is not None:
    hospital.hospital_name = json_data['hospital_name']
  if json_data.get('city_name') is not None:
    hospital.city_name = json_data['city_name']
  if json_data.get('state') is not None:
    hospital.state = json_data['state']
  if json_data.get('donations_orders') is not None:
    hospital.donations_orders = json_data['donations_orders']
  if json_data.get('donations_orders_done') is not None:
    hospital.donations_orders_done = json_data['donations_orders_done']
  if json_data.get('donations_orders_cancelled') is not None:
    hospital.donations_orders_cancelled = json_data['donations_orders_cancelled']
  return hospital

def check_hospital_db(hospital, city_name, state):
    try:
        hospital = Hospitals.query.filter_by(hospital_name=hospital).first()
        if hospital.city_name == city_name and hospital.state == state:
            return True
    except:
        return False

