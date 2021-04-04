from abc import ABC, abstractmethod

from app.data.schemas.risk_profile import personal_information
from app.data.schemas.risk_score import score


class BaseRiskScoreRule(ABC):

    key: ''

    def __init__(self, user_data: personal_information.PersonalInformationSchema):

        self.user_data = user_data

        self._base_score: int = sum(user_data.risk_questions)
        self._num_score: int = self._base_score
        self._final_score: score.ScoreEnum = score.ScoreEnum.INELIGIBLE

    @abstractmethod
    def calculate(self):
        pass

    @property
    def num_score(self):
        return self._num_score

    @num_score.setter
    def num_score(self, value):
        raise ValueError('Score cannot be changed in outside of rules!')

    @property
    def final_score(self):

        if not isinstance(self.num_score, int):
            return score.ScoreEnum.INELIGIBLE
        elif self.num_score <= 0:
            return score.ScoreEnum.ECONOMIC
        elif self.num_score in [1, 2]:
            return score.ScoreEnum.REGULAR
        elif self.num_score >= 3:
            return score.ScoreEnum.RESPONSIBLE
        else:
            return score.ScoreEnum.INELIGIBLE

    @final_score.setter
    def final_score(self, value):
        raise ValueError('Score cannot be changed in outside of rules!')
