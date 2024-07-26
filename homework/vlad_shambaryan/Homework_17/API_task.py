import requests


def add_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    # Проверяем, что статус-код 200 и есть ID в ответе
    assert response.status_code == 200, f"Не удалось добавить объект: {response.status_code}, {response.text}"
    json_response = response.json()
    assert "id" in json_response, "ID не найдено в ответе"
    print(f"Объект добавлен с ID: {json_response['id']}")


def object_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f"Не удалось создать объект: {response.status_code}, {response.text}"
    json_response = response.json()
    assert "id" in json_response, "ID не найден в ответе"
    return json_response["id"]


def delete_object_id(gadget_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")
    assert response.status_code == 200, f"Не удалось удалить объект: {response.status_code}, {response.text}"


def update_object():
    gadget_id = object_id()
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
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{gadget_id}",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, f"Не удалось обновить объект: {response.status_code}, {response.text}"
    json_response = response.json()
    assert json_response["data"]["color"] == "silver", "Цвет не правильно обновлен"

    print(json_response)
    delete_object_id(gadget_id)


def update_object_name():
    gadget_id = object_id()
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{gadget_id}",
        json=body,
        headers=headers
    )

    assert response.status_code == 200, f"Не удалось обновить имя объекта.: {response.status_code}, {response.text}"
    json_response = response.json()
    assert json_response["name"] == "Apple MacBook Pro 16 (Updated Name)", "Имя обновлено неправильно"
    print(json_response["name"])
    delete_object_id(gadget_id)


def delete_object():
    gadget_id = object_id()
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")
    assert response.status_code == 200, f"Не удалось удалить объект: {response.status_code}, {response.text}"
    print(response.status_code)


add_object()
update_object()
update_object_name()
delete_object()
