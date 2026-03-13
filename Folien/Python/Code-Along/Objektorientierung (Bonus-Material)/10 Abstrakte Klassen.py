# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Abstrakte Klassen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Motivation
#
# - Wir hatten bei einer Aufgabe zur Vererbung die folgende Klassenhierarchie:

# %%
class Employee: ...


# %%
class Manager(Employee): ...


# %%
class Worker(Employee): ...


# %% [markdown]
#
# - `Employee` dient nur dazu das gemeinsame Verhalten von `Manager` und `Worker`
#   zu definieren
# - Es sollten keine Instanzen von `Employee` erzeugt werden können
# - Im Moment ist das aber möglich

# %% [markdown]
#
# ## Abstrakte Klassen
#
# - Klassen, von denen keine direkte Instanz erzeugt werden kann
# - Haben die Klasse `abc.ABC` als Basisklasse
#     - (Eigentlich ist eine Metaklasse verantwortlich für das Verhalten)
# - Erlauben die Verwendung des `@abstractmethod` Decorators um abstrakte Methoden
#   zu definieren
#     - Der Rumpf einer abstrakten Methode ist oft `...`
# - Abstrakte Klassen, die nur abstrakte Methoden haben nennt man Interfaces
#     - Interfaces beschreiben Anforderungen an ihre Unterklassen

# %%

# %% [markdown]
#
# ### Die abstrakte `Employee` Klasse

# %%

# %%
class Employee:
    def salary(self) -> float:
        raise NotImplementedError("This method should be overridden")


# %%

# %%

# %% [markdown]
#
# ### Die `Manager` und `Worker` Klassen

# %%
class Manager(Employee):  # type: ignore
    def __repr__(self):
        return f"Manager()"

    def salary(self) -> float:
        return 100_000.0


# %%

# %%

# %%
class Worker(Employee):  # type: ignore
    def __repr__(self):
        return f"Worker()"

    def salary(self) -> float:
        return 50_000.0


# %%

# %%

# %% [markdown]
#
# ### Die `Company` Klasse
#
# - Wir definieren eine Klasse, die eine Liste von `Employee` Objekten verwaltet

# %%

# %%

# %%

# %% [markdown]
# - Abstrakte Methoden können eine Implementierung haben
# - Klassen, die von einer abstrakten Klasse erben aber nicht alle abstrakten
#   Methoden überschreiben sind selber abstrakt.

# %%
from abc import ABC, abstractmethod

# %%

# %%


# %%


# %%

# %%

# %% [markdown]
#
# ## Workshop: Nochmal Geometrische Formen
#
# In diesem Workshop implementieren Sie Klassen für geometrische Formen unter
# Verwendung von abstrakten Basisklassen (ABCs).
#
# - Erstellen Sie eine Basisklasse `Shape` mit abstrakten Methoden für die
#   Berechnung von Fläche und Umfang.
# - Erstellen Sie konkrete Unterklassen für Rechtecke und Kreise, die von der
#   Klasse `Shape` erben und die abstrakten Methoden implementieren.
# - Testen Sie Ihre Implementierung mit verschiedenen Dimensionen.


# %% [markdown]
#
# ### Hinweise
#
# - Sie können das Modul `math` für den Wert von π verwenden.
# - Die Fläche eines Rechtecks berechnet sich als `width * height`, der Umfang als
#   `2 * (width + height)`.
# - Die Fläche eines Kreises berechnet sich als `π * radius ** 2`, der Umfang als
#   `2 * π * radius`.


# %%

# %% [markdown]
#
# ### Bonusaufgaben:
#
# - Erweitern Sie den Workshop, indem Sie zusätzliche Klassen für geometrische
#   Formen wie `Triangle` erstellen, die von `Shape` erben und ihre jeweiligen
#   Methoden implementieren.
# - Erstellen Sie eine Klasse `Drawing`, die eine Liste von Formen speichert und
#   Methoden zur Berechnung der Gesamtfläche und des Gesamtumfangs aller Formen in
#   der Zeichnung implementiert (unter der Annahme, dass sie sich nicht
#   überschneiden).

# %%

# %% [markdown]
#
# ## Workshop: Bessere Versionen der bisherigen Aufgaben
#
# Wir haben in allen bisherigen Workshops Klassen definiert, von denen es keine
# Instanzen geben sollte. Das konnten wir bisher im Code aber nicht ausdrücken.
#
# Im vorherigen Workshop haben wir das fur die geometrischen Formen explizit
# geändert.
#
# Verbessern Sie die Lösungen der anderen Vererbungs-Workshops ebenfalls, indem
# Sie die Basisklassen als abstrakte Klassen definieren.

