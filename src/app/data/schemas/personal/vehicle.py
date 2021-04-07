from pydantic import BaseModel, Field
from pydantic.types import PositiveInt


class VehicleSchema(BaseModel):

    year: PositiveInt = Field(..., description="Year it was manufactured")
