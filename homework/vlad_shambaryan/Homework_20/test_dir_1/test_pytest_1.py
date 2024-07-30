import pytest
import requests
import allure

BASE_URL = "https://api.restful-api.dev/objects"


@allure.feature("Get request")
@allure.story("Страница объектов")
@allure.title("Getting information about one objects")
def test_get_one_object(new_object_id, for_all_session, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}/{new_object_id}"):
        response = requests.get(f"{BASE_URL}/{new_object_id}").json()
    with allure.step(f"Check sure the object ID is in the response {new_object_id}"):
        assert response["id"] == new_object_id


@allure.feature("Get request")
@allure.story("Страница объектов")
@allure.title("Check information about all objects")
@pytest.mark.medium
def test_get_all_objects(for_all_session, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}"):
        response = requests.get(f"{BASE_URL}").json()
    with allure.step("Check that the amount of objects is 13"):
        assert len(response) == 12


@allure.feature("Post request")
@allure.story("Создание нового гаджета")
@allure.title("Changing the object color")
@pytest.mark.critical
@pytest.mark.parametrize("body", [{"name": "Dell", "date": {"Price": "2000.99", "Memory": "1 TB"}},
                                  {"name": "Lenovo", "date": {"Price": "1500", "Memory": "2 TB"}},
                                  {"name": "Acer", "date": {"Price": "1400", "Memory": "1.5 TB"}}
                                  ])
def test_add_object(for_all_session, for_every_sessions, body):
    with allure.step(" "):
        headers = {"Content_Type": "application/json"}
        response = requests.post(
            f"{BASE_URL}",
            json=body,
            headers=headers
        )
    with allure.step(" "):
        assert response.status_code == 200
    with allure.step(" "):
        assert response.json()["id"]


@allure.feature("Put request")
@allure.story("Изменить цвет объекта")
@allure.title("Changing the object color")
def test_update_one_object(new_object_id, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}/{new_object_id} with body and headers"):
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
            f"{BASE_URL}/{new_object_id}",
            json=body,
            headers=headers
        ).json()
    with allure.step("Check object information a new color has been added: silver."):
        assert response["data"]["color"] == "silver", "Цвет не правильно обновлен"


@allure.feature("Put request")
@allure.story("Изменить год выпуска объекта")
@allure.title("Changing the object year")
def test_update_object_year(new_object_id, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}/{new_object_id} with body and headers"):
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
    with allure.step("checking object year change"):
        assert response["data"]["year"] == 2024, "год не правильно обновлен"


@allure.feature("Put request")
@allure.story("Изменить цену объекта")
@allure.title("Changing the object price")
def test_update_object_price(new_object_id, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}/{new_object_id} with body and headers"):
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2024,
                "price": 3000,
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
    with allure.step("checking object price change"):
        assert response["data"]["price"] == 3000, "price не правильно обновлен"


@allure.feature("Patch request")
@allure.story("Редактировать имя объекта")
@allure.title("Changing the object name")
def test_update_object_name(new_object_id, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}/{new_object_id} with body and headers"):
        body = {
            "name": "Apple MacBook Pro 16 (Updated Name)"
        }
        headers = {"Content_Type": "application/json"}
        response = requests.patch(
            f"{BASE_URL}/{new_object_id}",
            json=body,
            headers=headers
        ).json()
    with allure.step("checking object name change"):
        assert response["name"] == "Apple MacBook Pro 16 (Updated Name)", "Имя обновлено неправильно"
