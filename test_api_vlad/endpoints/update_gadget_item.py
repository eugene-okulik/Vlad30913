import requests
import allure
from test_api_vlad.endpoints.base_endpoint import Endpoint


class UpdateGadgetItem(Endpoint):

    @allure.step("Update the gadget name")
    def update_gadget_name(self, gadget_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{gadget_id}",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
