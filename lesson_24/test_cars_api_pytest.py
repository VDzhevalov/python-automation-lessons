import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger("car_search_test")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", mode='w', encoding='utf-8')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def session_with_token():
    session = requests.Session()

    logger.info("Авторизація користувача...")
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth('test_user', 'test_pass')
    )

    assert response.status_code == 200, f"Логін провалено: {response.text}"
    token = response.json().get("access_token")
    assert token, "Не отримано токен"

    session.headers.update({
        "Authorization": f"Bearer {token}"
    })

    logger.info("Токен додано в заголовки сесії")
    return session


def test_auth_success():
    response = requests.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth('test_user', 'test_pass')
    )
    logger.info(f"Авторизація: статус {response.status_code}, відповідь: {response.text}")
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_auth_failure():
    response = requests.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth('wrong_user', 'wrong_pass')
    )
    logger.info(f"Невдала авторизація: статус {response.status_code}, відповідь: {response.text}")
    assert response.status_code == 401


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 10),
    ("engine_volume", 7),
    ("brand", 3),
])
def test_car_search_with_params(session_with_token, sort_by, limit):
    params = {"sort_by": sort_by, "limit": limit}
    response = session_with_token.get(f"{BASE_URL}/cars", params=params)

    logger.info(f"Пошук: sort_by={sort_by}, limit={limit}, статус={response.status_code}")
    logger.info(f"Відповідь: {response.text}")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= limit
    assert all(sort_by in car for car in data)


@pytest.mark.parametrize("sort_by", ["price", "year", "engine_volume"])
def test_car_sorting(session_with_token, sort_by):
    params = {"sort_by": sort_by, "limit": 10}
    response = session_with_token.get(f"{BASE_URL}/cars", params=params)
    logger.info(f"Перевірка сортування за {sort_by}, статус={response.status_code}")

    assert response.status_code == 200
    data = response.json()
    values = [car[sort_by] for car in data]
    logger.info(f"{sort_by}: {values}")
    assert values == sorted(values), f"Дані не відсортовані по '{sort_by}'"