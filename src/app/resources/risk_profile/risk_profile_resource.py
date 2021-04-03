from fastapi import APIRouter

from app.data.schemas.risk_profile import personal_information as p_info
from app.data.schemas.risk_score import score
from app.engines.risk_score.risk_score_engine import RiskScoreEngine

router = APIRouter()


@router.post("/", status_code=201, response_model=score.RiskFinalScoreSchema)
async def post(user_data: p_info.PersonalInformationSchema):

    risk_score_engine = RiskScoreEngine(user_data=user_data)
    risk_score = risk_score_engine.calculate()

    return risk_score
