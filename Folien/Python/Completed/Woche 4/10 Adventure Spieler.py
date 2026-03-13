# %%
# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Spieler</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Version 3c: Command Pattern
#
# <img src="img/adventure-v3c-overview.svg" alt="Adventure Version 3c"
#      style="display:block;margin:auto;height:80%"/>

# %%
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from random import choice
from typing import Any

# %%
from action_v4 import Action, MoveAction
from location_v4 import Location
from simple_locations import simple_locations
from world_factory_v4 import WorldFactory


# %%
@dataclass
class Pawn:
    name: str
    location: Location

    def perform(self, action: Action):
        action.perform(self)


# %%
world_factory = WorldFactory()
world = world_factory.create(simple_locations)

# %%
pawn = Pawn("Alice", world.locations["Room 1"])
print(pawn)

# %%
action = MoveAction("north", world.locations["Room 2"])
pawn.perform(action)
print(pawn)


# %% [markdown]
#
# - Sowohl menschliche als auch computergesteuerte Spieler
# - Dazu notwendig:
#   - Generieren aller möglichen Aktionen (situationsabhängig)
#   - Auswählen einer Aktion
#   - Ausführen der Aktion
# - Wer soll diese Verantwortlichkeiten übernehmen?

# %% [markdown]
#
# - Informationsexperte:
#   - Im Moment kennt niemand alle Aktionen, die möglich sind
#   - `Pawn` weiß, wo er sich befindet
#   - `Pawn` enthält wahrscheinlich die meisten benötigten Informationen für
#     weitere Aktionen
# - Sollen wir die Verantwortung an `Pawn` übergeben?

# %% [markdown]
#
# ### Gegenargumente
#
# - Damit bekommt `Pawn` potenziell zu viele Verantwortlichkeiten
#   - Bewegung auf dem Spielfeld
#   - Darstellung der Grafik
#   - Strategie für computergesteuerte Spieler
#   - Interaktion mit menschlichem Benutzer
# - Niedrige Repräsentationslücke?

# %% [markdown]
#
# ### Domänenmodell

# %% [markdown]
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown]
#
# - `Player` ist für die Strategie zuständig
# - Wir sollten eine `Player`-Klasse einführen und ihr die Verantwortung
#   für die neuen Aufgaben übergeben

# %% [markdown]
#
# ## Version 4a: `Player`-Klasse
#
# <img src="img/adventure-v4a.svg" alt="Adventure Version 4a"
#      style="display:block;margin:auto;height:80%"/>

# %%
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
    def move_actions(self) -> list[Action]:
        return [
            MoveAction(direction, location)
            for direction, location in self.connections.items()
        ]


# %%
@dataclass
class Pawn:
    name: str
    location: Location

    @property
    def actions(self):
        return self.location.move_actions


# %%
class Action(ABC):  # noqa
    @property
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def perform(self, instigator: "Player") -> None: ...


# %%
@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def perform(self, instigator: "Player") -> None:
        instigator.location = self.target


# %%
@dataclass
class SkipTurnAction(Action):  # noqa
    @property
    def description(self) -> str:
        return "wait one turn"

    def perform(self, instigator: "Player") -> None:
        # Do nothing...
        pass


# %%
@dataclass
class Player:
    name: str
    pawn: Pawn

    @property
    def location(self) -> Location:
        return self.pawn.location

    @location.setter
    def location(self, value: Location):
        self.pawn.location = value

    def take_turn(self):
        action = self.select_action(self.actions)
        print(f"{self} performs: {action.description}")
        self.perform(action)

    @property
    def actions(self) -> list[Action]:
        return [*self.pawn.actions, SkipTurnAction()]

    @staticmethod
    def select_action(actions: list[Action]) -> Action:
        if not actions:
            raise ValueError("No actions available")
        # return actions[0]
        return choice(actions)

    def perform(self, action: Action):
        action.perform(self)

    def __str__(self):
        return f"Player {self.name} at {self.pawn.location.name}"


# %%
world_factory = WorldFactory()
world = world_factory.create(simple_locations)

# %%
pawn = Pawn("Alice", world.locations["Room 1"])
print(pawn)

# %%
player = Player("Alice", pawn)
print(player)

# %%
player.take_turn()
print(player)

# %%
for _ in range(10):
    player.take_turn()
