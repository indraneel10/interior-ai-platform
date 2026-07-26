from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from datetime import datetime

from app.database.base import Base


class ConversationHistory(Base):

    __tablename__ = "conversation_history"

    id = Column(Integer, primary_key=True)

    session_id = Column(Integer)

    speaker = Column(String(20))

    message = Column(String(2000))

    created_at = Column(DateTime, default=datetime.utcnow)
