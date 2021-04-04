def test_dont_have_income(risk_score_engine, user_data_without_income):

    final_score, _ = risk_score_engine.calculate(user_data=user_data_without_income)
    final_score_dict = final_score.dict()

    assert final_score_dict['disability'] == 'ineligible'


def test_dont_have_vehicle(risk_score_engine, user_data_without_vehicle):

    final_score, _ = risk_score_engine.calculate(user_data=user_data_without_vehicle)
    final_score_dict = final_score.dict()

    assert final_score_dict['auto'] == 'ineligible'


def test_dont_have_house(risk_score_engine, user_data_without_house):

    final_score, _ = risk_score_engine.calculate(user_data=user_data_without_house)
    final_score_dict = final_score.dict()

    assert final_score_dict['home'] == 'ineligible'


def test_age_over_60_years(risk_score_engine, user_data_age_over_60_years):

    final_score, _ = risk_score_engine.calculate(user_data=user_data_age_over_60_years)
    final_score_dict = final_score.dict()

    assert final_score_dict['disability'] == 'ineligible'
    assert final_score_dict['life'] == 'ineligible'


def test_age_under_30_years(risk_score_engine, user_common_data, user_data_age_under_30_years):

    _, first_number_score = risk_score_engine.calculate(user_data=user_common_data)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_age_under_30_years)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['disability'] - 1 == number_score_dict['disability']
    assert first_number_score_dict['life'] - 1 == number_score_dict['life']
    assert first_number_score_dict['home'] - 1 == number_score_dict['home']
    assert first_number_score_dict['auto'] - 1 == number_score_dict['auto']


def test_age_between_30_40_years(risk_score_engine, user_data_age_under_30_years, user_data_age_between_30_40_years):

    _, first_number_score = risk_score_engine.calculate(user_data=user_data_age_under_30_years)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_age_between_30_40_years)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['disability'] + 1 == number_score_dict['disability']
    assert first_number_score_dict['life'] + 1 == number_score_dict['life']
    assert first_number_score_dict['home'] + 1 == number_score_dict['home']
    assert first_number_score_dict['auto'] + 1 == number_score_dict['auto']


def test_income_above_200k(risk_score_engine, user_common_data, user_data_income_above_200k):

    _, first_number_score = risk_score_engine.calculate(user_data=user_common_data)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_income_above_200k)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['disability'] - 1 == number_score_dict['disability']
    assert first_number_score_dict['life'] - 1 == number_score_dict['life']
    assert first_number_score_dict['home'] - 1 == number_score_dict['home']
    assert first_number_score_dict['auto'] - 1 == number_score_dict['auto']


def test_house_mortgaged(risk_score_engine, user_common_data, user_data_house_mortgaged):

    _, first_number_score = risk_score_engine.calculate(user_data=user_common_data)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_house_mortgaged)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['home'] + 1 == number_score_dict['home']
    assert first_number_score_dict['disability'] + 1 == number_score_dict['disability']


def test_has_dependents(risk_score_engine, user_common_data, user_data_with_dependents):

    _, first_number_score = risk_score_engine.calculate(user_data=user_common_data)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_with_dependents)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['life'] + 1 == number_score_dict['life']
    assert first_number_score_dict['disability'] + 1 == number_score_dict['disability']


def test_is_married(risk_score_engine, user_common_data, user_data_married):

    _, first_number_score = risk_score_engine.calculate(user_data=user_common_data)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_married)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['life'] + 1 == number_score_dict['life']
    assert first_number_score_dict['disability'] - 1 == number_score_dict['disability']


def test_vehicle_produced_in_last_5_years(risk_score_engine, user_common_data, user_data_vehicle_last_5_years):

    _, first_number_score = risk_score_engine.calculate(user_data=user_common_data)
    first_number_score_dict = first_number_score.dict()

    _, number_score = risk_score_engine.calculate(user_data=user_data_vehicle_last_5_years)
    number_score_dict = number_score.dict()

    assert first_number_score_dict['auto'] + 1 == number_score_dict['auto']


def test_score_final_evaluation(risk_score_engine, user_mixed_data):

    final_score, number_score = risk_score_engine.calculate(user_data=user_mixed_data)

    final_score_dict = final_score.dict()

    assert final_score_dict['auto'] == 'regular'
    assert final_score_dict['disability'] == 'ineligible'
    assert final_score_dict['home'] == 'economic'
    assert final_score_dict['life'] == 'regular'
