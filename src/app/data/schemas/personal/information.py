from typing import Literal, Optional

from pydantic import BaseModel, Field

from .house import HouseSchema
from .risk_questions import RiskQuestionsSchema
from .vehicle import VehicleSchema


class PersonalInformationSchema(BaseModel):

    age: int = Field(..., ge=0)
    dependents: int = Field(..., ge=0)
    house: Optional[HouseSchema] = None
    income: int = Field(..., ge=0)
    marital_status: Literal["single", "married"]
    risk_questions: RiskQuestionsSchema
    vehicle: Optional[VehicleSchema] = None
