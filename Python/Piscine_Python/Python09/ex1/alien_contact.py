from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            message = "Telepathic contact requires at least 3 witnesses"
            raise ValueError(message)
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals should include received messages")
        return self


def show_contact(contact: AlienContact) -> None:
    print("ID:", contact.contact_id)
    print("Type:", contact.contact_type.value)
    print("Location:", contact.location)
    print("Signal:", str(contact.signal_strength) + "/10")
    print("Duration:", contact.duration_minutes, "minutes")
    print("Witnesses:", contact.witness_count)
    print("Message: '" + str(contact.message_received) + "'")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    contact = AlienContact(
        contact_id="AC_2026_001",
        timestamp="2026-09-10T20:00:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    print("Valid contact report:")
    show_contact(contact)

    print("======================================")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_BAD",
            timestamp=datetime.now(),
            location="Moon base",
            contact_type=ContactType.telepathic,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=1,
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
