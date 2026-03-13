# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GoF: Command Pattern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Beispiel: Textverarbeitung
#
# - `Document`-Klasse mit `modify()` und `append()`-Methoden

# %%
from dataclasses import dataclass


# %%
@dataclass
class Document:
    state: str = "<empty>"

    def modify(self, change: str | None):
        print("Document.modify()")
        print("  document state before: ", self.state)
        if change is not None:
            self.state = change
        else:
            self.state = "<empty>"
        print("  document state after:  ", self.state)

    def append(self, text: str, times: int = 1):
        print(f"Document::append({text!r}, {times!r})")
        print("  document state before: ", self.state)
        self.state += text * times
        print("  document state after:  ", self.state)


# %%
doc = Document()
doc.modify("Document Template")
doc.append("-append", 3)
doc.modify(None)


# %% [markdown]
#
# ## Command-Objekte für `Document`
#
# - Wie können wir die Methoden der `Document`-Klasse aufrufen?
# - Verschiedene Aufrufmöglichkeiten:
#   - Menü-System
#   - Toolbar-Buttons
#   - Tastaturkürzel
# - Methoden haben potenziell unterschiedliche Signaturen
# - Wir wollen sie aber möglichst einheitlich handhaben

# %%
from abc import ABC, abstractmethod  # noqa: E402


# %%


# %% [markdown]
#
# ### `ModifyCommandV1`

# %%


# %% [markdown]
#
# ### `AppendCommandV1`

# %%
@dataclass
class AppendCommandV1(CommandV1):
    text: str
    times: int = 1

    def execute(self, doc: Document):
        doc.append(self.text, self.times)


# %% [markdown]
#
# ### Verwendung

# %%

# %%

# %% [markdown]
#
# ## Funktionale Implementierung

# %%

# %%

# %%

# %%

# %%
class CommandV2(ABC):
    @abstractmethod
    def execute(self): ...


# %%
@dataclass
class ModifyCommandV2(CommandV2):
    doc: Document
    change: str | None

    def execute(self):
        self.doc.modify(self.change)


# %%
@dataclass
class AppendCommandV2(CommandV2):
    doc: Document
    text: str
    times: int = 1

    def execute(self):
        self.doc.append(self.text, self.times)


# %% [markdown]
#
# ### Verwendung

# %%

# %%

# %% [markdown]
#
# ## Kommandos mit Undo-Funktionalität

# %%
class CommandV3(ABC):
    @abstractmethod
    def execute(self): ...


# %% [markdown]
#
# ### `ModifyCommandV3`

# %%
@dataclass
class ModifyCommandV3(CommandV3):  # noqa
    doc: Document
    change: str | None

    def execute(self):
        self.doc.modify(self.change)


# %% [markdown]
#
# ### `AppendCommandV3`

# %%
@dataclass
class AppendCommandV3(CommandV3):  # noqa
    doc: Document
    text: str
    times: int = 1

    def execute(self):
        self.doc.append(self.text, self.times)


# %% [markdown]
#
# ### Verwendung

# %%
doc = Document()
template_command = ModifyCommandV3(doc, "Document Template")
append_command = AppendCommandV3(doc, "-append", 3)
clear_command = ModifyCommandV3(doc, None)

# %%
template_command.execute()
append_command.execute()
clear_command.execute()

# %%

# %%

# %%


# %% [markdown]
# <img src="img/command_example.svg"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown]
#
# ## Verbesserte Implementierung

# %%
class Command(ABC):  # noqa: F811
    history = []  # Note this is a class variable!
    redo_stack = []

    def __init__(self, doc: Document):
        self.doc = doc
        self.saved_state = ""

    @abstractmethod
    def do_execute(self): ...

    def execute(self):
        Command.redo_stack.clear()
        self._execute_keeping_redo_stack()

    def _undo_execution(self):
        self.doc.modify(self.saved_state)

    def _execute_keeping_redo_stack(self):
        self.saved_state = self.doc.state
        Command.history.append(self)
        self.do_execute()


# %% [markdown]
#
# ### Undo/Redo

# %%
def undo():
    if not Command.history:
        return
    last = Command.history.pop()
    Command.redo_stack.append(last)
    last._undo_execution()  # noqa


# %%
def redo():
    if not Command.redo_stack:
        return
    last = Command.redo_stack.pop()
    last._execute_keeping_redo_stack()  # noqa


# %% [markdown]
#
# ### `ModifyCommand`

# %%


# %% [markdown]
#
# ### `AppendCommand`

# %%


# %% [markdown]
#
# ### Beispiel-Anwendung

# %%
def run_text_processing():
    doc = Document()
    while True:
        print("Document state:", doc.state)
        print("Commands: [m]odify, [a]ppend, [u]ndo, [r]edo, [q]uit")
        user_input = input("Enter command: ")
        if not user_input or user_input.lower().startswith("q"):
            break
        elif user_input.lower().startswith("u"):
            undo()
        elif user_input.lower().startswith("r"):
            redo()
        else:
            command = create_command(doc, user_input)
            command.execute()


# %%
def create_command(doc: Document, user_input: str) -> Command:
    command, *args = user_input.split()
    if command.lower().startswith("m"):
        new_state = " ".join(args) or "<empty>"
        return ModifyCommand(doc, new_state)
    elif command.lower().startswith("a"):
        text = args[0] if args else "!"
        times = int(args[1]) if len(args) > 1 else 1
        return AppendCommand(doc, text, times)
    else:
        raise ValueError(f"Unknown command: {command}")


# %%

# %% [markdown]
#
# ### Zweck
#
# Kapselung eines Requests als Objekt, um so die Parametrisierung von Clients
# mit verschiedenen Requests, Warteschlangen- oder Logging-Operationen sowie
# das Rückgängigmachen von Operationen zu ermöglichen.

# %% [markdown]
#
# ### Auch bekannt als
#
# Action, Transaction

# %% [markdown]
#
# ### Motivation
#
# Kommandos in grafischen Benutzeroberflächen
#
# - Können auf mehrere Arten aktiviert werden (Menü, Tastatur, Maus)
# - Sollten oft Undo/Redo unterstützen
# - Sollten geloggt werden können
# - Sollten in Warteschlangen abgelegt werden können
# - Sollten für Macros verwendet werden können

# %% [markdown]
#
# Mögliche Lösung: Implementierung als Objekt
#
# - Jedes Kommando wird als Objekt implementiert
# - Das Kommando-Objekt kapselt die Operation und ihre Parameter
# - Das Kommando-Objekt bietet eine Methode `execute()`, die die Operation
#   ausführt

# %% [markdown]
#
# ### Struktur
#
# <img src="img/pat_command.svg"
#      style="display:block;margin:auto;width:40%"/>

# %% [markdown]
# ### Teilnehmer
#
# - `Command`
#   - Deklariert eine Schnittstelle für das Ausführen einer Operation
# - `ConcreteCommand`
#   - Definiert eine Verbindung zwischen einem `Receiver`-Objekt und einer
#     Operation
#   - Implementiert `execute()` durch Aufruf der entsprechenden Operation(en)
#     auf `Receiver`
# - `Client`
#   - Erstellt ein `ConcreteCommand`-Objekt und setzt dessen `Receiver`
# - `Invoker`
#   - Ruft `execute()` auf `ConcreteCommand` auf um die Anfrage auszuführen

# %% [markdown]
# ### Sequenzdiagramm
#
# <img src="img/pat_command_seq.svg"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown]
#
# ### Konsequenzen
#
# - Einfache Erweiterung des Systems durch neue `ConcreteCommand`-Klassen
#   (Open/Closed Principle)
# - Einfache Implementierung von Undo/Redo und anderen erweiterten Funktionen
# - Entkoppelt, das Objekt, das eine Operation auslöst von dem Objekt, das sie
#   ausführt
# - Zusammengesetzte Operationen sind möglich (z.B. Makros, siehe Composite Pattern)

# %% [markdown]
# ### Implementierung
#
# - Für einfache Szenarien kann eine `SimpleCommand`-Klasse, die einen Zeiger
#   auf eine Funktion oder Methode speichert, verwendet werden
# - ...

# %%
from document_commands import Document, Command, undo, redo  # noqa
from typing import Callable  # noqa: E402


# %%
class SimpleCommand(Command):
    def __init__(self, doc: Document, action: Callable, *args, **kwargs):
        super().__init__(doc)
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def do_execute(self):
        self.action(self.doc, *self.args, **self.kwargs)


# %%
doc = Document()
template_command = SimpleCommand(doc, Document.modify, "Document Template")
append_command = SimpleCommand(doc, Document.append, "-123", 2)
modify_command = SimpleCommand(doc, Document.modify, None)

# %%
template_command.execute()
append_command.execute()
modify_command.execute()

# %%
undo()

# %%
undo()

# %%
redo()

# %%
SimpleCommand(
    doc, lambda doc, text: doc.modify(f"{text}? {text}!"), "That's new"
).execute()

# %%
redo()


# %% [markdown]
#
# ## Workshop: Command Pattern
#
# ### Szenario
#
# Banken bieten verschiedene Funktionalitäten an Geldautomaten an, wie
# Kontostand abfragen, Geld abheben, Geld einzahlen und Geld überweisen. In
# unserer Simulation konzentrieren wir uns auf die Einzahlungs- und
# Auszahlungsfunktionen. Wir wollen eine ATM-Software entwerfen, die nicht nur
# diese Transaktionen verarbeitet, sondern auch die letzte Transaktion
# rückgängig machen kann.

# %% [markdown]
#
# ### Ziel
#
# Ihre Aufgabe ist es, die ATM-Operationen mit dem Command Pattern zu
# implementieren, so dass die Funktionalität des Systems in der Zukunft leicht
# zu erweitern ist, und eine Undo-Funktion für die letzte Transaktion
# bereitzustellen.

# %% [markdown]
# ### Starter Code

# %%
class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.balance}")
        else:
            print(f"Insufficient funds. Current Balance: ${self.balance}")

    def get_balance(self):
        return self.balance


# %%
class ATM:
    def __init__(self, initial_balance):
        self.account = Account(initial_balance)

    # TODO: Fügen Sie deposit(), withdraw(), and undo() Operationen mit dem
    # Command Pattern hinzu.
