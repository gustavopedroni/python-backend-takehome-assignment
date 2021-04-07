from app.data.schemas.score import FinalRiskScoreSchema, NumberRiskScoreSchema


def test_outputs_types(insurances_engine, user_mixed_data):
    """ Testing output data of calculate function
    """

    final_score, number_score = insurances_engine.calculate(user_data=user_mixed_data)

    assert isinstance(final_score, FinalRiskScoreSchema)
    assert isinstance(number_score, NumberRiskScoreSchema)


def test_score_sample_data(insurances_engine, user_mixed_data):
    """ Testing an example of user_data and expected output
    """

    final_score, number_score = insurances_engine.calculate(user_data=user_mixed_data)
    final_score_dict = final_score.dict()

    assert final_score_dict['auto'] == 'regular'
    assert final_score_dict['disability'] == 'ineligible'
    assert final_score_dict['home'] == 'economic'
    assert final_score_dict['life'] == 'regular'
