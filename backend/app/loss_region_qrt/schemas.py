from pydantic import BaseModel


class GetLossRegionQrt(BaseModel):
    id: int
    region: str
    year: int
    quarter: str
    balance: float
    lst_pmnt: float

    class Config:
        populate_by_name = True