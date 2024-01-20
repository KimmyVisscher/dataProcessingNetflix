from main import *


@app.get("/accounts", response_model=List[AccountRead])
def read_accounts(*,
                session: Session = Depends(get_session),
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        accounts = session.query(Account).all()
        if not accounts:
            raise HTTPException(status_code=404, detail="No accounts found")

        if accept and "application/xml" in accept:
            # account_data = {"account": [account.dict() for account in accounts]}
            # xml_content = xmltodict.unparse(account_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=account_to_xml_string(accounts), media_type="application/xml")
        else:
            return accounts


@app.get("/accounts/{account_id}", response_model=AccountRead)
def read_account(*, session: Session = Depends(get_session),
               account_id: int,
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        account = session.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"account": account.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=account_to_xml_string([account]), media_type="application/xml")
        else:
            return account


@app.get("/accounts/{account_id}/profiles", response_model=List[ProfileRead])
def read_profiles_by_account(
        *,
        session: Session = Depends(get_session),
        account_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profiles = session.query(Profile).filter(Profile.account_id == account_id).all()
        if not profiles:
            raise HTTPException(status_code=404, detail="No profiles found")

        if accept and "application/xml" in accept:
            # profiles_data = {"profile": [profile.dict() for profile in profiles]}
            # xml_content = xmltodict.unparse(profiles_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=profile_to_xml_string(profiles), media_type="application/xml")
        else:
            return profiles


@app.get("/profiles/{profile_id}", response_model=ProfileRead)
def read_profile_by_id(*, session: Session = Depends(get_session),
               profile_id: int,
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"profile": profile.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=profile_to_xml_string([profile]), media_type="application/xml")
        else:
            return profile


@app.post("/accounts", response_model=AccountRead)
def create_account(*, session: Session = Depends(get_session),
                 account_create: AccountCreate,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        account = Account(**account_create.dict())
        session.add(account)
        session.commit()
        return account


@app.post("/profiles", response_model=ProfileRead)
def create_profile(
        *,
        session: Session = Depends(get_session),
        profile_create: ProfileCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        account_id = profile_create.account_id
        if not session.query(Account).filter(Account.account_id == account_id).first():
            raise HTTPException(status_code=404, detail="Account not found")

        profile = Profile(**profile_create.dict())
        session.add(profile)
        session.commit()
        return profile


@app.put("/accounts/{account_id}", response_model=AccountRead)
def update_account(
        *,
        session: Session = Depends(get_session),
        account_id: int,
        account_update: AccountCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        account = session.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        for field, value in account_update.dict().items():
            setattr(account, field, value)

        session.commit()
        return account


@app.put("/profiles/{profile_id}", response_model=ProfileRead)
def update_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        profile_update: ProfileCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        for field, value in profile_update.dict().items():
            setattr(profile, field, value)

        session.commit()
        return profile


@app.delete("/accounts/{account_id}")
def delete_account(*, session: Session = Depends(get_session),
                   account_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        account = session.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        session.delete(account)
        session.commit()
        return {"message": "Account deleted successfully"}


@app.delete("/profiles/{profile_id}")
def delete_profile(*, session: Session = Depends(get_session),
                   profile_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        session.delete(profile)
        session.commit()
        return {"message": "Profile deleted successfully"}


@app.get("/accounts/totalrevenue/")
def read_totalrevenue(*, session: Session = Depends(get_session),
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        result = session.exec(text('CALL `CalculateTotalMonthlyRevenue`();'))
        total_revenue_row = result.fetchone()
        total_revenue = total_revenue_row[0]

        if accept and "application/xml" in accept:
            return PlainTextResponse(content=f"<revenue>{total_revenue}</revenue>", media_type="application/xml")
            pass
        else:
            return {"revenue": f"{total_revenue}"}