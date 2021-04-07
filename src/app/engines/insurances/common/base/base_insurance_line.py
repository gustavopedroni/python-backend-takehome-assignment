from abc import ABC, abstractmethod
from typing import Optional

from app.data.contants.insurances_line import InsurancesLineKey
from app.data.schemas.personal.information import PersonalInformationSchema


class BaseInsuranceLine(ABC):

    key: InsurancesLineKey

    def __init__(
        self,
        user_data: PersonalInformationSchema,
        key: Optional[InsurancesLineKey] = None,
    ):
        self.user_data = user_data
        self.key = key if key else self.key

    @abstractmethod
    def calculate(self):
        pass
