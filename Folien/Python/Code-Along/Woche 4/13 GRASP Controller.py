# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Controller</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Starten eines Spiels
#
# - Laden der Welt
# - Erzeugen der Pawn-Objekte für die Spieler
# - Erzeugen der Spieler
# - Ausführen der Spielrunde:
#   - Jeder Spieler wählt eine Aktion
#   - Die Aktion wird ausgeführt

# %%
from dataclasses import dataclass, field
from typing import Callable


# %%
from action_v4 import Action
from location_v4 import Location, LocationDescriptions
from pawn_v4 import Pawn
from player_v4 import Player, interactive_action_strategy, random_action_strategy
from simple_locations import simple_locations
from world_factory_v4 import WorldFactory
from world_v4 import World

# %%
world_factory = WorldFactory()
world = world_factory.create(simple_locations)

# %%
alice_pawn = Pawn("Alice", world.locations["Room 1"])
bob_pawn = Pawn("Bob", world.locations["Room 2"])

# %%
players = [
    Player("Alice", alice_pawn, interactive_action_strategy),
    Player("Bob", bob_pawn),
]


# %%
def run_game():
    for _ in range(5):
        for player in players:
            player.take_turn()


# %%
# run_game()

# %% [markdown]
#
# ## Zwei gegenläufige Anforderungen
#
# - Viele kleine, kohäsive Klassen und Funktionen für gute Struktur
# - Einfaches Interface für den Benutzer

# %% [markdown]
#
# # GRASP: Controller
#
# - Für jedes Modul/Subsystem: Externe Meldungen werden von Controller-Objekten
#   bearbeitet, die
#   - nicht Teil der Benutzeroberfläche sind,
#   - jeweils ein Subsystem oder einen Anwendungsfall abdecken
# - Der Controller ist das erste Objekt nach der Benutzeroberfläche, das
#   Ereignisse/Meldungen bearbeitet.
# - Der Controller ist oft eine Fassade, d.h. er delegiert seine Arbeit an andere
#   Objekte.
# - Möglicherweise koordiniert er das System aber auch.
# - Ein Use-Case-Controller bearbeitet immer einen kompletten Use-Case (Controller
#   können aber auch mehr als einen Use-Case bearbeiten).

# %% [markdown]
#
# ## Controller
#
# - Verwandt: Fassaden-Pattern (Domänen-Fassade), Domänencontroller
# - Siehe hexagonale Architektur: Controller sind die Ports in der hexagonalen
#   Architektur
# - Tests: Controller bieten eine zentrale Schnittstelle für einzelne
#   Subsysteme oder Anwendungsfälle

# %% [markdown]
#
# ## Controller in unserem Adventure-Game
#
# - Wo kommt die Controller-Klasse her?
#   - Anwendungsfälle (Use Cases)
#   - Domänenmodell

# %% [markdown]
#
# ### Domänenmodell

# %% [markdown]
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %%

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

# %%

# %%

# %% [markdown]
#
# ## Workshop: Controller für Bibliotheksverwaltung
#
# - Im Anschluss ist eine mögliche Implementierung für die Bibliotheksverwaltung
#   angegeben.
# - Implementieren Sie einen Controller für die Bibliotheksverwaltung
# - Modifizieren Sie das Anwendungsbeispiel so, dass der Controller verwendet wird
# - Wie hat sich die Benutzung des Systems verändert?

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
book_inventory = BookInventory()
member_registry = MemberRegistry()
rental_registry = RentalRegistry()

# %%
# Add books to the inventory
book1 = BookInfo("Book 1", ["Author 1"], "ISBN1", 2)
book2 = BookInfo("Book 2", ["Author 2"], "ISBN2", 1)
book_inventory.add_book(book1)
book_inventory.add_book(book2)

# %%
# Add members to the registry
member1 = MemberInfo("John Doe", "123 Main St", "M001")
member2 = MemberInfo("Jane Smith", "456 Elm St", "M002")
member_registry.add_member(member1)
member_registry.add_member(member2)

# %%
# Check availability
print(book_inventory.is_available("ISBN1"))  # True
print(book_inventory.is_available("ISBN2"))  # True

# %%
# Borrow books
rental_registry.borrow_book("M001", "ISBN1", book_inventory)
rental_registry.borrow_book("M001", "ISBN2", book_inventory)

# %%
# Check availability
print(book_inventory.is_available("ISBN1"))  # True
print(book_inventory.is_available("ISBN2"))  # False

# %%
# Borrow books
rental_registry.borrow_book("M002", "ISBN1", book_inventory)
rental_registry.borrow_book("M002", "ISBN2", book_inventory)

# %%
# Check availability
print(book_inventory.is_available("ISBN1"))  # False
print(book_inventory.is_available("ISBN2"))  # False


# %%
# Check member rentals
print(rental_registry.get_member_rentals("M001"))  # ["ISBN1", "ISBN2"]
print(rental_registry.get_member_rentals("M002"))  # ["ISBN1"]

# %%
# Check all rentals
print(
    rental_registry.get_all_rentals()
)  # {"M001": ["ISBN1", "ISBN2"], "M002": ["ISBN1"]}

# %%
# Return a book
rental_registry.return_book("M001", "ISBN1", book_inventory)
print(book_inventory.is_available("ISBN1"))  # True
