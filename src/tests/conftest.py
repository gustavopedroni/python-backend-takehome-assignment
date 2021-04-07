import pytest
from starlette.testclient import TestClient

from app.data.schemas.personal.information import PersonalInformationSchema
from app.engines.insurances.insurances_engine import InsurancesEngine
from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture
def user_common_data_dict():
    return {
        "age": 35,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 0, 0],
        "vehicle": {"year": 2000}
    }


@pytest.fixture
def user_common_data(user_common_data_dict):
    return PersonalInformationSchema(**user_common_data_dict)


@pytest.fixture
def user_mixed_data():
    user_data = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_without_income(user_common_data_dict):

    user_data = {**user_common_data_dict, "income": 0}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_without_vehicle(user_common_data_dict):

    user_data = {**user_common_data_dict, "vehicle": None}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_without_house(user_common_data_dict):

    user_data = {**user_common_data_dict, "house": None}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_age_over_60_years(user_common_data_dict):
    user_data = {**user_common_data_dict, "age": 65}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_age_under_30_years(user_common_data_dict):
    user_data = {**user_common_data_dict, "age": 29}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_age_between_30_40_years(user_common_data_dict):
    user_data = {**user_common_data_dict, "age": 35}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_income_above_200k(user_common_data_dict):
    user_data = {**user_common_data_dict, "income": 250000}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_house_mortgaged(user_common_data_dict):
    user_data = {**user_common_data_dict, "house": {"ownership_status": "mortgaged"}}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_with_dependents(user_common_data_dict):
    user_data = {**user_common_data_dict, "dependents": 1}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_married(user_common_data_dict):
    user_data = {**user_common_data_dict, "marital_status": "married"}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def user_data_vehicle_last_5_years(user_common_data_dict):
    user_data = {**user_common_data_dict, "vehicle": {"year": 2018}}

    return PersonalInformationSchema(**user_data)


@pytest.fixture
def insurances_engine():
    return InsurancesEngine()
