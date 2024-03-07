from preferences import *

from test_main import client


# GET genrepreference by profile ID

def test_read_genrepreference_by_profile_json_response():
    response = client.get("/profiles/1/genrepreference", headers={"X-API-KEY": "senior"})

    expected_data = [
        {
            "profile_id": 1,
            "genre": "ACTION",
            "genrepreference_id": 1
        },
        {
            "profile_id": 1,
            "genre": "FANTASY",
            "genrepreference_id": 2
        }
    ]

    assert response.status_code == 200
    assert response.json() == expected_data


def test_read_genrepreference_by_profile_xml_response():
    response = client.get("/profiles/1/genrepreference", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<genrepreferences>\n  <genreprefence>\n      <genrepreference_id>1</genrepreference_id>\n      <genre>Genre.ACTION</genre>\n      <profile_id>1</profile_id>\n </genrepreference>  <genreprefence>\n      <genrepreference_id>2</genrepreference_id>\n      <genre>Genre.FANTASY</genre>\n      <profile_id>1</profile_id>\n </genrepreference></genrepreferences>"


def test_read_genrepreference_by_profile_unauthorized():
    response = client.get("/profiles/1/genrepreference")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_genrepreference_by_profile_not_found():
    response = client.get("/profiles/6/genrepreference", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No genrepreferences found"
    }


def test_read_genrepreference_by_profile_no_permission():
    response = client.get("/profiles/1/genrepreference", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET genrepreference by ID

def test_read_genrepreference_by_id_json_response():
    response = client.get("/genrepreferences/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "profile_id": 1,
        "genre": "ACTION",
        "genrepreference_id": 1
    }


def test_read_genrepreference_by_id_xml_response():
    response = client.get("/genrepreferences/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<genrepreferences>\n  <genreprefence>\n      <genrepreference_id>1</genrepreference_id>\n      <genre>Genre.ACTION</genre>\n      <profile_id>1</profile_id>\n </genrepreference></genrepreferences>"


def test_read_genrepreference_by_id_unauthorized():
    response = client.get("/genrepreferences/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_genrepreference_by_id_not_found():
    response = client.get("/genrepreferences/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No genrepreferences found"
    }


def test_read_genrepreference_by_id_no_permission():
    response = client.get("/genrepreferences/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET indicationpreference by profile ID

def test_read_indicationpreference_by_profile_json_response():
    response = client.get("/profiles/1/indicationpreferences", headers={"X-API-KEY": "senior"})

    expected_data = [
        {
            "profile_id": 1,
            "indication": "VIOLENCE",
            "indicationpreference_id": 1
        },
        {
            "profile_id": 1,
            "indication": "PROFANITY_USAGE",
            "indicationpreference_id": 2
        }
    ]

    assert response.status_code == 200
    assert response.json() == expected_data


def test_read_indicationpreference_by_profile_xml_response():
    response = client.get("/profiles/1/indicationpreferences", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<indicationpreferences>\n  <indicationprefence>\n      <indicationpreference_id>1</indicationpreference_id>\n      <indication>ViewerIndication.VIOLENCE</indication>\n      <profile_id>1</profile_id>\n </indicationpreference>  <indicationprefence>\n      <indicationpreference_id>2</indicationpreference_id>\n      <indication>ViewerIndication.PROFANITY_USAGE</indication>\n      <profile_id>1</profile_id>\n </indicationpreference></indicationpreferences>"


def test_read_indicationpreference_by_profile_unauthorized():
    response = client.get("/profiles/1/indicationpreferences")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_indicationpreference_by_profile_not_found():
    response = client.get("/profiles/6/indicationpreferences", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No indicationpreferences found"
    }


def test_read_indicationpreference_by_profile_no_permission():
    response = client.get("/profiles/1/indicationpreferences", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET indicationpreference by ID

def test_read_indicationpreference_by_id_json_response():
    response = client.get("/indicationpreferences/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "profile_id": 1,
        "indication": "VIOLENCE",
        "indicationpreference_id": 1
    }


def test_read_indicationpreference_by_id_xml_response():
    response = client.get("/indicationpreferences/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<indicationpreferences>\n  <indicationprefence>\n      <indicationpreference_id>1</indicationpreference_id>\n      <indication>ViewerIndication.VIOLENCE</indication>\n      <profile_id>1</profile_id>\n </indicationpreference></indicationpreferences>"


def test_read_indicationpreference_by_id_unauthorized():
    response = client.get("/indicationpreferences/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_indicationpreference_by_id_not_found():
    response = client.get("/indicationpreferences/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No indicationpreferences found"
    }


def test_read_indicationpreference_by_id_no_permission():
    response = client.get("/indicationpreferences/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET agepreference by profile ID

def test_read_agepreferences_by_profile_json_response():
    response = client.get("/profiles/1/agepreferences", headers={"X-API-KEY": "senior"})

    expected_data = [
        {
            "profile_id": 1,
            "agerestriction": "SIX_YEARS",
            "agepreference_id": 1
        },
        {
            "profile_id": 1,
            "agerestriction": "TWELVE_YEARS",
            "agepreference_id": 2
        }
    ]

    assert response.status_code == 200
    assert response.json() == expected_data


def test_read_agepreferences_by_profile_xml_response():
    response = client.get("/profiles/1/agepreferences", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<agepreferences>\n  <agepreference>\n      <agepreference_id>1</agepreference_id>\n      <agerestriction>AgeRestriction.SIX_YEARS</agerestriction>\n      <profile_id>1</profile_id>\n </agepreference>  <agepreference>\n      <agepreference_id>2</agepreference_id>\n      <agerestriction>AgeRestriction.TWELVE_YEARS</agerestriction>\n      <profile_id>1</profile_id>\n </agepreference></agepreferences>"


def test_read_agepreferences_by_profile_unauthorized():
    response = client.get("/profiles/1/agepreferences")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_agepreferences_by_profile_not_found():
    response = client.get("/profiles/6/agepreferences", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No agepreferences found"
    }


def test_read_agepreferences_by_profile_no_permission():
    response = client.get("/profiles/1/agepreferences", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET agepreference by ID

def test_read_agepreference_by_id_json_response():
    response = client.get("/agepreferences/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "profile_id": 1,
        "agerestriction": "SIX_YEARS",
        "agepreference_id": 1
    }


def test_read_agepreference_by_id_xml_response():
    response = client.get("/agepreferences/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<agepreferences>\n  <agepreference>\n      <agepreference_id>1</agepreference_id>\n      <agerestriction>AgeRestriction.SIX_YEARS</agerestriction>\n      <profile_id>1</profile_id>\n </agepreference></agepreferences>"


def test_read_agepreference_by_id_unauthorized():
    response = client.get("/agepreferences/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_agepreference_by_id_not_found():
    response = client.get("/agepreferences/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No agepreferences found"
    }


def test_read_agepreference_by_id_no_permission():
    response = client.get("/agepreferences/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST genrepreference

def test_create_genrepreference_success():
    genrepreference_data = {
        "genrepreference_id": 5,
        "profile_id": 3,
        "genre": "ACTION"
    }

    response = client.post("/profiles/3/genrepreferences", json=genrepreference_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 201


def test_create_genrepreference_unauthorized():
    genrepreference_data = {
        "genrepreference_id": 5,
        "profile_id": 3,
        "genre": "ACTION"
    }

    response = client.post("/profiles/3/genrepreferences", json=genrepreference_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_genrepreference_not_found():
    genrepreference_data = {
        "genrepreference_id": 5,
        "profile_id": 3,
        "genre": "ACTION"
    }

    response = client.post("/profiles/999/genrepreferences", json=genrepreference_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Profile not found"
    }


def test_create_genrepreference_no_permission():
    genrepreference_data = {
        "genrepreference_id": 5,
        "profile_id": 3,
        "genre": "ACTION"
    }

    response = client.post("/profiles/3/genrepreferences", json=genrepreference_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST indicationpreference

def test_create_indicationpreference_success():
    indicationpreference_data = {
        "indicationpreference_id": 5,
        "profile_id": 3,
        "indication": "VIOLENCE"
    }

    response = client.post("/profiles/3/indicationpreferences", json=indicationpreference_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 201


def test_create_indicationpreference_unauthorized():
    indicationpreference_data = {
        "indicationpreference_id": 5,
        "profile_id": 3,
        "indication": "VIOLENCE"
    }

    response = client.post("/profiles/3/indicationpreferences", json=indicationpreference_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_indicationpreference_not_found():
    indicationpreference_data = {
        "indicationpreference_id": 5,
        "profile_id": 3,
        "indication": "VIOLENCE"
    }

    response = client.post("/profiles/999/indicationpreferences", json=indicationpreference_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Profile not found"
    }


def test_create_indicationpreference_no_permission():
    indicationpreference_data = {
        "indicationpreference_id": 5,
        "profile_id": 3,
        "indication": "VIOLENCE"
    }

    response = client.post("/profiles/3/indicationpreferences", json=indicationpreference_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST agepreferences

def test_create_agepreference_success():
    agepreference_data = {
        "agepreference_id": 5,
        "profile_id": 3,
        "agerestriction": "TWELVE_YEARS"
    }

    response = client.post("/profiles/3/agepreferences", json=agepreference_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 201


def test_create_agepreference_unauthorized():
    agepreference_data = {
        "agepreference_id": 5,
        "profile_id": 3,
        "agerestriction": "TWELVE_YEARS"
    }

    response = client.post("/profiles/3/agepreferences", json=agepreference_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_agepreference_not_found():
    agepreference_data = {
        "agepreference_id": 5,
        "profile_id": 3,
        "agerestriction": "TWELVE_YEARS"
    }

    response = client.post("/profiles/999/agepreferences", json=agepreference_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Profile not found"
    }


def test_create_agepreference_no_permission():
    agepreference_data = {
        "agepreference_id": 5,
        "profile_id": 3,
        "agerestriction": "TWELVE_YEARS"
    }

    response = client.post("/profiles/3/agepreferences", json=agepreference_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# PUT agepreference

def test_update_agepreference_success():
    updated_data = {
        "agepreference_id": 2,
        "profile_id": 1,
        "agerestriction": "NINE_YEARS"
    }

    response = client.put("/agepreferences/2", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == updated_data


def test_update_agepreference_unauthorized():
    updated_data = {
        "agepreference_id": 2,
        "profile_id": 1,
        "agerestriction": "NINE_YEARS"
    }

    response = client.put("/agepreferences/2", json=updated_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_update_agepreference_not_found():
    updated_data = {
        "agepreference_id": 999,
        "profile_id": 1,
        "agerestriction": "NINE_YEARS"
    }

    response = client.put("/agepreferences/999", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Agepreference not found"
    }


def test_update_agepreference_no_permission():
    updated_data = {
        "agepreference_id": 2,
        "profile_id": 1,
        "agerestriction": "NINE_YEARS"
    }

    response = client.put("/agepreferences/2", json=updated_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# DELETE agepreference

def test_delete_agepreference_success():
    response = client.delete("/agepreferences/4", headers={"X-API-KEY": "senior"})

    assert response.status_code == 204


def test_delete_agepreference_unauthorized():
    response = client.delete("/agepreferences/4")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_delete_agepreference_not_found():
    response = client.delete("/agepreferences/999", headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Agepreference not found"
    }


def test_delete_agepreference_no_permission():
    response = client.delete("/agepreferences/4", headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# PUT indicationpreference

def test_update_indicationpreference_success():
    updated_data = {
        "indicationpreference_id": 2,
        "profile_id": 1,
        "indication": "DISCRIMINATION"
    }

    response = client.put("/indicationpreferences/2", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == updated_data


def test_update_indicationpreference_unauthorized():
    updated_data = {
        "indicationpreference_id": 2,
        "profile_id": 1,
        "indication": "DISCRIMINATION"
    }

    response = client.put("/indicationpreferences/2", json=updated_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_update_indicationpreference_not_found():
    updated_data = {
        "indicationpreference_id": 999,
        "profile_id": 1,
        "indication": "DISCRIMINATION"
    }

    response = client.put("/indicationpreferences/999", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Indicationpreference not found"
    }


def test_update_indicationpreference_no_permission():
    updated_data = {
        "indicationpreference_id": 2,
        "profile_id": 1,
        "indication": "DISCRIMINATION"
    }

    response = client.put("/indicationpreferences/2", json=updated_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# DELETE indicationpreference

def test_delete_indicationpreference_success():
    response = client.delete("/indicationpreferences/4", headers={"X-API-KEY": "senior"})

    assert response.status_code == 204


def test_delete_indicationpreference_unauthorized():
    response = client.delete("/indicationpreferences/4")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_delete_indicationpreference_not_found():
    response = client.delete("/indicationpreferences/999", headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Indicationpreference not found"
    }


def test_delete_indicationpreference_no_permission():
    response = client.delete("/indicationpreferences/4", headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# PUT genrepreference

def test_update_genrepreference_success():
    updated_data = {
        "genrepreference_id": 2,
        "profile_id": 1,
        "genre": "HORROR"
    }

    response = client.put("/genrepreferences/2", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == updated_data


def test_update_genrepreference_unauthorized():
    updated_data = {
        "genrepreference_id": 2,
        "profile_id": 1,
        "genre": "HORROR"
    }

    response = client.put("/genrepreferences/2", json=updated_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_update_genrepreference_not_found():
    updated_data = {
        "genrepreference_id": 999,
        "profile_id": 1,
        "genre": "HORROR"
    }

    response = client.put("/genrepreferences/999", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Genrepreference not found"
    }


def test_update_genrepreference_no_permission():
    updated_data = {
        "genrepreference_id": 2,
        "profile_id": 1,
        "genre": "HORROR"
    }

    response = client.put("/genrepreferences/2", json=updated_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# DELETE genrepreference

def test_delete_genrepreference_success():
    response = client.delete("/genrepreferences/4", headers={"X-API-KEY": "senior"})

    assert response.status_code == 204


def test_delete_genrepreference_unauthorized():
    response = client.delete("/genrepreferences/4")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_delete_genrepreference_not_found():
    response = client.delete("/genrepreferences/999", headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Genrepreference not found"
    }


def test_delete_genrepreference_no_permission():
    response = client.delete("/genrepreferences/4", headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }
