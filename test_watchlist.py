from watchlist import *

from test_main import client


# GET watchlist by profile ID

def test_read_watchlist_by_profile_json_response():
    response = client.get("/profiles/1/watchlist", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "serie_id": None,
            "movie_id": 1,
            "profile_id": 1,
            "watchlist_id": 1
        },
        {
            "serie_id": 1,
            "movie_id": None,
            "profile_id": 1,
            "watchlist_id": 2
        }
    ]

    assert response.json() == expected_data


def test_read_watchlist_by_profile_xml_response():
    response = client.get("/profiles/1/watchlist", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<watchlists>\n  <watchlist>\n      <serie_id>None</serie_id>\n      <movie_id>1</movie_id>\n      <profile_id>1</profile_id>\n </watchlist>  <watchlist>\n      <serie_id>1</serie_id>\n      <movie_id>None</movie_id>\n      <profile_id>1</profile_id>\n </watchlist></watchlists>"


def test_read_watchlist_by_profile_unauthorized():
    response = client.get("/profiles/1/watchlist")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_watchlist_by_profile_not_found():
    response = client.get("/profiles/999/watchlist", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No watchlists found"
    }


def test_read_watchlist_by_profile_no_permission():
    response = client.get("/profiles/1/watchlist", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST movie to watchlist

def test_add_movie_to_watchlist_success():
    watchlist_data = {
        "watchlist_id": 3,
        "movie_id": 2,
        "serie_id": None,
        "profile_id": 2
    }

    response = client.post("/watchlist/movie", json=watchlist_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 201


def test_add_movie_to_watchlist_unauthorized():
    watchlist_data = {
        "watchlist_id": 3,
        "movie_id": 2,
        "serie_id": None,
        "profile_id": 2
    }

    response = client.post("/watchlist/movie", json=watchlist_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_add_movie_to_watchlist_no_permission():
    watchlist_data = {
        "watchlist_id": 3,
        "movie_id": 2,
        "serie_id": None,
        "profile_id": 2
    }

    response = client.post("/watchlist/movie", json=watchlist_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST series to watchlist

def test_add_serie_to_watchlist_success():
    watchlist_data = {
        "watchlist_id": 4,
        "movie_id": None,
        "serie_id": 2,
        "profile_id": 2
    }

    response = client.post("/watchlist/serie", json=watchlist_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 201


def test_add_serie_to_watchlist_unauthorized():
    watchlist_data = {
        "watchlist_id": 4,
        "movie_id": None,
        "serie_id": 2,
        "profile_id": 2
    }

    response = client.post("/watchlist/serie", json=watchlist_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_add_serie_to_watchlist_no_permission():
    watchlist_data = {
        "watchlist_id": 4,
        "movie_id": None,
        "serie_id": 2,
        "profile_id": 2
    }

    response = client.post("/watchlist/serie", json=watchlist_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# PUT watchlist by ID

def test_update_watchlist_success():
    updated_data = {
        "watchlist_id": 1,
        "movie_id": 3,
        "serie_id": None,
        "profile_id": 1
    }

    response = client.put("/watchlist/1", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == updated_data


def test_update_watchlist_unauthorized():
    updated_data = {
        "watchlist_id": 1,
        "movie_id": 3,
        "serie_id": None,
        "profile_id": 1
    }

    response = client.put("/watchlist/1", json=updated_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_update_watchlist_not_found():
    updated_data = {
        "watchlist_id": 999,
        "movie_id": 3,
        "serie_id": None,
        "profile_id": 1
    }

    response = client.put("/watchlist/999", json=updated_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Watchlist not found"
    }


def test_update_watchlist_no_permission():
    updated_data = {
        "watchlist_id": 1,
        "movie_id": 3,
        "serie_id": None,
        "profile_id": 1
    }

    response = client.put("/watchlist/1", json=updated_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# DELETE watchlist by ID

def test_delete_watchlist_success():
    response = client.delete("/watchlist/2", headers={"X-API-KEY": "senior"})

    assert response.status_code == 204


def test_delete_watchlist_unauthorized():
    response = client.delete("/watchlist/2")

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_delete_watchlist_not_found():
    response = client.delete("/watchlist/999", headers={"X-API-KEY": "senior"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Watchlist not found"
    }


def test_delete_watchlist_no_permission():
    response = client.delete("/watchlist/2", headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }
