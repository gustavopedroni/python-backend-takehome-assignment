from app.data.schemas.risk_score import score
from .base_rule import BaseRiskScoreRule


class HomeRiskScoreRule(BaseRiskScoreRule):

    key = 'home'

    def calculate(self) -> score.ScoreEnum:
        return score.ScoreEnum.ineligible
