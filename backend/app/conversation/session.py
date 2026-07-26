from dataclasses import dataclass


@dataclass
class ConversationSession:

    session_id: str

    language: str | None = None

    property_type: str | None = None

    bhk: str | None = None

    rooms: int | None = None

    budget: float | None = None

    package: str | None = None

    state: str = "WELCOME"