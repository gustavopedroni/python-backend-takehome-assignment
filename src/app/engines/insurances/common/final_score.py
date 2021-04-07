from app.data.schemas.score import FinalScoreEnum
from .risk_score import RiskScore


class FinalScore(RiskScore):
    """Apply a business rule, mapping the score to its respective FinalScore type
    """

    def get_final_score(self) -> FinalScoreEnum:

        if not isinstance(self.num_score, int):
            return FinalScoreEnum.INELIGIBLE
        elif self.num_score <= 0:
            return FinalScoreEnum.ECONOMIC
        elif self.num_score in [1, 2]:
            return FinalScoreEnum.REGULAR
        elif self.num_score >= 3:
            return FinalScoreEnum.RESPONSIBLE
        else:
            return FinalScoreEnum.INELIGIBLE
