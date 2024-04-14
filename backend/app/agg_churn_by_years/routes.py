import csv
from typing import List

from fastapi import APIRouter

from app.exception_handler import error_handler
from app.path import get_path
from app.agg_churn_by_years.schemas import GetAggChurnByYears


router = APIRouter()
FILE = "agg_churn_by_years.csv"

@router.get("/agg_churn_by_years", summary="Get agg_churn_by_years",
            response_model=List[GetAggChurnByYears], tags=["agg_churn_by_years"])
@error_handler
async def agg_churn_by_years() -> List[GetAggChurnByYears]:
    data = []
    path = get_path(FILE)

    with open(path, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        first = next(reader)
        for line in reader:
            d = {}
            d[first[0]] = line[0]
            d[first[1]] = line[1]
            d[first[2]] = line[2]
            d[first[3]] = line[3]
            data.append(d)
    return [GetAggChurnByYears.model_validate(ix) for ix in data]



