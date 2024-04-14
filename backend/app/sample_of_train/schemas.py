
from pydantic import BaseModel

TIMEZONE = 'Europe/Moscow'

class GetSampleOfTrain(BaseModel):
    slctn_nmbr: int   # 1
    client_id: str    # 0xA095932790098744A2325A8D152C05C7,
    npo_account_id: str  # 0xD4DBBAC6561929409BA45725A220613E,
    npo_accnts_nmbr: int  # 1,
    pmnts_type: int  # 2,
    year: int # 2017,
    quarter: str # 2017Q4,
    gender: int # 1,
    age: int # 48,
    clnt_cprtn_time_d: int # 8091,
    actv_prd_d: int  # 0,
    lst_pmnt_rcnc_d: int # 6757,
    balance: float # 679.37,
    oprtn_sum_per_qrtr: float # 31.34,
    oprtn_sum_per_year: float # 31.34,
    frst_pmnt_date: str # 1999-07-02,
    lst_pmnt_date_per_qrtr: str | None # ,
    frst_pmnt: float # 96.25,
    lst_pmnt: float # 0.09,
    pmnts_sum: float # 96.25,
    pmnts_nmbr: int # 1,
    pmnts_sum_per_qrtr:  float # -0.0,
    pmnts_sum_per_year:  float # -0.0,
    pmnts_nmbr_per_qrtr: int  # 0,
    pmnts_nmbr_per_year: int # 0,
    incm_sum: float # 583.12,
    incm_per_qrtr: float # 31.34,
    incm_per_year: float # 31.34,
    mgd_accum_period: float # 1.8,
    mgd_payment_period: float # 1.8,
    phone_number: int # 0,
    email: str | int # 0,
    lk: int # -1,
    assignee_npo: int # -1,
    assignee_ops: int # -1,
    postal_code: str # 446254.0,
    region: str # САМАРСКАЯ ОБЛ,
    citizen: int # -1,
    fact_addrss: int # -1,
    appl_mrkr: int # 0,
    evry_qrtr_pmnt: float # 0,0
    churn: int # 0

    class Config:
        populate_by_name = True