from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
    description: str = ""
    connections: dict[str, "Location"] = field(default_factory=dict)

    @classmethod
    def from_description(cls, data: LocationDescription) -> "Location":
        return cls(data["name"], data.get("description", ""))

    def __getitem__(self, direction: str) -> "Location | None":
        return self.connections.get(direction)
