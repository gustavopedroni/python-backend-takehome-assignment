from app.data.schemas.risk_score import score
from .base_rule import BaseRiskScoreRule


class DisabilityRiskScoreRule(BaseRiskScoreRule):

    key = 'disability'

    def calculate(self) -> score.ScoreEnum:
        return score.ScoreEnum.ineligible
