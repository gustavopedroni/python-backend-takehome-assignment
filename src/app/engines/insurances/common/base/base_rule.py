from abc import ABC, abstractmethod
from typing import Optional

from app.data.contants.insurances_line import InsurancesLineKey
from app.data.schemas.personal.information import PersonalInformationSchema


class BaseRule(ABC):

    line_key = None

    def __init__(self, line_key: InsurancesLineKey):
        self.line_key = line_key

    @abstractmethod
    def apply(self, data: PersonalInformationSchema, score: int) -> Optional[int]:
        """
        apply the business rule, changing the score as necessary
        :param data: PersonalInformationSchema
        :param score: current score
        :return: new score value
        """
        return score

    def check(self, data: PersonalInformationSchema, score: Optional[int]) -> Optional[int]:
        """Checks if there is a date and if the score is valid, after applying the current rule
        """

        if not data:
            return score

        if score is None:
            return score

        return self.apply(data=data, score=score)
