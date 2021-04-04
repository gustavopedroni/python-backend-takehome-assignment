import pytest

from app.engines.risk_score.risk_score_engine import RiskScoreEngine


@pytest.fixture
def risk_score_engine():
    return RiskScoreEngine()
