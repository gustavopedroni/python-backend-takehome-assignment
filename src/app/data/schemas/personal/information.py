from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from app.data.schemas.personal.house import HouseSchema
from app.data.schemas.personal.vehicle import VehicleSchema


class PersonalInformationSchema(BaseModel):

    age: int = Field(..., ge=0)
    dependents: int = Field(..., ge=0)
    house: Optional[HouseSchema] = None
    income: int = Field(..., ge=0)
    marital_status: Literal["single", "married"]
    risk_questions: List[bool] = Field(..., min_items=3, max_items=3)
    vehicle: Optional[VehicleSchema] = None
