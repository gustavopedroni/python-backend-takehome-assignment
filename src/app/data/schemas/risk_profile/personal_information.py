from typing import Optional, Literal

from pydantic import BaseModel, Field, conlist

from .house import HouseSchema
from .vehicle import VehicleSchema


class PersonalInformationSchema(BaseModel):

    age: int = Field(..., ge=0)
    dependents: int = Field(..., ge=0)
    house: Optional[HouseSchema] = None
    income: int = Field(..., ge=0)
    marital_status: Literal['single', 'married']
    risk_questions: conlist(bool, min_items=3, max_items=3)
    vehicle: Optional[VehicleSchema] = None
