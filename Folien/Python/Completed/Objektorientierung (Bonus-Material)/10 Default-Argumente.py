# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Default-Argumente</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Default-Argumente
#
# Funktionsparameter können einen Default-Wert haben.
# - Der Default-Wert wird mit der Syntax `parameter=wert` angegeben
# - Wird das entsprechende Argument nicht übergeben so wird der Default-Wert eingesetzt
# - Hat ein Parameter einen Default-Wert, so müssen alle rechts davon stehenden
#   Werte ebenfalls einen haben

# %%
def say_hi(greeting, name="world", end="."):
    print(greeting + " " + name + end)


# %%
say_hi("Hello")
say_hi("Hi", "Joe")
say_hi("What's up", "Jane", "?")


# %% [markdown]
# ## Vorsicht mit veränderlichen Default-Argumenten

# %%
def append_value(value, my_list=[]):
    my_list.append(value)
    return my_list

# %%
my_list = []

# %%
append_value(1, my_list)

# %%
append_value(2, my_list)

# %%
append_value(1)

# %%
append_value(2)


# %% [markdown]
#
# Lösung: verwende `Null` als Argument, erzeuge in jedem Aufruf eine neue Liste

# %%
def append_value(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# %%
append_value(1)

# %%
append_value(2)
