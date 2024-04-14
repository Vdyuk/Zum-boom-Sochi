from pydantic import BaseModel

TIMEZONE = 'Europe/Moscow'

class GetAggChurnByYears(BaseModel):
    year: int
    quarter_number: int
    region: str
    churn: float

    class Config:
        populate_by_name = True