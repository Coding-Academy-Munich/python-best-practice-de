from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence, TYPE_CHECKING

if TYPE_CHECKING:
    from action_v4 import Action

LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
    description: str = ""
    connections: dict[str, "Location"] = field(default_factory=dict)

    @classmethod
    def from_description(cls, data: dict[str, Any]) -> "Location":
        return cls(data["name"], data.get("description", ""))

    def __getitem__(self, direction: str) -> "Location | None":
        return self.connections.get(direction)

    @property
    def move_actions(self) -> list["Action"]:
        from action_v4 import MoveAction

        return [
            MoveAction(direction, location)
            for direction, location in self.connections.items()
        ]
