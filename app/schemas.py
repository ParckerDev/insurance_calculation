from pydantic import BaseModel
from typing import Optional

class RateCreate(BaseModel):
    carco_type: str
    rate: float


class RateUpload(BaseModel):
    rates: dict[str, list[RateCreate]]


class RateResponse(BaseModel):
    cargo_type: str
    rate: float