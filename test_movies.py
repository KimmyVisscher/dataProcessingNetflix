from movies import *

from test_main import client


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


# POST movie

def test_create_movie_success(mock_db_session, mock_check_apikey_role):
    movie_data = {
        "title": "The Good, the Bad and the Ugly",
        "movie_duration": 161,
        "movie_id": 21,
        "age_restriction": "TWELVE_YEARS"
    }

    response = client.post("/movies", json=movie_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == movie_data


# def test_create_movie_unauthorized():
# def test_create_movie_no_premission():
