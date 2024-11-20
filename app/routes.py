from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated
from sqlalchemy import insert, update, select, delete
from sqlalchemy.orm import Session
from schemas import RateUpload
from models import Rate
from database import get_db
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/rates", tags=["rates"])


@router.get("")
async def get_all_rates(db: Annotated[AsyncSession, Depends(get_db)]):
    rates = db.scalars(select(Rate)).all()
    return rates


@router.post("/upload")
async def upload_rates(db: Annotated[AsyncSession, Depends()], rate_upload: RateUpload):
    for date_str, rates in rate_upload.rates.items():
        for rate in rates:
            await db.execute(
                insert(Rate).values(
                    cargo_type=rate.cargo_type,
                    rate=rate.rate,
                    effective_date=datetime.strptime(date_str, "%Y-%m-%d").date(),
                )
            )
            await db.commit()
    return {"message": "Rate upload successfull"}
