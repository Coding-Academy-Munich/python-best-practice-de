# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Clean Code: Namen (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Disinformation und sinnvolle Unterscheidungen
#
# - Namen bedeuten etwas
# - Disinformation:
#   - Die Bedeutung des Namens impliziert etwas anderes als der Programmcode:


# %%
verify_configuration = False

# %%
if verify_configuration:
    print("Deleting configuration files...")

# %%
from typing import NamedTuple


# %%
class Pair(NamedTuple):
    first: int
    second: int
    third: int


# %%
class Triple(NamedTuple):
    first: int
    second: int
    third: int


# %% [markdown]
#
# ## Regeln zur Vermeidung von Disinformation
#
# - Nimm keinen Typ in einen Variablennamen auf, wenn die Variable nicht von
#   diesem Typ ist
#   - Meistens: Gib überhaupt keinen Typ in einem Variablennamen an

# %%
vector_of_cards: int = 0

# %%
num_cards = 0

# %%
card_deck: list = [...]

# %% [markdown]
#
# ## Regeln zur Vermeidung von Disinformation
#
# - Sei vorsichtig mit Namen, die sich nur geringfügig unterscheiden

# %%
is_melee_defence_available = True
is_melee_defense_available = False

# %%
print(is_melee_defence_available == is_melee_defense_available)  # Oops...

# %% [markdown]
#
# ## Regeln zur Vermeidung von Disinformation
#
# - Benutze Namen, die etwas bedeuten

# %%
foobar = 0
bar = 1

# %%
number_of_visitors = 0
days_till_release = 1

# %% [markdown]
#
# ## Regeln zur Vermeidung von Disinformation
#
# - Sei bei der Namensgebung konsistent

# %%
number_of_objects = 10
num_buyers = 12
n_transactions = 2

# %%
num_objects = 10
num_buyers = 12
num_transactions = 2

# %%
n_objects = 10
n_buyers = 12
n_transactions = 2

# %% [markdown]
#
# ## Sinnvolle Unterscheidungen
#
# - Verwende Namen, die die Bedeutung der Konzepte so klar wie möglich ausdrücken


# %%
a1 = "Fluffy"
a2 = "Garfield"

# %%
my_dog = "Fluffy"
jons_cat = "Garfield"

# %%
INCLUDE_NONE = 0
INCLUDE_FIRST = 1
INCLUDE_SECOND = 2
INCLUDE_BOTH = 3

# %%
INCLUDE_NO_DATE = 0
INCLUDE_START_DATE = 1
INCLUDE_END_DATE = 2
INCLUDE_START_AND_END_DATE = 3

# %%
from enum import IntEnum


# %%
class DatesToInclude(IntEnum):
    NONE = 0
    START = 1
    END = 2
    START_AND_END = 3


# %% [markdown]
#
# ## Sinnvolle Unterscheidungen
#
# - Verwende denselben Namen für dasselbe Konzept


# %%
from pathlib import Path

# %%
my_path = Path.home()
your_dir = Path.home()
file_loc = Path.home()

# %%
my_path = Path.home()
your_path = Path.home()
file_path = Path.home()

# %%
my_dir = Path.home()
your_dir = Path.home()
file_dir = Path.home()

# %% [markdown]
#
# ## Workshop: Namen in existierendem Code
#
# - Analysieren Sie ein Programm, an dem Sie arbeiten ob die Namen gut sind
# - Verbessern Sie die Namen, falls das möglich ist
#   - Achten Sie aber darauf, dass Sie nicht gegen die Coding-Standards
#     des Projekts verstoßen
# - Verbessert sich die Lesbarkeit des Codes?
# - Diskutieren Sie Ihre Ergebnisse mit Ihren Kollegen
