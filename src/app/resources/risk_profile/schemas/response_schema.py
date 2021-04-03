from enum import Enum
from pydantic import BaseModel


class ScoreEnum(Enum):
    economic = 'economic'
    regular = 'regular'
    responsible = 'responsible'
    ineligible = 'ineligible'


class RiskProfileResponseSchema(BaseModel):

    auto: ScoreEnum
    disability: ScoreEnum
    home: ScoreEnum
    life: ScoreEnum
