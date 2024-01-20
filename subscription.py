from main import *


@app.get("/subscriptions/totalSubscriptionSD/")
def read_totalsd(*, session: Session = Depends(get_session),
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        result = session.exec(text('CALL `calculateTotalSubscriptionSD`();'))
        total_sd_row = result.fetchone()
        total_sd = total_sd_row[0]

        if accept and "application/xml" in accept:
            return PlainTextResponse(content=f"<amount>{total_sd}</amount>", media_type="application/xml")
            pass
        else:
            return {"amount": f"{total_sd}"}