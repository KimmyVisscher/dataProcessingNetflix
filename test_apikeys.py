from apikeys import *

from test_main import client


# POST apikey

def test_create_api_key_success():
    apikey_data = {
        "apikey": "newkey",
        "role": "JUNIOR"
    }

    response = client.post("/apikeys", json=apikey_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200


def test_create_api_key_unauthorized():
    apikey_data = {
        "apikey": "newkey",
        "role": "JUNIOR"
    }

    response = client.post("/apikeys", json=apikey_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_api_key_no_permission():
    apikey_data = {
        "apikey": "newkey",
        "role": "JUNIOR"
    }

    response = client.post("/apikeys", json=apikey_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# DELETE apikey

def test_delete_api_key_success():
    response = client.delete("/apikeys/unauthorizedkey", headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == {"message": "API key deleted successfully"}


def test_delete_api_key_unauthorized():
    response = client.delete("/apikeys/unauthorizedkey")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_delete_api_key_not_found():
    response = client.delete("/apikeys/nonexistentkey", headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "API key not found"
    }


def test_delete_api_key_no_permission():
    response = client.delete("/apikeys/unauthorizedkey", headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET apikey

def test_read_apikey_json_response():
    response = client.get("/apikey/senior", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "role": "SENIOR",
        "apikey": "senior"
    }


def test_read_apikey_xml_response():
    response = client.get("/apikey/senior", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<apikey><apikey>senior</apikey><role>Role.SENIOR</role></apikey>" or response.text == "<apikey><role>Role.SENIOR</role><apikey>senior</apikey></apikey>"


def test_read_apikey_unauthorized():
    response = client.get("/apikey/senior")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_apikey_not_found():
    response = client.get("/apikey/nonexistentkey", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "APIKey not found"
    }


def test_read_movie_no_permission():
    response = client.get("/apikey/senior", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }
