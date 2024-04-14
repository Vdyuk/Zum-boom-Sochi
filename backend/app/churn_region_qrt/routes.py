import csv
from typing import List

from fastapi import APIRouter

from app.churn_region_qrt.schemas import GetChurnRegionQrt
from app.exception_handler import error_handler
from app.path import get_path


router = APIRouter()
FILE = "churn_region_qrt.csv"

@router.get("/churn_region_qrt", summary="Get churn_region_qrt",
            response_model=List[GetChurnRegionQrt], tags=["churn_region_qrt"])
@error_handler
async def churn_region_qrt() -> List[GetChurnRegionQrt]:
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
            d[first[4]] = line[4]
            data.append(d)
    return [GetChurnRegionQrt.model_validate(ix) for ix in data]



