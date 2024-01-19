from main import *


@app.get("/profiles/{profile_id}/genrepreference", response_model=List[GenrespreferenceRead])
def read_genrepreference_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        genrepreferences = session.query(Genrespreference).filter(Genrespreference.profile_id == profile_id).all()
        if not genrepreferences:
            raise HTTPException(status_code=404, detail="No genrepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=genrepreferences_to_xml_string(genrepreferences), media_type="application/xml")
        else:
            return genrepreferences


@app.get("/genrepreferences/{genrepreference_id}", response_model=GenrespreferenceRead)
def read_genrepreference_by_id(
        *,
        session: Session = Depends(get_session),
        genrepreference_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        genrepreference = session.get(Genrespreference, genrepreference_id)
        if not genrepreference:
            raise HTTPException(status_code=404, detail="No genrepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=genrepreferences_to_xml_string(([genrepreference])), media_type="application/xml")
        else:
            return genrepreference


@app.get("/profiles/{profile_id}/indicationpreferences", response_model=List[IndicationpreferenceRead])
def read_indicationpreference_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        indicationpreferences = session.query(Indicationpreference).filter(Indicationpreference.profile_id == profile_id).all()
        if not indicationpreferences:
            raise HTTPException(status_code=404, detail="No indicationpreferences found")

        if accept and "application/xml" in accept:
            return Response(content=indicationpreferences_to_xml_string(indicationpreferences), media_type="application/xml")
        else:
            return indicationpreferences


@app.get("/indicationpreferences/{indicationpreference_id}", response_model=IndicationpreferenceRead)
def read_indicationpreference_by_id(
        *,
        session: Session = Depends(get_session),
        indicationpreference_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        indicationpreference = session.get(Indicationpreference, indicationpreference_id)
        if not indicationpreference:
            raise HTTPException(status_code=404, detail="No indicationpreferences found")

        if accept and "application/xml" in accept:
            return Response(content=indicationpreferences_to_xml_string(([indicationpreference])), media_type="application/xml")
        else:
            return indicationpreference


@app.get("/profiles/{profile_id}/agepreferences", response_model=List[AgepreferenceRead])
def read_agepreferences_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        agepreferences = session.query(Agepreference).filter(Agepreference.profile_id == profile_id).all()
        if not agepreferences:
            raise HTTPException(status_code=404, detail="No agepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=agepreferences_to_xml_string(agepreferences), media_type="application/xml")
        else:
            return agepreferences


@app.get("/agepreferences/{agepreference_id}", response_model=AgepreferenceRead)
def read_agepreference_by_id(
        *,
        session: Session = Depends(get_session),
        agepreference_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        agepreference = session.get(Agepreference, agepreference_id)
        if not agepreference:
            raise HTTPException(status_code=404, detail="No agepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=agepreferences_to_xml_string(([agepreference])), media_type="application/xml")
        else:
            return agepreference