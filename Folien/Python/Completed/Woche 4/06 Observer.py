# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Observer</b>
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
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from random import randint, normalvariate, sample
import weakref


# %%
@dataclass
class Stock:
    name: str
    price: float


# %%
@dataclass
class StockMarket:
    stocks: list[Stock] = field(default_factory=list)
    price_dist_mean: float = 1.0
    price_dist_stddev: float = 0.3

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        print(f"Updated price for {stock.name} to {stock.price:.2f}")

    def update_prices(self):
        stocks_to_update = self._select_stocks_to_update()
        self._update_prices_for(stocks_to_update)
        for stock in stocks_to_update:
            print(f"Updated price for {stock.name} to {stock.price:.2f}")

    def _select_stocks_to_update(self) -> list[Stock]:
        num_stocks_to_update = randint(0, len(self.stocks) - 1)
        return sample(self.stocks, num_stocks_to_update)

    def _update_prices_for(self, stocks: list[Stock]):
        for stock in stocks:
            change_percent = normalvariate(self.price_dist_mean, self.price_dist_stddev)
            stock.price *= change_percent


# %%
market = StockMarket()

# %%
market.add_stock(Stock("Banana", 100.0))
market.add_stock(Stock("Billionz", 200.0))
market.add_stock(Stock("Macrosoft", 300.0))
market.add_stock(Stock("BCD", 400.0))

# %%
for i in range(10):
    print(f"============= Update {i + 1} =============")
    market.update_prices()


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
# - Verletzung des Single Responsibility Principle/hohe Kohäsion
# - Verletzung des Open-Closed-Prinzips
# - Hohe Kopplung (an alle Clients)

# %% [markdown]
# ## Observer
#
# ### Zweck
#
# - 1:n Beziehung zwischen Objekten
# - Automatische Benachrichtigung aller abhängigen Objekte bei Zustandsänderung
#
# ### Motivation
#
# - Konsistenz zwischen zusammenhängenden Objekten erhalten
# - Dabei aber lose Kopplung erhalten
# - Ein *Subject* kann beliebig viele *Observers* haben
# - *Observer* werden automatisch über Änderungen am *Subject* benachrichtigt

# %% [markdown]
#
# ### Klassendiagramm mit Observer
#
# <img src="img/stock_example.png"
#      style="display:block;margin:auto;width:90%"/>

# %%
class StockObserver(ABC):
    @abstractmethod
    def update(self, stocks: list["Stock"]): ...


# %%
@dataclass
class StockMarket:
    stocks: list[Stock] = field(default_factory=list)
    price_dist_mean: float = 1.0
    price_dist_stddev: float = 0.3
    observers: list[weakref.ref] = field(default_factory=list)

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)
        self._notify_observers([stock])

    def update_prices(self):
        stocks_to_update = self._select_stocks_to_update()
        self._update_prices_for(stocks_to_update)
        self._notify_observers(stocks_to_update)

    def _select_stocks_to_update(self) -> list[Stock]:
        num_stocks_to_update = len(self.stocks) // 2
        return sample(self.stocks, num_stocks_to_update)

    def _update_prices_for(self, stocks: list[Stock]):
        for stock in stocks:
            change_percent = normalvariate(self.price_dist_mean, self.price_dist_stddev)
            stock.price *= change_percent

    def attach_observer(self, observer: StockObserver):
        self.observers.append(weakref.ref(observer))

    def _notify_observers(self, stocks: list[Stock]):
        for weak_observer in self.observers:
            observer = weak_observer()
            if observer:
                observer.update(stocks)


# %%
class PrintingStockObserver(StockObserver):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def update(self, stocks: list[Stock]):
        print(f"PrintingStockObserver {self.name} received update:")
        for stock in stocks:
            print(f"  {stock.name}: {stock.price:.2f}")


# %%
class RisingStockObserver(StockObserver):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.old_prices = {}

    def update(self, stocks: list[Stock]):
        print(f"RisingStockObserver {self.name} received update:")
        for stock in stocks:
            old_price = self.old_prices.get(stock.name, float("-inf"))
            if stock.price > old_price:
                print(f"  {stock.name}: {old_price:.2f} -> {stock.price:.2f}")
            self.old_prices[stock.name] = stock.price


# %%
market = StockMarket()

# %%
printing_observer = PrintingStockObserver("PrintingObserver")
rising_observer = RisingStockObserver("RisingObserver")

# %%
market.attach_observer(printing_observer)
market.attach_observer(rising_observer)

# %%
market.add_stock(Stock("Banana", 100.0))
market.add_stock(Stock("Billionz", 200.0))
market.add_stock(Stock("Macrosoft", 300.0))
market.add_stock(Stock("BCD", 400.0))

# %%
for i in range(10):
    print(f"============= Update {i + 1} =============")
    market.update_prices()

# %%
del printing_observer

# %%
for i in range(10):
    print(f"============= Update {i + 1} =============")
    market.update_prices()


# %% [markdown]
#
# ### Anwendbarkeit
#
# - Ein Objekt muss andere Objekte benachrichtigen, ohne Details zu kennen
# - Eine Änderung in einem Objekt führt zu Änderungen in (beliebig vielen)
#   anderen Objekten
# - Eine Abstraktion hat zwei Aspekte, wobei einer vom anderen abhängt

# %% [markdown]
# ### Struktur: Pull Observer
#
# <img src="img/pat_observer_pull.png"
#      style="display:block;margin:auto;width:100%"/>


# %% [markdown]
# ## Observer (Verhaltensmuster)
#
# ### Teilnehmer
#
# - `Subject`
#   - kennt seine Observer. Jede Anzahl von Observern kann ein Subject
#     beobachten
#   - stellt eine Schnittstelle zum Hinzufügen und Entfernen von Observern
#     bereit
# - `Observer`
#   - definiert eine Aktualisierungs-Schnittstelle für Objekte, die über
#     Änderungen eines Subjects informiert werden sollen

# %% [markdown]
# - `ConcreteSubject`
#   - Speichert den Zustand, der für `ConcreteObserver`-Objekte von Interesse
#     ist
#   - Sendet eine Benachrichtigung an seine Observer, wenn sich sein Zustand
#     ändert
# - `ConcreteObserver`
#   - Kann eine Referenz auf ein `ConcreteSubject`-Objekt halten
#   - Speichert Zustand, der mit dem des Subjects konsistent bleiben soll
#   - Implementiert die `Observer`-Aktualisierungs-Schnittstelle, um seinen
#     Zustand mit dem des Subjects konsistent zu halten

# %% [markdown]
# ### Interaktionen: Pull Observer
#
# <img src="img/pat_observer_pull_seq.png"
#      style="display:block;margin:auto;width:65%"/>


# %% [markdown]
# ### Zusammenarbeit
#
# - `ConcreteSubject` benachrichtigt seine Observer über Änderungen in seinem
#   Zustand
# - Nachdem ein `ConcreteObserver` über eine Änderung im `ConcreteSubject`
#   informiert wurde, holt es den neuen Zustand vom Subjekt
# - `ConcreteObserver` verwendet diese Informationen, um seinen Zustand mit dem
#   des Subjects in Einklang zu bringen


# %% [markdown]
# ### Struktur: Push Observer
#
# <img src="img/pat_observer_push.png"
#      style="display:block;margin:auto;width:100%"/>

# %% [markdown]
# ### Interaktion: Push Observer
#
# <img src="img/pat_observer_push_seq.png"
#      style="display:block;margin:auto;width:65%"/>

# %% [markdown]
# ### Konsequenzen
#
# - `Subject` und `Observer` können unabhängig voneinander
#    - variiert werden
#    - wiederverwendet werden
# - Hinzufügen neuer `Observer` ohne Änderungen am `Subject`
# - Abstrakte Kopplung zwischen `Subject` und `Observer`
# - Unterstützung für Broadcast-Kommunikation
# - Unerwartete Updates

# %% [markdown]
# ### Praxisbeispiele
#
# - Event-Listener in Benutzeroberflächen
#
# ### Verwandte Patterns
#
# - Mediator: Durch die Kapselung komplexer Update-Semantik fungiert der
#   `ChangeManager` als Mediator zwischen Subjects und Observers
# - Singleton: ...


# %% [markdown]
# ## Mini-Workshop: Produktion von Werkstücken
#
# In einem Produktionssystem wollen Sie verschiedene andere Systeme
# benachrichtigen, wenn Sie ein Werkstück erzeugt haben. Dabei sollen diese
# Systeme vom konkreten Produzenten unabhängig sein und auch der Produzent
# keine (statische) Kenntnis über die benachrichtigten Systeme haben.
#
# Implementieren Sie ein derartiges System mit dem Observer-Muster.
# Implementieren Sie dazu einen konkreten Observer `PrintingObserver`, der den
# Zustand des beobachteten Objekts ausgibt.
#
# *Hinweis:* Sie können das System sowohl mit Pull- als auch mit Push-Observern
# implementieren. Es ist eine gute Übung, wenn Sie beide Varianten
# implementieren und vergleichen.


# %%
from abc import ABC, abstractmethod  # noqa: E402


# %%
class PullObserver(ABC):
    @abstractmethod
    def update(self): ...

    @property
    @abstractmethod
    def id(self) -> int: ...


# %%
import weakref  # noqa


# %%
class PullSubject:

    def __init__(self):
        self.observers: list[weakref.ref] = []

    def attach(self, observer: PullObserver):
        self.observers.append(weakref.ref(observer))
        self.print_observers("after attaching")

    def detach(self, observer: PullObserver):
        self.observers = [o for o in self.observers if o() is not observer]
        self.print_observers("after detaching")

    def notify(self):
        self.print_observers("before notifying")
        for weak_observer in self.observers:
            observer = weak_observer()
            if observer:
                observer.update()

    def get_state(self) -> list[int]:
        raise NotImplementedError

    def print_observers(self, context: str):
        print(f"Observers {context} are:", end="")
        for weak_observer in self.observers:
            observer = weak_observer()
            if observer:
                print(f" Observer-{observer.id}", end="")
            else:
                print(" Observer-<deleted>", end="")
        print()


# %%
class PrintingPullObserver(PullObserver):

    def __init__(self, id_: int):
        super().__init__()
        self.id_ = id_
        self.subject: PullSubject | None = None
        self.observer_state: list[int] = []

    def update(self):
        print(f"Observer {self.id}: Observing {self.subject}.")
        print(f"  Old observer state is {self.observer_state}.")
        self.observer_state = self.subject.get_state().copy()
        print(f"  New observer state is {self.observer_state}.")

    @property
    def id(self) -> int:
        return self.id_

    def attach_to(self, subject: PullSubject):
        subject.attach(self)
        self.subject = subject

    def detach_from_subject(self):
        if self.subject is not None:
            self.subject.detach(self)
            self.subject = None


# %%
class PullProducer(PullSubject):

    def __init__(self):
        super().__init__()
        self.available_items: list[int] = []

    def produce_item(self, item: int):
        self.available_items.append(item)
        self.notify()

    def get_state(self) -> list[int]:
        return self.available_items


# %%
p = PullProducer()
o1 = PrintingPullObserver(1)
o1.attach_to(p)
o2 = PrintingPullObserver(2)
o2.attach_to(p)

# %%
p.produce_item(1)
p.produce_item(2)

# %%
o1.detach_from_subject()
p.produce_item(3)

# %%
o1.attach_to(p)
del o2
p.produce_item(4)


# %%
class PushObserver(ABC):
    @abstractmethod
    def update(self, item: int): ...

    @property
    @abstractmethod
    def id(self) -> int: ...


# %%
class PushSubject:
    def __init__(self):
        self.observers: list[weakref.ref] = []

    def attach(self, observer: PushObserver):
        self.observers.append(weakref.ref(observer))
        self.print_observers("after attaching")

    def detach(self, observer: PushObserver):
        self.observers = [o for o in self.observers if o() is not observer]
        self.print_observers("after detaching")

    def notify(self, item: int):
        self.print_observers("before notifying")
        for weak_observer in self.observers:
            observer = weak_observer()
            if observer:
                observer.update(item)

    def print_observers(self, context: str):
        print(f"Observers {context} are:", end="")
        for weak_observer in self.observers:
            observer = weak_observer()
            if observer:
                print(f" Observer-{observer.id}", end="")
            else:
                print(" Observer-<deleted>", end="")
        print()


# %%
class PrintingPushObserver(PushObserver):

    def __init__(self, id_: int):
        super().__init__()
        self.id_ = id_

    def update(self, item: int):
        print(f"Observer {self.id}")
        print(f"  Received item {item}.")

    @property
    def id(self) -> int:
        return self.id_


# %%
class PushProducer(PushSubject):

    def __init__(self):
        super().__init__()
        self.available_items: list[int] = []

    def produce_item(self, item: int):
        self.available_items.append(item)
        self.notify(item)


# %%
p = PushProducer()
o1 = PrintingPushObserver(1)
p.attach(o1)
o2 = PrintingPushObserver(2)
p.attach(o2)

# %%
p.produce_item(1)
p.produce_item(2)

# %%
p.detach(o1)
p.produce_item(3)

# %%
p.attach(o1)
del o2
p.produce_item(4)

# %%
