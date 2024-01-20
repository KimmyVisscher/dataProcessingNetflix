from subtitles import *

from test_main import client


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


# POST subtitle by episode ID

def test_create_subtitle_for_episode_success():
    subtitle_data = {
        "subtitle_id": 49,
        "language": "ENGLISH",
        "subtitle_location": "/path/to/subtitles/episode2_eng.srt",
        "movie_id": None,
        "episode_id": 2
    }

    response = client.post("/episodes/2/subtitles", json=subtitle_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == subtitle_data


def test_create_subtitle_for_episode_unauthorized():
    subtitle_data = {
        "subtitle_id": 49,
        "language": "ENGLISH",
        "subtitle_location": "/path/to/subtitles/episode2_eng.srt",
        "movie_id": None,
        "episode_id": 2
    }

    response = client.post("/episodes/2/subtitles", json=subtitle_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_subtitle_for_episode_no_permission():
    subtitle_data = {
        "subtitle_id": 49,
        "language": "ENGLISH",
        "subtitle_location": "/path/to/subtitles/episode2_eng.srt",
        "movie_id": None,
        "episode_id": 2
    }

    response = client.post("/episodes/2/subtitles", json=subtitle_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST subtitle by movie ID

def test_create_subtitle_for_movie_success():
    subtitle_data = {
        "subtitle_id": 50,
        "language": "ENGLISH",
        "subtitle_location": "/path/to/subtitles/episode2_eng.srt",
        "movie_id": 3,
        "episode_id": None
    }

    response = client.post("/movies/3/subtitles", json=subtitle_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == subtitle_data


def test_create_subtitle_for_movie_unauthorized():
    subtitle_data = {
        "subtitle_id": 50,
        "language": "ENGLISH",
        "subtitle_location": "/path/to/subtitles/episode2_eng.srt",
        "movie_id": 3,
        "episode_id": None
    }

    response = client.post("/movies/3/subtitles", json=subtitle_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_subtitle_for_movie_no_permission():
    subtitle_data = {
        "subtitle_id": 50,
        "language": "ENGLISH",
        "subtitle_location": "/path/to/subtitles/episode2_eng.srt",
        "movie_id": 3,
        "episode_id": None
    }

    response = client.post("/movies/3/subtitles", json=subtitle_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }
