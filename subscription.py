from main import *


@app.get("/subscriptions/gettotal")
def read_total_accounts_by_quality(*, session: Session = Depends(get_session),
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None),
               quality: Quality
               ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        result = session.execute(
            text('CALL `calculateTotalAccountsWithParam`(:parameter);'),
            {"parameter": quality.name}
        )
        print(result)
        total_row = result.fetchone()
        total = total_row[0]

        if accept and "application/xml" in accept:
            return PlainTextResponse(content=f"<amount>{total}</amount>", media_type="application/xml")
            pass
        else:
            return {"amount": f"{total}"}