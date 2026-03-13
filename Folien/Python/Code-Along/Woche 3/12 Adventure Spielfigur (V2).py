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


# %%
@dataclass
class Pawn:
    name: str
    location: Location

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
