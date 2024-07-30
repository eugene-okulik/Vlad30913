import allure
import requests

BASE_URL = "https://api.restful-api.dev/objects"

@allure.feature("Delete request")
@allure.story("Удалить объект")
@allure.title("Deleting object information")
def test_delete_object(new_object_id, for_every_sessions):
    with allure.step(f"Send request {BASE_URL}/{new_object_id}"):
        response = requests.delete(f"{BASE_URL}/{new_object_id}")
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200
