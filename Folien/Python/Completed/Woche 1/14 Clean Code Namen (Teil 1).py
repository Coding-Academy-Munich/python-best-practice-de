# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Clean Code: Namen (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Namen
#
# Unterschätze niemals die Macht von Namen!

# %% [markdown]
#
# Namen sind ein mächtiges Kommunikationsmittel.
# - Sie sind überall im Programm zu finden
# - Sie verbinden den Code mit Domänen-Konzepten.


# %%
def foo(a: float, b: float) -> float:
    if b > 40.0:
        raise ValueError("Not allowed!")
    return 40.0 * a + 60.0 * b


# %%
foo(40.0, 3.5)

# %%
REGULAR_PAY_PER_HOUR = 40.0
OVERTIME_PAY_PER_HOUR = 60.0
MAX_ALLOWED_OVERTIME = 40.0


# %%
def compute_total_salary(
    regular_hours_worked: float, overtime_hours_worked: float
) -> float:
    if overtime_hours_worked > MAX_ALLOWED_OVERTIME:
        raise ValueError(
            f"Not allowed to work {overtime_hours_worked:.1f} hours overtime!"
        )
    regular_pay = regular_hours_worked * REGULAR_PAY_PER_HOUR
    overtime_pay = overtime_hours_worked * OVERTIME_PAY_PER_HOUR
    return regular_pay + overtime_pay


# %%
compute_total_salary(40.0, 3.5)

# %%
# compute_total_salary(20.0, 50.0)

# %%
from dataclasses import field, dataclass


# %%
@dataclass
class BadNames:  # type: ignore
    the_list: list

    def get_them(self):
        list1 = []
        for x in self.the_list:
            if x[1] == 1:
                list1.append(x)
        return list1


# %%
thing = BadNames([(i, 0, 0) for i in range(64)])
thing.the_list[2] = (2, 1, 0)
thing.get_them()

# %% [markdown]
#
# <img src="img/minesweeper.png" style="display:block;margin:auto;width:20%">

# %% [markdown]
#
# Siehe
# - `bad_names_01.ipynb` für ein Notebook und
# - `bad_names_01.py` für ein Python-Modul
# zum Refactoring dieses Beispiels.

# %%
UNFLAGGED = 0
FLAGGED = 1

# %%
@dataclass
class MineSweeper:  # type: ignore
    board: list

    def get_flagged_cells(self):
        flagged_cells = []
        for cell in self.board:
            if cell[1] == FLAGGED:
                flagged_cells.append(cell)
        return flagged_cells


# %%
game = MineSweeper([(i, UNFLAGGED, 0) for i in range(64)])
game.board[2] = (2, FLAGGED, 0)
game.get_flagged_cells()


# %%
from enum import IntEnum


# %%
class Status(IntEnum):
    FLAGGED = 1
    UNFLAGGED = 2


# %%
@dataclass
class Cell:
    index: int
    status: Status = Status.UNFLAGGED
    bomb_count: int = 0


# %%
Board = list[Cell]


# %%
def make_board(size=64) -> Board:
    return [Cell(index) for index in range(size)]


# %%
@dataclass
class MineSweeper:
    board: Board = field(default_factory=make_board)

    def get_flagged_cells(self):
        """Return all flagged cells."""
        return [cell for cell in self.board if cell.status == Status.FLAGGED]


# %%
game = MineSweeper()
game.board[2].status = Status.FLAGGED
game.get_flagged_cells()

# %% [markdown]
#
# ## Was ist ein guter Name?
#
# - Ausdrucksstark (nicht notwendigerweise bequem)
# - Präzise (sagt was er meint, meint was er sagt)
# - Beantwortet
#   - Warum gibt es diese Variable (Funktion, Klasse, Modul, Objekt...)?
#   - Was macht sie?
#   - Wie wird sie verwendet?
# - Kommuniziert die Intention (ist "intention revealing")
#
# Gute Namen sind schwer zu finden!


# %% [markdown]
#
# ## Was ist ein schlechter Name?
#
# - Braucht einen Kommentar
# - Kann nur verstanden werden, wenn man sich den Code ansieht
# - Verbreitet Disinformation
# - Entspricht nicht den Namensregeln

# %% [markdown]
#
# ## Workshop: Rezepte
#
# Das folgende Programm enthält Klassen, mit denen sich ein Rezeptbuch verwalten
# lässt. Leider hat der Programmierer sehr schlechte Namen verwendet, dadurch
# ist das Programm schwer zu verstehen.
#
# Ändern Sie die Namen so, dass das Programm leichter verständlich wird.
#
# #### Hinweise
#
# - Verwenden Sie die Refactoring-Tools Ihrer Entwicklungsumgebung
# - Sie können dazu auch die Python-Version des Workshops (im Ordner `Python`)
#   verwenden, falls Ihre Entwicklungsumgebung Notebooks nicht unterstützt.

# %%
from dataclasses import dataclass, field
from typing import Optional


# %%
@dataclass
class One:  # ein Rezept
    aaa: str  # Name
    bbb: list[str]  # Liste der Zutaten
    ccc: str  # Anweisungen
    ddd: Optional[int] = None  # Bewertung


# %%
@dataclass
class Many:
    foo: list[One] = field(default_factory=list)

    def add_thing(self, thing: One):
        self.foo.append(thing)

    def get_thing(self, aaa: str) -> One:
        for thing in self.foo:
            if thing.aaa == aaa:
                return thing
        raise KeyError(f"recipe {aaa} not found!")

    def get_things_1(self, bbb: str) -> list[One]:
        result = []
        for thing in self.foo:
            if bbb in thing.bbb:
                result.append(thing)
        return result

    def get_things_2(self, ddd: int) -> list[One]:
        result = []
        for thing in self.foo:
            if thing.ddd == ddd:
                result.append(thing)
        return result

    def get_things_3(self, ddd: int) -> list[One]:
        result = []
        for thing in self.foo:
            if thing.ddd is None or thing.ddd >= ddd:
                result.append(thing)
        return result


# %%
@dataclass
class Recipe:
    name: str
    ingredients: list[str]
    instructions: str
    rating: Optional[int] = None


# %%
@dataclass
class RecipeBook:
    recipes: list[Recipe] = field(default_factory=list)

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def get_recipe(self, name: str) -> Recipe:
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        raise KeyError(f"Recipe {name} not found!")

    def get_recipes_with_ingredient(self, ingredient: str) -> list[Recipe]:
        result = []
        for recipe in self.recipes:
            if ingredient in recipe.ingredients:
                result.append(recipe)
        return result

    def get_recipes_with_rating(self, rating: int) -> list[Recipe]:
        result = []
        for recipe in self.recipes:
            if recipe.rating == rating:
                result.append(recipe)
        return result

    def get_recipes_with_rating_or_higher(self, rating: int) -> list[Recipe]:
        result = []
        for recipe in self.recipes:
            if recipe.rating is None or recipe.rating >= rating:
                result.append(recipe)
        return result
