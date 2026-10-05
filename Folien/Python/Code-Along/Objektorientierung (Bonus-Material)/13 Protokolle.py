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

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop: Protokolle
#
# Implementieren Sie ein zur Laufzeit überprüfbares Protokoll `SupportsConnect`,
# das Instanzen von Klassen beschreibt, die eine Methode `connect(self, device)`
# haben.

# %%

# %%

# %% [markdown]
#
# Implementieren Sie Klassen `Plugboard` und `PatchCord`, die das
# `SupportsConnect` Protokoll unterstützen.

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# - Erfüllt die folgende Klasse das Protokoll `SupportsConnect`?
# - Lässt sich das zur Laufzeit feststellen?

# %%
class SelfConnector:
    def connect(self):  # noqa
        print("Connecting to self!")

# %%
