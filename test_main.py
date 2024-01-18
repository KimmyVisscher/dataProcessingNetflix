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
    response = client.get("/movies/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET all movies

def test_read_movies_json_response():
    response = client.get("/movies", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {"title": "The Shawshank Redemption", "movie_duration": 142, "age_restriction": "SIXTEEN_YEARS", "movie_id": 1},
        {"title": "The Godfather", "movie_duration": 175, "age_restriction": "ALL_AGES", "movie_id": 2},
        {"title": "Pulp Fiction", "movie_duration": 154, "age_restriction": "ALL_AGES", "movie_id": 3},
        {"title": "The Dark Knight", "movie_duration": 152, "age_restriction": "SIXTEEN_YEARS", "movie_id": 4},
        {"title": "Schindler's List", "movie_duration": 195, "age_restriction": "SIXTEEN_YEARS", "movie_id": 5},
        {"title": "Inception", "movie_duration": 148, "age_restriction": "SIXTEEN_YEARS", "movie_id": 6},
        {"title": "Fight Club", "movie_duration": 139, "age_restriction": "SIXTEEN_YEARS", "movie_id": 7},
        {"title": "Forrest Gump", "movie_duration": 142, "age_restriction": "ALL_AGES", "movie_id": 8},
        {"title": "The Matrix", "movie_duration": 136, "age_restriction": "SIX_YEARS", "movie_id": 9},
        {"title": "The Silence of the Lambs", "movie_duration": 118, "age_restriction": "TWELVE_YEARS", "movie_id": 10},
        {"title": "The Green Mile", "movie_duration": 189, "age_restriction": "SIXTEEN_YEARS", "movie_id": 11},
        {"title": "The Godfather: Part II", "movie_duration": 202, "age_restriction": "TWELVE_YEARS", "movie_id": 12}
    ]

    assert response.json() == expected_data


def test_read_movies_xml_response():
    response = client.get("/movies", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<movies>\n  <movie>\n      <title>The Shawshank Redemption</title>\n      <movie_duration>142</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>The Godfather</title>\n      <movie_duration>175</movie_duration>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </movie>  <movie>\n      <title>Pulp Fiction</title>\n      <movie_duration>154</movie_duration>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </movie>  <movie>\n      <title>The Dark Knight</title>\n      <movie_duration>152</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>Schindler's List</title>\n      <movie_duration>195</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>Inception</title>\n      <movie_duration>148</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>Fight Club</title>\n      <movie_duration>139</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>Forrest Gump</title>\n      <movie_duration>142</movie_duration>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </movie>  <movie>\n      <title>The Matrix</title>\n      <movie_duration>136</movie_duration>\n      <age_restriction>AgeRestriction.SIX_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>The Silence of the Lambs</title>\n      <movie_duration>118</movie_duration>\n      <age_restriction>AgeRestriction.TWELVE_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>The Green Mile</title>\n      <movie_duration>189</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>The Godfather: Part II</title>\n      <movie_duration>202</movie_duration>\n      <age_restriction>AgeRestriction.TWELVE_YEARS</age_restriction>\n  </movie></movies>"


def test_read_movies_unauthorized():
    response = client.get("/movies")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_movies_no_permission():
    response = client.get("/movies", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET all movies by genre

def test_read_movies_by_genre_json_response():
    response = client.get("/movies/genre/ACTION", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "title": "The Shawshank Redemption",
            "movie_duration": 142,
            "age_restriction": "SIXTEEN_YEARS",
            "movie_id": 1
        },
        {
            "title": "The Godfather",
            "movie_duration": 175,
            "age_restriction": "ALL_AGES",
            "movie_id": 2
        }
    ]

    assert response.json() == expected_data


def test_read_movies_by_genre_xml_response():
    response = client.get("/movies/genre/ACTION", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<movies>\n  <movie>\n      <title>The Shawshank Redemption</title>\n      <movie_duration>142</movie_duration>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </movie>  <movie>\n      <title>The Godfather</title>\n      <movie_duration>175</movie_duration>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </movie></movies>"


def test_read_movies_by_genre_unauthorized():
    response = client.get("/movies/genre/ACTION")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_movies_by_genre_no_permission():
    response = client.get("/movies/genre/ACTION", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET all series

def test_read_all_series_json_response():
    response = client.get("/series", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {"serie_name": "Stranger Things", "age_restriction": "SIXTEEN_YEARS", "serie_id": 1},
        {"serie_name": "The Crown", "age_restriction": "SIXTEEN_YEARS", "serie_id": 2},
        {"serie_name": "Breaking Bad", "age_restriction": "SIXTEEN_YEARS", "serie_id": 3},
        {"serie_name": "Friends", "age_restriction": "ALL_AGES", "serie_id": 4},
        {"serie_name": "Black Mirror", "age_restriction": "SIXTEEN_YEARS", "serie_id": 5},
        {"serie_name": "The Mandalorian", "age_restriction": "TWELVE_YEARS", "serie_id": 6},
        {"serie_name": "Money Heist", "age_restriction": "SIXTEEN_YEARS", "serie_id": 7},
        {"serie_name": "Narcos", "age_restriction": "SIXTEEN_YEARS", "serie_id": 8},
        {"serie_name": "The Witcher", "age_restriction": "SIXTEEN_YEARS", "serie_id": 9},
        {"serie_name": "Peaky Blinders", "age_restriction": "ALL_AGES", "serie_id": 10},
        {"serie_name": "The Office", "age_restriction": "ALL_AGES", "serie_id": 11},
        {"serie_name": "Game of Thrones", "age_restriction": "SIXTEEN_YEARS", "serie_id": 12}
    ]

    assert response.json() == expected_data


def test_read_all_series_xml_response():
    response = client.get("/series", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<series>\n  <serie>\n      <serie_name>Stranger Things</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>The Crown</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>Breaking Bad</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>Friends</serie_name>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </serie>  <serie>\n      <serie_name>Black Mirror</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>The Mandalorian</serie_name>\n      <age_restriction>AgeRestriction.TWELVE_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>Money Heist</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>Narcos</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>The Witcher</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>Peaky Blinders</serie_name>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </serie>  <serie>\n      <serie_name>The Office</serie_name>\n      <age_restriction>AgeRestriction.ALL_AGES</age_restriction>\n  </serie>  <serie>\n      <serie_name>Game of Thrones</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie></series>"


def test_read_all_series_unauthorized():
    response = client.get("/series")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_all_series_no_permission():
    response = client.get("/series", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


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
    response = client.get("/series/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
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
    response = client.get("/episodes/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
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
    response = client.get("/accounts/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET profiles by account ID
#
# GET profile by ID

def test_read_profile_by_id_json_response():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "profile_image": "/path/to/image",
        "profile_child": 0,
        "language": "DUTCH",
        "account_id": 1,
        "profile_id": 1
    }


def test_read_profile_by_id_xml_response():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<profiles>\n  <profile>\n      <profile_image>/path/to/image</profile_image>\n      <profile_child>0</profile_child>\n      <language>Language.DUTCH</language>\n      <account_id>1</account_id>\n  </profile></profiles>"


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
    response = client.get("/profiles/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
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
