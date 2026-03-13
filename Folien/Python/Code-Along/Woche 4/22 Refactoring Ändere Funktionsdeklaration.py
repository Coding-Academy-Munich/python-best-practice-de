# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Refactoring: Ändere Funktionsdeklaration</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# ### Ändere Funktionsdeklaration
#
# Auch bekannt als:
# - Benenne Funktion um
# - Ändere Signatur
# - Benenne Methode um
# - Füge Parameter hinzu
# - Entferne Parameter

# %%
from order_line import make_order_lines


# %%
def ttl(discount: bool, order_lines: list) -> float:
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    if discount:
        total *= 0.9
    return total


# %%
print(ttl(False, make_order_lines()))
print(ttl(True, make_order_lines()))


# %%
def compute_total(order_lines: list, discount: bool = False) -> float:
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    if discount:
        total *= 0.9
    return total


# %%
print(compute_total(make_order_lines(), False))
print(compute_total(make_order_lines(), True))

# %% [markdown]
# #### Motivation
#
# - Der Name der Funktion spiegelt nicht mehr ihre Intention wieder
# - Die Signatur der Funktion ist nicht mehr passend
#   - inkonsistente Parameterreihenfolge zwischen ähnlichen Funktionen
#   - zu viele Parameter
#   - "falsche" Parametertypen

# %% [markdown]
# #### Einfache Mechanik
#
# - Beim Entfernen von Parametern: Stelle sicher, dass der Parameter nicht
#   im Rumpf verwendet wird
# - Ändere die Deklaration/Definition der Funktion
# - Ändere alle Aufrufe der Funktion
# - Teste das Programm

# %% [markdown]
# #### Migrations-Mechanik
#
# - If necessary, refactor the body of the function to facilitate the following steps
# - Use *Extract Function* to extract the body of the function into a new function
# - If the extracted function requires additional parameters, use the simple
#   mechanics to add them
# - Test the program
# - Use *Inline Function* for the old function
# - Test the program
# - If the new function has a temporary name, use *Change Function Declaration*
#   to change its name
# - Test the program

# %% [markdown]
# - Mit der Migrations-Mechanik können wir auch ein veröffentlichtes Interface
#   ändern
# - Dazu entfernen wir das alte Interface nach dem Inlining nicht, sondern
#   markieren es als veraltet
# - In einem späteren Schritt können wir das alte Interface entfernen
