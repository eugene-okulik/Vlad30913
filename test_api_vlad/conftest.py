import pytest
from test_api_vlad.endpoints.get_gadget import GetOneGadget
from test_api_vlad.endpoints.get_gadget import GetAllGadgets
from test_api_vlad.endpoints.create_gadget import CreateGadget
from test_api_vlad.endpoints.update_gadget import UpdateGadget
from test_api_vlad.endpoints.delete_gadget import DeleteGadget
from test_api_vlad.endpoints.update_gadget_item import UpdateGadgetItem


@pytest.fixture()
def get_one_gadget_endpoint():
    return GetOneGadget()


@pytest.fixture()
def get_all_gadgets_endpoint():
    return GetAllGadgets()


@pytest.fixture()
def create_gadget_endpoint():
    return CreateGadget()


@pytest.fixture()
def update_gadget_endpoint():
    return UpdateGadget()


@pytest.fixture()
def update_gadget_item_endpoint():
    return UpdateGadgetItem()


@pytest.fixture()
def delete_gadget_endpoint():
    return DeleteGadget()


@pytest.fixture()
def new_gadget_id_endpoint(create_gadget_endpoint, delete_gadget_endpoint):
    payload = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                        "Hard disk size": "1 TB"}}
    create_gadget_endpoint.add_new_gadget(payload)
    gadget_id = create_gadget_endpoint.gadget_id
    print(f"New gadget id: {gadget_id} created")
    yield gadget_id
    delete_gadget_endpoint.delete_gadget(gadget_id)


@pytest.fixture()
def delete_gadget_id_endpoint(create_gadget_endpoint, delete_gadget_endpoint):
    payload = {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                        "Hard disk size": "1 TB"}}
    create_gadget_endpoint.add_new_gadget(payload)
    gadget_id = create_gadget_endpoint.gadget_id
    print(f"New gadget id: {gadget_id} created")
    yield gadget_id
