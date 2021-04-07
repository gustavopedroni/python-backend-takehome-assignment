from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.views.risk_profile import risk_profile_view

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    risk_profile_view.router, prefix="/v1/risk_profile", tags=["Risk Profile"]
)
