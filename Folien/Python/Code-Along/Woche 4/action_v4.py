from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING
from location_v4 import Location

if TYPE_CHECKING:
    from player_v4 import Player


class Action(ABC):
    @property
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def perform(self, instigator: "Player") -> None: ...


@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def perform(self, instigator: "Player") -> None:
        instigator.location = self.target


@dataclass
class SkipTurnAction(Action):
    @property
    def description(self) -> str:
        return "wait one turn"

    def perform(self, instigator: "Player") -> None:
        # Do nothing...
        pass
