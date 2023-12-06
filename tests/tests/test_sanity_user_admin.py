from saiyan import Saiyanquest
import pytest
from utils import complete_generate_user
import json

#URL = 'https://doevida.onrender.com/'
URL = 'http://localhost:5000/'


def route(route, sub_route=None):
    return f'{route}/{sub_route}'


def decode_json(json_data, key1, key2=None):
    if key2:
        return json.loads(json_data.content.decode('utf-8'))[key1][key2]
    return json.loads(json_data.content.decode('utf-8'))[key1]


@pytest.fixture(scope='session')
def quest():
    quest = Saiyanquest(URL)
    return quest


def test_login_as_admin(quest):
    try:
        quest.get_access_token(user=dict(username="doe.vidaesangue@gmail.com", password="doevida2023"))
        assert quest.access_token is not None
    except Exception as e:
        raise e


def test_access_to_any_user_route(quest):
    try:
        response = quest.get(route("users", 6), by_id=True)
        assert response.status_code == 200 and decode_json(response, "data", "id") == "6"
    except Exception as e:
        raise e
