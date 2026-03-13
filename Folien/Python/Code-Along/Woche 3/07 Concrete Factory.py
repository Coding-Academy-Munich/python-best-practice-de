# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Concrete Factory</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ### Adventure Game Version 2b
#
# - Zuweisung von Funktionalität zu `World` und `Location` ist sinnvoll
# - `World` ist in Gefahr ist, zu viele "Änderungsgründe" zu haben
#   - Änderungen an der Implementierung der Spiele-Welt
#   - Änderungen an den Initialisierungsdaten (z.B. XML statt JSON)
# - Können wir das vermeiden?

# %% [markdown]
#
# # Concrete Factory (Simple Factory)
#
# - Einfachere Version des Abstract Factory Patterns aus dem GoF Buch
#
# ### Frage
#
# - Wer soll ein Objekt erzeugen, wenn es Umstände gibt, die gegen Creator
#   sprechen?
#   - Komplexe Logik zur Erzeugung
#   - SRP/Kohäsion
#   - Viele Parameter zur Erzeugung notwendig
#
# ### Antwort
#
# - Eine Klasse, die nur für die Erzeugung von Objekten zuständig ist
# - Diese Klassen werden oft als *Factory* bezeichnet

# %%
import json
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint
from typing import Any, Mapping, Sequence

# %%
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)

# %%
LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


# %%
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


# %%
def _build_connections_for_all_locations(
    locations: dict[str, Location], location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: locations[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        locations[location_description["name"]].connections = connections


# %%
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    def __getitem__(self, location_name: str):
        return self.locations[location_name]

    @classmethod
    def from_location_descriptions(cls, location_descriptions: LocationDescriptions):
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        initial_location_name = location_descriptions[0]["name"]
        _build_connections_for_all_locations(locations, location_descriptions)
        return cls(locations, initial_location_name)

# %% [markdown]
#
# ## Die `WorldFactory`-Klasse

# %%

# %% [markdown]
#
# ### Verwendung der Factory

# %%

# %%

# %%

# %% [markdown]
#
# - Factories sind Beispiele für das GRASP Pattern "Pure Fabrication"
# - Sie können die Kohäsion von Klassen erhöhen und ihre Komplexität reduzieren
# - Sie erhöhen aber auch die Gesamtkomplexität des Systems

# %% [markdown]
#
# ## Mini-Workshop: Factory im Bibliothekssystem
#
# - Sie haben in vorhergehenden Workshops den Beginn eines Bibliothekssystems
#   implementiert
# - Implementieren Sie eine Möglichkeit, die Daten Ihrer Bibliothek aus einer
#   JSON-Datei zu laden. (Legen Sie dazu eine JSON-Datei an, die strukturell
#   zu Ihrer Implementierung passt)
# - Verlagern Sie dann die Erzeugung des Bibliothekssystems in eine Factory-Klasse
