from typing import Optional

from pydantic import BaseModel

from app.data.contants.final_score import FinalScoreEnum


class FinalRiskScoreSchema(BaseModel):
    auto: FinalScoreEnum
    disability: FinalScoreEnum
    home: FinalScoreEnum
    life: FinalScoreEnum


class NumberRiskScoreSchema(BaseModel):
    auto: Optional[int] = None
    disability: Optional[int] = None
    home: Optional[int] = None
    life: Optional[int] = None
