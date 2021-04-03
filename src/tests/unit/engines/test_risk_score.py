from app.data.schemas.risk_profile import personal_information
from app.engines.risk_score.risk_score_engine import RiskScoreEngine


def test_dont_have_income():
    fake_user_data_dict = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    final_score_dict = risk_score_engine.calculate().dict()

    assert final_score_dict['disability'] == 'ineligible'


def test_dont_have_vehicles():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 1000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": None
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    final_score_dict = risk_score_engine.calculate().dict()

    assert final_score_dict['auto'] == 'ineligible'


def test_dont_have_houses():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 2,
        "house": None,
        "income": 1000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    final_score_dict = risk_score_engine.calculate().dict()

    assert final_score_dict['home'] == 'ineligible'


def test_dont_have_over_60_years():

    fake_user_data_dict = {
        "age": 65,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 1000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    final_score_dict = risk_score_engine.calculate().dict()

    assert final_score_dict['disability'] == 'ineligible'
    assert final_score_dict['life'] == 'ineligible'


def test_under_30_years():

    fake_user_data_dict = {
        "age": 29,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 1000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert scores_dict['disability'] == 2
    assert scores_dict['life'] == 2
    assert scores_dict['home'] == 2
    assert scores_dict['auto'] == 2


def test_between_30_40_years():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 1000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert scores_dict['disability'] == 1
    assert scores_dict['life'] == 1
    assert scores_dict['home'] == 1
    assert scores_dict['auto'] == 1


def test_income_above_200k():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 250000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert scores_dict['disability'] == 1
    assert scores_dict['life'] == 1
    assert scores_dict['home'] == 1
    assert scores_dict['auto'] == 1


def test_house_mortgaged():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 250000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    first_scores_dict = risk_score_engine.get_scores().dict()
    first_score_home = first_scores_dict['home']
    first_score_disability = first_scores_dict['disability']

    fake_user_data_dict['house'] = {"ownership_status": "mortgaged"}

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert first_score_home + 1 == scores_dict['home']
    assert first_score_disability + 1 == scores_dict['disability']


def test_has_dependents():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "income": 250000,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    first_scores_dict = risk_score_engine.get_scores().dict()
    first_score_life = first_scores_dict['life']
    first_score_disability = first_scores_dict['disability']

    fake_user_data_dict['dependents'] = 1

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert first_score_life + 1 == scores_dict['life']
    assert first_score_disability + 1 == scores_dict['disability']


def test_is_married():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "income": 250000,
        "marital_status": "single",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    first_scores_dict = risk_score_engine.get_scores().dict()
    first_score_life = first_scores_dict['life']
    first_score_disability = first_scores_dict['disability']

    fake_user_data_dict['marital_status'] = 'married'

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert first_score_life + 1 == scores_dict['life']
    assert first_score_disability - 1 == scores_dict['disability']


def test_vehicle_produced_in_last_5_years():

    fake_user_data_dict = {
        "age": 35,
        "dependents": 0,
        "house": {"ownership_status": "owned"},
        "income": 250000,
        "marital_status": "single",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    first_scores_dict = risk_score_engine.get_scores().dict()
    first_score_auto = first_scores_dict['auto']

    fake_user_data_dict['marital_status'] = 'married'

    fake_user_data = personal_information.PersonalInformationSchema(**fake_user_data_dict)

    risk_score_engine = RiskScoreEngine(user_data=fake_user_data)
    risk_score_engine.calculate()

    scores_dict = risk_score_engine.get_scores().dict()

    assert first_score_auto + 1 == scores_dict['auto']


def test_score_final_evaluation():

    # 0 and below maps to “economic”.
    # 1 and 2 maps to “regular”.
    # 3 and above maps to “responsible”.

    pass
