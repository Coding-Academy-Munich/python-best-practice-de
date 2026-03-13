# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Mocking mit pytest-mock</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Mocking-Frameworks
#
# - Manuelle Test Doubles sind einfach und explizit
# - Aber: Viel Boilerplate-Code für viele Tests
# - Mocking-Frameworks automatisieren die Erstellung
# - Python: `unittest.mock` und `pytest-mock`

# %% [markdown]
#
# ## Installation von pytest-mock
#
# ```bash
# pip install pytest-mock
# # oder
# uv add pytest-mock
# ```
#
# - Wrapper um `unittest.mock`
# - Bietet `mocker` Fixture für einfache Verwendung
# - Automatisches Cleanup nach jedem Test

# %% [markdown]
#
# ## Mock und MagicMock
#
# - `Mock`: Objekt, das jeden Methodenaufruf akzeptiert
# - `MagicMock`: Wie Mock, aber mit Magic Methods
# - Beide zeichnen alle Interaktionen auf

# %%
from unittest.mock import Mock, MagicMock

# %%
mock_service = Mock()

# %%
mock_service.some_method()

# %%
mock_service.any_attribute.nested.method("arg1", key="value")

# %%
mock_service.some_method.call_count

# %%
mock_service.any_attribute.nested.method.call_count

# %% [markdown]
#
# ## Rückgabewerte konfigurieren

# %%
mock_inventory = Mock()

# %%
mock_inventory.check_stock.return_value = True

# %%
mock_inventory.check_stock("PROD-1", 10)

# %%
mock_inventory.reserve_items.return_value = True
mock_inventory.reserve_items("PROD-1", 10)

# %% [markdown]
#
# ## Side Effects
#
# - Verschiedene Rückgabewerte bei mehreren Aufrufen
# - Oder: Exceptions auslösen

# %%
mock = Mock()
mock.method.side_effect = [True, False, True]

# %%
mock.method()

# %%
mock.method()

# %%
mock.method()

# %%
mock_payment = Mock()
mock_payment.process_payment.side_effect = ConnectionError("Network error")

# %%
try:
    mock_payment.process_payment(100.0, "test@example.com")
except ConnectionError as e:
    print(f"Caught: {e}")

# %% [markdown]
#
# ## Assertions auf Mocks

# %%
mock = Mock()
mock.method("arg1", "arg2", key="value")

# %%
mock.method.assert_called()

# %%
mock.method.assert_called_once()

# %%
mock.method.assert_called_with("arg1", "arg2", key="value")

# %%
mock.method.assert_called_once_with("arg1", "arg2", key="value")

# %%
mock.method.call_args

# %%
mock.method.call_args_list

# %% [markdown]
#
# ## Typsichere Mocks mit `spec`
#
# - `spec`: Mock hat nur Attribute des angegebenen Typs
# - Verhindert Tippfehler und falsche Methodenaufrufe
# - Empfohlen für alle produktiven Tests

# %%
from abc import ABC, abstractmethod

class InventoryService(ABC):
    @abstractmethod
    def check_stock(self, product_id: str, quantity: int) -> bool:
        ...

    @abstractmethod
    def reserve_items(self, product_id: str, quantity: int) -> bool:
        ...

# %%
mock_inventory = Mock(spec=InventoryService)

# %%
mock_inventory.check_stock.return_value = True
mock_inventory.check_stock("PROD-1", 5)

# %%
try:
    mock_inventory.nonexistent_method()
except AttributeError as e:
    print(f"Error: {e}")

# %% [markdown]
#
# ## Die `mocker` Fixture
#
# - pytest-mock stellt die `mocker` Fixture bereit
# - Automatisches Cleanup nach jedem Test
# - Zugriff auf alle Mock-Funktionen

# %% [markdown]
#
# ### Beispiel: Test mit mocker
#
# ```python
# def test_order_with_mocks(mocker):
#     # Create mocks
#     mock_inventory = mocker.Mock(spec=InventoryService)
#     mock_payment = mocker.Mock(spec=PaymentGateway)
#     mock_notifications = mocker.Mock(spec=NotificationService)
#
#     # Configure behavior
#     mock_inventory.check_stock.return_value = True
#     mock_inventory.reserve_items.return_value = True
#     mock_payment.process_payment.return_value = True
#
#     # Create processor with mocks
#     processor = OrderProcessor(mock_inventory, mock_payment, mock_notifications)
#     order = Order("ORD-001", "test@example.com", [OrderItem("P1", 1, 10.0)])
#
#     # Act
#     result = processor.process_order(order)
#
#     # Assert
#     assert result.status == OrderStatus.CONFIRMED
#     mock_notifications.send_order_confirmation.assert_called_once()
# ```

# %% [markdown]
#
# ## Manuelle Doubles vs. Mock-Framework
#
# | Aspekt | Manuelle Doubles | Mock-Framework |
# |--------|------------------|----------------|
# | Lesbarkeit | Explizit, klar | Kann unübersichtlich werden |
# | Wiederverwendbarkeit | Hoch | Gering |
# | Flexibilität | Begrenzt | Sehr hoch |
# | Setup-Aufwand | Höher | Geringer |
# | Typsicherheit | Vollständig | Mit `spec` möglich |

# %% [markdown]
#
# ## Empfehlung
#
# - Beginnen Sie mit manuellen Doubles für häufig verwendete Abhängigkeiten
# - Verwenden Sie Mocks für einmalige oder komplexe Szenarien
# - Immer `spec` verwenden für Typsicherheit
# - Bevorzugen Sie `assert_called_once_with()` gegenüber `assert_called()`

# %% [markdown]
#
# ## Workshop: Tests mit pytest-mock
#
# Öffnen Sie das Projekt `TestDoubles` und betrachten Sie die Tests:
#
# 1. `tests/test_with_doubles.py` - Tests mit manuellen Doubles
# 2. `tests/test_with_mocks.py` - Tests mit pytest-mock
#
# Vergleichen Sie die beiden Ansätze und diskutieren Sie:
# - Welcher Ansatz ist lesbarer?
# - Welcher ist flexibler?
# - Wann würden Sie welchen verwenden?
