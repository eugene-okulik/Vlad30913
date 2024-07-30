import pytest
import requests

BASE_URL = "https://api.restful-api.dev/objects"

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
        f"{BASE_URL}",
        json=body,
        headers=headers
    )
    object_id = response.json()["id"]
    yield object_id
    requests.delete(f"{BASE_URL}/{object_id}")


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
