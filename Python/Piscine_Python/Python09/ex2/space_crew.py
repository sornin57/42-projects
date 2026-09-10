from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        if not self.has_leader():
            message = "Mission must have at least one Commander or Captain"
            raise ValueError(message)
        if self.duration_days > 365 and not self.has_enough_experience():
            raise ValueError("Long missions need 50% experienced crew")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self

    def has_leader(self) -> bool:
        for member in self.crew:
            if member.rank == Rank.commander or member.rank == Rank.captain:
                return True
        return False

    def has_enough_experience(self) -> bool:
        experienced = 0
        for member in self.crew:
            if member.years_experience >= 5:
                experienced = experienced + 1
        return experienced >= len(self.crew) / 2


def show_mission(mission: SpaceMission) -> None:
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print("Duration:", mission.duration_days, "days")
    print("Budget: $" + str(mission.budget_millions) + "M")
    print("Crew size:", len(mission.crew))
    print("Crew members:")
    for member in mission.crew:
        print("-", member.name, "(" + member.rank.value + ")", end=" ")
        print("-", member.specialization)


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    crew = [
        CrewMember(
            member_id="C001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=42,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="C002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=32,
            specialization="Navigation",
            years_experience=7,
        ),
        CrewMember(
            member_id="C003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=29,
            specialization="Engineering",
            years_experience=6,
        ),
    ]
    mission = SpaceMission(
        mission_id="M2026_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-12-01T08:00:00",
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )
    print("Valid mission created:")
    show_mission(mission)

    print("=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M_BAD",
            mission_name="Bad Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=20,
            crew=[crew[1]],
            budget_millions=100.0,
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
