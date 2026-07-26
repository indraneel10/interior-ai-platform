from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.lead import LeadCreate
from app.services.lead_service import (
    create_lead,
    get_all_leads,
    get_lead,
)

router = APIRouter(
    prefix="/lead",
    tags=["Lead"]
)


@router.post("/")
def create_new_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):
    return create_lead(db, lead)


@router.get("/")
def read_all_leads(
    db: Session = Depends(get_db)
):
    return get_all_leads(db)


@router.get("/{lead_id}")
def read_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):
    return get_lead(db, lead_id)