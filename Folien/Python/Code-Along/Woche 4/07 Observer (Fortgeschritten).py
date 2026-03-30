# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Observer (Fortgeschritten)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Wiederholung: Push Observer
#
# - Publisher hält eine Liste von Subscribern
# - Bei Zustandsänderung: Publisher benachrichtigt alle Subscriber
# - Subscriber erhalten die relevanten Daten als Parameter

# %%
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# %%
@dataclass
class Stock:
    name: str
    price: float


# %%
class StockObserver(ABC):
    @abstractmethod
    def update(self, stocks: list[Stock]): ...


# %%
@dataclass
class StockMarket:
    stocks: list[Stock] = field(default_factory=list)
    observers: list[StockObserver] = field(default_factory=list)

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        self._notify_observers([stock])

    def update_stock_price(self, name: str, new_price: float):
        for stock in self.stocks:
            if stock.name == name:
                stock.price = new_price
                self._notify_observers([stock])
                return
        raise ValueError(f"Stock {name!r} not found")

    def attach(self, observer: StockObserver):
        self.observers.append(observer)

    def detach(self, observer: StockObserver):
        self.observers.remove(observer)

    def _notify_observers(self, stocks: list[Stock]):
        for observer in self.observers:
            observer.update(stocks)


# %%
class PrintingStockObserver(StockObserver):
    def __init__(self, name: str):
        self.name = name

    def update(self, stocks: list[Stock]):
        print(f"[{self.name}]")
        for stock in stocks:
            print(f"  {stock.name}: {stock.price:.2f}")


# %% [markdown]
#
# ## Problem: Lebenszeit von Observern
#
# - Was passiert, wenn ein Observer gelöscht wird?
# - Der Publisher hält noch eine Referenz auf den Observer
# - Der Observer wird nicht vom Garbage Collector entfernt
# - `_notify_observers()` ruft `update()` auf einem "gelöschten" Observer auf

# %%
market = StockMarket()
observer1 = PrintingStockObserver("Observer-1")
observer2 = PrintingStockObserver("Observer-2")

# %%
market.attach(observer1)
market.attach(observer2)

# %%
market.add_stock(Stock("Banana", 100.0))

# %%
del observer1

# %%
market.update_stock_price("Banana", 110.0)

# %% [markdown]
#
# - `del observer1` entfernt nur die lokale Variable
# - `StockMarket` hält weiterhin eine Referenz
# - Der Observer wird weiterhin benachrichtigt!

# %% [markdown]
#
# ## Lösung 1: Explizites Detach
#
# - Observer muss vor dem Löschen explizit entfernt werden
# - `market.detach(observer)` entfernt die Referenz
# - Einfach, aber fehleranfällig (Aufrufer kann das Detach vergessen)

# %% [markdown]
#
# ## Lösung 2: Weak References
#
# - `weakref.ref()` erzeugt eine schwache Referenz
# - Verhindert nicht, dass der Garbage Collector das Objekt entfernt
# - Aufruf der Referenz gibt das Objekt oder `None` zurück

# %%
import weakref


# %%
obj = PrintingStockObserver("Test")
weak = weakref.ref(obj)

# %%
weak()

# %%
del obj

# %%
weak()

# %%
weak() is None


# %% [markdown]
#
# ## StockMarket mit Weak References

# %%
@dataclass
class StockMarket:
    stocks: list[Stock] = field(default_factory=list)
    observers: list[StockObserver] = field(default_factory=list)

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        self._notify_observers([stock])

    def update_stock_price(self, name: str, new_price: float):
        for stock in self.stocks:
            if stock.name == name:
                stock.price = new_price
                self._notify_observers([stock])
                return
        raise ValueError(f"Stock {name!r} not found")

    def attach(self, observer: StockObserver):
        self.observers.append(observer)

    def detach(self, observer: StockObserver):
        self.observers.remove(observer)

    def _notify_observers(self, stocks: list[Stock]):
        for observer in self.observers:
            observer.update(stocks)


# %%
market = StockMarket()
observer1 = PrintingStockObserver("Observer-1")
observer2 = PrintingStockObserver("Observer-2")

# %%
market.attach(observer1)
market.attach(observer2)

# %%
market.add_stock(Stock("Banana", 100.0))

# %%
del observer1

# %%
market.update_stock_price("Banana", 110.0)


# %% [markdown]
#
# - Nach `del observer1` wird der Observer automatisch entfernt
# - Nur Observer-2 wird noch benachrichtigt
# - Kein explizites `detach()` nötig

# %% [markdown]
#
# ## Pull Observer
#
# - Alternative zum Push Observer
# - Publisher benachrichtigt ohne Daten: `update()` ohne Parameter
# - Observer fragt den Publisher nach dem aktuellen Zustand
# - Observer hält eine Referenz auf den Publisher

# %% [markdown]
#
# ### Struktur: Pull Observer
#
# <img src="img/pat_observer_pull.png"
#      style="display:block;margin:auto;width:100%"/>

# %% [markdown]
#
# ### Interaktion: Pull Observer
#
# <img src="img/pat_observer_pull_seq.png"
#      style="display:block;margin:auto;width:65%"/>

# %% [markdown]
#
# ## Pull Observer: Implementierung

# %%
class PullStockObserver(ABC):
    @abstractmethod
    def update(self): ...


# %%
@dataclass
class PullStockMarket:
    stocks: list[Stock] = field(default_factory=list)
    observers: list[PullStockObserver] = field(default_factory=list)

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        self._notify_observers()

    def update_stock_price(self, name: str, new_price: float):
        for stock in self.stocks:
            if stock.name == name:
                stock.price = new_price
                self._notify_observers()
                return
        raise ValueError(f"Stock {name!r} not found")

    def get_stocks(self) -> list[Stock]:
        return list(self.stocks)

    def attach(self, observer: PullStockObserver):
        self.observers.append(observer)

    def detach(self, observer: PullStockObserver):
        self.observers.remove(observer)

    def _notify_observers(self):
        for observer in self.observers:
            observer.update()


# %%
class PrintingPullObserver(PullStockObserver):
    def __init__(self, name: str, market: "PullStockMarket"):
        self.name = name
        self.market = market

    def update(self):
        stocks = self.market.get_stocks()
        print(f"[{self.name}]")
        for stock in stocks:
            print(f"  {stock.name}: {stock.price:.2f}")


# %%
pull_market = PullStockMarket()
pull_observer = PrintingPullObserver("PullPrinter", pull_market)

# %%
pull_market.attach(pull_observer)

# %%
pull_market.add_stock(Stock("Banana", 100.0))
pull_market.add_stock(Stock("Billionz", 200.0))

# %%
pull_market.update_stock_price("Banana", 105.0)


# %% [markdown]
#
# ## Push vs. Pull: Vergleich
#
# | | Push | Pull |
# |---|---|---|
# | **Datenfluss** | Publisher → Subscriber | Subscriber ← Publisher |
# | **`update()`** | Erhält Daten als Parameter | Keine Parameter |
# | **Abhängigkeit** | Subscriber kennt Publisher nicht | Subscriber kennt Publisher |
# | **Flexibilität** | Alle Subscriber erhalten gleiche Daten | Jeder Subscriber wählt seine Daten |
# | **Einfachheit** | Einfacher zu implementieren | Komplexere Abhängigkeiten |

# %% [markdown]
#
# ### Wann welche Variante?
#
# - **Push** bevorzugen, wenn:
#   - Die relevanten Daten für alle Subscriber gleich sind
#   - Subscriber den Publisher nicht kennen sollen (lose Kopplung)
#   - Event-basierte Systeme (UI, Messaging)
# - **Pull** bevorzugen, wenn:
#   - Verschiedene Subscriber unterschiedliche Daten brauchen
#   - Der Gesamtzustand sehr groß ist
#   - Subscriber nur an bestimmten Teilen des Zustands interessiert sind

# %% [markdown]
#
# ## Mini-Workshop: Pull Observer
#
# Refaktorieren Sie das Produktionssystem aus dem vorherigen Workshop
# (Push Observer) zu einem Pull Observer:
#
# - `ItemObserver.update()` hat keinen Parameter
# - `Producer` hat eine Methode `get_last_item()`, die das zuletzt erzeugte
#   Item zurückgibt
# - `PrintingObserver` hält eine Referenz auf den `Producer` und ruft
#   `get_last_item()` in `update()` auf

# %%
@dataclass
class Item:
    name: str
    serial_number: int


# %%

# %%

# %%

# %%
pull_producer = PullProducer()
pull_printer = PullPrintingObserver(pull_producer)

# %%
pull_producer.attach(pull_printer)

# %%
pull_producer.produce_item("Widget", 1)

# %%
pull_producer.produce_item("Gadget", 2)

# %%
pull_producer.produce_item("Gizmo", 3)

# %%
