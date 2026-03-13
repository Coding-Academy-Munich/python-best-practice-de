# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Spielfigur (V2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Version 3b: Enumeration der Aktionen
#
# - Enumeration `Action` mit allen möglichen Aktionen
# - `Pawn`-Klasse hat nur noch eine `perform_action()`-Methode
# - `perform_action()`-Methode bekommt eine `action` als Parameter

# %% [markdown]
#
# ## Version 3b: Spielfiguren mit Enumeration
#
# <img src="img/adventure-v3b-overview.svg" alt="Adventure Version 3b"
#      style="display:block;margin:auto;height:80%"/>

# %%
from dataclasses import dataclass
from enum import Enum

# %%
from location_v2 import Location


# %%
class Action(str, Enum):
    MOVE = "move"
    SKIP_TURN = "skip turn"


# %%
@dataclass
class Pawn:
    name: str
    location: Location

    def perform_action(self, action: Action, **kwargs):
        if action == Action.MOVE:
            new_location = self.location[kwargs["direction"]]
            if new_location:
                self.location = new_location
            else:
                print(
                    f"{self.name!r}: Cannot move in direction {kwargs['direction']!r}."
                )
        elif action == Action.SKIP_TURN:
            print(f"{self.name!r} skips turn.")
        else:
            print(f"Unknown action: {action!r}")


# %% [markdown]
#
# ## GRASP und SOLID Prinzipien
#
# - GRASP:
#   - Geschützte Variation (Protected Variation)
#   - Indirektion
#   - Polymorphie
# - SOLID:
#   - Open-Closed Principle
