import csv
from typing import List

from fastapi import APIRouter

from app.acc_churn_t1.schemas import GetAccChurnT1
from app.exception_handler import error_handler
from app.path import get_path


router = APIRouter()
FILE = "acc_churn_t1.csv"

@router.get("/acc_churn_t1", summary="Get acc_churn_t1",
            response_model=List[GetAccChurnT1], tags=["acc_churn_t1"])
@error_handler
async def acc_churn_t1() -> List[GetAccChurnT1]:
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
            d[first[5]] = line[5]
            d[first[6]] = line[6]
            d[first[7]] = line[7]
            d[first[8]] = line[8]
            d[first[9]] = line[9]
            d[first[10]] = line[10]
            d[first[11]] = line[11]
            d[first[12]] = line[12]
            data.append(d)
    return [GetAccChurnT1.model_validate(ix) for ix in data]



