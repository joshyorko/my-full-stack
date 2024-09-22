import uuid
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel, Column, String, DateTime, Interval
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid
from pydantic import EmailStr
from datetime import datetime



# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=40)
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=40)


class UserUpdateMe(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int


# Shared properties
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


# Properties to receive on item creation
class ItemCreate(ItemBase):
    pass


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID


class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)

class Allocation(SQLModel, table=True):
    __tablename__ = 'allocation'

    dcn: str = Field(default=None, primary_key=True)
    status: str | None = Field(default=None, nullable=True)
    hyperlink: str | None = Field(default=None, nullable=True)
    mrdcn: str | None = Field(default=None, nullable=True)
    xray: str | None = Field(default=None, nullable=True)
    xcn: str | None = Field(default=None, nullable=True)
    doc_type: str | None = Field(default=None, nullable=True)
    attach: str | None = Field(default=None, nullable=True)
    electronic_attachments: str | None = Field(default=None, nullable=True)
    pos: str | None = Field(default=None, nullable=True)
    npi: str | None = Field(default=None, nullable=True)
    prov_id: str | None = Field(default=None, nullable=True)
    svc_ofc: str | None = Field(default=None, nullable=True)
    ch_reg_nbr: str | None = Field(default=None, nullable=True)
    clearning_house: str | None = Field(default=None, nullable=True)
    dob: str | None = Field(default=None, nullable=True)
    sex: str | None = Field(default=None, nullable=True)
    tar_noa_from: str | None = Field(default=None, nullable=True)
    tar_noa_thru: str | None = Field(default=None, nullable=True)
    adjud_date: str | None = Field(default=None, nullable=True)
    corr_date: str | None = Field(default=None, nullable=True)
    corr_cd: str | None = Field(default=None, nullable=True)
    submit_amt: float | None = Field(default=None, nullable=True)
    allow_amt: float | None = Field(default=None, nullable=True)
    suspended: bool | None = Field(default=None, nullable=True)
    prev_dcc: str | None = Field(default=None, nullable=True)
    curr_dcc: str | None = Field(default=None, nullable=True)
    dcc_date: str | None = Field(default=None, nullable=True)
    dcc_time: str | None = Field(default=None, nullable=True)
    dcc_reason: str | None = Field(default=None, nullable=True)
    days_in_dcc: int | None = Field(default=None, nullable=True)
    days_in_suspense: int | None = Field(default=None, nullable=True)
    ovrd_1: str | None = Field(default=None, nullable=True)
    opid_1: str | None = Field(default=None, nullable=True)
    ovrd_2: str | None = Field(default=None, nullable=True)
    opid_2: str | None = Field(default=None, nullable=True)
    ovrd_3: str | None = Field(default=None, nullable=True)
    opid_3: str | None = Field(default=None, nullable=True)
    ovrd_4: str | None = Field(default=None, nullable=True)
    opid_4: str | None = Field(default=None, nullable=True)
    ovrd_5: str | None = Field(default=None, nullable=True)
    opid_5: str | None = Field(default=None, nullable=True)
    ovrd_6: str | None = Field(default=None, nullable=True)
    opid_6: str | None = Field(default=None, nullable=True)
    ovrd_7: str | None = Field(default=None, nullable=True)
    opid_7: str | None = Field(default=None, nullable=True)
    err_1: str | None = Field(default=None, nullable=True)
    err_2: str | None = Field(default=None, nullable=True)
    err_3: str | None = Field(default=None, nullable=True)
    err_4: str | None = Field(default=None, nullable=True)
    err_5: str | None = Field(default=None, nullable=True)
    err_6: str | None = Field(default=None, nullable=True)
    err_7: str | None = Field(default=None, nullable=True)
    err_8: str | None = Field(default=None, nullable=True)
    err_9: str | None = Field(default=None, nullable=True)
    err_10: str | None = Field(default=None, nullable=True)
    err_11: str | None = Field(default=None, nullable=True)
    err_12: str | None = Field(default=None, nullable=True)
    err_13: str | None = Field(default=None, nullable=True)
    err_14: str | None = Field(default=None, nullable=True)
    err_15: str | None = Field(default=None, nullable=True)
    err_16: str | None = Field(default=None, nullable=True)
    err_17: str | None = Field(default=None, nullable=True)
    err_18: str | None = Field(default=None, nullable=True)
    err_19: str | None = Field(default=None, nullable=True)
    err_20: str | None = Field(default=None, nullable=True)
    err_21: str | None = Field(default=None, nullable=True)
    err_22: str | None = Field(default=None, nullable=True)
    err_23: str | None = Field(default=None, nullable=True)
    err_24: str | None = Field(default=None, nullable=True)
    err_25: str | None = Field(default=None, nullable=True)
    err_26: str | None = Field(default=None, nullable=True)
    err_27: str | None = Field(default=None, nullable=True)
    err_28: str | None = Field(default=None, nullable=True)
    err_29: str | None = Field(default=None, nullable=True)
    err_30: str | None = Field(default=None, nullable=True)
    err_31: str | None = Field(default=None, nullable=True)
    err_32: str | None = Field(default=None, nullable=True)
    err_33: str | None = Field(default=None, nullable=True)
    err_34: str | None = Field(default=None, nullable=True)
    err_35: str | None = Field(default=None, nullable=True)
    err_36: str | None = Field(default=None, nullable=True)
    err_37: str | None = Field(default=None, nullable=True)
    err_38: str | None = Field(default=None, nullable=True)
    err_39: str | None = Field(default=None, nullable=True)
    err_40: str | None = Field(default=None, nullable=True)
    err_41: str | None = Field(default=None, nullable=True)
    err_42: str | None = Field(default=None, nullable=True)
    err_43: str | None = Field(default=None, nullable=True)
    err_44: str | None = Field(default=None, nullable=True)
    err_45: str | None = Field(default=None, nullable=True)
    err_46: str | None = Field(default=None, nullable=True)
    err_47: str | None = Field(default=None, nullable=True)
    err_48: str | None = Field(default=None, nullable=True)
    err_49: str | None = Field(default=None, nullable=True)
    err_50: str | None = Field(default=None, nullable=True)
    err_51: str | None = Field(default=None, nullable=True)
    err_52: str | None = Field(default=None, nullable=True)
    err_53: str | None = Field(default=None, nullable=True)
    err_54: str | None = Field(default=None, nullable=True)
    err_55: str | None = Field(default=None, nullable=True)
    err_56: str | None = Field(default=None, nullable=True)
    err_57: str | None = Field(default=None, nullable=True)
    err_58: str | None = Field(default=None, nullable=True)
    err_59: str | None = Field(default=None, nullable=True)
    err_60: str | None = Field(default=None, nullable=True)
    err_61: str | None = Field(default=None, nullable=True)
    err_62: str | None = Field(default=None, nullable=True)
    err_63: str | None = Field(default=None, nullable=True)
    err_64: str | None = Field(default=None, nullable=True)
    err_65: str | None = Field(default=None, nullable=True)
    already_processed: bool | None = Field(default=None, nullable=True)
    aging_bucket: str | None = Field(default=None, nullable=True)
    julian_date: str | None = Field(default=None, nullable=True)
    docutype: str | None = Field(default=None, nullable=True)
    combo: str | None = Field(default=None, nullable=True)
    date: str | None = Field(default=None, nullable=True)
    procedure_codes: str | None = Field(default=None, nullable=True)
    dates_of_service: str | None = Field(default=None, nullable=True)
    error_codes: str | None = Field(default=None, nullable=True)
    field_error_codes: str | None = Field(default=None, nullable=True)
    white_glove: bool | None = Field(default=None, nullable=True)
    assigned_to: str | None = Field(default=None, nullable=True)
    start_time: str | None = Field(default=None, nullable=True)
    end_time: str | None = Field(default=None, nullable=True)
    time_worked: str | None = Field(default=None, nullable=True)