# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Refactoring: Inline Function</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# ### Inline Function
#
# - Invers zu *Extrahiere Funktion*

# %%
from order_line import OrderLine, make_order_lines


# %%
def order_line_price(order_line: OrderLine):
    return order_line.price


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line_price(order_line)
    return total


# %%
print(compute_total(make_order_lines()))


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price  # <-- inline function
    return total


# %%
print(compute_total(make_order_lines()))

# %% [markdown]
# #### Motivation
#
# - Manchmal ist eine Funktion nicht leichter zu verstehen als ihr Codeblock
# - Manchmal sind die von einer Funktion verwendeten Hilfsfunktionen nicht gut
#   strukturiert
# - Generell: Potenziell anwendbar, wenn man aufgrund zu vieler Indirektionen den
#   Überblick verliert

# %% [markdown]
# #### Mechanik
#
# - Stelle sicher, dass die Funktion keiner objektorientierten Polymorphie
#   unterliegt, wie dies bei virtuellen Funktionen in C++ der Fall ist.
#   - In Python gibt es keine expliziten virtuellen Funktionen, aber die Funktion
#     sollte nicht in einer Weise überschrieben werden, die die Semantik des
#     Programms bei einer Entfernung ändern würde.
# - Finde alle Aufrufe der Funktion.
# - Ersetze jeden Aufruf durch den Codeblock der Funktion.
# - Teste nach jedem Schritt!
# - Entferne die Funktionsdefinition.
# - Brich ab, falls Schwierigkeiten wegen Rekursion, mehreren `return`-Anweisungen,
#   etc. auftreten.
