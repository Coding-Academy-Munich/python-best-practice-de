# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Refactoring: Inline Variable</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# ### Inline Variable

# %%
from order_line import make_order_lines


# %%
def order_line_price(order_line):
    return order_line.quantity * order_line.price


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        price = order_line_price(order_line)
        total += price
    return total


# %%
print(compute_total(make_order_lines()))


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line_price(order_line)  # <-- inline variable
    return total


# %%
print(compute_total(make_order_lines()))

# %% [markdown]
# #### Motivation
#
# - Manchmal kommuniziert der Name der Variable nicht mehr als der Ausdruck selbst
# - Manchmal verhindert eine Variable das Refactoring von anderem Code

# %% [markdown]
# #### Mechanik
#
# - Stelle sicher, dass der Initialisierungs-Ausdruck frei von Seiteneffekten ist
# - Falls die Variable nicht schon konstant ist, mache sie konstant und teste
#   das Programm
# - Finde die erste Referenz auf die Variable
# - Ersetze die Variable durch ihren Initialisierungs-Ausdruck
# - Teste das Programm
# - Wiederhole für jede Referenz auf die Variable
