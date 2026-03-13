# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Refactoring: Extrahiere Variable</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# ### Extrahiere Variable

# %%
from order_line import make_order_lines


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    return total


# %%
print(compute_total(make_order_lines()))


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        order_line_price = order_line.quantity * order_line.price  # new variable
        total += order_line_price
    return total


# %%
print(compute_total(make_order_lines()))

# %% [markdown]
# #### Motivation
#
# - Hilft dabei, komplexe Ausdrücke zu verstehen
#   - Erklärende Variablen/Konstanten
# - Debugging oft einfacher

# %% [markdown]
# #### Mechanik
#
# - Stelle sicher, dass der Ausdruck frei von Seiteneffekten ist
# - Erzeuge eine neue Variable
# - Initialisiere sie mit dem Ausdruck
# - Ersetze den Ausdruck durch die Variable
# - Teste das Programm
