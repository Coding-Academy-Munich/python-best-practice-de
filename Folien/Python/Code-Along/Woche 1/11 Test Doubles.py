# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Test Doubles</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Test Doubles
#
# - Test Double: Vereinfachte Version einer Abhängigkeit im System
#   - z.B. Ersetzen einer Datenbankabfrage durch einen fixen Wert
# - Test Doubles sind wichtig zum Vereinfachen von Tests
# - Sie benötigen typischerweise ein Interface, das sie implementieren
# - Aber: zu viele oder komplexe Test Doubles machen Tests unübersichtlich
#   - Was wird von einem Test eigentlich getestet?

# %% [markdown]
#
# ## Arten von Test Doubles
#
# - Ausgehende Abhängigkeiten ("Mocks")
#   - Mocks
#   - Spies
# - Eingehende Abhängigkeiten ("Stubs")
#   - Dummies
#   - Stubs
#   - Fakes

# %% [markdown]
#
# ## Dummy
#
# - Objekt, das nur als Platzhalter dient
# - Wird übergeben, aber nicht verwendet
# - In Python manchmal `None`
# - Auch für ausgehende Abhängigkeiten

# %% [markdown]
#
# ## Stub
#
# - Objekt, das eine minimale Implementierung einer Abhängigkeit bereitstellt
# - Gibt typischerweise immer den gleichen Wert zurück
# - Wird verwendet um
#  - komplexe Abhängigkeiten zu ersetzen
#  - Tests deterministisch zu machen

# %% [markdown]
#
# ## Fake
#
# - Objekt, das eine einfachere Implementierung einer Abhängigkeit bereitstellt
# - Kann z.B. eine In-Memory-Datenbank sein
# - Wird verwendet um
#   - Tests zu beschleunigen
#   - Konfiguration von Tests zu vereinfachen

# %% [markdown]
#
# ## Spy
#
# - Objekt, das Informationen über die Interaktion mit ihm speichert
# - Wird verwendet um
#   - zu überprüfen, ob eine Abhängigkeit korrekt verwendet wird

# %% [markdown]
#
# ## Mock
#
# - Objekt, das Information über die erwartete Interaktion speichert
# - Typischerweise deklarativ konfigurierbar
# - Automatisierte Implementierung von Spies
# - Wird verwendet um
#   - zu überprüfen, ob eine Abhängigkeit korrekt verwendet wird

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
# ## Typischer Einsatz von Test Doubles
#
# - Zugriff auf Datenbank, Dateisystem
# - Zeit, Zufallswerte
# - Nichtdeterminismus
# - Verborgener Zustand

# %% [markdown]
#
# ## Workshop: Test Doubles in der Praxis
#
# - Wir entwickeln ein Bestellsystem
# - Der `OrderProcessor` verarbeitet Bestellungen
# - Er verwendet drei externe Dienste:
#   - `InventoryService`: Prüft und reserviert Lagerbestand
#   - `PaymentGateway`: Verarbeitet Zahlungen
#   - `NotificationService`: Sendet Bestätigungen

# %% [markdown]
#
# ### Domain-Modelle

# %%
from dataclasses import dataclass
from enum import Enum

# %%
class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    FAILED = "failed"

# %%
@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float

    @property
    def total_price(self) -> float:
        return self.quantity * self.unit_price

# %%
@dataclass
class Order:
    order_id: str
    customer_email: str
    items: list[OrderItem]

    @property
    def total_amount(self) -> float:
        return sum(item.total_price for item in self.items)

# %%
@dataclass
class OrderResult:
    status: OrderStatus
    message: str

# %% [markdown]
#
# ### Service-Interfaces

# %%
class InventoryService(ABC):
    @abstractmethod
    def check_stock(self, product_id: str, quantity: int) -> bool:
        ...

    @abstractmethod
    def reserve_items(self, product_id: str, quantity: int) -> bool:
        ...

# %%
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float, customer_email: str) -> bool:
        ...

# %%
class NotificationService(ABC):
    @abstractmethod
    def send_order_confirmation(self, order: Order, customer_email: str) -> None:
        ...

# %% [markdown]
#
# ### Warum brauchen wir Test Doubles?
#
# Echte Implementierungen haben Testbarkeitsprobleme:
#
# - `StripePaymentGateway`: HTTP-Aufrufe, API-Keys, echtes Geld!
# - `DatabaseInventoryService`: PostgreSQL-Datenbank erforderlich
# - `SmtpNotificationService`: Sendet echte E-Mails
#
# Diese sind für Unit-Tests ungeeignet.

# %% [markdown]
#
# ### Der OrderProcessor (System Under Test)

# %%
class OrderProcessor:
    def __init__(
        self,
        inventory: InventoryService,
        payment: PaymentGateway,
        notifications: NotificationService,
    ):
        self.inventory = inventory
        self.payment = payment
        self.notifications = notifications

    def process_order(self, order: Order) -> OrderResult:
        # Check stock for all items
        for item in order.items:
            if not self.inventory.check_stock(item.product_id, item.quantity):
                return OrderResult(
                    OrderStatus.FAILED, f"Insufficient stock for {item.product_id}"
                )

        # Reserve items
        for item in order.items:
            if not self.inventory.reserve_items(item.product_id, item.quantity):
                return OrderResult(
                    OrderStatus.FAILED, f"Could not reserve {item.product_id}"
                )

        # Process payment
        if not self.payment.process_payment(order.total_amount, order.customer_email):
            return OrderResult(OrderStatus.FAILED, "Payment failed")

        # Send confirmation
        self.notifications.send_order_confirmation(order, order.customer_email)

        return OrderResult(OrderStatus.CONFIRMED, "Order processed successfully")

# %% [markdown]
#
# ### Workshop-Aufgabe
#
# Schreiben Sie Tests für die folgenden Szenarien:
#
# 1. Erfolgreiche Bestellungsverarbeitung
# 2. Bestellung schlägt fehl wegen unzureichendem Lagerbestand
# 3. Bestellung schlägt fehl wegen Zahlungsfehler
#
# Implementieren Sie die benötigten Test Doubles.
#
# Siehe `examples/TestDoublesStarterKit` für den Starter-Code.

# %% [markdown]
#
# ### Diskussion: Welche Test Doubles haben Sie verwendet?
#
# | Abhängigkeit | Typ | Grund |
# |--------------|-----|-------|
# | InventoryService | **Stub** | Eingehend: Liefert Werte für Bestandsprüfung |
# | PaymentGateway | **Stub** | Eingehend: Liefert Ergebnis der Zahlung |
# | NotificationService | **Spy** | Ausgehend: Wir prüfen, ob Benachrichtigung gesendet wurde |

# %% [markdown]
#
# ### Wichtige Erkenntnis
#
# - **Stubs** für eingehende Abhängigkeiten
#   - Wir kontrollieren die Rückgabewerte
#   - Ermöglicht deterministische Tests
# - **Spies/Mocks** für ausgehende Abhängigkeiten
#   - Wir überprüfen die Seiteneffekte
#   - Stellt sicher, dass Aktionen ausgeführt wurden
#
# Vollständige Lösung: siehe `examples/TestDoubles`
