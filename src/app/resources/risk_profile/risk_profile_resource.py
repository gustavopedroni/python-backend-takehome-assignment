from fastapi import APIRouter

from .schemas import response_schema, request_schema

router = APIRouter()


@router.post("/", status_code=201, response_model=response_schema.RiskProfileResponseSchema)
async def post(body: request_schema.RiskProfileRequestSchema):

    fake_response = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "economic",
        "life": "regular"
    }

    return fake_response
