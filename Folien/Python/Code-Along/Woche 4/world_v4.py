from dataclasses import dataclass

from location_v4 import Location


@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    def __getitem__(self, location_name: str):
        """Get a location by name."""
        return self.locations[location_name]

    @property
    def initial_location(self) -> Location:
        return self[self.initial_location_name]
