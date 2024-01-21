from fastapi.testclient import TestClient

from secrets import *

from main import app


client = TestClient(app)
