# backend/app/api/routes/allocation.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any
from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
import requests

router = APIRouter()

@router.get("/get_attachment/")
def get_attachment(
    dcn: str, 
    provider: str = "all", 
    current_user: models.User = Depends(deps.get_current_active_user)
):
    if not dcn:
        raise HTTPException(status_code=400, detail="No electronic attachment provided")
    try:
        response = requests.get(f"{settings.ATTACHMENT_SERVICE_URL}/prod/all/{dcn}?provider={provider}")
        return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=404, detail="Unable to get attachment information")

@router.get("/get_work/", response_model=schemas.Allocation)
def get_work(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    work = crud.allocation.get_user_work(db, email=current_user.email)
    if not work:
        raise HTTPException(status_code=404, detail="No work available")
    return work

@router.patch("/update_status/", response_model=schemas.Allocation)
def update_status(
    dcn: str,
    status: str,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    if not dcn or not status:
        raise HTTPException(status_code=400, detail="DCN and status are required")
    updated_allocation = crud.allocation.update_status(db, dcn=dcn, status_value=status)
    if not updated_allocation:
        raise HTTPException(status_code=404, detail="Allocation not found")
    return updated_allocation

@router.get("/get_work_count/", response_model=dict)
def get_work_count(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
):
    return crud.allocation.get_count_user_work(db, email=current_user.email)

@router.get("/maui_api/")
def get_access_token(
    current_user: models.User = Depends(deps.get_current_active_user)
):
    return {"access_token": settings.MAUI_API_KEY}