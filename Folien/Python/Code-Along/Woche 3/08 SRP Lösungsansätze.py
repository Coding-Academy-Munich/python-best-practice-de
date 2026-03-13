# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>SRP: Lösungsansätze</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Ein Änderungsgrund?
#
# <img src="img/book_01.svg"
#      style="display:block;margin:auto;width:35%"/>
#

# %% [markdown]
#
# ## Verletzung des SRPs
#
# <img src="img/book_02.svg"
#      style="display:block;margin:auto;width:60%"/>

# %%
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def print(self):
        # Lots of code that handles the printer
        print(f"Printing {self.title} to printer.")

    def save(self):
        # Lots of code that handles the database
        print(f"Saving {self.title} to database.")


# %%
book = Book("Clean Code", "Robert C. Martin", 464)
book.print()
book.save()


# %% [markdown]
#
# ## Auflösung der SRP-Verletzung (Version 1a)
#
# Vorschlag von Robert C. Martin in Clean Architecture:
#
# <img src="img/book_resolution_1a_srp.svg"
#      style="display:block;margin:auto;width:40%"/>

# %%
class BookV1a:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages


# %%
class BookPrinterV1a:
    def __init__(self, book):
        self.book = book

    def print(self):
        # Lots of code that handles the printer
        print(f"Printing {self.book.title} to printer.")


# %%
class BookDatabaseV1a:
    def __init__(self, book):
        self.book = book

    def save(self):
        # Lots of code that handles the database
        print(f"Saving {self.book.title} to database.")


# %%
book_v1a = BookV1a("Clean Code", "Robert C. Martin", 464)

# %%
book_printer_v1a = BookPrinterV1a(book_v1a)
book_printer_v1a.print()

# %%
book_database_v1a = BookDatabaseV1a(book_v1a)
book_database_v1a.save()


# %% [markdown]
#
# ## Auflösung der SRP-Verletzung (Version 1a mit Fassade)
#
# <img src="img/book_resolution_1a_srp_facade.svg"
#      style="display:block;margin:auto;width:50%"/>

# %%
class BookPrinterFacadeV1a:
    def __init__(self, book):
        self.book_printer = BookPrinterV1a(book)
        self.book_database = BookDatabaseV1a(book)

    def print(self):
        self.book_printer.print()

    def save(self):
        self.book_database.save()


# %%
book_printer_facade_v1a = BookPrinterFacadeV1a(book_v1a)
book_printer_facade_v1a.print()
book_printer_facade_v1a.save()


# %% [markdown]
#
# ## Auflösung der SRP-Verletzung (Version 1)
#
# <img src="img/book_resolution_1_srp.svg"
#      style="display:block;margin:auto;width:50%"/>

# %%
class BookV1:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages


# %%
class BookPrinterV1:
    @staticmethod
    def print(book):
        # Lots of code that handles the printer
        print(f"Printing {book.title} to printer.")


# %%
class BookDatabaseV1:
    @staticmethod
    def save(book):
        # Lots of code that handles the database
        print(f"Saving {book.title} to database.")


# %%
book_v1 = BookV1("Clean Code", "Robert C. Martin", 464)
book_printer_v1 = BookPrinterV1()
book_database_v1 = BookDatabaseV1()


# %%
book_printer_v1.print(book_v1)

# %%
book_database_v1.save(book_v1)


# %% [markdown]
#
# ## Auflösung der SRP-Verletzung (Version 1 mit Facade)
#
# <img src="img/book_resolution_1_srp_facade.svg"
#      style="display:block;margin:auto;width:50%"/>

# %%
class BookFacadeV1:
    def __init__(self, book):
        self.book = book
        self.book_printer = BookPrinterV1()
        self.book_database = BookDatabaseV1()

    def print(self):
        self.book_printer.print(self.book)

    def save(self):
        self.book_database.save(self.book)


# %%
book_facade_v1 = BookFacadeV1(book_v1)

# %%
book_facade_v1.print()

# %%
book_facade_v1.save()


# %% [markdown]
#
# ### Implementierung als Funktionen

# %%
def print_book(book):
    # Lots of code that handles the printer
    print(f"Printing {book.title} to printer.")


# %%
def save_book(book):
    # Lots of code that handles the database
    print(f"Saving {book.title} to database.")


# %%
print_book(book_v1)

# %%
save_book(book_v1)


# %% [markdown]
#
# ## Auflösung der SRP-Verletzung (Version 2)
#
# <img src="img/book_resolution_2_srp.svg"
#      style="display:block;margin:auto;width:60%"/>

# %%
class BookV2:
    def __init__(
        self, title: str, author: str, pages: int, book_printer, book_database
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_printer = book_printer
        self.book_database = book_database

    def print(self):
        # Assuming book_printer has a print method takes a BookV2 instance.
        self.book_printer.print(self)

    def save(self):
        # Assuming book_database has a save method takes a BookV2 instance.
        self.book_database.save(self)


# %%
class BookPrinterV2:
    def print(self, book):
        # Lots of code that handles the printer
        print(f"Printing {book.title} to printer.")


# %%
class BookDatabaseV2:
    def save(self, book):
        # Lots of code that handles the database
        print(f"Saving {book.title} to database.")


# %%
book_v2 = BookV2(
    "Clean Code", "Robert C. Martin", 464, BookPrinterV2(), BookDatabaseV2()
)

# %%
book_v2.print()

# %%
book_v2.save()

# %% [markdown]
#
# ## Vergleich
#
# <div>
# <img src="img/book_resolution_1_srp.svg"
#      style="float:left;padding:5px;width:40%"/>
# <img src="img/book_resolution_2_srp.svg"
#      style="float:right;padding:5px;width:50%"/>
# </div>

# %% [markdown]
#
# ## Workshop: SRP-Verletzung auflösen
#
# - Implementieren Sie die fehlen Funktionalität in Ihrem Bibliothekssystem,
#   falls Sie das noch nicht gemacht haben
# - Untersuchen Sie die Klassen Ihres Bibliothekssystems, ob Sie darin
#   bereits SRP-Verletzungen finden
# - Falls dies der Fall ist, lösen Sie sie auf
