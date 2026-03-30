# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Observer (Publish/Subscribe)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ### Beispiel: Aktienkurse
#
# - Aktienkurse ändern sich ständig
# - Viele verschiedene Clients wollen über Änderungen informiert werden
# - Clients sollen unabhängig voneinander sein
# - Die Anwendung soll nicht über konkrete Clients Bescheid wissen

# %%
from dataclasses import dataclass, field


# %%
@dataclass
class Stock:
    name: str
    price: float


# %%
@dataclass
class StockMarket:
    _stocks: list[Stock] = field(default_factory=list)
    _old_prices: dict[str, float] = field(default_factory=dict)

    def add_stock(self, stock: Stock):
        self._stocks.append(stock)
        self._print_stock(stock)
        self._print_rising_stock(stock)

    def update_stock_price(self, name: str, new_price: float):
        for stock in self._stocks:
            if stock.name == name:
                stock.price = new_price
                self._print_stock(stock)
                self._print_rising_stock(stock)
                return
        raise ValueError(f"Stock {name!r} not found")

    def _print_stock(self, stock: Stock):
        print(f"  {stock.name}: {stock.price:.2f}")

    def _print_rising_stock(self, stock: Stock):
        old_price = self._old_prices.get(stock.name, float("-inf"))
        if stock.price > old_price:
            print(f"  RISING: {stock.name}: {old_price:.2f} -> {stock.price:.2f}")
        self._old_prices[stock.name] = stock.price


# %%
market = StockMarket()

# %%
market.add_stock(Stock("Banana", 100.0))

# %%
market.add_stock(Stock("Billionz", 200.0))

# %%
market.add_stock(Stock("Macrosoft", 300.0))

# %%
market.update_stock_price("Banana", 105.0)

# %%
market.update_stock_price("Billionz", 190.0)

# %%
market.update_stock_price("Macrosoft", 310.0)

# %% [markdown]
#
# ### Konsequenzen
#
# - Die Lösung implementiert die Grundanforderungen
# - Änderung des Ausgabeformats nur durch Änderung des `StockMarket`
# - Keine einfache Möglichkeit, Clients hinzuzufügen oder zu entfernen

# %% [markdown]
#
# ### Probleme
#
# - Verletzung des Single Responsibility Principle
# - Verletzung des Open-Closed-Prinzips
# - Hohe Kopplung (an alle Clients)

# %% [markdown]
# ## Observer (Verhaltensmuster)
#
# ### Zweck
#
# - 1:n-Beziehung zwischen Objekten
# - Automatische Benachrichtigung aller abhängigen Objekte bei Zustandsänderung
#
# ### Auch bekannt als
#
# - Publish/Subscribe (Pub/Sub)
# - Event-Listener

# %% [markdown]
#
# ### Klassendiagramm: Aktienkurse mit Observer
#
# <img src="img/stock_example.png"
#      style="display:block;margin:auto;width:90%"/>

# %% [markdown]
#
# ## Implementierung: Push Observer
#
# - Der Publisher "pusht" die relevanten Daten an die Subscriber
# - Subscriber erhalten die Daten als Parameter in der `update()`-Methode
# - Einfache Abhängigkeitsstruktur: Daten fließen in eine Richtung

# %%
from abc import ABC, abstractmethod


# %%
class StockObserver(ABC):
    @abstractmethod
    def update(self, stock: Stock): ...


# %%
@dataclass
class StockMarket:
    _stocks: list[Stock] = field(default_factory=list)
    _old_prices: dict[str, float] = field(default_factory=dict)

    def add_stock(self, stock: Stock):
        self._stocks.append(stock)
        self._print_stock(stock)
        self._print_rising_stock(stock)

    def update_stock_price(self, name: str, new_price: float):
        for stock in self._stocks:
            if stock.name == name:
                stock.price = new_price
                self._print_stock(stock)
                self._print_rising_stock(stock)
                return
        raise ValueError(f"Stock {name!r} not found")

    def _print_stock(self, stock: Stock):
        print(f"UPDATE: {stock.name}: {stock.price:.2f}")

    def _print_rising_stock(self, stock: Stock):
        old_price = self._old_prices.get(stock.name, float("-inf"))
        if stock.price > old_price:
            print(f"RISING: {stock.name}: {old_price:.2f} -> {stock.price:.2f}")
        self._old_prices[stock.name] = stock.price


# %%
class PrintingStockObserver(StockObserver):
    def __init__(self, name: str):
        self.name = name

    def update(self, stock: Stock):
        print(f"[{self.name}] {stock.name}: {stock.price:.2f}")


# %%
class RisingStockObserver(StockObserver):
    def __init__(self, name: str):
        self.name = name
        self.old_prices: dict[str, float] = {}

    def update(self, stock: Stock):
        old_price = self.old_prices.get(stock.name, float("-inf"))
        if stock.price > old_price:
            print(
                f"[{self.name}] {stock.name}: {old_price:.2f} -> {stock.price:.2f}"
            )
        self.old_prices[stock.name] = stock.price


# %%
market = StockMarket()
printing_observer = PrintingStockObserver("Printer")
rising_observer = RisingStockObserver("RisingAlert")

# %%
market.attach(printing_observer)
market.attach(rising_observer)

# %%
market.add_stock(Stock("Banana", 100.0))

# %%
market.add_stock(Stock("Billionz", 200.0))

# %%
market.add_stock(Stock("Macrosoft", 300.0))

# %%
market.update_stock_price("Banana", 105.0)

# %%
market.update_stock_price("Billionz", 190.0)

# %%
market.update_stock_price("Macrosoft", 310.0)

# %% [markdown]
#
# ### Was haben wir erreicht?
#
# - Single Responsibility: `StockMarket` ist nur für Aktien zuständig
# - Open-Closed: Neue Observer können hinzugefügt werden, ohne `StockMarket`
#   zu ändern
# - Lose Kopplung: `StockMarket` kennt nur das `StockObserver`-Interface
# - Dynamisch: Observer können zur Laufzeit hinzugefügt und entfernt werden

# %%
market.detach(printing_observer)

# %%
market.update_stock_price("Banana", 110.0)

# %%
market.update_stock_price("Banana", 90.0)

# %% [markdown]
#
# ### Struktur: Push Observer
#
# <img src="img/pat_observer_push.png"
#      style="display:block;margin:auto;width:100%"/>

# %% [markdown]
#
# ### Teilnehmer (Pub/Sub-Terminologie)
#
# | Pub/Sub | GoF-Name | Rolle |
# |---------|----------|-------|
# | Publisher | Subject | Kennt seine Subscriber, benachrichtigt sie |
# | Subscriber | Observer | Definiert die `update()`-Schnittstelle |
# | Konkreter Publisher | ConcreteSubject | Enthält den relevanten Zustand |
# | Konkreter Subscriber | ConcreteObserver | Reagiert auf Zustandsänderungen |

# %% [markdown]
#
# ### Interaktion: Push Observer
#
# <img src="img/pat_observer_push_seq.png"
#      style="display:block;margin:auto;width:65%"/>

# %% [markdown]
#
# ### Anwendbarkeit
#
# - Ein Publisher muss mehrere Subscriber benachrichtigen, ohne sie zu kennen
# - Änderungen in einem Objekt sollen automatisch andere Objekte aktualisieren
# - Lose Kopplung zwischen zusammenhängenden Objekten ist gewünscht

# %% [markdown]
#
# ### Konsequenzen
#
# - Publisher und Subscriber können unabhängig voneinander variiert und
#   wiederverwendet werden
# - Neue Subscriber können ohne Änderungen am Publisher hinzugefügt werden
# - Unterstützung für Broadcast-Kommunikation
# - Mögliche unerwartete Updates

# %% [markdown]
#
# ### Praxisbeispiele
#
# - Event-Listener in Benutzeroberflächen (z.B. JavaScript `addEventListener`)
# - Django Signals
# - Message Broker (z.B. RabbitMQ, Kafka)

# %% [markdown]
#
# ### Verwandtes Pattern
#
# - **Mediator**: Zentraler Vermittler statt direkter Publisher-Subscriber-Beziehung

# %% [markdown]
#
# ## Workshop: Produktion von Werkstücken
#
# In einem Produktionssystem wollen Sie verschiedene andere Systeme
# benachrichtigen, wenn Sie ein Werkstück erzeugt haben. Dabei sollen diese
# Systeme vom konkreten Produzenten unabhängig sein und auch der Produzent
# keine (statische) Kenntnis über die benachrichtigten Systeme haben.
#
# Implementieren Sie ein System mit dem Push-Observer-Muster:
#
# - Ein `Item`-Datentyp mit `name` und `serial_number`
# - Ein `ItemObserver`-Interface mit einer `update(item: Item)`-Methode
# - Eine `Producer`-Klasse, die als Publisher fungiert
# - Einen konkreten `PrintingObserver`, der den Zustand des erzeugten Items
#   ausgibt
# - Einen konkreten `CountingObserver`, der zählt, wie viele Items erzeugt
#   wurden

# %%
from abc import ABC, abstractmethod  # noqa: E402
from dataclasses import dataclass  # noqa: E402


# %%
@dataclass
class Item:
    name: str
    serial_number: int


# %%

# %%

# %%

# %%

# %%
producer = Producer()
printer = PrintingObserver()
counter = CountingObserver()

# %%
producer.attach(printer)
producer.attach(counter)

# %%
producer.produce_item("Widget", 1)

# %%
producer.produce_item("Gadget", 2)

# %%
producer.produce_item("Gizmo", 3)

# %%
producer.detach(printer)
producer.produce_item("Doohickey", 4)

# %%
counter.count

# %%
