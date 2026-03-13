# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Informations-Experte</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# - Use Case "Spiel initialisieren"
# - Bisher:
#   - `World` und `Location` Klassen
#   - `World` erzeugt alle `Location` Objekte
# - Nächster Schritt:
#   - Speichern von Information über die Verbindung zwischen den `Location`
#     Objekten
#   - Hilfreich dazu: Finden von Locations anhand ihres Namens
# - Frage:
#   - Wer findet `Location` Objekte anhand ihres Namens?

# %% [markdown]
#
# ## Kandidaten

# %% [markdown]
# <div style="float:left;margin:auto;padding:80px 0;width:25%">
# <ul>
# <li> <code>Player</code></li>
# <li> <code>Game</code></li>
# <li> <code>Pawn</code></li>
# <li> <code>Location</code></li>
# <li> <code>World</code></li>
# </ul>
# </div>
# <img src="img/adv-domain-03-small.svg"
#      style="float:right;margin:auto;width:70%"/>

# %% [markdown]
#
# ## Informations-Experte (engl. "Information Expert", GRASP)
#
# ### Frage
#
# An welche Klasse sollen wir eine Verantwortung delegieren?
#
# ### Antwort
#
# An die Klasse, die die meisten Informationen hat, die für die Erfüllung der
# Verantwortung notwendig sind.

# %% [markdown]
#
# ## Wer ist der Informationsexperte?

# %% [markdown]
# <div style="float:left;margin:auto;padding:80px 0;width:25%">
# <ul>
# <li> <strike><code>Player</code></strike></li>
# <li> <strike><code>Game</code></strike></li>
# <li> <strike><code>Pawn</code></strike></li>
# <li> <strike><code>Location</code></strike></li>
# <li> <b><code>World</code></b></li>
# </ul>
# </div>
# <img src="img/adv-domain-03-small.svg"
#      style="float:right;margin:auto;width:70%"/>

# %%
from dataclasses import dataclass
import json
from pathlib import Path


# %%
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)


# %%
@dataclass
class Location:
    name: str
    description: str

    @classmethod
    def from_description(cls, description: dict) -> "Location":
        return cls(description["name"], description.get("description", ""))


# %%
def _world_from_location_descriptions(location_descriptions):
    locations = {
        data["name"]: Location.from_description(data) for data in location_descriptions
    }
    initial_location_name = location_descriptions[0]["name"]
    return World(locations, initial_location_name)


# %%
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    @staticmethod
    def from_location_descriptions(location_descriptions: list[dict]) -> "World":
        return _world_from_location_descriptions(location_descriptions)

    def __getitem__(self, location_name: str):
        return self.locations[location_name]


# %%
world = World.from_location_descriptions(simple_locations)

# %%
world["Room 1"]

# %%
world["Room 2"]
