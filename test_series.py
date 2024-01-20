from series import *

from test_main import client


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


# POST series

def test_create_series_success():
    series_data = {
        "serie_name": "Planet Earth",
        "serie_id": 13,
        "age_restriction": "SIX_YEARS"
    }

    response = client.post("/series", json=series_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == series_data


def test_create_series_unauthorized():
    series_data = {
        "serie_name": "Planet Earth",
        "serie_id": 13,
        "age_restriction": "SIX_YEARS"
    }

    response = client.post("/series", json=series_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_series_no_permission():
    series_data = {
        "serie_id": 13,
        "serie_name": "Planet Earth",
        "age_restriction": "SIX_YEARS"
    }

    response = client.post("/series", json=series_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# POST episode

def test_create_episode_success():
    episode_data = {
        "episode_id": 37,
        "title": "From Pole to Pole",
        "episode_duration": 49,
        "serie_id": 13
    }

    response = client.post("/episodes", json=episode_data, headers={"X-API-KEY": "senior"})

    assert response.status_code == 200
    assert response.json() == episode_data


def test_create_episode_unauthorized():
    episode_data = {
        "episode_id": 37,
        "title": "From Pole to Pole",
        "episode_duration": 49,
        "serie_id": 13
    }

    response = client.post("/episodes", json=episode_data)

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_create_episode_no_permission():
    episode_data = {
        "episode_id": 37,
        "title": "From Pole to Pole",
        "episode_duration": 49,
        "serie_id": 13
    }

    response = client.post("/episodes", json=episode_data, headers={"X-API-KEY": "unauthorized"})

    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }
