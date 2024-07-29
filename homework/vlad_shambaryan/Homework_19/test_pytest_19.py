import pytest
import requests


@pytest.fixture()
def new_object_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"https://api.restful-api.dev/objects/{object_id}")


@pytest.fixture(scope="session")
def for_all_session():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def for_every_sessions():
    print("Before test")
    yield
    print("After test")


def test_get_one_object(new_object_id, for_all_session, for_every_sessions):
    response = requests.get(f"https://api.restful-api.dev/objects/{new_object_id}").json()
    assert response["id"] == new_object_id


@pytest.mark.medium
def test_get_all_objects(for_all_session, for_every_sessions):
    response = requests.get("https://api.restful-api.dev/objects").json()
    assert len(response) == 13


@pytest.mark.parametrize("body", [{"name": "Dell", "date": {"Price": "2000.99", "Memory": "1 TB"}},
                                  {"name": "Lenovo", "date": {"Price": "1500", "Memory": "2 TB"}},
                                  {"name": "Acer", "date": {"Price": "1400", "Memory": "1.5 TB"}}
                                  ])
def test_add_object(for_all_session, for_every_sessions, body):
    headers = {"Content_Type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["id"]


def test_update_one_object(new_object_id, for_every_sessions):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{new_object_id}",
        json=body,
        headers=headers
    ).json()
    assert response["data"]["color"] == "silver", "Цвет не правильно обновлен"


def test_update_object_year(new_object_id, for_every_sessions):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{new_object_id}",
        json=body,
        headers=headers
    ).json()
    assert response["data"]["year"] == 2024, "year не правильно обновлен"


@pytest.mark.critical
def test_update_object_name(new_object_id, for_every_sessions):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {"Content_Type": "application/json"}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{new_object_id}",
        json=body,
        headers=headers
    ).json()
    assert response["name"] == "Apple MacBook Pro 16 (Updated Name)", "Имя обновлено неправильно"


def test_delete_object(new_object_id, for_every_sessions):
    response = requests.delete(f"https://api.restful-api.dev/objects/{new_object_id}")
    assert response.status_code == 200
