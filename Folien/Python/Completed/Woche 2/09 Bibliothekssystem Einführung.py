# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Bibliothekssystem: Einführung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Bibliotheks-Verwaltungssystem: Einführung
#
# - Bibliotheks-Verwaltungssystem
# - Nutzer
#   - Bibliothekare
#   - Bibliotheksbenutzer
#   - Administratoren
# - Anforderungen
#   - Leicht zu erweitern und zu warten
#   - ...

# %% [markdown]
#
# - Anforderungen
# - Domänenmodell

# %% [markdown]
#
# ## Anforderungen
#
# - Verwalten von Mitgliedern
#   - Aufnehmen, Löschen, Suchen, Anzeigen und Ändern von Mitgliedern
# - Verwalten von Büchern
#   - Aufnehmen, Löschen, Suchen, Anzeigen und Ändern von Büchern
# - Ausleihen und Rückgabe von Büchern
# - Erinnerungen und Gebühren

# %% [markdown]
#
# ## Workshop: Bibliotheks-Verwaltungssystem (Teil 1)
#
# - Entwickeln Sie ein erstes Domänenmodell für das Bibliotheks-Verwaltungssystem
#   - Sie können z.B. ein Klassendiagramm verwenden oder einfach nur eine Liste
#     von Klassen und Attributen
# - Welche Klassen in Ihrem Domänenmodell haben Assoziationen zu
#   - Mitgliedern?
#   - Büchern?

# %% [markdown]
#
# - Verwenden Sie das Creator Pattern um zu entscheiden, welche Klasse die
#   Verantwortung für das Erstellen von Mitgliedern und welche die Verantwortung
#   für das Erstellen von Büchern hat
# - Verwenden Sie das Information Expert Pattern um zu entscheiden, welche Klasse
#   die Verantwortung für das Suchen von Mitgliedern und welche die Verantwortung
#   für das Suchen von Büchern hat
# - Implementieren Sie diesen Teil des Domänenmodells in Python
# - Versuchen Sie dabei das Prinzip der niedrigen Repräsentationslücke anzuwenden

# %%
from dataclasses import dataclass, field


# %%
@dataclass
class Member:
    name: str
    address: str
    email: str


# %%
@dataclass
class Book:
    title: str
    isbn: str


# %%
@dataclass
class LibrarySystem:
    members: list[Member] = field(default_factory=list)
    books: list[Book] = field(default_factory=list)

    def __str__(self):
        result = "Members:\n"
        for member in self.members:
            result += f"  {member.name}\n"
        result += "Books:\n"
        for book in self.books:
            result += f"  {book.title}\n"
        return result

    def add_member(self, name: str, address: str, email: str):
        member = Member(name, address, email)
        self.members.append(member)

    def add_book(self, title: str, isbn: str):
        book = Book(title, isbn)
        self.books.append(book)

    def find_member(self, name: str) -> Member | None:
        for member in self.members:
            if member.name == name:
                return member
        return None

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None


# %%
library = LibrarySystem()

# %%
library.add_member("Max Mustermann", "Musterstraße 1", "max@example.com")

# %%
library.add_book("Design Patterns", "978-0-20163-361-0")

# %%
library.find_member("Max Mustermann")

# %%
library.find_book("Design Patterns")

# %%
print(library)


# %%
@dataclass
class MemberCatalog:
    members: list = field(default_factory=list)

    def add_member(self, name: str, address: str, email: str):
        member = Member(name, address, email)
        self.members.append(member)

    def find_member(self, name: str) -> Member | None:
        for member in self.members:
            if member.name == name:
                return member
        return None


# %%
class BookFactory:
    def create_book(self, title: str, isbn: str):
        return Book(title, isbn)

    def from_json(self, path_to_json_file):
        ...
        # self.create_book(...)
        ...

    def from_database(self, db_connection):
        ...


# %%
@dataclass
class BookCatalog:
    books: list[Book] = field(default_factory=list)
    book_factory: BookFactory = BookFactory()

    def add_book(self, title: str, isbn: str):
        book = self.book_factory.create_book(title, isbn)
        self.books.append(book)

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None


# %%
@dataclass
class LibrarySystem:
    members = MemberCatalog()
    books = BookCatalog()

    def add_member(self, name: str, address: str, email: str):
        self.members.add_member(name, address, email)

    def add_book(self, title: str, isbn: str):
        self.books.add_book(title, isbn)

    def find_member(self, name: str) -> Member | None:
        return self.members.find_member(name)

    def find_book(self, title: str) -> Book | None:
        return self.books.find_book(title)


# %%
library = LibrarySystem()
library.add_member("Max Mustermann", "Musterstraße 1", "max@example.com")
library.add_book("Design Patterns", "978-0-20163-361-0")

# %%
library.find_member("Max Mustermann")

# %%
library.find_book("Design Patterns")

# %%
print(library)
