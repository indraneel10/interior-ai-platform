from app.conversation.prompts import PROMPTS
from app.conversation.package_selector import determine_package


class ConversationManager:

    def get_welcome(self):

        return PROMPTS["WELCOME"]["English"]

    def choose_package(self, budget):

        return determine_package(budget)