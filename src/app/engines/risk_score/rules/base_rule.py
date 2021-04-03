from abc import ABC, abstractmethod

from app.data.schemas.risk_profile import personal_information
from app.data.schemas.risk_score import score


class BaseRiskScoreRule(ABC):

    key: str

    def __init__(self, user_data: personal_information.PersonalInformationSchema):

        self.user_data = user_data
        self._score = 0

    @abstractmethod
    def calculate(self) -> score.ScoreEnum:
        return score.ScoreEnum.ineligible

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        raise ValueError('Score cannot be changed in runtime execution!')
