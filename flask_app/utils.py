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