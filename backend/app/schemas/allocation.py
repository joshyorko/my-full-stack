# backend/app/schemas/allocation.py

from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

class AllocationBase(BaseModel):
    dcn: str
    status: Optional[str] = None
    hyperlink: Optional[str] = None
    mrdcn: Optional[str] = None
    xray: Optional[str] = None
    xcn: Optional[str] = None
    doc_type: Optional[str] = None
    attach: Optional[str] = None
    electronic_attachments: Optional[str] = None
    pos: Optional[str] = None
    npi: Optional[str] = None
    prov_id: Optional[str] = None
    svc_ofc: Optional[str] = None
    ch_reg_nbr: Optional[str] = None
    clearning_house: Optional[str] = None
    dob: Optional[str] = None
    sex: Optional[str] = None
    tar_noa_from: Optional[str] = None
    tar_noa_thru: Optional[str] = None
    adjud_date: Optional[str] = None
    corr_date: Optional[str] = None
    corr_cd: Optional[str] = None
    submit_amt: Optional[str] = None
    allow_amt: Optional[str] = None
    suspended: Optional[str] = None
    prev_dcc: Optional[str] = None
    curr_dcc: Optional[str] = None
    dcc_date: Optional[str] = None
    dcc_time: Optional[str] = None
    dcc_reason: Optional[str] = None
    days_in_dcc: Optional[str] = None
    days_in_suspense: Optional[str] = None
    ovrd_1: Optional[str] = None
    opid_1: Optional[str] = None
    ovrd_2: Optional[str] = None
    opid_2: Optional[str] = None
    ovrd_3: Optional[str] = None
    opid_3: Optional[str] = None
    ovrd_4: Optional[str] = None
    opid_4: Optional[str] = None
    ovrd_5: Optional[str] = None
    opid_5: Optional[str] = None
    ovrd_6: Optional[str] = None
    opid_6: Optional[str] = None
    ovrd_7: Optional[str] = None
    opid_7: Optional[str] = None
    err_1: Optional[str] = None
    err_2: Optional[str] = None
    err_3: Optional[str] = None
    err_4: Optional[str] = None
    err_5: Optional[str] = None
    err_6: Optional[str] = None
    err_7: Optional[str] = None
    err_8: Optional[str] = None
    err_9: Optional[str] = None
    err_10: Optional[str] = None
    err_11: Optional[str] = None
    err_12: Optional[str] = None
    err_13: Optional[str] = None
    err_14: Optional[str] = None
    err_15: Optional[str] = None
    err_16: Optional[str] = None
    err_17: Optional[str] = None
    err_18: Optional[str] = None
    err_19: Optional[str] = None
    err_20: Optional[str] = None
    err_21: Optional[str] = None
    err_22: Optional[str] = None
    err_23: Optional[str] = None
    err_24: Optional[str] = None
    err_25: Optional[str] = None
    err_26: Optional[str] = None
    err_27: Optional[str] = None
    err_28: Optional[str] = None
    err_29: Optional[str] = None
    err_30: Optional[str] = None
    err_31: Optional[str] = None
    err_32: Optional[str] = None
    err_33: Optional[str] = None
    err_34: Optional[str] = None
    err_35: Optional[str] = None
    err_36: Optional[str] = None
    err_37: Optional[str] = None
    err_38: Optional[str] = None
    err_39: Optional[str] = None
    err_40: Optional[str] = None
    err_41: Optional[str] = None
    err_42: Optional[str] = None
    err_43: Optional[str] = None
    err_44: Optional[str] = None
    err_45: Optional[str] = None
    err_46: Optional[str] = None
    err_47: Optional[str] = None
    err_48: Optional[str] = None
    err_49: Optional[str] = None
    err_50: Optional[str] = None
    err_51: Optional[str] = None
    err_52: Optional[str] = None
    err_53: Optional[str] = None
    err_54: Optional[str] = None
    err_55: Optional[str] = None
    err_56: Optional[str] = None
    err_57: Optional[str] = None
    err_58: Optional[str] = None
    err_59: Optional[str] = None
    err_60: Optional[str] = None
    err_61: Optional[str] = None
    err_62: Optional[str] = None
    err_63: Optional[str] = None
    err_64: Optional[str] = None
    err_65: Optional[str] = None
    already_processed: Optional[str] = None
    aging_bucket: Optional[str] = None
    julian_date: Optional[str] = None
    docutype: Optional[str] = None
    combo: Optional[str] = None
    date: Optional[str] = None
    procedure_codes: Optional[str] = None
    dates_of_service: Optional[str] = None
    error_codes: Optional[str] = None
    field_error_codes: Optional[str] = None
    white_glove: Optional[str] = None
    assigned_to: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    time_worked: Optional[timedelta] = None

    class Config:
        from_attributes = True

class AllocationCreate(AllocationBase):
    pass

class AllocationUpdate(AllocationBase):
    pass

class AllocationInDBBase(AllocationBase):
    class Config:
        orm_mode = True

class Allocation(AllocationInDBBase):
    pass

class AllocationInDB(AllocationInDBBase):
    pass