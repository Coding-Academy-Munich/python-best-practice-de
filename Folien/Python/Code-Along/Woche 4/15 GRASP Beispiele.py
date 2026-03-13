# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Beispiele</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Problem: Anbindung an externe Bibliotheken
#
# - Wir haben externe Bibliotheken, die wir in unserem Programm verwenden wollen.
# - Leider sind diese plattformspezifisch.
# - Wie wollen unsere Anwendung so schreiben, dass wir die Bibliothek austauschen
#   können, ohne die Anwendung ändern zu müssen.

# %%
class ExternalLibraryPC:
    @staticmethod
    def specific_request(n: int, text: str) -> str:
        return f"ExternalLibraryPC: {text * n}"


# %%
class ExternalLibraryMac:
    @staticmethod
    def specific_request(text: str, n: int, sep: str = "") -> str:
        return f"ExternalLibraryMac: {(text + sep) * n}"


# %% [markdown]
#
# Wie können wir das Problem mit den GRASP-Patterns lösen?

# %% [markdown]
#
# ### Protected Variations
#
# - Wir können die Anbindung an die externe Bibliothek als eine geschützte
#   Variation betrachten.
# - Der Variationspunkt ist der Aufruf der Funktion, die den String erzeugt.
# - Alle anderen Teile unserer Anwendung sollen vor Änderungen geschützt sein.

# %% [markdown]
#
# ### Indirection/Polymorphie
#
# - Welchen Mechanismus können wir dafür verwenden?
# - Wir führen eine Indirektion ein, und zwar konkret ein Interface, das die
#   gewünschte Funktionalität abstrahiert.
# - Dieses Interface ist eine Pure Fabrication


# %%
from abc import ABC, abstractmethod


# %%
class LibraryAdapter(ABC):
    @abstractmethod
    def process_string(self, text: str, sep: str, n: int) -> str: ...


# %% [markdown]
#
# Wir verwenden das Interface in unserer Anwendung:

# %%
class Application:
    def __init__(self, adapter: LibraryAdapter):
        self.adapter = adapter

    def process(self, text: str) -> str:
        return self.adapter.process_string(text, "! ", 3)


# %% [markdown]
#
# Wir implementieren das Interface für jede Variation, die wir unterstützen wollen:

# %%
class PcAdapter(LibraryAdapter):
    def process_string(self, text: str, sep: str, n: int) -> str:
        return ExternalLibraryPC.specific_request(n, text + sep)


# %%
class MacAdapter(LibraryAdapter):
    def process_string(self, text: str, sep: str, n: int) -> str:
        return ExternalLibraryMac.specific_request(text, n, sep)


# %% [markdown]
#
# Jetzt können wir den Variationspunkt in unserer Anwendung austauschen:

# %%
app = Application(PcAdapter())
print(app.process("Go"))

# %%
app = Application(MacAdapter())
print(app.process("Stop"))


# %% [markdown]
#
# ## Beispiel: Adapter-Pattern
#
# <img src="img/pat_adapter.svg"
#      style="display: block; margin: auto; width: 80%;"/>

# %% [markdown]
#
# ## Beispiel: Strategie-Pattern
#
# Bei der Auswahl der nächsten Aktion durch den Spieler in unserem Adventure-Spiel
# hatten wir das Strategie-Pattern angewendet:
#
# <img src="img/pat_strategy.svg"
#      style="display:block;margin:auto;width:80%"/>
#
# Wie können wir diese Anwendung des Strategie-Patterns mit den abstrakten
# GRASP-Patterns analysieren?

# %% [markdown]
#
# ## Beispiel: Template-Methoden-Pattern
#
# Analysieren Sie, wie sich die Anwendung der abstrakten GRASP-Patterns
# auf das Template-Methoden-Pattern von der Anwendung auf das Strategie-Pattern
# unterscheidet.
#
# <img src="img/pat_template_method.svg"
#      style="display:block;margin:auto;width:40%"/>

# %% [markdown]
#
# ## Workshop: GRASP-Abstraktionen
#
# Analysieren Sie die folgenden Beispiele auf ähnliche Art und Weise:

# %% [markdown]
#
# ### Beispiel: Command-Pattern
#
# Wir haben das Command-Pattern verwendet, um die Aktionen des Spielers
# zu realisieren. Wie können wir das mit den abstrakten GRASP-Patterns
# analysieren?
#
# <img src="img/pat_command.svg"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown]
#
# ### Beispiel: Push Observer
#
# Um Benachrichtigungen über Änderungen im Spielzustand zu erhalten, haben
# wir eine Variante des Observer-Patterns verwendet, bei der der Observer
# mehrere `notify...()`-Methoden hat, die von den Subjects aufgerufen werden.
#
# Analysieren Sie diese Anwendung des Observer-Patterns mit den abstrakten
# GRASP-Patterns.
#
# <img src="img/pat_observer_push.svg"
#      style="display:block;margin:auto;width:100%"/>
