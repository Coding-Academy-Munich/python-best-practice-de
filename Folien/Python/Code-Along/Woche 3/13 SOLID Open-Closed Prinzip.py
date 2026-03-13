# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>SOLID: Open-Closed Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Open-Closed Prinzip (SOLID)
#
# Klassen sollen
#
# - offen für Erweiterung
# - geschlossen für Modifikation
#
# sein.

# %%
from enum import Enum


# %%
class MovieKindV0(Enum):
    REGULAR = 1
    CHILDREN = 2


# %%
class MovieV0:
    def __init__(self, title: str, kind=MovieKindV0.REGULAR):
        self.title = title
        self.kind = kind

    def compute_price(self) -> float:
        match self.kind:
            case MovieKindV0.REGULAR:
                return 4.99
            case MovieKindV0.CHILDREN:
                return 5.99
            case _:
                return 0.0

    def print_info(self):
        print(f"{self.title} costs {self.compute_price()}")


# %%
m1 = MovieV0("Casablanca")
m2 = MovieV0("Shrek", MovieKindV0.CHILDREN)


# %%
m1.print_info()
m2.print_info()

# %% [markdown]
#
# <img src="img/movie_v0.svg" alt="MovieV0"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown]
#
# Was passiert, wenn wir eine neue Filmart hinzufügen wollen?

# %%
from enum import Enum


# %%
class MovieKind(Enum):
    REGULAR = 1
    CHILDREN = 2


# %%
class MovieV1:
    def __init__(self, title: str, kind=MovieKind.REGULAR):
        self.title = title
        self.kind = kind

    def compute_price(self) -> float:
        match self.kind:
            case MovieKindV0.REGULAR:
                return 4.99
            case MovieKindV0.CHILDREN:
                return 5.99
            case _:
                return 0.0

    def print_info(self) -> None:
        print(f"{self.title} costs {self.compute_price()}")


# %%
m1 = MovieV1("Casablanca")
m2 = MovieV1("Shrek", MovieKind.CHILDREN)
m3 = MovieV1("Brand New", MovieKind.NEW_RELEASE)

# %%
m1.print_info()
m2.print_info()
m3.print_info()

# %% [markdown]
#
# <img src="img/movie_v1.svg" alt="MovieV1"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown]
#
# ## OCP-Verletzung
#
# - Neue Filmarten erfordern Änderungen an `MovieV1`
# - `MovieV1` ist nicht geschlossen für Modifikation

# %% [markdown]
#
# ## Auflösung (Versuch 1: Vererbung)
#
# - Neue Filmarten werden als neue Klassen implementiert
# - `MovieV2` wird abstrakt
# - `MovieV2` ist geschlossen für Modifikation

# %%
from abc import ABC, abstractmethod


# %%
class MovieV2(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def compute_price(self) -> float: ...

    def print_info(self) -> None:
        print(f"{self.title} costs {self.compute_price()}")


# %%
class RegularMovie(MovieV2):
    def compute_price(self) -> float:
        return 4.99


# %%
class ChildrenMovie(MovieV2):
    def compute_price(self) -> float:
        return 5.99


# %%
class NewReleaseMovie(MovieV2):
    def compute_price(self) -> float:
        return 6.99


# %%

# %%

# %%


# %% [markdown]
#
# <img src="img/movie_v2.svg" alt="MovieV0"
#      style="display:block;margin:auto;width:100%"/>


# %% [markdown]
#
# - `MovieV2` ist offen für Erweiterung
# - Neue Filmarten können hinzugefügt werden, ohne die bestehenden Klassen zu
#   ändern
# - Aber: Die Vererbungshierarchie umfasst die ganze Klasse
#   - Nur eine Art von Variabilität
# - Was ist, wenn wir für andere Zwecke eine andere Klassifikation brauchen?
#   - Z.B. DVD, BluRay, Online?
# - Mehrfachvererbung?
# - Produkt von Klassen?
#   - `ChildrenDVD`, `ChildrenBluRay`, `ChildrenOnline`, ...

# %% [markdown]
#
# ## Bessere Auflösung: Strategy Pattern
#
# - Das Strategy-Pattern erlaubt es uns, die Vererbung auf kleinere Teile der
#   Klasse anzuwenden
# - In fast allen Fällen ist das die bessere Lösung!
# - Vererbung ist ein sehr mächtiges Werkzeug
# - Aber je kleiner und lokaler wir unsere Vererbungshierarchien halten, desto
#   besser


# %% [markdown]
#
# ## Workshop: Zoo-Management-System
#
# In diesem Workshop werden wir mit einem hypothetischen Szenario arbeiten, das
# ein Zoo-Management-System für die Fütterungspläne der Tiere betrifft. Die
# Herausforderung? Das vorhandene System verstößt gegen das OCP, und es liegt
# an uns, das zu korrigieren.

# %% [markdown]
#
# ### Szenario
#
# Stellen Sie sich einen Zoo vor. Dieser Zoo hat eine Vielzahl von Tieren:
# Säugetiere, Vögel, Reptilien und Wasserlebewesen. Jede Art von Tier hat ihren
# eigenen einzigartigen Fütterungsplan und ihre eigenen Ernährungsbedürfnisse.
#
# Nun muss das digitale System des Zoos diese Fütterungspläne verfolgen. Das
# Problem mit dem aktuellen System ist seine Verwendung einer Enumeration, um
# den Tier-Typ und basierend darauf seinen Fütterungsplan zu bestimmen. Dieser
# Ansatz ist nicht skalierbar und verstößt gegen das OCP. Was passiert, wenn der
# Zoo eine neue Tierart erwirbt? Oder was ist, wenn sich der Fütterungsplan für
# Reptilien ändert? Die aktuelle Code-Struktur erfordert Änderungen an mehreren
# Stellen.

# %%
from enum import Enum, auto


# %%
class AnimalType(Enum):
    Mammal = auto()
    Bird = auto()
    Reptile = auto()
    Aquatic = auto()


# %%
class AnimalV0:
    def __init__(self, animal_type):
        self._type = animal_type

    @property
    def feeding_schedule(self) -> str:
        if self._type == AnimalType.Mammal:
            return "Feed at 9am and 5pm."
        elif self._type == AnimalType.Bird:
            return "Feed at 8am and 4pm."
        elif self._type == AnimalType.Reptile:
            return "Feed at 12pm."
        elif self._type == AnimalType.Aquatic:
            return "Feed at 11am and 6pm."
        else:
            return f"No feeding schedule for {self._type}!"

    @property
    def diet(self) -> str:
        if self._type == AnimalType.Mammal:
            return "Diet: Grass and fruits."
        elif self._type == AnimalType.Bird:
            return "Diet: Seeds and insects."
        elif self._type == AnimalType.Reptile:
            return "Diet: Insects."
        elif self._type == AnimalType.Aquatic:
            return "Diet: Algae and small fish."
        else:
            return f"No diet for {self._type}!"


# %%
animals_original = [
    AnimalV0(AnimalType.Mammal),
    AnimalV0(AnimalType.Bird),
    AnimalV0(AnimalType.Reptile),
]


# %%
def display_feeding_info(animals):
    for animal in animals:
        print(f"{animal.feeding_schedule} {animal.diet}")


# %%
display_feeding_info(animals_original)

# %% [markdown]
#
# - Beseitigen Sie das Problem mit der OCP-Verletzung im vorhandenen Code
# - Sie können entweder den vorhandenen Code ändern oder eine neue Lösung von
#   Grund auf erstellen
