# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Command Pattern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Letzter Stand: Spielfiguren mit Enumeration
#
# <img src="img/adventure-v3b-overview.svg" alt="Adventure Version 3b"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown]
#
# ### Probleme
#
# - Signatur von `Pawn.perform()` ist nicht sehr klar
#   - Verschiedene Aktionen benötigen verschiedene Parameter
#   - In Python können wir das mit `*args` und `**kwargs` umgehen
# - Open-Closed Prinzip verletzt
#   - Neue Aktionen benötigen Änderungen an `Pawn` und `Action`

# %% [markdown]
#
# ### Lösung: Command Pattern
#
# - Aktionen werden in eigene Klassen ausgelagert
# - `Pawn.perform()` nimmt ein `Action`-Objekt
# - Die zur Ausführung der Aktion benötigten Daten werden im `Action`-Objekt
#   gespeichert
# - `Action`-Objekte können zusätzliche Funktion zur Verfügung stellen, z.B.
#    Texte für das UI bereitstellen

# %% [markdown]
#
# ## Version 3c: Command Pattern
#
# <img src="img/adventure-v3c-overview.svg" alt="Adventure Version 3c"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown]
#
# ### Vorteile
#
# - Open-Closed Prinzip wird eingehalten
# - `Pawn.perform()` hat eine klare Signatur
# - `Action`-Klassen können zusätzliche Funktionen bereitstellen

# %%
from abc import ABC, abstractmethod
from dataclasses import dataclass

from location_v2 import Location


# %%
@dataclass
class Pawn:
    name: str
    location: Location

    def perform(self, action: "Action"):
        action.perform(self)


# %%
class Action(ABC):
    @property
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def perform(self, instigator: "Pawn") -> None: ...


# %%
@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def perform(self, instigator: "Pawn") -> None:
        instigator.location = self.target


# %%
@dataclass
class SkipTurnAction(Action):
    @property
    def description(self) -> str:
        return "wait one turn"

    def perform(self, instigator: "Pawn") -> None:
        # Do nothing...
        pass


# %%
from world_factory_v2 import WorldFactory  # noqa: E402
from simple_locations import simple_locations  # noqa: E402

# %%
world = WorldFactory.create(simple_locations)

# %%
room_1: Location = world["Room 1"]
room_2: Location = world["Room 2"]

# %%
print({d: loc.name for (d, loc) in room_1.connections.items()})

# %%
pawn = Pawn("Player", room_1)

# %%
print(pawn.name, "is in", pawn.location.name)

# %%
pawn.perform(MoveAction("north", room_2))

# %%
print(pawn.name, "is in", pawn.location.name)
