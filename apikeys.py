from main import *


@app.post("/apikeys/")
def create_api_key(*, session: Session = Depends(get_session),
                   role: str,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.SENIOR.value):
        if role != "JUNIOR" and role != "MEDIOR" and role != "SENIOR":
            raise HTTPException(status_code=400, detail="Invalid role")


        key_length = 15
        letters = string.ascii_letters

        while True:
            api_key = ''.join(random.choice(letters) for _ in range(key_length))
            existing_api_key = session.get(APIKey, api_key)
            if not existing_api_key:
                break

        apikey_model = APIKey(apikey=api_key, role=role)
        session.add(apikey_model)
        session.commit()

        return {"api_key": api_key}


@app.delete("/apikeys/{apikey}", response_model=dict)
def delete_api_key(apikey: str,
                   session: Session = Depends(get_session),
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.SENIOR.value):
        delete_api_key = session.query(APIKey).filter(APIKey.apikey == apikey).first()
        if not delete_api_key:
            raise HTTPException(status_code=404, detail="API key not found")

        session.delete(delete_api_key)
        session.commit()

        return {"message": "API key deleted successfully"}


@app.get("/apikey/{apikey}", response_model=APIKey)
def read_apikey(*, session: Session = Depends(get_session),
                apikey: str,
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    if check_apikey_role(session, api_key_header, Role.SENIOR.value):
        apikey = session.get(APIKey, apikey)
        if not apikey:
            raise HTTPException(status_code=404, detail="APIKey not found")

        if accept and "application/xml" in accept:
            xml_content = xmltodict.unparse({"apikey": apikey.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
        else:
            return apikey