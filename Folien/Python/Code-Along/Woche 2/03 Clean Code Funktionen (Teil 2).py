# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Clean Code: Funktionen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Typ-Tags und Switch-Anweisungen

# %%
from enum import IntEnum
from dataclasses import dataclass


# %%
class EmployeeType(IntEnum):
    COMMISSIONED = 0
    HOURLY = 1
    SALARIED = 2


# %%
@dataclass
class EmployeeV1:
    type_: EmployeeType


# %%
def calculate_pay(e: EmployeeV1):
    if e.type_ == EmployeeType.COMMISSIONED:
        return calculate_commissioned_pay(e)
    elif e.type_ == EmployeeType.HOURLY:
        return calculate_hourly_pay(e)
    elif e.type_ == EmployeeType.SALARIED:
        return calculate_salaried_pay(e)
    else:
        raise ValueError("No valid employee type.")


# %%
def calculate_commissioned_pay(e: EmployeeV1):
    return 100.0


# %%
def calculate_hourly_pay(e: EmployeeV1):
    return 120.0


# %%
def calculate_salaried_pay(e: EmployeeV1):
    return 80.0


# %%
e1 = EmployeeV1(EmployeeType.HOURLY)
e2 = EmployeeV1(EmployeeType.SALARIED)

# %%
print(calculate_pay(e1))
print(calculate_pay(e2))

# %% [markdown]
#
# - Switch-Anweisungen führen oft Operationen auf der gleichen Abstraktionsebene
#   aus. (für "Subtypen" anstelle des ursprünglichen Typs)
# - "Subtypen" werden oft durch Typ-Tags unterschieden
# - In Python wird das mit `if`-`elif`-`else`-Ketten realisiert, da es keine
#   `switch`-Anweisung gibt

# %% [markdown]
#
# ## Ersetze Switch-Anweisung durch Polymorphie
#
# Es ist oft besser, switch-Anweisungen durch Vererbung und Polymorphie zu
# ersetzen:

# %%
from abc import ABC, abstractmethod


# %%
class EmployeeV2(ABC):
    @abstractmethod
    def calculate_pay(self):
        ...


# %%
@dataclass
class CommissionedEmployee(EmployeeV2):
    def calculate_pay(self):
        return 100.0


# %%
@dataclass
class HourlyEmployee(EmployeeV2):
    def calculate_pay(self):
        return 120.0


# %%
@dataclass
class SalariedEmployee(EmployeeV2):
    def calculate_pay(self):
        return 80.0


# %%
def create_employee_v2(employee_type: EmployeeType):
    if employee_type == EmployeeType.COMMISSIONED:
        return CommissionedEmployee()
    elif employee_type == EmployeeType.HOURLY:
        return HourlyEmployee()
    elif employee_type == EmployeeType.SALARIED:
        return SalariedEmployee()
    else:
        raise ValueError("Not a valid employee type.")


# %%
e1 = create_employee_v2(EmployeeType.HOURLY)
e2 = create_employee_v2(EmployeeType.SALARIED)

# %%
print(e1.calculate_pay())
print(e2.calculate_pay())

# %% [markdown]
#
# ## Trade-Offs: Vererbungsvariante
#
# - Neue "Bezahlvarianten" könne ohne Änderung des bestehenden Codes hinzugefügt
#   werden
# - Potentiell Explosion von Unterklassen (bei mehreren Enumerationstypen)

# %% [markdown]
#
# ## Trade-Offs: Switch-Variante
#
# - Einfacher zu verstehen
# - Erleichtert die Definition von Funktionen, die auf die Enumeration zugreifen
#   - In Python gibt es aber `functools.singledispatch` für die Vererbungsvariante

# %% [markdown]
#
# ## Trade-Offs: Design
#
# - Spiegelt sich die Unterscheidung zwischen den Subtypen im Domänenmodell
#   wieder?

# %% [markdown]
#
# ## Ersetzen der Enumeration durch Vererbung
#
# - Polymorphie statt Enumeration
# - Nicht auf der Ebene der gesamten Klasse
# - Mildert die Nachteile der Vererbungsvariante

# %% [markdown]
#
# ### Beispiel
#
# - Abstrakte Klasse `PaymentCalculator` statt `EmployeeType`
# - Konkrete Unterklasse pro "Bezahlvariante"
# - `Employee` delegiert Berechnung an `PaymentCalculator`

# %%
from abc import ABC, abstractmethod


# %%
class PaymentCalculator(ABC):
    @abstractmethod
    def calculate_pay(self, employee):
        ...


# %%
class CommissionedPaymentCalculator(PaymentCalculator):
    def calculate_pay(self, employee):
        return 100.0


# %%
class HourlyPaymentCalculator(PaymentCalculator):
    def calculate_pay(self, employee):
        return 120.0


# %%
class SalariedPaymentCalculator(PaymentCalculator):
    def calculate_pay(self, employee):
        return 80.0


# %%
from dataclasses import dataclass


# %%
@dataclass
class EmployeeV3:
    payment_calculator: PaymentCalculator

    def calculate_pay(self):
        return self.payment_calculator.calculate_pay(self)


# %%
def create_employee_v3(employee_type: EmployeeType):
    if employee_type == EmployeeType.COMMISSIONED:
        return EmployeeV3(CommissionedPaymentCalculator())
    elif employee_type == EmployeeType.HOURLY:
        return EmployeeV3(HourlyPaymentCalculator())
    elif employee_type == EmployeeType.SALARIED:
        return EmployeeV3(SalariedPaymentCalculator())
    else:
        raise ValueError("Not a valid employee type.")


# %%
e1 = create_employee_v3(EmployeeType.HOURLY)
e2 = create_employee_v3(EmployeeType.SALARIED)

# %%
print(e1.calculate_pay())
print(e2.calculate_pay())

# %% [markdown]
#
# ## Mini-Workshop: Ersetzen von Switch-Anweisungen
#
# Strukturieren Sie den folgenden Code so um, dass nur noch bei der Erzeugung
# der Objekte eine "switch-Anweisung" verwendet wird:

# %%
from dataclasses import dataclass

# %%
COMPUTER_TYPE_PC = 0
COMPUTER_TYPE_MAC = 1
COMPUTER_TYPE_CHROMEBOOK = 2


# %%
@dataclass
class ComputerV1:
    computer_type: int


# %%
def compile_code(computer: ComputerV1):
    if computer.computer_type == COMPUTER_TYPE_PC:
        print("Compiling code for PC.")
    elif computer.computer_type == COMPUTER_TYPE_MAC:
        print("Compiling code for Mac.")
    elif computer.computer_type == COMPUTER_TYPE_CHROMEBOOK:
        print("Compiling code for Chromebook.")
    else:
        raise ValueError(f"Don't know how to compile code for {computer}.")


# %%
my_pc = ComputerV1(COMPUTER_TYPE_PC)
my_mac = ComputerV1(COMPUTER_TYPE_MAC)
my_chromebook = ComputerV1(COMPUTER_TYPE_CHROMEBOOK)

# %%
compile_code(my_pc)
compile_code(my_mac)
compile_code(my_chromebook)

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

# %%

# %%

# %%

# %%

# %%
