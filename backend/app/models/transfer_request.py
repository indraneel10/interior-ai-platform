from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.base import Base


class TransferRequest(Base):

    __tablename__ = "transfer_requests"

    id = Column(Integer, primary_key=True)

    customer_phone = Column(String(20))

    transfer_to = Column(String(20))

    reason = Column(String(200))

    status = Column(String(50), default="PENDING")

    created_at = Column(DateTime, default=datetime.utcnow)
