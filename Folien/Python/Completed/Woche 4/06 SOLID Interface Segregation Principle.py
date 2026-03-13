# %%
# <!--
# clang-format off
# -->
# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>SOLID: Interface Segregation Principle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## SOLID : Interface Segregation Prinzip
#
# - Kein Client einer Klasse `C` sollte von Methoden abhängen, die er nicht
#   benutzt.
# - Wenn das nicht der Fall ist
# - Unterteile die Schnittstelle von `C` in mehrere unabhängige Schnittstellen.
# - Ersetze `C` in jedem Client durch die vom Client tatsächlich verwendeten
#   Schnittstellen.

# %%
class Car:
    def drive(self):
        print("Accelerating.")

    def repair(self):
        print("Repairing.")


# %%
class Driver:
    def drive(self, car):
        car.drive()


# %%
class Mechanic:
    def work_on(self, car):
        car.repair()


# %%
d = Driver()
m = Mechanic()
c = Car()

# %%
d.drive(c)

# %%
m.work_on(c)

# %%
from abc import ABC, abstractmethod


# %%
class Drivable(ABC):
    @abstractmethod
    def drive(self): ...


# %%
class Repairable(ABC):
    @abstractmethod
    def repair(self): ...


# %%
class Car2(Drivable, Repairable):
    def drive(self):
        print("Accelerating.")

    def repair(self):
        print("Repairing.")


# %%
class Driver2:
    def drive(self, car: Drivable):
        car.drive()


# %%
class Mechanic2:
    def work_on(self, car: Repairable):
        car.repair()


# %%
d2 = Driver2()
m2 = Mechanic2()
c2 = Car2()

# %%
d2.drive(c2)

# %%
m2.work_on(c2)

# %% [markdown]
#
# ## Workshop:
#
# In diesem Workshop werden wir an einem Restaurant-Management-System arbeiten.
#
# Stellen Sie sich vor, Sie haben den Code eines Restaurant-Management-Systems
# erhalten. Das System hat derzeit eine einzige Schnittstelle
# `RestaurantOperations`, die alle Operationen definiert, die in einem
# Restaurant durchgeführt werden können. Verschiedene Rollen im Restaurant, wie
# der Kunde, der Koch, der Kassierer und der Hausmeister, verwenden alle
# dieselbe Schnittstelle, aber jede Rolle verwendet nur einen Teil ihrer
# Funktionen.
#
# Ihre Aufgabe ist es, dieses System so umzubauen, dass es dem Interface
# Segregation Principle entspricht. Das bedeutet, dass kein Client gezwungen
# werden sollte, von Schnittstellen abhängig zu sein, die er nicht verwendet.

# %% [markdown]
#
# 1. Identifizieren Sie, welche Operationen für welche Rollen relevant sind.
# 2. Teilen Sie das RestaurantOperations-Interface in kleinere,
#    rollenspezifische Schnittstellen auf.
# 3. Passen Sie die `Restaurant`-Klasse und die rollenbasierten Client-Klassen
#    (`Customer`, `Chef`, `Cashier`, `Janitor`) an die neuen Schnittstellen an.
# 4. Stellen Sie sicher, dass jede Client-Klasse nur über die für ihre Rolle

# %%
from abc import ABC, abstractmethod


# %%
class RestaurantOperations(ABC):
    @abstractmethod
    def place_order(self):
        pass

    @abstractmethod
    def cook_order(self):
        pass

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def clean_tables(self):
        pass


# %%
class Restaurant(RestaurantOperations):
    def place_order(self):
        print("Order has been placed.")

    def cook_order(self):
        print("Order is being cooked.")

    def calculate_bill(self):
        print("Bill is being calculated.")

    def clean_tables(self):
        print("Tables are being cleaned.")


# %%
class Customer:
    def __init__(self, restaurant: RestaurantOperations):
        self.restaurant = restaurant

    def make_order(self):
        self.restaurant.place_order()
        self.restaurant.calculate_bill()


# %%
class Chef:
    def __init__(self, restaurant: RestaurantOperations):
        self.restaurant = restaurant

    def prepare_food(self):
        self.restaurant.cook_order()


# %%
class Cashier:
    def __init__(self, restaurant: RestaurantOperations):
        self.restaurant = restaurant

    def generate_bill(self):
        self.restaurant.calculate_bill()


# %%
class Janitor:
    def __init__(self, restaurant: RestaurantOperations):
        self.restaurant = restaurant

    def clean(self):
        self.restaurant.clean_tables()


# %%
restaurant = Restaurant()
customer = Customer(restaurant)
chef = Chef(restaurant)
cashier = Cashier(restaurant)
janitor = Janitor(restaurant)

# %%
customer.make_order()
chef.prepare_food()
cashier.generate_bill()
janitor.clean()

# %%
from abc import ABC, abstractmethod


class Ordering(ABC):
    @abstractmethod
    def place_order(self):
        pass


# %%
class Cooking(ABC):
    @abstractmethod
    def cook_order(self):
        pass


# %%
class Billing(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass


# %%
class Cleaning(ABC):
    @abstractmethod
    def clean_tables(self):
        pass


# %%
class Restaurant(Ordering, Cooking, Billing, Cleaning):
    def place_order(self):
        print("Order has been placed.")

    def cook_order(self):
        print("Order is being cooked.")

    def calculate_bill(self):
        print("Bill is being calculated.")

    def clean_tables(self):
        print("Tables are being cleaned.")


# %%
class Customer:
    def __init__(self, ordering, billing: Billing):
        self.ordering = ordering
        self.billing = billing

    def make_order(self):
        self.ordering.place_order()
        self.billing.calculate_bill()


# %%
class Chef:
    def __init__(self, cooking: Cooking):
        self.cooking = cooking

    def prepare_food(self):
        self.cooking.cook_order()


# %%
class Cashier:
    def __init__(self, billing: Billing):
        self.billing = billing

    def generate_bill(self):
        self.billing.calculate_bill()


# %%
class Janitor:
    def __init__(self, cleaning: Cleaning):
        self.cleaning = cleaning

    def clean(self):
        self.cleaning.clean_tables()


# %%
restaurant = Restaurant()
customer = Customer(restaurant, restaurant)
chef = Chef(restaurant)
cashier = Cashier(restaurant)
janitor = Janitor(restaurant)

# %%
customer.make_order()
chef.prepare_food()
cashier.generate_bill()
janitor.clean()

# %%
