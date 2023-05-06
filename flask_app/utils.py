import re
import jwt
from flask import jsonify, request, g
from functools import wraps
from . import app
from jwt.exceptions import DecodeError, ExpiredSignatureError
from datetime import datetime

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Verifica se o token está presente nos headers da requisição
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
            #token = token.split(' ')
            #token = token[0]
        print(token)
        
        
        # Caso o token não esteja presente
        if not token:
            return jsonify({'error': 'Token não encontrado!'}), 401

        try:
            # Decodifica o token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            exp = data.get("exp")
            if exp is not None:
                now = datetime.utcnow()
                if now < datetime.fromtimestamp(exp):
                    return jsonify({'mensagem': 'Token de acesso expirado'}), 401
            g.current_user = data

        except ExpiredSignatureError:
            return jsonify({'error': 'Token expirado!'}), 401
        except DecodeError:
            return jsonify({'error': 'Token inválido!'}), 401

        # Passa o identificador do usuário como argumento para a função da rota
        return f(data['username'], *args, **kwargs)

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