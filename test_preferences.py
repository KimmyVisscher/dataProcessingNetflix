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

# POST indicationpreference

# POST agepreferences

# PUT agepreference

# DELETE agepreference

# PUT indicationpreference

# DELETE indicationpreference

# PUT genrepreference

# DELETE genrepreference
