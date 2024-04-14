from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from app.db.session import get_db
from app.exception_handler import error_handler
from app.train.models import TrainModel
from app.train.schemas import TrainSchema

router = APIRouter()
FILE = "train.csv"


@router.get("/client_by_id", summary="Get client_by_id",
            response_model=TrainSchema, tags=["train"])
@error_handler
async def get_client_by_id(client_id: str, db: AsyncSession = Depends(get_db)) -> TrainSchema:
    async with db as session, session.begin():
        res_client_by_id = await session.execute(select(TrainModel.slctn_nmbr, TrainModel.client_id, TrainModel.npo_account_id,    TrainModel.npo_accnts_nmbr,    TrainModel.pmnts_type,    TrainModel.year,    TrainModel.quarter,    TrainModel.gender,    TrainModel.age,    TrainModel.clnt_cprtn_time_d,    TrainModel.actv_prd_d,    TrainModel.lst_pmnt_rcnc_d,    TrainModel.balance,    TrainModel.oprtn_sum_per_qrtr,    TrainModel.oprtn_sum_per_year,    TrainModel.frst_pmnt_date,    TrainModel.lst_pmnt_date_per_qrtr,    TrainModel.frst_pmnt,    TrainModel.lst_pmnt,    TrainModel.pmnts_sum,    TrainModel.pmnts_nmbr, TrainModel.pmnts_sum_per_qrtr,    TrainModel.pmnts_sum_per_year,    TrainModel.pmnts_nmbr_per_qrtr,    TrainModel.pmnts_nmbr_per_year,    TrainModel.incm_sum,    TrainModel.incm_per_qrtr,    TrainModel.incm_per_year,    TrainModel.mgd_accum_period,    TrainModel.mgd_payment_period,    TrainModel.phone_number,    TrainModel.email,    TrainModel.lk,    TrainModel.assignee_npo,    TrainModel.assignee_ops,    TrainModel.postal_code,    TrainModel.region,    TrainModel.citizen,    TrainModel.fact_addrss,    TrainModel.appl_mrkr,    TrainModel.evry_qrtr_pmnt,    TrainModel.churn).where(TrainModel.client_id==client_id))
        client_by_id = res_client_by_id.mappings().all()
        if not client_by_id:
            raise HTTPException(status_code=422, detail=f'Введите корректные данные, {client_id} нет в таблице train')
        return TrainSchema.model_validate(client_by_id[0])




