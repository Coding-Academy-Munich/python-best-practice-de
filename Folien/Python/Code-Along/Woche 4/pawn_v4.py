from dataclasses import dataclass
from location_v4 import Location


@dataclass
class Pawn:
    name: str
    location: Location

    @property
    def actions(self):
        return self.location.move_actions
