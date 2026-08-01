from app.conversation.prompts import PROMPTS
from app.conversation.package_selector import determine_package
from app.conversation.session import ConversationSession


class ConversationManager:

    def __init__(self):

        self.sessions = {}

    def create_session(self, session_id):

        session = ConversationSession(session_id=session_id)

        self.sessions[session_id] = session

        return session

    def get_session(self, session_id):

        if session_id not in self.sessions:

            return self.create_session(session_id)

        return self.sessions[session_id]

    def process_message(self, session_id, message):

        session = self.get_session(session_id)

        # Welcome
        if session.state == "WELCOME":

            session.state = "LANGUAGE"

            return PROMPTS["WELCOME"]["English"]

        # Language Selection
        if session.state == "LANGUAGE":

            message = message.lower().strip()

            if message == "english":

                session.language = "English"

            elif message == "hindi":

                session.language = "Hindi"

            else:

                return "Please say English or Hindi."

            session.state = "PROPERTY"

            return PROMPTS["PROPERTY"][session.language]

        # Property Selection
        if session.state == "PROPERTY":

            message = message.lower().strip()

            if message == "flat":

                session.property_type = "Flat"

                session.state = "BHK"

                return PROMPTS["BHK"][session.language]

            elif message == "bungalow":

                session.property_type = "Bungalow"

                session.state = "ROOMS"

                return PROMPTS["ROOMS"][session.language]

            else:

                return "Please say Flat or Bungalow."

        # BHK Selection
        if session.state == "BHK":

            session.bhk = message

            session.state = "BUDGET"

            return PROMPTS["BUDGET"][session.language]

        # Room Selection
        if session.state == "ROOMS":

            try:

                session.rooms = int(message)

            except ValueError:

                return "Please tell the number of rooms."

            session.state = "BUDGET"

            return PROMPTS["BUDGET"][session.language]

        # Budget
        
        if session.state == "BUDGET":

            try:

                session.budget = float(message)

            except ValueError:

                return "Please tell your budget in lakhs."

            session.package = determine_package(session.budget)

            session.state = "PACKAGE"

            if session.package == "Luxury Package":

                return (
                    "You are eligible for the Luxury Package. "
                    "I'll connect you with our senior design expert."
                )

            return (
                f"You are eligible for the {session.package}. "
                "Thank you for your interest."
            )

        return "Conversation Finished"