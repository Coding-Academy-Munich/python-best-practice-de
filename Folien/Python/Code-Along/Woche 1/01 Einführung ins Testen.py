# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung ins Testen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Warum schreiben wir Tests?

# %% [markdown]
#
# ...

# %% [markdown]
#
# - Vermeidung von Fehlern/Regressionen
# - Vorschriften (ISO 26262, DO-178C, ...)
# - Dokumentation
# - Vorantreiben/Validieren des Designs
# - **Ermöglichen von Refactoring $\Rightarrow$ konstantes Tempo**
# - ...

# %% [markdown]
#
# <img src="img/velocity-tests-01.png"
#      alt="Velocity vs. Tests 1"
#      style="width: 75%; margin-left: auto; margin-right: auto;"/>

# %% [markdown]
#
# <img src="img/velocity-tests-02.png"
#      alt="Velocity vs. Tests 2"
#      style="width: 75%; margin-left: auto; margin-right: auto;"/>

# %% [markdown]
#
# <img src="img/velocity-tests-03.png"
#      alt="Velocity vs. Tests 3"
#      style="width: 75%; margin-left: auto; margin-right: auto;"/>

# %% [markdown]
#
# - Tests sind Code
# - Code ist Kredit, nicht Gespartes!
# - Testen sollten mehr Nutzen bringen als sie kosten


# %% [markdown]
#
# ## Welche Eigenschaften sollte ein Test haben?
#
# - Zeigt Fehler/Regressionen im Code auf
# - Gibt schnelle Rückmeldung
# - Ist leicht zu warten
# - **Unempfindlich gegenüber Refactorings**
#
# Leider stehen diese Eigenschaften oft im Konflikt zueinander!

# %% [markdown]
#
# ## Aufzeigen von Fehlern/Regressionen
#
# Möglichst wenige falsche Negative!
#
# ### Einflüsse
#
# - Menge des abgedeckten Codes
# - Komplexität des abgedeckten Codes
# - Signifikanz des abgedeckten Codes für die Domäne/das System

# %%
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.price})"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Item):
            return False
        return self.name == __value.name and self.price == __value.price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            value = -value
        self._price = value


# %%
class Order:
    def __init__(self, *items):
        self._items = [Item(name, price) for (name, price) in items]

    def __repr__(self) -> str:
        return f"Order({self.items})"

    @property
    def items(self):
        return [(item.name, item.price) for item in self._items]

    @property
    def total(self):
        return sum(item.price for item in self._items)


# %%
def test_item_name():
    item = Item("Apple", 1.0)
    assert item.name == "Apple"

# %%

# %%

# %%


# %% [markdown]
#
# ## Schnelle Rückmeldung
#
# - Menge des abgedeckten Codes
# - Komplexität/Iteration des abgedeckten Codes
# - Interaktion mit externen Systemen

# %% [markdown]
#
# ## Leicht zu warten
#
# - Einfache, standardisierte Struktur
# - Wenig Code
#   - Boilerplate
#   - Testcode

# %% [markdown]
#
# ## Unempfindlich gegenüber Refactorings
#
# - Möglichst wenige falsche Positive!
# - Typischerweise vorhanden oder nicht, wenig Zwischenstufen
#
# ### Einflüsse
#
# - Bezug zu Domäne/System
# - Zugriff auf interne Strukturen

# %%
source = '    def __repr__(self) -> str:\n        return f"Order({self.items})"\n'

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# Die folgenden Einflüsse stehen im Konflikt zueinander:
#
# - Unempfindlich gegenüber Refactorings
# - Erkennen von Fehlern/Regressionen
# - Schnelle Rückmeldung
#
# Die Qualität eines Tests hängt vom *Produkt* dieser Faktoren ab!

# %% [markdown]
#
# ## Wie finden wir den Trade-Off?
#
# - Unempfindlich gegenüber Refactorings kann *nie* geopfert werden
# - Wir müssen also einen Kompromiss finden zwischen
#   - Erkennen von Fehlern/Regressionen
#   - Schnelle Rückmeldung
#
# ### Typischerweise
#
# - Schnelles Feedback für die meisten Tests (Unit-Tests)
# - Gründliche Fehlererkennung für wenige Tests (Integrationstests)
