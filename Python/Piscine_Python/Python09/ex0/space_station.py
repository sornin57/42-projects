from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def show_station(station: SpaceStation) -> None:
    print("ID:", station.station_id)
    print("Name:", station.name)
    print("Crew:", station.crew_size, "people")
    print("Power:", str(station.power_level) + "%")
    print("Oxygen:", str(station.oxygen_level) + "%")
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-09-10T10:00:00",
    )
    print("Valid station created:")
    show_station(station)

    print("========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD001",
            name="Bad Station",
            crew_size=99,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
