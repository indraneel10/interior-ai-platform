from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from datetime import datetime

from app.database.base import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100))

    phone_number = Column(String(20), unique=True)

    language = Column(String(20))

    property_type = Column(String(20))

    bhk = Column(String(20))

    rooms = Column(Integer)

    budget = Column(Integer)

    package = Column(String(20))

    status = Column(String(30), default="NEW")

    created_at = Column(DateTime, default=datetime.utcnow)
