from sqlalchemy.orm import Session

from app.conversation.conversation_manager import ConversationManager
from app.services.lead_service import create_lead_from_session


class ConversationService:

    def __init__(self):

        self.manager = ConversationManager()

    def process(self, db: Session, session_id: str, message: str):

        response = self.manager.process_message(session_id, message)

        session = self.manager.get_session(session_id)

        if session.state == "PACKAGE":

            create_lead_from_session(db, session)

        return response