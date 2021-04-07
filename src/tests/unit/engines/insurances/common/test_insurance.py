import pytest

from app.data.contants.insurances_line import InsurancesLineKey
from app.data.schemas.personal.information import PersonalInformationSchema
from app.engines.insurances.common.insurance_line import InsuranceLine


@pytest.mark.parametrize(
    "risk_questions, base_score",
    (([0, 0, 0], 0), ([0, 0, 1], 1), ([0, 1, 1], 2), ([1, 1, 1], 3)),
)
def test_insurance_base_score(
    risk_questions, base_score, user_common_data: PersonalInformationSchema
):
    """Test if Insurance sum the RiskQuestions and apply on base_score and num_score"""

    user_common_data.risk_questions = risk_questions

    insurance = InsuranceLine(user_data=user_common_data, key=InsurancesLineKey.GENERIC)

    assert insurance.base_score == base_score
    assert insurance.num_score == base_score
