import csv
from typing import List

from fastapi import APIRouter

from app.exception_handler import error_handler
from app.path import get_path
from app.sample_of_train.schemas import GetSampleOfTrain


router = APIRouter()
FILE = "sample_of_train.csv"

@router.get("/sample_of_train", summary="Get sample_of_train",
            response_model=List[GetSampleOfTrain], tags=["sample_of_train"])
@error_handler
async def sample_of_train() -> List[GetSampleOfTrain]:
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
            d[first[13]] = line[13]
            d[first[14]] = line[14]
            d[first[15]] = line[15]
            d[first[16]] = line[16]
            d[first[17]] = line[17]
            d[first[18]] = line[18]
            d[first[19]] = line[19]
            d[first[20]] = line[20]
            d[first[21]] = line[21]
            d[first[22]] = line[22]
            d[first[23]] = line[23]
            d[first[24]] = line[24]
            d[first[25]] = line[25]
            d[first[26]] = line[26]
            d[first[27]] = line[27]
            d[first[28]] = line[28]
            d[first[29]] = line[29]
            d[first[30]] = line[30]
            d[first[31]] = line[31]
            d[first[32]] = line[32]
            d[first[33]] = line[33]
            d[first[34]] = line[34]
            d[first[35]] = line[35]
            d[first[36]] = line[36]
            d[first[37]] = line[37]
            d[first[38]] = line[38]
            d[first[39]] = line[39]
            d[first[40]] = line[40]
            d[first[41]] = line[41]
            data.append(d)
    return [GetSampleOfTrain.model_validate(ix) for ix in data]



