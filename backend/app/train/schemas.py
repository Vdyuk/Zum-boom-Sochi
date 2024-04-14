from typing import Optional

from pydantic import BaseModel


class TrainSchema(BaseModel):
    slctn_nmbr: Optional[int] = None   # 1
    client_id: Optional[str] = None    # 0xA095932790098744A2325A8D152C05C7,
    npo_account_id: Optional[str] = None  # 0xD4DBBAC6561929409BA45725A220613E,
    npo_accnts_nmbr: Optional[int] = None  # 1,
    pmnts_type: Optional[int] = None  # 2,
    year: Optional[int] = None # 2017,
    quarter: Optional[str] = None # 2017Q4,
    gender: Optional[int] = None # 1,
    age: Optional[int] = None # 48,
    clnt_cprtn_time_d: Optional[int] = None # 8091,
    actv_prd_d: Optional[int] = None  # 0,
    lst_pmnt_rcnc_d: Optional[int] = None # 6757,
    balance: Optional[float] = None # 679.37,
    oprtn_sum_per_qrtr: Optional[float] = None # 31.34,
    oprtn_sum_per_year: Optional[float] = None # 31.34,
    frst_pmnt_date: Optional[str] = None # 1999-07-02,
    lst_pmnt_date_per_qrtr: Optional[str] = None # ,
    frst_pmnt: Optional[float] = None # 96.25,
    lst_pmnt: Optional[float] = None # 0.09,
    pmnts_sum: Optional[float] = None # 96.25,
    pmnts_nmbr: Optional[int] = None # 1,
    pmnts_sum_per_qrtr:  Optional[float] = None # -0.0,
    pmnts_sum_per_year:  Optional[float] = None # -0.0,
    pmnts_nmbr_per_qrtr: Optional[int] = None  # 0,
    pmnts_nmbr_per_year: Optional[int] = None # 0,
    incm_sum: Optional[float] = None # 583.12,
    incm_per_qrtr: Optional[float] = None # 31.34,
    incm_per_year: Optional[float] = None # 31.34,
    mgd_accum_period: Optional[float] = None # 1.8,
    mgd_payment_period: Optional[float] = None # 1.8,
    phone_number: Optional[int] = None # 0,
    email: Optional[str] = None # 0,
    lk: Optional[int] = None # -1,
    assignee_npo: Optional[int] = None # -1,
    assignee_ops: Optional[int] = None # -1,
    postal_code: Optional[str] = None # 446254.0,
    region: Optional[str] = None # САМАРСКАЯ ОБЛ,
    citizen: Optional[int] = None # -1,
    fact_addrss: Optional[int] = None # -1,
    appl_mrkr: Optional[int] = None # 0,
    evry_qrtr_pmnt: Optional[float] = None # 0,0
    churn: Optional[int] = None # 0
