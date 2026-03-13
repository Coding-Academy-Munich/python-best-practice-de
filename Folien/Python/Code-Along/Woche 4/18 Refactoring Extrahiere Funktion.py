# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Refactoring: Extrahiere Funktion</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# ### Extrahiere Funktion
#
# - Invers zu *Inline Function*

# %%
from order_line import OrderLine, make_order_lines


# %%
def print_receipt(order_lines: list[OrderLine]):
    # Print the line items
    for order_line in order_lines:
        print(
            f"{order_line.product:<12} {order_line.quantity:>4} x {order_line.price:6.2f}€"
        )
    # Compute the total
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    # Print the total
    print(f"Total: {total:.2f}€")


# %%
print_receipt(make_order_lines())


# %%
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    return total


# %%
def print_receipt(order_lines):
    for order_line in order_lines:
        print(
            f"{order_line.product:<12} {order_line.quantity:>4} x {order_line.price:6.2f}€"
        )
    total = compute_total(order_lines)  # <-- call new function
    print(f"Total: {total:.2f}€")


# %%
print_receipt(make_order_lines())

# %% [markdown]
# #### Motivation
#
# - Jedes Code-Fragment, das man nicht unmittelbar versteht, sollte in eine
#   Funktion extrahiert werden
# - Name der Funktion spiegelt wieder, **was** die Intention des Codes ist
# - Das kann zu Funktionen führen, die nur eine Zeile Code enthalten
# - Es ist dabei besonders wichtig, dass die Funktionen **gute** Namen haben
# - Kommentare in Funktionen, die sagen, was der nächste Code-Block macht,
#   sind ein Hinweis auf eine mögliche Extraktion


# %% [markdown]
# #### Mechanism
#
# - Create a new function
#   - Name it according to the intention of the code
# - Copy the extracted code into the new function
# - Pass all variables that the function needs as parameters
#   - If previously declared variables are only used in the new function,
#     they can also be declared as local variables in the new function
# - Abort the extraction if the function gets too many parameters
#   - Instead, apply other refactorings that make the extraction easier
#     (Split Variables, Replace Temp with Query, ...)
