from dataclasses import dataclass
from random import choice
from typing import Callable

from action_v4 import Action
from location_v4 import Location
from pawn_v4 import Pawn


def first_action_strategy(player: "Player"):
    """Return the first available action.

    If no action is available, return a wait action."""

    actions = player.actions
    if actions:
        return actions[0]
    else:
        from action_v4 import SkipTurnAction

        return SkipTurnAction()


def random_action_strategy(player: "Player"):
    """Return a random choice from the available actions.

    If no action is available, return a wait action."""

    actions = player.actions
    if actions:
        return choice(actions)
    else:
        from action_v4 import SkipTurnAction

        return SkipTurnAction()


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


@dataclass
class Player:
    name: str
    pawn: Pawn
    select_action: Callable[["Player"], Action] = random_action_strategy

    @property
    def location(self) -> Location:
        return self.pawn.location

    @location.setter
    def location(self, new_location: Location):
        self.pawn.location = new_location

    @property
    def description(self) -> str:
        return f"{self.name} at {self.location.name}"

    @property
    def actions(self) -> list[Action]:
        from action_v4 import SkipTurnAction

        return [*self.pawn.actions, SkipTurnAction()]

    def take_turn(self):
        action = self.select_action(self)
        print(f"{self.description} performs: {action.description}")
        action.perform(self)
