from fastapi.testclient import TestClient

from secrets import *

from main import app


client = TestClient(app)


#

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
