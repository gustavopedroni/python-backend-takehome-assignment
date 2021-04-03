from enum import Enum

from pydantic import BaseModel


class ScoreEnum(str, Enum):
    economic = 'economic'
    regular = 'regular'
    responsible = 'responsible'
    ineligible = 'ineligible'


class RiskFinalScoreSchema(BaseModel):
    auto: ScoreEnum
    disability: ScoreEnum
    home: ScoreEnum
    life: ScoreEnum


class RiskNumberScoreSchema(BaseModel):
    auto: int
    disability: int
    home: int
    life: int
