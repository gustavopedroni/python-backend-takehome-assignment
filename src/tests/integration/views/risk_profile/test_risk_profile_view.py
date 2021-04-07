import json

import pytest

from app.engines.insurances import insurances_engine


def test_post_risk_profile_response(test_app, mocker, user_common_data_dict):
    """Tests if the InsurancesEngine.calculate method is called
       and if the data is returned in the correct structure
    """
    spy_calculate = mocker.spy(insurances_engine.InsurancesEngine, 'calculate')

    response = test_app.post("/v1/risk_profile/", data=json.dumps(user_common_data_dict))

    assert response.status_code == 201

    user_data_schema = spy_calculate.call_args[1]['user_data']

    assert user_data_schema.dict() == user_common_data_dict
    assert spy_calculate.call_count == 1

    response_json = response.json()

    assert 'auto' in response_json
    assert 'disability' in response_json
    assert 'home' in response_json
    assert 'life' in response_json


@pytest.mark.parametrize(
    "field,value", [
        ("age", -120), ("age", None),
        ("dependents", -120), ("dependents", None),
        ("income", -120), ("income", None),
        ("marital_status", 'singled'), ("marital_status", ''), ("marital_status", None),
        ("risk_questions", [2, -1, 1]), ("risk_questions", [1, 1, 1, 1]), ("risk_questions", [1, 1]),
        ("house", {"status": "owned"}), ("house", 2), ("house", {"ownership_status": "mortgage"}),
        ("vehicle", {"year_of_model": 2050}), ("vehicle", 2), ("vehicle", {"year": -3})
    ]
)
def test_invalid_response_fields(field, value, user_common_data_dict, test_app):
    """Test if all field have the correct type validation
    """

    user_data = user_common_data_dict.copy()
    user_data[field] = value

    response = test_app.post("/v1/risk_profile/", data=json.dumps(user_data))
    assert response.status_code == 422
