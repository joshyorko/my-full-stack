# backend/app/crud/crud_allocation.py

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.crud.base import CRUDBase
from app.models.allocation import Allocation
from app.schemas.allocation import AllocationCreate, AllocationUpdate

class CRUDAllocation(CRUDBase[Allocation, AllocationCreate, AllocationUpdate]):
    def get_user_work(self, db: Session, email: str):
        assigned_to = ' '.join([name.title() for name in email.split('@')[0].split('.')])
        return db.query(Allocation).filter(
            ((Allocation.electronic_attachments != None) & (func.trim(Allocation.electronic_attachments) != '')) |
            ((Allocation.clearning_house != None) & (func.trim(Allocation.clearning_house) != ''))
        ).filter(
            Allocation.assigned_to == assigned_to,
            (Allocation.status.notin_(['Completed', 'Skipped']) | (Allocation.status == None))
        ).first()

    def update_status(self, db: Session, dcn: str, status_value: str):
        allocation = db.query(Allocation).filter(Allocation.dcn == dcn).first()
        if allocation:
            allocation.status = status_value
            allocation.end_time = func.now()
            allocation.time_worked = allocation.end_time - allocation.start_time
            db.commit()
            db.refresh(allocation)
        return allocation

    def get_count_user_work(self, db: Session, email: str):
        assigned_to = ' '.join([name.title() for name in email.split('@')[0].split('.')])
        queue_count = db.query(func.count(Allocation.dcn)).filter(
            Allocation.assigned_to == assigned_to,
            (Allocation.status.notin_(['Completed', 'Skipped']) | (Allocation.status == None))
        ).scalar()
        completed_count = db.query(func.count(Allocation.dcn)).filter(
            Allocation.assigned_to == assigned_to,
            Allocation.status == 'Completed'
        ).scalar()
        skipped_count = db.query(func.count(Allocation.dcn)).filter(
            Allocation.assigned_to == assigned_to,
            Allocation.status == 'Skipped'
        ).scalar()
        return {
            "queue": queue_count,
            "completed": completed_count,
            "skipped": skipped_count
        }

allocation = CRUDAllocation(Allocation)