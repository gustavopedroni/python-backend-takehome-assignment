from fastapi import APIRouter

from app.data.schemas.personal.information import PersonalInformationSchema
from app.data.schemas.score import FinalRiskScoreSchema
from app.engines.insurances.insurances_engine import InsurancesEngine

router = APIRouter()


@router.post("/", status_code=201, response_model=FinalRiskScoreSchema)
async def post(user_data: PersonalInformationSchema):

    insurances_engine = InsurancesEngine()
    final_score, _ = insurances_engine.calculate(user_data=user_data)

    return final_score
