from app.data.schemas.risk_score import score
from .base_rule import BaseRiskScoreRule


class LifeRiskScoreRule(BaseRiskScoreRule):

    key = 'life'

    def calculate(self) -> score.ScoreEnum:
        return score.ScoreEnum.ineligible
