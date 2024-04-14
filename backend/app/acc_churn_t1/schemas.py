from pydantic import BaseModel



class GetAccChurnT1(BaseModel):
    client_id: str    # 0xA095932790098744A2325A8D152C05C7,
    npo_account_id: str  # 0xD4DBBAC6561929409BA45725A220613E,
    churn_prop: float
    gender: str
    age: int  # 48,
    region: str  # САМАРСКАЯ ОБЛ,
    npo_accnts_nmbr: int  # 1,
    pmnts_type: str
    balance: float  # 679.37,
    lst_pmnt_date_per_qrtr: str | None  # ,
    phone_number: str
    email: str | int  # 0,
    lk: str

    class Config:
        populate_by_name = True