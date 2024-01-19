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

def test_read_episodes_by_series_json_response():
    response = client.get("/series/1/episodes", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "title": "The Beginning",
            "episode_duration": 45,
            "serie_id": 1,
            "episode_id": 1
        },
        {
            "title": "Secrets Unveiled",
            "episode_duration": 42,
            "serie_id": 1,
            "episode_id": 2
        },
        {
            "title": "Into the Abyss",
            "episode_duration": 40,
            "serie_id": 1,
            "episode_id": 3
        },
        {
            "title": "Hidden Truths",
            "episode_duration": 38,
            "serie_id": 1,
            "episode_id": 4
        },
        {
            "title": "Fallen Heroes",
            "episode_duration": 41,
            "serie_id": 1,
            "episode_id": 5
        },
        {
            "title": "Deception",
            "episode_duration": 37,
            "serie_id": 1,
            "episode_id": 6
        },
        {
            "title": "Betrayal",
            "episode_duration": 44,
            "serie_id": 1,
            "episode_id": 7
        },
        {
            "title": "Rising Tensions",
            "episode_duration": 39,
            "serie_id": 1,
            "episode_id": 8
        },
        {
            "title": "The Reckoning",
            "episode_duration": 43,
            "serie_id": 1,
            "episode_id": 9
        },
        {
            "title": "Final Stand",
            "episode_duration": 36,
            "serie_id": 1,
            "episode_id": 10
        },
        {
            "title": "Epiphany",
            "episode_duration": 40,
            "serie_id": 1,
            "episode_id": 11
        },
        {
            "title": "Closure",
            "episode_duration": 42,
            "serie_id": 1,
            "episode_id": 12
        }
    ]

    assert response.json() == expected_data


def test_read_episodes_by_series_xml_response():
    response = client.get("/series/1/episodes", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<episodes>\n  <episode>\n      <title>The Beginning</title>\n      <episode_duration>45</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Secrets Unveiled</title>\n      <episode_duration>42</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Into the Abyss</title>\n      <episode_duration>40</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Hidden Truths</title>\n      <episode_duration>38</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Fallen Heroes</title>\n      <episode_duration>41</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Deception</title>\n      <episode_duration>37</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Betrayal</title>\n      <episode_duration>44</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Rising Tensions</title>\n      <episode_duration>39</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>The Reckoning</title>\n      <episode_duration>43</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Final Stand</title>\n      <episode_duration>36</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Epiphany</title>\n      <episode_duration>40</episode_duration>\n      <serie_id>1</serie_id>\n  </episode>  <episode>\n      <title>Closure</title>\n      <episode_duration>42</episode_duration>\n      <serie_id>1</serie_id>\n  </episode></episodes>"


def test_read_episodes_by_series_unauthorized():
    response = client.get("/series/1/episodes")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_episodes_by_series_not_found():
    response = client.get("/series/4/episodes", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No episodes found for the serie"
    }


def test_read_episodes_by_series_no_permission():
    response = client.get("/series/1/episodes", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET series by genre

def test_read_series_by_genre_json_response():
    response = client.get("/series/genre/ACTION", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "serie_name": "Stranger Things",
            "age_restriction": "SIXTEEN_YEARS",
            "serie_id": 1
        },
        {
            "serie_name": "The Crown",
            "age_restriction": "SIXTEEN_YEARS",
            "serie_id": 2
        }
    ]

    assert response.json() == expected_data


def test_read_series_by_genre_xml_response():
    response = client.get("/series/genre/ACTION", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<series>\n  <serie>\n      <serie_name>Stranger Things</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie>  <serie>\n      <serie_name>The Crown</serie_name>\n      <age_restriction>AgeRestriction.SIXTEEN_YEARS</age_restriction>\n  </serie></series>"


def test_read_series_by_genre_unauthorized():
    response = client.get("/series/genre/ACTION")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_series_by_genre_no_permission():
    response = client.get("/series/genre/ACTION", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET subtitles by movie ID

def test_read_subtitles_by_movie_json_response():
    response = client.get("/movies/1/subtitles", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "language": "ENGLISH",
            "subtitle_location": "/path/to/subtitles/movie1_eng.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 1
        },
        {
            "language": "DUTCH",
            "subtitle_location": "/path/to/subtitles/movie1_nl.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 2
        },
        {
            "language": "FRENCH",
            "subtitle_location": "/path/to/subtitles/movie1_fr.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 3
        },
        {
            "language": "SPANISH",
            "subtitle_location": "/path/to/subtitles/movie1_es.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 4
        },
        {
            "language": "GERMAN",
            "subtitle_location": "/path/to/subtitles/movie1_de.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 5
        },
        {
            "language": "ITALIAN",
            "subtitle_location": "/path/to/subtitles/movie1_it.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 6
        },
        {
            "language": "JAPANESE",
            "subtitle_location": "/path/to/subtitles/movie1_jp.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 7
        },
        {
            "language": "CHINESE",
            "subtitle_location": "/path/to/subtitles/movie1_cn.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 8
        },
        {
            "language": "RUSSIAN",
            "subtitle_location": "/path/to/subtitles/movie1_ru.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 9
        },
        {
            "language": "PORTUGUESE",
            "subtitle_location": "/path/to/subtitles/movie1_pt.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 10
        },
        {
            "language": "ARABIC",
            "subtitle_location": "/path/to/subtitles/movie1_ar.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 11
        },
        {
            "language": "KOREAN",
            "subtitle_location": "/path/to/subtitles/movie1_kr.srt",
            "movie_id": 1,
            "episode_id": None,
            "subtitle_id": 12
        }
    ]

    assert response.json() == expected_data


def test_read_subtitles_by_movie_xml_response():
    response = client.get("/movies/1/subtitles", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<subtitles>\n  <subtitle>\n      <language>Language.ENGLISH</language>\n      <subtitle_location>/path/to/subtitles/movie1_eng.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.DUTCH</language>\n      <subtitle_location>/path/to/subtitles/movie1_nl.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.FRENCH</language>\n      <subtitle_location>/path/to/subtitles/movie1_fr.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.SPANISH</language>\n      <subtitle_location>/path/to/subtitles/movie1_es.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.GERMAN</language>\n      <subtitle_location>/path/to/subtitles/movie1_de.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.ITALIAN</language>\n      <subtitle_location>/path/to/subtitles/movie1_it.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.JAPANESE</language>\n      <subtitle_location>/path/to/subtitles/movie1_jp.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.CHINESE</language>\n      <subtitle_location>/path/to/subtitles/movie1_cn.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.RUSSIAN</language>\n      <subtitle_location>/path/to/subtitles/movie1_ru.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.PORTUGUESE</language>\n      <subtitle_location>/path/to/subtitles/movie1_pt.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.ARABIC</language>\n      <subtitle_location>/path/to/subtitles/movie1_ar.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.KOREAN</language>\n      <subtitle_location>/path/to/subtitles/movie1_kr.srt</subtitle_location>\n      <movie_id>1</movie_id>\n      <episode_id>None</episode_id>\n  </subtitle></subtitles>"


def test_read_subtitles_by_movie_unauthorized():
    response = client.get("/movies/1/subtitles")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_subtitles_by_movie_not_found():
    response = client.get("/movies/5/subtitles", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No subtitles found"
    }


def test_read_subtitles_by_movie_no_permission():
    response = client.get("/movies/1/subtitles", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET subtitles by episode ID

def test_read_subtitles_by_episode_json_response():
    response = client.get("/episodes/1/subtitles", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "language": "ENGLISH",
            "subtitle_location": "/path/to/subtitles/episode1_eng.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 25
        },
        {
            "language": "DUTCH",
            "subtitle_location": "/path/to/subtitles/episode1_nl.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 26
        },
        {
            "language": "FRENCH",
            "subtitle_location": "/path/to/subtitles/episode1_fr.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 27
        },
        {
            "language": "SPANISH",
            "subtitle_location": "/path/to/subtitles/episode1_es.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 28
        },
        {
            "language": "GERMAN",
            "subtitle_location": "/path/to/subtitles/episode1_de.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 29
        },
        {
            "language": "ITALIAN",
            "subtitle_location": "/path/to/subtitles/episode1_it.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 30
        },
        {
            "language": "JAPANESE",
            "subtitle_location": "/path/to/subtitles/episode1_jp.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 31
        },
        {
            "language": "CHINESE",
            "subtitle_location": "/path/to/subtitles/episode1_cn.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 32
        },
        {
            "language": "RUSSIAN",
            "subtitle_location": "/path/to/subtitles/episode1_ru.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 33
        },
        {
            "language": "PORTUGUESE",
            "subtitle_location": "/path/to/subtitles/episode1_pt.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 34
        },
        {
            "language": "ARABIC",
            "subtitle_location": "/path/to/subtitles/episode1_ar.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 35
        },
        {
            "language": "KOREAN",
            "subtitle_location": "/path/to/subtitles/episode1_kr.srt",
            "movie_id": None,
            "episode_id": 1,
            "subtitle_id": 36
        }
    ]

    assert response.json() == expected_data


def test_read_subtitles_by_episode_xml_response():
    response = client.get("/episodes/1/subtitles", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<subtitles>\n  <subtitle>\n      <language>Language.ENGLISH</language>\n      <subtitle_location>/path/to/subtitles/episode1_eng.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.DUTCH</language>\n      <subtitle_location>/path/to/subtitles/episode1_nl.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.FRENCH</language>\n      <subtitle_location>/path/to/subtitles/episode1_fr.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.SPANISH</language>\n      <subtitle_location>/path/to/subtitles/episode1_es.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.GERMAN</language>\n      <subtitle_location>/path/to/subtitles/episode1_de.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.ITALIAN</language>\n      <subtitle_location>/path/to/subtitles/episode1_it.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.JAPANESE</language>\n      <subtitle_location>/path/to/subtitles/episode1_jp.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.CHINESE</language>\n      <subtitle_location>/path/to/subtitles/episode1_cn.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.RUSSIAN</language>\n      <subtitle_location>/path/to/subtitles/episode1_ru.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.PORTUGUESE</language>\n      <subtitle_location>/path/to/subtitles/episode1_pt.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.ARABIC</language>\n      <subtitle_location>/path/to/subtitles/episode1_ar.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle>  <subtitle>\n      <language>Language.KOREAN</language>\n      <subtitle_location>/path/to/subtitles/episode1_kr.srt</subtitle_location>\n      <movie_id>None</movie_id>\n      <episode_id>1</episode_id>\n  </subtitle></subtitles>"


def test_read_subtitles_by_episode_unauthorized():
    response = client.get("/episodes/1/subtitles")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_subtitles_by_episode_not_found():
    response = client.get("/episodes/5/subtitles", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No subtitles found"
    }


def test_read_subtitles_by_episode_no_permission():
    response = client.get("/episodes/1/subtitles", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET all accounts

def test_read_all_accounts_json_response():
    response = client.get("/accounts", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "email": "john.doe@example.com",
            "payment_method": "credit_card",
            "username": "john_doe",
            "subscription_id": 1
        },
        {
            "email": "jane.smith@example.com",
            "payment_method": "paypal",
            "username": "jane_smith",
            "subscription_id": 2
        },
        {
            "email": "alice.jones@example.com",
            "payment_method": "debit_card",
            "username": "alice_jones",
            "subscription_id": 1
        },
        {
            "email": "bob.white@example.com",
            "payment_method": "credit_card",
            "username": "bob_white",
            "subscription_id": 3
        },
        {
            "email": "mary.green@example.com",
            "payment_method": "paypal",
            "username": "mary_green",
            "subscription_id": 2
        },
        {
            "email": "sam.brown@example.com",
            "payment_method": "debit_card",
            "username": "sam_brown",
            "subscription_id": 1
        },
        {
            "email": "emily.wilson@example.com",
            "payment_method": "credit_card",
            "username": "emily_wilson",
            "subscription_id": 3
        },
        {
            "email": "charlie.rogers@example.com",
            "payment_method": "paypal",
            "username": "charlie_rogers",
            "subscription_id": 1
        },
        {
            "email": "olivia.hall@example.com",
            "payment_method": "debit_card",
            "username": "olivia_hall",
            "subscription_id": 2
        },
        {
            "email": "david.lee@example.com",
            "payment_method": "credit_card",
            "username": "david_lee",
            "subscription_id": 3
        },
        {
            "email": "sophie.collins@example.com",
            "payment_method": "paypal",
            "username": "sophie_collins",
            "subscription_id": 2
        },
        {
            "email": "max.miller@example.com",
            "payment_method": "debit_card",
            "username": "max_miller",
            "subscription_id": 1
        }
    ]

    assert response.json() == expected_data


def test_read_all_accounts_xml_response():
    response = client.get("/accounts", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<accounts>\n  <account>\n      <email>john.doe@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>john_doe</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>jane.smith@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>jane_smith</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>alice.jones@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>alice_jones</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>bob.white@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>bob_white</username>\n      <subscription_id>3</subscription_id>\n  </account>  <account>\n      <email>mary.green@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>mary_green</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>sam.brown@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>sam_brown</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>emily.wilson@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>emily_wilson</username>\n      <subscription_id>3</subscription_id>\n  </account>  <account>\n      <email>charlie.rogers@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>charlie_rogers</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>olivia.hall@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>olivia_hall</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>david.lee@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>david_lee</username>\n      <subscription_id>3</subscription_id>\n  </account>  <account>\n      <email>sophie.collins@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>sophie_collins</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>max.miller@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>max_miller</username>\n      <subscription_id>1</subscription_id>\n  </account></accounts>"


def test_read_all_accounts_unauthorized():
    response = client.get("/accounts")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_all_accounts_no_permission():
    response = client.get("/accounts", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


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
