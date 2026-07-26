from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.base import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)

    phone_number = Column(String)

    language = Column(String)

    property_type = Column(String)

    bhk = Column(String)

    budget = Column(Integer)

    package = Column(String)

    status = Column(String)