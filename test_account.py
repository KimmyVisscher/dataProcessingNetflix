from account import *

from test_main import client


# GET all accounts

def test_read_all_accounts_json_response():
    response = client.get("/accounts", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "email": "john.doe@example.com",
            "payment_method": "credit_card",
            "username": "john_doe",
            "subscription_id": 1
        },
        {
            "email": "jane.smith@example.com",
            "payment_method": "paypal",
            "username": "jane_smith",
            "subscription_id": 2
        },
        {
            "email": "alice.jones@example.com",
            "payment_method": "debit_card",
            "username": "alice_jones",
            "subscription_id": 1
        },
        {
            "email": "bob.white@example.com",
            "payment_method": "credit_card",
            "username": "bob_white",
            "subscription_id": 3
        },
        {
            "email": "mary.green@example.com",
            "payment_method": "paypal",
            "username": "mary_green",
            "subscription_id": 2
        },
        {
            "email": "sam.brown@example.com",
            "payment_method": "debit_card",
            "username": "sam_brown",
            "subscription_id": 1
        },
        {
            "email": "emily.wilson@example.com",
            "payment_method": "credit_card",
            "username": "emily_wilson",
            "subscription_id": 3
        },
        {
            "email": "charlie.rogers@example.com",
            "payment_method": "paypal",
            "username": "charlie_rogers",
            "subscription_id": 1
        },
        {
            "email": "olivia.hall@example.com",
            "payment_method": "debit_card",
            "username": "olivia_hall",
            "subscription_id": 2
        },
        {
            "email": "david.lee@example.com",
            "payment_method": "credit_card",
            "username": "david_lee",
            "subscription_id": 3
        },
        {
            "email": "sophie.collins@example.com",
            "payment_method": "paypal",
            "username": "sophie_collins",
            "subscription_id": 2
        },
        {
            "email": "max.miller@example.com",
            "payment_method": "debit_card",
            "username": "max_miller",
            "subscription_id": 1
        }
    ]

    assert response.json() == expected_data


def test_read_all_accounts_xml_response():
    response = client.get("/accounts", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<accounts>\n  <account>\n      <email>john.doe@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>john_doe</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>jane.smith@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>jane_smith</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>alice.jones@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>alice_jones</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>bob.white@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>bob_white</username>\n      <subscription_id>3</subscription_id>\n  </account>  <account>\n      <email>mary.green@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>mary_green</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>sam.brown@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>sam_brown</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>emily.wilson@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>emily_wilson</username>\n      <subscription_id>3</subscription_id>\n  </account>  <account>\n      <email>charlie.rogers@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>charlie_rogers</username>\n      <subscription_id>1</subscription_id>\n  </account>  <account>\n      <email>olivia.hall@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>olivia_hall</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>david.lee@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>david_lee</username>\n      <subscription_id>3</subscription_id>\n  </account>  <account>\n      <email>sophie.collins@example.com</email>\n      <payment_method>paypal</payment_method>\n      <username>sophie_collins</username>\n      <subscription_id>2</subscription_id>\n  </account>  <account>\n      <email>max.miller@example.com</email>\n      <payment_method>debit_card</payment_method>\n      <username>max_miller</username>\n      <subscription_id>1</subscription_id>\n  </account></accounts>"


def test_read_all_accounts_unauthorized():
    response = client.get("/accounts")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_all_accounts_no_permission():
    response = client.get("/accounts", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET account by ID

def test_read_account_json_response():
    response = client.get("/accounts/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "email": "john.doe@example.com",
        "payment_method": "credit_card",
        "username": "john_doe",
        "subscription_id": 1
    }


def test_read_account_xml_response():
    response = client.get("/accounts/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<accounts>\n  <account>\n      <email>john.doe@example.com</email>\n      <payment_method>credit_card</payment_method>\n      <username>john_doe</username>\n      <subscription_id>1</subscription_id>\n  </account></accounts>"


def test_read_account_unauthorized():
    response = client.get("/accounts/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_account_not_found():
    response = client.get("/accounts/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Account not found"
    }


def test_read_account_no_permission():
    response = client.get("/accounts/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET profiles by account ID

def test_read_profiles_by_account_json_response():
    response = client.get("/accounts/1/profiles", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200

    expected_data = [
        {
            "profile_image": "/path/to/image",
            "profile_child": 0,
            "language": "DUTCH",
            "account_id": 1,
            "profile_id": 1
        },
        {
            "profile_image": "/path/to/image",
            "profile_child": 0,
            "language": "DUTCH",
            "account_id": 1,
            "profile_id": 2
        }
    ]

    assert response.json() == expected_data


def test_read_profiles_by_account_xml_response():
    response = client.get("/accounts/1/profiles", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<profiles>\n  <profile>\n      <profile_image>/path/to/image</profile_image>\n      <profile_child>0</profile_child>\n      <language>Language.DUTCH</language>\n      <account_id>1</account_id>\n  </profile>  <profile>\n      <profile_image>/path/to/image</profile_image>\n      <profile_child>0</profile_child>\n      <language>Language.DUTCH</language>\n      <account_id>1</account_id>\n  </profile></profiles>"


def test_read_profiles_by_account_unauthorized():
    response = client.get("/accounts/1/profiles")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_profiles_by_account_not_found():
    response = client.get("/accounts/999/profiles", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No profiles found"
    }


def test_read_profiles_by_account_no_permission():
    response = client.get("/accounts/1/profiles", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }


# GET profile by ID

def test_read_profile_by_id_json_response():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior"})
    assert response.status_code == 200
    assert response.json() == {
        "profile_image": "/path/to/image",
        "profile_child": 0,
        "language": "DUTCH",
        "account_id": 1,
        "profile_id": 1
    }


def test_read_profile_by_id_xml_response():
    response = client.get("/profiles/1", headers={"X-API-KEY": "senior", "accept": "application/xml"})
    assert response.status_code == 200
    assert response.text == "<profiles>\n  <profile>\n      <profile_image>/path/to/image</profile_image>\n      <profile_child>0</profile_child>\n      <language>Language.DUTCH</language>\n      <account_id>1</account_id>\n  </profile></profiles>"


def test_read_profile_by_id_unauthorized():
    response = client.get("/profiles/1")
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid API key"
    }


def test_read_profile_by_id_not_found():
    response = client.get("/profiles/999", headers={"X-API-KEY": "senior"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Profile not found"
    }


def test_read_profile_by_id_no_permission():
    response = client.get("/profiles/1", headers={"X-API-KEY": "unauthorized"})
    assert response.status_code == 403
    assert response.json() == {
        "detail": "No permission"
    }
