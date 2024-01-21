# Henkflix
Deze repository bevat alle bestanden voor Henkflix.

## Voor gebruik
Als eerste is het van belang om **[Python]** 3.10 of hoger geïnstalleerd te hebben.

[Python]: https://www.python.org/downloads/

Om de API te kunnen gebruiken dienen eerst alle benodigde libraries te installeren. Alle libraries staan in requirement.txt en kunnen via de commandline geïnstalleerd worden met het volgende commando:
```
pip install -r requirements.txt
```
---
secrets.py.dist bevat twee velden die ingevuld dienen te worden. Maar eerst, voordat er informatie in gezet wordt, dient de .dist extensie weggehaald te worden. Dus het bestand dient hernoemd te worden naar secrets.py. Dan voor het invullen van de variabelen. Ten eerste de connectiestring voor de database, en als tweede een omdbkey, die vereist is om een verbinding te leggen met de OMDb-API. De OMDb-key kan **[hier]** opgehaald worden.

[hier]: https://omdbapi.com/apikey.aspx

---

De folder genaamd SQL bevat .sql-bestanden met daarin de opbouw van de database en ook testdata:
* DI.sql bevat alle stored procedures en triggers.
* DP_netflix_testing.sql bevat de database structuur met testdata. Deze testdata worden ook gebruikt bij het unit testen.
* users.sql bevat informatie over de typen gebruikers en hun permissies.

Het JSON-bestand endpoints.json bevat informatie over alle endpoints volgens de **[OpenAPI Specification]**.

[OpenAPI Specification]: https://spec.openapis.org/oas/latest.html

---

De API opstarten gaat via de terminal. Hiervoor wordt het volgende commando gebruikt in de map die de .py-bestanden bevat:
```
uvicorn main:app --reload
```

In dezelfde map kunnen ook de unit tests gerund worden door het volgende commando in de terminal in te voeren:
```
pytest
```