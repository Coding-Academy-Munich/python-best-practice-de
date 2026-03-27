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

# %%

# %%
