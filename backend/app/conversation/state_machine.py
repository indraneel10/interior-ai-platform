from enum import Enum


class ConversationState(Enum):

    WELCOME = "WELCOME"

    LANGUAGE = "LANGUAGE"

    PROPERTY = "PROPERTY"

    BHK = "BHK"

    ROOMS = "ROOMS"

    BUDGET = "BUDGET"

    PACKAGE = "PACKAGE"

    TRANSFER = "TRANSFER"

    COMPLETE = "COMPLETE"