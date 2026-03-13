# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Creator</b>
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
#   - `World`- und `Location`-Klassen
#   - Attribute und Getter
# - Frage:
#   - Wer erzeugt die `Location`-Instanzen?

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
# ## Das Creator Pattern (GRASP)
#
# ### Frage
#
# - Wer ist verantwortlich für die Erzeugung eines Objekts?
#
# ### Antwort
#
# Klasse `A` bekommt die Verantwortung, ein Objekt der Klasse `B` zu erzeugen,
# wenn eine oder mehrere der folgenden Bedingungen zutreffen:
#
# - `A` enthält `B` (oder ist Eigentümer von `B`)
# - `A` verwaltet `B` (registriert, zeichnet auf)
# - `A` verwendet `B` intensiv
# - `A` hat die initialisierenden Daten, die `B` benötigt


# %% [markdown]
#
# ### Bemerkung
#
# - Factory ist oft eine Alternative zu Creator

# %% [markdown]
#
# ## Creator

# %% [markdown]
# <div style="float:left;margin:auto;padding:80px 0;width:25%">
# <ul>
# <li> <strike><code>Player</code></strike></li>
# <li> <strike><code>Game</code></strike></li>
# <li> <code>Pawn</code></li>
# <li> <code>Location</code></li>
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
@dataclass
class Location:
    name: str
    description: str

    @classmethod
    def from_description(cls, description: dict) -> "Location":
        return cls(description["name"], description.get("description", ""))


# %%
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)


# %%
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

# %% [markdown]
#
# - Wir können die `World`-Klasse jetzt verwenden.

# %%

# %%
