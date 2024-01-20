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


@app.post("/profiles/{profile_id}/genrepreferences", response_model=GenrespreferenceRead)
def create_genrepreference(
    *,
    session: Session = Depends(get_session),
    profile_id: int,
    genrepreference_create: GenrespreferenceCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        preference_data = genrepreference_create.dict()
        preference_data["profile_id"] = profile_id

        preference = Genrespreference(**preference_data)
        session.add(preference)
        session.commit()
        return preference


@app.post("/profiles/{profile_id}/indicationpreferences", response_model=IndicationpreferenceRead)
def create_indicationpreference(
    *,
    session: Session = Depends(get_session),
    profile_id: int,
    indicationpreference_create: IndicationpreferenceCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        preference_data = indicationpreference_create.dict()
        preference_data["profile_id"] = profile_id

        preference = Indicationpreference(**preference_data)
        session.add(preference)
        session.commit()
        return preference


@app.post("/profiles/{profile_id}/indicationpreferences", response_model=AgepreferenceRead)
def create_agepreference(
    *,
    session: Session = Depends(get_session),
    profile_id: int,
    agepreference_create: AgepreferenceCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        preference_data = agepreference_create.dict()
        preference_data["profile_id"] = profile_id

        preference = Agepreference(**preference_data)
        session.add(preference)
        session.commit()
        return preference


@app.put("/agepreferences/{agepreference_id}", response_model=AgepreferenceRead)
def update_agepreference(
        *,
        session: Session = Depends(get_session),
        agepreference_id: int,
        agepreference_update: AgepreferenceCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        agepreference = session.get(Agepreference, agepreference_id)
        if not agepreference:
            raise HTTPException(status_code=404, detail="Agepreference not found")

        for field, value in agepreference_update.dict().items():
            setattr(agepreference, field, value)

        session.commit()
        return agepreference


@app.delete("/agepreferences/{agepreference_id}")
def delete_agepreference(*, session: Session = Depends(get_session),
                    agepreference_id: int,
                    api_key_header: Optional[str] = Depends(api_key_header)
                    ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        agepreference = session.get(Agepreference, agepreference_id)
        if not agepreference:
            raise HTTPException(status_code=404, detail="Agepreference not found")

        session.delete(agepreference)
        session.commit()
        return {"message": "Agepreference deleted successfully"}


@app.put("/indicationpreferences/{indicationpreference_id}", response_model=IndicationpreferenceRead)
def update_indicationpreference(
        *,
        session: Session = Depends(get_session),
        indicationpreference_id: int,
        indicationpreference_update: IndicationpreferenceCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        indicationpreference = session.get(Indicationpreference, indicationpreference_id)
        if not indicationpreference:
            raise HTTPException(status_code=404, detail="Indicationpreference not found")

        for field, value in indicationpreference_update.dict().items():
            setattr(indicationpreference, field, value)

        session.commit()
        return indicationpreference


@app.delete("/indicationpreferences/{indicationpreference_id}")
def delete_indicationpreference(*, session: Session = Depends(get_session),
                    indicationpreference_id: int,
                    api_key_header: Optional[str] = Depends(api_key_header)
                    ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        indicationpreference = session.get(Indicationpreference, indicationpreference_id)
        if not indicationpreference:
            raise HTTPException(status_code=404, detail="Indicationpreference not found")

        session.delete(indicationpreference)
        session.commit()
        return {"messindication": "Indicationpreference deleted successfully"}


@app.put("/genrepreferences/{genrepreference_id}", response_model=GenrespreferenceRead)
def update_genrepreference(
        *,
        session: Session = Depends(get_session),
        genrepreference_id: int,
        genrepreference_update: GenrespreferenceCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        genrepreference = session.get(Genrespreference, genrepreference_id)
        if not genrepreference:
            raise HTTPException(status_code=404, detail="Genrepreference not found")

        for field, value in genrepreference_update.dict().items():
            setattr(genrepreference, field, value)

        session.commit()
        return genrepreference


@app.delete("/genrepreferences/{genrepreference_id}")
def delete_genrepreference(*, session: Session = Depends(get_session),
                    genrepreference_id: int,
                    api_key_header: Optional[str] = Depends(api_key_header)
                    ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        genrepreference = session.get(Genrespreference, genrepreference_id)
        if not genrepreference:
            raise HTTPException(status_code=404, detail="Genrepreference not found")

        session.delete(genrepreference)
        session.commit()
        return {"messgenre": "Genrepreference deleted successfully"}