# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Spielfigur (V1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %%
from dataclasses import dataclass
from location_v2 import Location


# %%
@dataclass
class Pawn:
    name: str
    location: Location


# %% [markdown]
#
# ## Version 3a: Spielfiguren
#
# <img src="img/adventure-v3a-overview.svg" alt="Adventure Version 3a"
#      style="display:block;margin:auto;height:80%"/>

# %%
@dataclass
class Pawn:
    name: str
    location: Location

    def move(self, direction):
        new_location = self.location[direction]
        if new_location:
            self.location = new_location
        else:
            print(f"{self.name!r}: Cannot move in direction {direction!r}.")

