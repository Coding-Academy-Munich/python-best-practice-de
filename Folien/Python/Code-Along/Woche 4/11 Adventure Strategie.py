# %%
# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Strategie</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Version 4a: `Player`-Klasse
#
# <img src="img/adventure-v4a.svg" alt="Adventure Version 4a"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown]
#
# - `Player`-Klasse ist für die Strategie zuständig
# - Im Moment nur eine fest verdrahtete Strategie:
#   - Spieler nimmt immer zufälligen Eintrag in der Liste der Aktionen
# - Wir wollen mehrere Strategien unterstützen
# - Mit einer "interaktiven" Strategie wollen wir den menschlichen Spieler
#   einbinden
# - Versuchen wir eine Enumeration aller möglichen Strategien

# %% [markdown]
#
# ## Version 4b: Mehrere Strategien
#
# <img src="img/adventure-v4b.svg" alt="Adventure Version 4b"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown]
#
# - Das Klassendiagramm sieht nicht so schlecht aus
# - Implementierung ist unübersichtlich
# - Open-Closed Prinzip ist verletzt
# - Besser: Strategie Pattern

# %% [markdown]
#
# ## Version 4c: Strategy Pattern
#
# <img src="img/adventure-v4c.svg" alt="Adventure Version 4c"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown]
#
# ## Version 4d: Vereinfachung mit First-Class-Funktionen
#
# <img src="img/adventure-v4d.svg" alt="Adventure Version 4d"
#      style="display:block;margin:auto;height:60%"/>

# %%
from dataclasses import dataclass
from random import choice
from typing import Callable

# %%
from action_v4 import Action, SkipTurnAction
from location_v4 import Location
from pawn_v4 import Pawn
from simple_locations import simple_locations
from world_factory_v4 import WorldFactory


# %%

# %%
@dataclass
class Player:
    name: str
    pawn: Pawn

    @staticmethod
    def select_action(actions: list[Action]) -> Action:
        if not actions:
            raise ValueError("No actions available")
        return choice(actions)

    def perform(self, action: Action):
        action.perform(self)

    @property
    def location(self) -> Location:
        return self.pawn.location

    @location.setter
    def location(self, value: Location):
        self.pawn.location = value

    @property
    def description(self) -> str:
        return f"{self.name} at {self.location.name}"

    def take_turn(self):
        action = self.select_action(self.actions)
        print(f"{self.description} performs: {action.description}")
        self.perform(action)

    @property
    def actions(self) -> list[Action]:
        return [*self.pawn.actions, SkipTurnAction()]


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


# %%
def interactive_action_strategy(player: "Player"):
    print(f"Available actions for {player.description}:")
    for i, action in enumerate(player.actions, 1):
        print(f"{i}: {action.description}")
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 < choice <= len(player.actions):
                return player.actions[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(player.actions)}!")
        except ValueError:
            print("Please enter a valid number!")


# %%
player = Player("Iris", pawn, interactive_action_strategy)

# %%
# for _ in range(5):
#     player.take_turn()

# %% [markdown]
#
# ## Nächste Schritte
#
# - Verbesserung der Strategien
# - Kommunikation des Spiel-Fortschritts
