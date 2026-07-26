from sqlalchemy import (
    Column,
    Integer,
    String,
)

from app.database.base import Base


class AgentConfiguration(Base):

    __tablename__ = "agent_configuration"

    id = Column(Integer, primary_key=True)

    greeting = Column(String(500))

    transfer_number = Column(String(20))

    language = Column(String(20))

    active = Column(String(10))
