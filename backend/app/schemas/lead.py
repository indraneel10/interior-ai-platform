from pydantic import BaseModel


class LeadCreate(BaseModel):
    customer_name: str
    phone_number: str
    language: str
    property_type: str
    bhk: str | None = None
    rooms: int | None = None
    budget: int
    package: str


class LeadResponse(LeadCreate):
    id: int
    status: str

    class Config:
        from_attributes = True