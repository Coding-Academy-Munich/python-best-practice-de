# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Clean Code: Namen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Namensregeln für Python
#
# Namen entsprechen den
# [PEP-8 Konventionen](https://peps.python.org/pep-0008/#naming-conventions)


# %% [markdown]
#
# ## Clean Code Namensregeln
#
# Gute Namen
#
# - sind selbsterklärend
# - kommunizieren die Intention
# - sind aussprechbar und durchsuchbar
# - beschreiben das Problem, nicht die Implementierung
# - vermeiden Kodierungen (ungarische Notation) und Füllwörter
# - verwenden die richtige Wortart (lexikalische Kategorie)
# - verwenden die Regeln für Umfang und Länge (Scope-Length Rules)
# - vermeiden Disinformation und benennen eine sinnvolle Unterscheidung

# %% [markdown]
#
# ## Selbsterklärende Namen

# %%
# Elapsed time in days
d = 0

# %%
elapsed_time_in_days = 0

# %% [markdown]
#
# ## Kommuniziere Intention
#
# Namen sollen Absicht, Verhalten, Existenzberechtigung reflektieren

# %%
my_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# %%
dpm_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# %%
_dpm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# %% [markdown]
#
# ## Aussprechbare Namen
#
# Sind oft auch besser zu suchen

# %%
hw_crsr_pxy = [0, 0]

# %%


# %% [markdown]
#
# ## Beschreibe Problem, nicht Implementierung
#
# Vermeide Namen, die sich auf Implementierungsdetails beziehen:
# - Sie verraten nicht, warum der Code so geschrieben wurde, wie er geschrieben
#   ist
# - Aber die Kommunikation der Intention hinter dem Code hat höchste Priorität!

# %%
def add_elements(lst):
    return sum(lst)


# %%
add_elements(days_per_month)  # Seems reasonable


# %%

# %%


# %% [markdown]
#
# ## Vermeide Kodierungen
#
# Verwende keine ungarische Notation:

# %%
i_days = 12
i_month = 3


# %% [markdown]
#
# ## Vermeide Kodierungen
#
# Verwende keine Präfixe für Attribute:

# %%
from dataclasses import dataclass


# %%
@dataclass
class MyClass:
    m_days: int
    m_months: int


# %% [markdown]
#
# ## Vermeide Kodierungen
#
# Vermeiden Sie Präfixe wie C/I: CClass, IInterface

# %%
@dataclass
class CMyClass:
    days: int
    months: int


# %% [markdown]
#
# ## Verwende die richtige lexikalische Kategorie
#
# - Klassen und Variablen: Substantive oder Substantivphrasen
# - Funktionen: Verben oder Verbphrasen
# - Enums: oft Adjektive
# - Boolesche Variablen und Funktionen: oft Prädikate: `ist_...`, `hat_...`

# %%
@dataclass
class GoToTheServer:
    def connection(self):
        ...

    def server_availability(self) -> bool:
        return True

# %%


# %% [markdown]
#
# ## Vermeide Füllwörter
#
# Vermeide Wörter, die keine Bedeutung haben, wie Manager, Processor, Data,
# Info

# %%
class ObjectManager:
    pass


# %% [markdown]
#
# ## Python-Spezifisch
#
# Vermeide Getter/Setter für Zugriff auf Attribute:

# %%
class MyBox:
    def __init__(self, x) -> None:
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, new_value):
        self._x = new_value


# %%
my_box = MyBox(1)
print(my_box.get_x())
my_box.set_x(200)
print(my_box.get_x())


# %%
class YourBox:
    def __init__(self, x) -> None:
        self.x = x


# %%
your_box = YourBox(1)
print(your_box.x)
your_box.x = 200
print(your_box.x)


# %% [markdown]
#
# Mit Properties kann die bestehende Syntax für kontrollierten oder berechneten Zugriff
# auf Attribute beibehalten werden:

# %%
class YourControlledBox:  # type: ignore
    def __init__(self, x) -> None:
        self.x = x


# %%
your_box = YourControlledBox(1)
print(your_box.__dict__)
print(your_box.x)
your_box.x = 200
print(your_box.__dict__)
print(your_box.x)

# %% [markdown]
#
# ## Regeln für Umfang und Länge (Scope-Length Rules)
#
# - Variablen:
#   - Langer Geltungsbereich = langer Name
#   - Kurzer Geltungsbereich = kurzer Name
# - Klassen und Methoden
#   - Langer Geltungsbereich = kurzer Name (wenn häufig verwendet?)
#   - Kurzer Geltungsbereich = langer Name (wenn selten verwendet?)
#
# **Oder:** Verwende lange Namen für lange Geltungsbereiche


# %%
class FixedSizeOrderedCollectionIndexedByInts:
    pass

# %%


# %% [markdown]
# ## Mini-Workshop: Namen
#
# Das folgende Programm verwendet sehr schlechte Namen. Ändern Sie die Namen
# so, dass sie den PEP-8 Konventionen folgen und den Regeln für gute Namen
# folgen.

# %%
from dataclasses import dataclass, field


# %%
# Class representing Line Items:
@dataclass
class LI:
    # number of items
    X: int
    # description of the items
    ChrLst: str
    # price per item
    Y: float

    # compute the total price
    def foo(self):
        return self.X * self.Y


# %%
# Class representing an Order
@dataclass
class LIManager:
    # a list of line items
    LIVec: list[LI] = field(default_factory=list)

    # compute the total price
    def my_result(self):
        return sum(li.foo() for li in self.LIVec)


# %%
# Prepare an order
my_order = LIManager([LI(2, "tea", 0.99), LI(3, "coffee", 0.89)])
print(my_order.my_result())
