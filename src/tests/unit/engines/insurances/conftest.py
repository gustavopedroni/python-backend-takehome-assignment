import pytest

from app.data.contants.insurances_line import InsurancesLineKey
from app.engines.insurances.common.final_score import FinalScore
from app.engines.insurances.common.insurance_line import InsuranceLine
from app.engines.insurances.common.risk_score import RiskScore


@pytest.fixture
def risk_score():
    return RiskScore()


@pytest.fixture
def final_score():
    return FinalScore()


@pytest.fixture
def generic_insurance_line(user_common_data):
    return InsuranceLine(user_data=user_common_data, key=InsurancesLineKey.GENERIC)
