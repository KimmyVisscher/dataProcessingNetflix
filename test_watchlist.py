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
