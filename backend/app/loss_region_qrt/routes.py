import csv
from typing import List

from fastapi import APIRouter

from app.exception_handler import error_handler
from app.loss_region_qrt.schemas import GetLossRegionQrt
from app.path import get_path


router = APIRouter()
FILE = "loss_region_qrt.csv"

@router.get("/loss_region_qrt", summary="Get loss_region_qrt",
            response_model=List[GetLossRegionQrt], tags=["loss_region_qrt"])
@error_handler
async def agg_loss_region_qrt() -> List[GetLossRegionQrt]:
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
            data.append(d)
    return [GetLossRegionQrt.model_validate(ix) for ix in data]



