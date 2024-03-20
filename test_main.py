import requests

BASE_URL = "http://127.0.0.1:8000/v1/phone-numbers"

def test_phone_number_with_plus_and_country_code():
    response = requests.get(f"{BASE_URL}?phoneNumber=%2B12125690123")
    assert response.status_code == 200
    assert response.json() == {
        "phoneNumber": "+1 212-569-0123",
        "countryCode": "US",
        "areaCode": "212",
        "localPhoneNumber": "5690123"
    }

def test_phone_number_with_spaces_and_country_code():
    response = requests.get(f"{BASE_URL}?phoneNumber=%2B52%20631%20311%208150")
    assert response.status_code == 200
    assert "countryCode" in response.json()
    assert response.json()["countryCode"] == "MX"

def test_phone_number_without_plus_but_with_country_code():
    response = requests.get(f"{BASE_URL}?phoneNumber=915872200&countryCode=ES")
    assert response.status_code == 200
    assert "countryCode" in response.json()
    assert response.json()["countryCode"] == "ES"

def test_invalid_phone_number_with_spaces():
    response = requests.get(f"{BASE_URL}?phoneNumber=351%2021%20094%202000")
    assert response.status_code == 400
    assert "error" in response.json()

def test_missing_phone_number_parameter():
    response = requests.get(BASE_URL)
    assert response.status_code == 400
    assert "error" in response.json()

def test_missing_country_code_for_number_without_plus():
    response = requests.get(f"{BASE_URL}?phoneNumber=6313118150")
    assert response.status_code == 400
    assert response.json() == {
        "phoneNumber": "6313118150",
        "error": {"countryCode": "required value is missing"}
    }
