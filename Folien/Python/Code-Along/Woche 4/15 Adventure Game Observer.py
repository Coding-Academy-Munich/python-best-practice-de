# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure Game: Observer</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>

# %% [markdown]
#
# ## Adventure Version 4
#
# - OCP mit Strategy Pattern
# - Debug-Ausgaben mit Print Statement in `Player.take_turn()`

# %% [markdown]
#
# ### Für wen wollen wir (potenziell) Information ausgeben?
#
# - Spieler
# - Zuschauer
# - Entwickler (Logging)

# %% [markdown]
#
# ### Information pro Spieler
#
# - Zug hat begonnen
# - Mögliche Aktionen für den Spieler
# - Beginn einer Aktion
# - Ende einer Aktion
# - Aktion konnte nicht ausgeführt werden
# - Zug ist zu Ende

# %% [markdown]
#
# ### Information pro Spiel
#
# - Spieler ist dem Spiel beigetreten
# - Spiel hat begonnen
# - Spiel ist zu Ende
# - Ergebnis des Spiels (Gewonnen/Verloren, Zusammenfassung der Ereignisse)
# - Ein Fehler ist aufgetreten

# %%
from dataclasses import dataclass, field
from typing import Callable

# %%
from action_v4 import Action, SkipTurnAction
from location_v4 import Location, LocationDescriptions
from pawn_v4 import Pawn
from player_v4 import Player, interactive_action_strategy, random_action_strategy
from simple_locations import simple_locations
from world_factory_v4 import WorldFactory
from world_v4 import World


# %%
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
        return [*self.pawn.actions, SkipTurnAction()]

    def take_turn(self):
        action = self.select_action(self)
        print(f"{self.description} performs: {action.description}")
        action.perform(self)


# %%
action_strategies = {
    "interactive": interactive_action_strategy,
    "random": random_action_strategy,
}


# %%
def create_player(
    world: World,
    name: str,
    location: str | Location | None,
    action_strategy: str | Callable[[Player], Action] | None,
):
    if location is None:
        location = world.initial_location
    elif isinstance(location, str):
        location = world.locations[location]
    if action_strategy is None:
        action_strategy = random_action_strategy
    elif isinstance(action_strategy, str):
        action_strategy = action_strategies[action_strategy]
    pawn = Pawn(name, location)
    player = Player(name, pawn, action_strategy)
    return player


# %%
@dataclass
class Game:  # noqa: F811
    location_descriptions: LocationDescriptions
    players: list[Player] = field(default_factory=list)
    world: World = field(init=False)

    def __post_init__(self):
        self.world = WorldFactory.create(self.location_descriptions)

    def add_player(self, name: str, location, action_strategy=None):
        player = create_player(self.world, name, location, action_strategy)
        self.players.append(player)
        self.note_player_joined(player)

    def play_round(self):
        self.note_round_started()
        for player in self.players:
            player.take_turn()
        self.note_round_ended()

    def play_game(self):
        self.note_game_started()
        for _ in range(3):
            self.play_round()
        self.note_game_ended()

    def note_player_joined(self, player: Player):  # noqa
        print(f"Player {player.name} has joined the game.")

    def note_game_started(self):  # noqa
        print("Game started.")

    def note_game_ended(self):  # noqa
        print("Game ended.")

    def note_round_started(self):  # noqa
        print("Round started.")

    def note_round_ended(self):  # noqa
        print("Round ended.")


# %%

# %%

# %%

# %% [markdown]
#
# ## Probleme
#
# - Ausgabeformat ist fest im Code verankert
# - Detailgrad der Ausgabe ist fix
# - Keine Möglichkeit, Ausgaben in mehreren Formaten/auf mehreren Kanälen zu
#   erzeugen

# %% [markdown]
#
# ## Lösungsansatz: Observer Pattern
#
# <ul>
#   <li>Das Observer Pattern ermöglicht die Entkopplung von Subjekt und Beobachter</li>
#   <li>Pub/Sub-System</li>
#   <li>Nur eine Art von Ereignis</li>
#   <li><code>notify(msg: str)</code> statt <code>print(msg)</code>?</li>
#   <li class="fragment">
#     Nicht ideal: Wir würden gerne strukturierte Information ausgeben
#   </li>
#   <li class="fragment">
#     <b>Wir können das Pattern an unsere Bedürfnisse anpassen</b>
#   </li>
# </ul>

# %%
class GameObserver:
    def notify_player_joined(self, player: Player): ...

    def notify_game_started(self): ...

    def notify_game_ended(self): ...

    def notify_round_started(self): ...

    def notify_round_ended(self): ...

    def notify_turn_started(self, player: Player): ...

    def notify_turn_ended(self, player: Player): ...

    def notify_action_selected(self, player: Player, action: Action): ...


# %%
class DebugGameObserver(GameObserver):
    def notify_player_joined(self, player: Player):
        print(f"DEBUG: Player {player.name} has joined the game.")

    def notify_game_started(self):
        print("DEBUG: Game started.")

    def notify_game_ended(self):
        print("DEBUG: Game ended.")

    def notify_round_started(self):
        print("DEBUG: Round started.")

    def notify_round_ended(self):
        print("DEBUG: Round ended.")

    def notify_turn_started(self, player: Player):
        print(f"DEBUG: Turn started for {player.name}.")

    def notify_turn_ended(self, player: Player):
        print(f"DEBUG: Turn ended for {player.name}.")

    def notify_action_selected(self, player: Player, action: Action):
        print(f"DEBUG: {player.name} performs: {action.description}")


# %%
class CliObserver(GameObserver):
    def notify_player_joined(self, player: Player):
        print(f"Player {player.name} has joined the game.")

    def notify_turn_started(self, player: Player):
        print(f"{player.name} is in {player.location.name}:")
        print(f"{player.location.description}")

    def notify_action_selected(self, player: Player, action: Action):
        print(f"{player.name} performs: {action.description}")


# %%
@dataclass
class Player:
    name: str
    pawn: Pawn
    select_action: Callable[["Player"], Action] = random_action_strategy

    @property
    def location(self) -> Location: return self.pawn.location
    @location.setter
    def location(self, new_location: Location): self.pawn.location = new_location
    @property
    def description(self) -> str: return f"{self.name} at {self.location.name}"
    @property
    def actions(self) -> list[Action]: return [*self.pawn.actions, SkipTurnAction()]

    def take_turn(self):
        self.note_turn_started()
        action = self.select_action(self)
        self.note_action_selected(action)
        action.perform(self)
        self.note_turn_ended()

    def note_turn_started(self):
        print(f"Turn started for {self.name}.")

    def note_turn_ended(self):
        print(f"Turn ended for {self.name}.")

    def note_action_selected(self, action: Action):
        print(f"{self.name} performs: {action.description}")


# %%
@dataclass
class Game:
    location_descriptions: LocationDescriptions
    players: list[Player] = field(default_factory=list)
    world: World = field(init=False)
    observers: list[GameObserver] = field(default_factory=list)

    def __post_init__(self):
        self.world = WorldFactory.create(self.location_descriptions)

    def add_player(self, name, location, action_strategy=None):
        player = create_player(self.world, name, location, action_strategy)
        self.players.append(player)
        for observer in self.observers: player.attach_observer(observer)
        self.note_player_joined(player)

    def play_round(self):
        self.note_round_started()
        for player in self.players: player.take_turn()
        self.note_round_ended()

    def play_game(self):
        self.note_game_started()
        for _ in range(3): self.play_round()
        self.note_game_ended()

    def attach_observer(self, observer: GameObserver):
        self.observers.append(observer)
        for player in self.players:
            player.attach_observer(observer)

    def note_player_joined(self, player: Player):
        for observer in self.observers: observer.notify_player_joined(player)
    def note_game_started(self):
        for observer in self.observers: observer.notify_game_started()
    def note_game_ended(self):
        for observer in self.observers: observer.notify_game_ended()
    def note_round_started(self):
        for observer in self.observers: observer.notify_round_started()
    def note_round_ended(self):
        for observer in self.observers: observer.notify_round_ended()


# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop: Observer Pattern für die Bibliothesverwaltung
#
# - In einem der letzten Videos hatten wir eine Bibliotheksverwaltung implementiert
# - Im Folgenden ist der entsprechende Code nochmal angegeben
# - Fügen Sie einen Observer hinzu, der die Ereignisse in der Bibliothek
#   auf der Standardausgabe ausgibt

# %% [markdown]
#
# Nach hinzufügen des Observers sollte die Ausgabe fúr den
# Beispielcode in etwa so aussehen:
#
# ```
# Book added: Book 1 by Author 1 (ISBN: ISBN1)
# Book added: Book 2 by Author 2 (ISBN: ISBN2)
# Member added: John Doe (ID: M001)
# Member added: Jane Smith (ID: M002)
# Book borrowed: Member M001 borrowed book with ISBN ISBN1
# Book borrowed: Member M001 borrowed book with ISBN ISBN2
# Book borrowed: Member M002 borrowed book with ISBN ISBN1
# Error: Book with ISBN ISBN2 is not available
# Book returned: Member M001 returned book with ISBN ISBN2
# Book borrowed: Member M002 borrowed book with ISBN ISBN2
# Error: Book with ISBN ISBN3 is not available
# ```

# %%
from dataclasses import dataclass, field  # noqa


# %%
@dataclass
class BookInfo:
    title: str
    authors: list[str]
    isbn: str
    num_copies: int = 1


# %%
@dataclass
class MemberInfo:
    name: str
    address: str
    member_id: str


# %%
@dataclass
class BookInventory:
    books: dict[str, BookInfo] = field(default_factory=dict)

    def add_book(self, book: BookInfo):
        if book.isbn in self.books:
            self.books[book.isbn].num_copies += book.num_copies
        else:
            self.books[book.isbn] = book

    def is_available(self, isbn: str) -> bool:
        return isbn in self.books and self.books[isbn].num_copies > 0


# %%
@dataclass
class MemberRegistry:
    members: dict[str, MemberInfo] = field(default_factory=dict)

    def add_member(self, member: MemberInfo):
        self.members[member.member_id] = member


# %%
@dataclass
class RentalRegistry:
    rentals: dict[str, list[str]] = field(default_factory=dict)

    def borrow_book(self, member_id: str, isbn: str, book_inventory: BookInventory):
        if book_inventory.is_available(isbn):
            if member_id not in self.rentals:
                self.rentals[member_id] = []
            if isbn not in self.rentals[member_id]:
                self.rentals[member_id].append(isbn)
                book_inventory.books[isbn].num_copies -= 1

    def return_book(self, member_id: str, isbn: str, book_inventory: BookInventory):
        if member_id in self.rentals and isbn in self.rentals[member_id]:
            self.rentals[member_id].remove(isbn)
            book_inventory.books[isbn].num_copies += 1

    def get_member_rentals(self, member_id: str) -> list[str]:
        return self.rentals.get(member_id, [])

    def get_all_rentals(self) -> dict[str, list[str]]:
        return self.rentals


# %%
@dataclass
class Library:
    book_inventory: BookInventory = field(default_factory=BookInventory)
    member_registry: MemberRegistry = field(default_factory=MemberRegistry)
    rental_registry: RentalRegistry = field(default_factory=RentalRegistry)

    def add_book(self, title: str, authors: list[str], isbn: str, num_copies: int = 1):
        self.book_inventory.add_book(BookInfo(title, authors, isbn, num_copies))

    def add_member(self, name: str, address: str, member_id: str):
        self.member_registry.add_member(MemberInfo(name, address, member_id))

    def borrow_book(self, member_id: str, isbn: str):
        self.rental_registry.borrow_book(member_id, isbn, self.book_inventory)

    def return_book(self, member_id: str, isbn: str):
        self.rental_registry.return_book(member_id, isbn, self.book_inventory)

    def is_book_available(self, isbn: str) -> bool:
        return self.book_inventory.is_available(isbn)

    def get_member_rentals(self, member_id: str) -> list[str]:
        return self.rental_registry.get_member_rentals(member_id)

    def get_all_rentals(self) -> dict[str, list[str]]:
        return self.rental_registry.get_all_rentals()


# %%
library = Library()

# %%
library.add_book("Book 1", ["Author 1"], "ISBN1", 2)
library.add_book("Book 2", ["Author 2"], "ISBN2", 1)

# %%
library.add_member("John Doe", "123 Main St", "M001")
library.add_member("Jane Smith", "456 Elm St", "M002")

# %%
library.borrow_book("M001", "ISBN1")
library.borrow_book("M001", "ISBN2")

# %%
library.borrow_book("M002", "ISBN1")
library.borrow_book("M002", "ISBN2")

# %%
library.return_book("M001", "ISBN2")
library.borrow_book("M002", "ISBN2")
library.borrow_book("M002", "ISBN3")

# %%
library.get_member_rentals("M001")

# %%
library.get_all_rentals()

# %%

# %%
