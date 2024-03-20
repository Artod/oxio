from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import phonenumbers
from phonenumbers import NumberParseException, geocoder
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Go to": "/v1/phone-numbers"}

@app.get("/v1/phone-numbers")
async def get_phone_number_info(phoneNumber: Optional[str] = Query(None, alias="phoneNumber"), countryCode: Optional[str] = Query(None)):
    """
    Retrieves detailed information about a phone number.

    This endpoint accepts a phone number and, optionally, a country code. It returns the phone number's country code, area code, and local phone number. The phone number should be provided in E.164 format, but the '+' prefix is optional. Spaces within the phone number are allowed for readability.

    Parameters:
    - `phoneNumber`: The phone number in E.164 format (e.g., +12125690123, +52 631 3118150). The '+' prefix is optional.
    - `countryCode`: The ISO 3166-1 alpha-2 country code (e.g., US, MX). Required if the phone number does not include a country code.

    Returns:
    - On success, returns a JSON object with the phone number's country code, area code, and local phone number.
    - On failure, returns an error message indicating what went wrong (e.g., invalid phone number format, missing required parameters).
    """
    
    if phoneNumber is None:
        return JSONResponse(status_code=400, content={"error": "phoneNumber parameter is required"})

    try:
        if phoneNumber.startswith('+'):
            parsed_number = phonenumbers.parse(phoneNumber, None)
        else:
            if not countryCode:
                content = {
                    "phoneNumber": phoneNumber,
                    "error": {
                        "countryCode": "required value is missing"
                    }
                }
                return JSONResponse(status_code=400, content=content)
            parsed_number = phonenumbers.parse(phoneNumber, countryCode)

        if not phonenumbers.is_valid_number(parsed_number):
            return JSONResponse(status_code=400, content={"error": "Invalid phone number"})

        country_code = str(parsed_number.country_code)
        national_number = str(parsed_number.national_number)
        area_code, local_phone_number = national_number[:-7], national_number[-7:]

        return {
            "phoneNumber": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "countryCode": geocoder.region_code_for_number(parsed_number),
            "areaCode": area_code,
            "localPhoneNumber": local_phone_number
        }
    except NumberParseException:
        return JSONResponse(status_code=400, content={"error": "Invalid phone number format"})
