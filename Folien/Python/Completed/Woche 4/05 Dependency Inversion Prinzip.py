# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Dependency Inversion Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Abhängigkeiten
#
# - Wir müssen zwei Arten von Abhängigkeiten unterscheiden:
#   - Daten- und Kontrollfluss
#   - Quellcode-Abhängigkeiten
# - Daten- und Kontrollfluss-Abhängigkeiten sind inhärent in der Logik
# - Quellcode-Abhängigkeiten können wir durch die Architektur kontrollieren

# %% [markdown]
#
# ## Beispiel
#
# - Modul `my_module.py` schreibt Daten in eine Datenbank
# - Datenfluss: von `my_module.py` zur Datenbank
# - Quellcode-Abhängigkeit: `my_module.py` hängt von der Datenbank (`sqlite3`) ab

# %% [markdown]
#
# Modul `my_module.py`:

# %%
import sqlite3  # Quellcode-Abhängigkeit


# %%
class MyDomainClassV1:
    def __init__(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE my_table (data text)")
        conn.commit()
        self.conn = conn

    def perform_work(self, data: str):
        data = "Processed: " + data
        self.conn.execute("INSERT INTO my_table VALUES (?)", (data,))
        self.conn.commit()

    def retrieve_result(self):
        cur = self.conn.execute("SELECT * FROM my_table")
        return cur.fetchall()


# %% [markdown]
#
# Modul `main.py`:

# %%
# from my_module import MyDomainClassV1

my_domain_object = MyDomainClassV1()
my_domain_object.perform_work("Hello World")
print(my_domain_object.retrieve_result())

# %% [markdown]
#
# Die Quellcode-Abhängigkeit geht in die gleiche Richtung wie der Datenfluss:
#
# `my_module.py` ⟹ `sqlite3`
#
# <img src="img/dependency-01.svg"
#      style="display:block;margin:auto;width:75%"/>


# %% [markdown]
#
# Wir würden derartige Abhängigkeiten im Kern unsere Anwendung gerne vermeiden
#
# - Einfacher zu testen
# - Einfacher zu erweitern
# - Einfacher externe Abhängigkeiten zu ersetzen
# - Einfacher den Code zu verstehen
# - ...

# %% [markdown]
#
# <img src="img/dependency-02.svg"
#      style="display:block;margin:auto;width:75%"/>

# %% [markdown]
#
# - Modul `my_module.py`:
#   - Keine Abhängigkeit mehr zu `sqlite3`
#   - Kombination aus Adapter und Strategy Pattern

# %%
from abc import ABC, abstractmethod


# %%
class DatabaseAdapter(ABC):
    @abstractmethod
    def save_object(self, data: str):
        ...

    @abstractmethod
    def retrieve_data(self):
        ...


# %%
class MyDomainClassV2:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    def perform_work(self, data: str):
        data = "Processed: " + data
        self.db.save_object(data)

    def retrieve_result(self):
        return self.db.retrieve_data()


# %% [markdown]
#
# - Modul `sqlite_adapter.py`:
#   - Implementiert `DatabaseAdapter` für `sqlite3`
#   - Hängt von `sqlite3` ab

# %%
import sqlite3


# %%
class SqliteAdapter(DatabaseAdapter):
    def __init__(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE my_table (data text)")
        conn.commit()
        self.conn = conn

    def save_object(self, data: str):
        self.conn.execute("INSERT INTO my_table VALUES (?)", (data,))
        self.conn.commit()

    def retrieve_data(self):
        cur = self.conn.execute("SELECT * FROM my_table")
        return cur.fetchall()


# %% [markdown]
#
# - Modul `main.py`:

# %%
# from my_module import MyDomainClassV2
# from sqlite_adapter import SqliteAdapter


# %%
my_domain_object = MyDomainClassV2(SqliteAdapter())
my_domain_object.perform_work("Hello World")
print(my_domain_object.retrieve_result())

# %% [markdown]
#
# # SOLID: Dependency Inversion Prinzip
#
# - Die Kernfunktionalität eines Systems hängt nicht von seiner Umgebung ab
#   - **Konkrete Artefakte hängen von Abstraktionen ab** (nicht umgekehrt)
#   - **Instabile Artefakte hängen von stabilen Artefakten ab** (nicht umgekehrt)
#   - **Äußere Schichten** der Architektur **hängen von inneren Schichten ab**
#     (nicht umgekehrt)
#   - Klassen/Module hängen von Abstraktionen (z. B. Schnittstellen) ab,
#     nicht von anderen Klassen/Modulen
# - Abhängigkeitsinversion (Dependency Inversion) erreicht dies durch die Einführung
#   von Schnittstellen, die "die Abhängigkeiten umkehren"

# %% [markdown]
#
# ### Vorher
# <img src="img/dependency-01.svg"
#      style="display:block;margin:auto;width:75%"/>
#
# ### Nachher
# <img src="img/dependency-02.svg"
#      style="display:block;margin:auto;width:75%"/>

# %% [markdown]
#
# <img src="img/dip-01.svg"
#      style="display:block;margin:auto;width:95%"/>

# %% [markdown]
#
# <img src="img/dip-02.svg"
#      style="display:block;margin:auto;width:95%"/>

# %% [markdown]
#
# <img src="img/dip-03.svg"
#      style="display:block;margin:auto;width:95%"/>

# %% [markdown]
#
# ## Beispiel

# %%
from dataclasses import dataclass
from pprint import pprint

# %%
from augurdb import AugurDatabase


# %%
@dataclass
class BadEmployee:
    id: int
    name: str
    database: AugurDatabase

    def save(self):
        self.database.start_transaction()
        self.database.store_field(self.id, "name", self.name)
        self.database.commit_transaction()


# %%
db = AugurDatabase()
be = BadEmployee(123, "Joe", db)

# %%
be.save()

# %%
pprint(db.records)

# %% [markdown]
#
# - Einführen eines Interfaces

# %%
from abc import ABC, abstractmethod


# %%
# module employee
class DatabaseAdapter(ABC):
    @abstractmethod
    def save(self, e: "BetterEmployee"):
        ...


# %% [markdown]
#
# - Verwenden des Interfaces

# %%
# module employee
@dataclass
class BetterEmployee:
    id: int
    name: str
    database: DatabaseAdapter

    def save(self):
        self.database.save(self)


# %% [markdown]
#
# - Konkrete Implementierung des Interfaces

# %%
from dataclasses import dataclass, field


# %%
# module db
@dataclass
class AugurDatabaseAdapter(DatabaseAdapter):
    database: AugurDatabase = field(default_factory=AugurDatabase)

    def save(self, e: "BetterEmployee"):
        self.database.start_transaction()
        self.database.store_field(e.id, "name", e.name)
        self.database.commit_transaction()


# %%
db = AugurDatabaseAdapter()
be = BetterEmployee(123, "Joe", db)

# %%
be.save()

# %%
pprint(db.database.records)


# %% [markdown]
#
# ## Workshop: Wetterbericht
#
# In einem Programm wird ein Wetterbericht von einem Server abgerufen. Leider ist
# dabei die Abhängigkeit zum Server hart kodiert.
#
# - Führen Sie eine Abstraktion ein, um die Abhängigkeit umzukehren
# - Schreiben Sie eine konkrete Implementierung der Abstraktion
# - Testen Sie die Implementierung

# %%
from dataclasses import dataclass


# %%
@dataclass
class WeatherReport:
    temperature: float
    humidity: float


# %%
@dataclass
class WeatherServer:
    def get_weather_report(self) -> WeatherReport:
        from random import random

        return WeatherReport(20 + 10 * random(), 0.5 + 0.5 * random())


# %%
class WeatherReporter:
    def __init__(self, server: WeatherServer):
        self.server: WeatherServer = server

    def report(self):
        report = self.server.get_weather_report()
        if report.temperature > 25:
            return "It's hot"
        else:
            return "It's not hot"


# %%
reporter = WeatherReporter(WeatherServer())

# %%
reporter.report()


# %%
from abc import ABC, abstractmethod


# %%
class WeatherDataSource(ABC):
    @abstractmethod
    def get_weather_report(self) -> WeatherReport:
        ...


# %%
class DiWeatherReporter:
    def __init__(self, data_source: WeatherDataSource):
        self.data_source: WeatherDataSource = data_source

    def report(self):
        report = self.data_source.get_weather_report()
        if report.temperature > 25:
            return "It's hot"
        else:
            return "It's not hot"


# %%
class WeatherServerAdapter(WeatherDataSource):
    def __init__(self, server: WeatherServer):
        self.server: WeatherServer = server

    def get_weather_report(self) -> WeatherReport:
        return self.server.get_weather_report()


# %%
reporter = DiWeatherReporter(WeatherServerAdapter(WeatherServer()))

# %%
reporter.report()
