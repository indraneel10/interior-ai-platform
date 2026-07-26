from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from datetime import datetime

from app.database.base import Base


class ConversationSession(Base):

    __tablename__ = "conversation_sessions"

    id = Column(Integer, primary_key=True)

    call_sid = Column(String(200), unique=True)

    customer_phone = Column(String(20))

    current_step = Column(String(100))

    language = Column(String(20))

    started_at = Column(DateTime, default=datetime.utcnow)

    ended_at = Column(DateTime)
