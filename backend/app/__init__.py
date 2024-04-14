from fastapi import APIRouter

from app.acc_churn_t1 import routes as acc_churn_t1
from app.agg_churn_by_years import routes as agg_churn_by_years
from app.churn_region_qrt import routes as churn_region_qrt
from app.loss_region_qrt import routes as loss_region_qrt
from app.sample_of_train import routes as sample_of_train
from app.train import routes as train

router = APIRouter()

router.include_router(acc_churn_t1.router)
router.include_router(agg_churn_by_years.router)
router.include_router(churn_region_qrt.router)
router.include_router(loss_region_qrt.router)
router.include_router(sample_of_train.router)
router.include_router(train.router)
