from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ScoreEnum(str, Enum):
    ECONOMIC = 'economic'
    REGULAR = 'regular'
    RESPONSIBLE = 'responsible'
    INELIGIBLE = 'ineligible'


class RiskFinalScoreSchema(BaseModel):
    auto: ScoreEnum
    disability: ScoreEnum
    home: ScoreEnum
    life: ScoreEnum


class RiskNumberScoreSchema(BaseModel):
    auto: Optional[int] = None
    disability: Optional[int] = None
    home: Optional[int] = None
    life: Optional[int] = None
