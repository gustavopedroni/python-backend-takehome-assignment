from typing import Literal

from pydantic import BaseModel, Field


class HouseSchema(BaseModel):

    ownership_status: Literal['owned', 'mortgaged'] = Field(..., description="Status can be 'owned' or 'mortgaged'")
