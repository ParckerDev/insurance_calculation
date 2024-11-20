from datetime import datetime


""" @router.get("calculate/")
async def calculate_insurance(
    db: Annotated[AsyncSession, Depends(get_db)],
    cargo_type: str,
    declared_value: float,
    date: str,
):
    query = select(models.Rate).where(
        models.Rate.cargo_type == cargo_type,
        models.Rate.effective_date <= datetime.strptime(date, "%Y-%m-%d").date(),
    )
    rate = await database.fetch_one(query)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    return {"insurance_cost": declared_value * rate.rate} """


date = '2024-02-11'
f = datetime.strptime(date, "%Y-%m-%d").date()
print(f)
print(str(datetime.now().date()))