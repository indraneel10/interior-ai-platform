from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.schemas.lead import LeadCreate


def create_lead(db: Session, lead: LeadCreate):

    db_lead = Lead(
        customer_name=lead.customer_name,
        phone_number=lead.phone_number,
        language=lead.language,
        property_type=lead.property_type,
        bhk=lead.bhk,
        rooms=lead.rooms,
        budget=lead.budget,
        package=lead.package,
    )

    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    return db_lead


def get_all_leads(db: Session):
    return db.query(Lead).all()


def get_lead(db: Session, lead_id: int):
    return db.query(Lead).filter(Lead.id == lead_id).first()