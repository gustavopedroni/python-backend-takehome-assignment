import pytest
from pytest_lazyfixture import lazy_fixture


from app.data.contants.insurances_line import InsurancesLineKey
from app.engines.insurances.lines.rules import house, vehicle, personal


@pytest.mark.parametrize(
    'rule_class, line_key, user_data',
    [
        (house.NotHaveHouseRule, InsurancesLineKey.HOME, lazy_fixture('user_data_without_house')),
        (personal.NotHaveIncomeRule, InsurancesLineKey.DISABILITY, lazy_fixture('user_data_without_income')),
        (vehicle.NotHaveVehicleRule, InsurancesLineKey.AUTO, lazy_fixture('user_data_without_vehicle')),
    ]
)
def test_dont_have_rule(rule_class, line_key, user_data, risk_score):
    """Tests if the rule returns empty on the correct line
    """

    rule = rule_class(line_key=line_key)
    score = rule.apply(
        data=user_data,
        score=risk_score.num_score
    )

    assert score is None

    others_keys = tuple([x for x in InsurancesLineKey if x is not line_key])

    for key in others_keys:

        rule = personal.NotHaveIncomeRule(line_key=key)
        score = rule.apply(
            data=user_data,
            score=risk_score.num_score
        )

        assert score is not None


def test_age_over_60_years(risk_score, user_data_age_over_60_years):
    """Tests if the OldAgeRule return empty on DISABILITY and LIFE, but only on them
    """

    allowed_keys = (InsurancesLineKey.LIFE, InsurancesLineKey.DISABILITY)
    others_keys = tuple([x for x in InsurancesLineKey if x not in allowed_keys])

    for key in allowed_keys:
        rule = personal.OldAgeRule(line_key=key)

        score = rule.apply(
            data=user_data_age_over_60_years,
            score=risk_score.num_score
        )

        assert score is None

    for key in others_keys:

        rule = personal.OldAgeRule(line_key=key)
        score = rule.apply(
            data=user_data_age_over_60_years,
            score=risk_score.num_score
        )

        assert score is not None


def test_age_under_30_years(risk_score, user_data_age_under_30_years):
    """Test if the YoungAgeRule reduces 2 point on score in all lines
    """

    for key in tuple(InsurancesLineKey):

        rule = personal.YoungAgeRule(line_key=key)
        score = rule.apply(
            data=user_data_age_under_30_years,
            score=risk_score.num_score
        )

        assert risk_score.num_score - 2 == score


def test_age_between_30_40_years(risk_score, user_data_age_between_30_40_years):
    """Test if the AdultAgeRule reduces 1 point on score in all lines
    """

    for key in tuple(InsurancesLineKey):

        rule = personal.AdultAgeRule(line_key=key)
        score = rule.apply(
            data=user_data_age_between_30_40_years,
            score=risk_score.num_score
        )

        assert risk_score.num_score - 1 == score


def test_income_above_200k(risk_score, user_data_income_above_200k):
    """Test if the HighIncomeRule reduces 1 point on score in all lines
    """

    for key in tuple(InsurancesLineKey):

        rule = personal.HighIncomeRule(line_key=key)
        score = rule.apply(
            data=user_data_income_above_200k,
            score=risk_score.num_score
        )

        assert risk_score.num_score - 1 == score


def test_house_mortgaged(risk_score, user_data_house_mortgaged):
    """Tests if the HouseMortgagedRule adds 1 point on DISABILITY and HOME lines, but only on them
    """

    allowed_keys = (InsurancesLineKey.HOME, InsurancesLineKey.DISABILITY)
    others_keys = tuple([x for x in InsurancesLineKey if x not in allowed_keys])

    for key in allowed_keys:
        rule = house.HouseMortgagedRule(line_key=key)

        score = rule.apply(
            data=user_data_house_mortgaged,
            score=risk_score.num_score
        )

        assert risk_score.num_score + 1 == score

    for key in others_keys:

        rule = house.HouseMortgagedRule(line_key=key)
        score = rule.apply(
            data=user_data_house_mortgaged,
            score=risk_score.num_score
        )

        assert risk_score.num_score == score


def test_has_dependents(risk_score, user_data_with_dependents):
    """Tests if the HasDependentsRule adds 1 point on DISABILITY and LIFE lines, but only on them
    """

    allowed_keys = (InsurancesLineKey.LIFE, InsurancesLineKey.DISABILITY)
    others_keys = tuple([x for x in InsurancesLineKey if x not in allowed_keys])

    for key in allowed_keys:
        rule = personal.HasDependentsRule(line_key=key)

        score = rule.apply(
            data=user_data_with_dependents,
            score=risk_score.num_score
        )

        assert risk_score.num_score + 1 == score

    for key in others_keys:

        rule = personal.HasDependentsRule(line_key=key)
        score = rule.apply(
            data=user_data_with_dependents,
            score=risk_score.num_score
        )

        assert risk_score.num_score == score


def test_is_married(risk_score, user_data_married):
    """Tests if the MarriedRule adds 1 point on LIFE line and reduces 1 point on DISABILITY line
       but only changes the score on them
    """

    rule = personal.MarriedRule(line_key=InsurancesLineKey.LIFE)
    score = rule.apply(
        data=user_data_married,
        score=risk_score.num_score
    )

    assert risk_score.num_score + 1 == score

    rule = personal.MarriedRule(line_key=InsurancesLineKey.DISABILITY)
    score = rule.apply(
        data=user_data_married,
        score=risk_score.num_score
    )

    assert risk_score.num_score - 1 == score

    others_keys = tuple([
        x for x in InsurancesLineKey
        if x not in (InsurancesLineKey.LIFE, InsurancesLineKey.DISABILITY)
    ])

    for key in others_keys:

        rule = personal.MarriedRule(line_key=key)
        score = rule.apply(
            data=user_data_married,
            score=risk_score.num_score
        )

        assert risk_score.num_score == score


def test_vehicle_produced_in_last_5_years(risk_score, user_data_vehicle_last_5_years):
    """Tests if the VehicleProducedLast5YearsRule adds 1 point on AUTO line, but only on them
    """
    rule = vehicle.VehicleProducedLast5YearsRule(line_key=InsurancesLineKey.AUTO)
    score = rule.apply(
        data=user_data_vehicle_last_5_years,
        score=risk_score.num_score
    )

    assert risk_score.num_score + 1 == score

    others_keys = tuple([
        x for x in InsurancesLineKey
        if x is not InsurancesLineKey.AUTO
    ])

    for key in others_keys:
        rule = vehicle.VehicleProducedLast5YearsRule(line_key=key)
        score = rule.apply(
            data=user_data_vehicle_last_5_years,
            score=risk_score.num_score
        )

        assert risk_score.num_score == score
