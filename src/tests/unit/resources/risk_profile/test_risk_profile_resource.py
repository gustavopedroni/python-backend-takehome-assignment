import json


def test_post_risk_profile(test_app):

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    test_response_payload = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "economic",
        "life": "regular"
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_post_invalid_age(test_app):

    test_request_payload = {
        "age": -120,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422


def test_post_invalid_dependents(test_app):

    test_request_payload = {
        "age": -120,
        "dependents": -1,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422


def test_post_invalid_house(test_app):

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": 1,
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned_status"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422


def test_post_invalid_income(test_app):

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": None,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422


def test_post_invalid_marital_status(test_app):

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "wrong_status",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": False,
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422


def test_post_invalid_risk_questions(test_app):
    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [5, 2, 0],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0, 1],
        "vehicle": {
            "year": 2018
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422


def test_post_invalid_vehicle(test_app):

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": 2
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422

    test_request_payload = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {
            "year": 0
        }
    }

    response = test_app.post("/v1/risk_profile/", data=json.dumps(test_request_payload))
    assert response.status_code == 422




