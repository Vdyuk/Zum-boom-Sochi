from pydantic import BaseModel


class GetChurnRegionQrt(BaseModel):
    region: str
    year: int
    quarter: str
    churn: float
    qrtr_numb: int

    class Config:
        populate_by_name = True