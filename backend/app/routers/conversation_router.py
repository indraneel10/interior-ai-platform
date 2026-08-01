from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.conversation_service import ConversationService

router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"]
)

service = ConversationService()


class ConversationRequest(BaseModel):

    session_id: str

    message: str


@router.post("/")
def process_message(
    request: ConversationRequest,
    db: Session = Depends(get_db)
):

    return {
        "response": service.process(
            db,
            request.session_id,
            request.message
        )
    }