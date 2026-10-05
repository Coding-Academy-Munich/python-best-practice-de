# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Protokolle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>
#
#

# %% [markdown]
#
# # Protokolle
#
# Durch Protokolle unterstützt Python strukturelles Subtyping, bei dem
# Subtyp-Beziehungen aus der Struktur der Klassen erschlossen werden (im Gegensatz zum
# nominalen Subtyping, bei dem die Beziehungen explizit deklariert werden müssen).

# %%
from typing import Protocol, runtime_checkable, SupportsInt


# %%
class MyNumber:
    def __int__(self):
        return 0


# %%
my_number = MyNumber()
int(my_number)

# %%
isinstance(MyNumber, SupportsInt)


# %%
@runtime_checkable
class SupportsCastSpell(Protocol):
    def cast_spell(self, name):
        ...


# %%
@runtime_checkable
class SupportsHit(Protocol):
    def hit(self, who, how):
        ...


# %%
class Mage:
    def __init__(self, name="The Mage"):
        self.name = name

    def cast_spell(self, spell):
        print(f"{self.name} casts a {spell} spell.")


# %%
class Fighter:
    @property
    def name(self):
        return "The Fighter"

    def hit(self, opponent, weapon):
        print(f"{self.name} attacks {opponent} with {weapon}.")


# %%
class Bard:
    def __init__(self, name="The Bard"):
        self.name = name


# %%
p1 = Mage()
p2 = Fighter()
p3 = Bard()

# %%
issubclass(Mage, SupportsCastSpell)

# %%
issubclass(Fighter, SupportsCastSpell)

# %%
isinstance(p1, SupportsCastSpell)

# %%
isinstance(p2, SupportsCastSpell)

# %%
isinstance(p3, SupportsCastSpell)

# %%
isinstance(p1, SupportsHit)

# %%
isinstance(p2, SupportsHit)

# %%
isinstance(p3, SupportsHit)


# %%
@runtime_checkable
class HasName(Protocol):
    @property
    def name(self):  # noqa
        ...


# %%
isinstance(p1, HasName)

# %%
isinstance(p2, HasName)

# %%
isinstance(p3, HasName)

# %% [markdown]
#
# ## Workshop: Protokolle
#
# Implementieren Sie ein zur Laufzeit überprüfbares Protokoll `SupportsConnect`,
# das Instanzen von Klassen beschreibt, die eine Methode `connect(self, device)`
# haben.

# %%
from typing import Protocol, runtime_checkable


# %%
@runtime_checkable
class SupportsConnect(Protocol):
    def connect(self, device):
        ...


# %% [markdown]
#
# Implementieren Sie Klassen `Plugboard` und `PatchCord`, die das
# `SupportsConnect` Protokoll unterstützen.

# %%
class Plugboard:
    def connect(self, device):  # noqa
        print("Connecting plugboard to device.")


# %%
assert issubclass(Plugboard, SupportsConnect)

# %%
assert isinstance(Plugboard(), SupportsConnect)


# %%
class PatchCord:
    def connect(self, device):  # noqa
        print("Connecting patch cord to device.")


# %%
assert issubclass(PatchCord, SupportsConnect)

# %%
assert isinstance(PatchCord(), SupportsConnect)


# %% [markdown]
#
# - Erfüllt die folgende Klasse das Protokoll `SupportsConnect`?
# - Lässt sich das zur Laufzeit feststellen?

# %%
class SelfConnector:
    def connect(self):  # noqa
        print("Connecting to self!")


# %%
assert issubclass(SelfConnector, SupportsConnect)
