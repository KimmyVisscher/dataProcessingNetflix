from fastapi.testclient import TestClient

from secrets import *

from main import app


client = TestClient(app)


# GET movie by ID

def test_read_movie_json_response():
    response = client.get("/movies/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "title": "The Shawshank Redemption",
        "movie_duration": 142,
        "age_restriction": "SIXTEEN_YEARS",
        "movie_id": 1
    }


def test_read_movie_xml_response():
    response = client.get("/movies/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<movies>\n  <movie>\n      <title>The Shawshank Redemption</title>\n      <movie_duration>142</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie></movies>"


def test_read_movie_unauthorized():
    response = client.get("/movies/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_movie_not_found():
    response = client.get("/movies/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Movie not found"
    }


def test_read_movie_no_permission():
    response = client.get("/movies/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
        # To test this I need to create a role in main.py with value < 1.
        # Then make an api-key in the database with this role. Then we can run this test.
    }


# GET all movies
#
# GET all movies by genre
#
# GET all series
#
# GET series by ID

def test_read_series_json_response():
    response = client.get("/series/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "serie_name": "Stranger Things",
        "age_restriction": "SIXTEEN_YEARS",
        "serie_id": 1
    }


def test_read_series_xml_response():
    response = client.get("/series/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<series>\n  <serie>\n      <serie_name>Stranger Things</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie></series>"


def test_read_series_unauthorized():
    response = client.get("/series/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_series_not_found():
    response = client.get("/series/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No series found"
    }


def test_read_series_no_permission():
    response = client.get("/series/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
        # To test this I need to create a role in main.py with value < 1.
        # Then make an api-key in the database with this role. Then we can run this test.
    }


# GET episode by ID

def test_read_episode_json_response():
    response = client.get("/episodes/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "title": "The Beginning",
        "episode_duration": 45,
        "serie_id": 1,
        "episode_id": 1
    }


def test_read_episode_xml_response():
    response = client.get("/episodes/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<episodes>\n  <episode>\n      <title>The Beginning</title>\n      <episode_duration>45</episode_duration>\n      <serie_id>1</serie_id>\n  </episode></episodes>"


def test_read_episode_unauthorized():
    response = client.get("/episodes/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_episode_not_found():
    response = client.get("/episodes/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Episode not found"
    }


def test_read_episode_no_permission():
    response = client.get("/episodes/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
        # To test this I need to create a role in main.py with value < 1.
        # Then make an api-key in the database with this role. Then we can run this test.
    }


# GET episode by serie ID
#
# GET series by genre
#
# GET subtitles by movie ID
#
# GET subtitles by episode ID
#
# GET all accounts
#
# GET account by ID

def test_read_account_json_response():
    response = client.get("/accounts/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "email": "john.doe@example.com",
        "payment_method": "credit_card",
        "username": "john_doe",
        "subscription_id": 1
    }


def test_read_account_xml_response():
    response = client.get("/accounts/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<accounts>\n  <account>\n      <email>john.doe@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>john_doe</username>\n      <subscription_id>1</subscription_id>\n  </account></accounts>"


def test_read_account_unauthorized():
    response = client.get("/accounts/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_account_not_found():
    response = client.get("/accounts/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Account not found"
    }


def test_read_account_no_permission():
    response = client.get("/accounts/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
        # To test this I need to create a role in main.py with value < 1.
        # Then make an api-key in the database with this role. Then we can run this test.
    }


# GET profiles by account ID
#
# GET profile by ID

def test_read_profile_by_id_json_response():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "email": "john.doe@example.com",
        "payment_method": "credit_card",
        "username": "john_doe",
        "subscription_id": 1
    }


def test_read_profile_by_id_xml_response():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<accounts>\n  <account>\n      <email>john.doe@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>john_doe</username>\n      <subscription_id>1</subscription_id>\n  </account></accounts>"


def test_read_profile_by_id_unauthorized():
    response = client.get("/profiles/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_profile_by_id_not_found():
    response = client.get("/profiles/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Profile not found"
    }


def test_read_profile_by_id_no_permission():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
        # To test this I need to create a role in main.py with value < 1.
        # Then make an api-key in the database with this role. Then we can run this test.
    }


# GET watchlist by profile ID
#
# POST movie
#
# POST series
#
# POST episode
#
# POST subtitle by episode ID
#
# POST subtitle by movie ID
#
# POST account
#
# POST profile
#
# PUT movie by ID
#
# PUT series by ID
#
# PUT episode by ID
#
# PUT subtitle by ID
#
# PUT account by ID
#
# PUT profile by ID
#
# DELETE movie by ID
#
# DELETE series by ID
#
# DELETE episode by ID
#
# DELETE subtitle by ID
#
# DELETE account by ID
#
# DELETE profile by ID
#
# GET imdbrating by movie ID
#
# GET imdbrating by series ID
#
# POST apikey
#
# DELETE apikey
