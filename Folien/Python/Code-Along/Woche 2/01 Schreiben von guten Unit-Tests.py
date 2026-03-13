# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Schreiben von guten Unit-Tests</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Welche Form hat ein Unit Test?
#
# - Arrange / Given
# - Act / When
# - Assert / Then

# %%


# %% [markdown]
#
# ## Wie finden wir gute Tests?

# %% [markdown]
#
# ## Versuch: Erschöpfendes Testen
#
# - Wir schreiben erschöpfende Tests, d.h. Tests, die alle möglichen Eingaben eines
#   Programms abdecken

# %% [markdown]
#
# - Erschöpfendes Testen ist nicht möglich
# - Beispiel Passworteingabe:
#   - Angenommen, Passwörter mit maximal 20 Zeichen sind zulässig,
#     80 Eingabezeichen sind erlaubt (große und kleine Buchstaben, Sonderzeichen)
#   - Das ergibt $80^{20}$ = 115.292.150.460.684.697.600.000.000.000.000.000.000
#     mögliche Eingaben
#   - Bei 10ns für einen Test würde man ca. $10^{24}$ Jahre brauchen, um alle Eingaben
#     zu testen
#   - Das Universum ist ungefähr $1.4 \times 10^{10}$ Jahre alt

# %% [markdown]
#
# ## Effektivität und Effizienz von Tests
#
# - Unit-Tests sollen effektiv und effizient sein
#   - Effektiv: Die Tests sollen so viele Fehler wie möglich finden
#   - Effizient: Wir wollen die größte Anzahl an Fehlern mit der geringsten Anzahl
#     an möglichst einfachen Tests finden
# - Effizienz ist wichtig, da Tests selbst Code sind, der gewartet werden muss und
#   Fehler enthalten kann

# %% [markdown]
#
# ## Eigenschaften von guten Unit-Tests
#
# Unit-Tests sollen
# - automatisiert sein: keine manuelle Interaktion
# - selbsttestend sein: Pass/Fail
# - feingranular sein
# - isoliert sein
# - zu jedem Zeitpunkt erfolgreich ausführbar sein
# - effektiv und effizient sein
#   - nicht viel Zeit zur Ausführung benötigen
#   - für alle wichtigen Systembestandteile geschrieben werden
#   - alle wichtigen Zustände jedes getesteten Elements abdecken

# %% [markdown]
#
# ## Wie schreibt man gute Unit-Tests?
#
# - Teste beobachtbares Verhalten, nicht Implementierung
# - Teste kleine Einheiten
# - Verwende Test-Doubles dann (aber auch nur dann), wenn eine Abhängigkeit
#   "eine Rakete abfeuert"
# - Bevorzuge Tests von Werten gegenüber Tests von Zuständen
# - Bevorzuge Tests von Zuständen gegenüber Tests von Verhalten
# - (Diese Regeln setzen voraus, dass der Code solche Tests erlaubt)

# %% [markdown]
#
# ### Warum Tests von beobachtbarem Verhalten, nicht Implementierung?
#
# Beobachtbares Verhalten
# - ist leichter zu verstehen
# - ist stabiler als Implementierung
# - entspricht eher dem Kundennutzen

# %% [markdown]
#
# ## Teste beobachtbares Verhalten, nicht Implementierung
#
# - Abstrahiere so weit wie möglich von Implementierungsdetails
#   - Auch auf Unit-Test Ebene
# - Oft testen sich verschiedene Methoden gegenseitig
# - Dies erfordert manchmal die Einführung von zusätzlichen Methoden
#     - Diese Methoden sollen für Anwender sinnvoll sein, nicht nur für Tests
#     - Oft "abstrakter Zustand" von Objekten
#     - **Nicht:** konkreten Zustand öffentlich machen

# %%
class Stack:
    def __init__(self):
        self._items = []

    def push(self, new_item):
        self._items.append(new_item)

    def pop(self):
        return self._items.pop()


# %%
my_stack = Stack()
my_stack.push(5)

# %%
assert my_stack._items == [5]  # noqa <- This might tell you something :)

# %% [markdown]
#
# ## Teste kleine Einheiten (bei Unit-Tests)
#
# - Test von kleinen Einheiten
#   - spezifizieren das Verhalten der getesteten Einheit besser
#   - erleichtern die Lokalisierung von Fehlern
#   - sind leichter zu pflegen
# - Tests größerer Einheiten oder des Gesamtsystems sind wichtig als
#   - Integrationstests
#   - Systemtests
#   - Akzeptanztests

# %% [markdown]
#
# ## Test Doubles
#
# - Test Double: Vereinfachte Version einer Abhängigkeit im System
#   - Dummy, Stub, Fake, Spy, Mock
# - Test Doubles sind wichtig zum Vereinfachen von Tests
# - Aber: zu viele oder komplexe Test Doubles machen Tests unübersichtlich
#   - Was wird von einem Test eigentlich getestet?


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
# ## Werte > Zustand > Kommunikation
#
# - Verständlicher
# - Leichter zu testen
# - Oft stabiler gegenüber Refactorings
#
# Ausnahme: Testen von Protokollen


# %% [markdown]
#
# ### Funktionen/Werte

# %%
def add(x, y):
    return x + y

# %%


# %% [markdown]
#
# ### Zustand

# %%
class Adder:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.result = None

    def add(self):
        self.result = self.x + self.y


# %%

# %%

# %%


# %% [markdown]
#
# ### Verhalten

# %%
def call_fun(fun):
    _hidden_result = fun(2, 3)
    # Presumably do something with _hidden_result...
    return "How do you test that fun was called?"


# %%

# %%
class AdderSpy:
    def __init__(self):
        self.was_called = False
        self.args = None

    def __call__(self, x, y):
        self.was_called = True
        self.args = (x, y)
        return x + y

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Wie schreibt man testbaren Code?
#
# - Umwandeln von weniger testbarem in besser testbaren Stil
#   - Beobachtbarkeit
#   - Keine globalen oder statischen Daten
#   - Funktionale (unveränderliche) Datenstrukturen
# - Gutes objektorientiertes Design
#   - Hohe Kohäsion
#   - Geringe Kopplung, Management von Abhängigkeiten
# - Etc.


# %% [markdown]
#
# ## Prozess
#
# - Iteratives Vorgehen
#   - Kleine Schritte mit Tests
# - Test-Driven Development (TDD)
#   - Schreiben von Tests vor Code

# %% [markdown]
#
# ## Workshop: Bessere Testbarkeit
#
# - Wie können Sie Tests für die folgenden Funktionen/Klassen schreiben?
# - Wie können Sie die folgenden Funktionen/Klassen verbessern, um sie besser
#   testbar zu machen?
# - Was für Nachteile ergeben sich dadurch?

# %%
def make_counter():
    result = 0

    def count():
        nonlocal result
        result += 1
        return result

    return count


# %%
count = make_counter()

# %%
for i in range(3):
    print(count())

# %%

# %%

# %%

# %%
from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1


# %%
class Switch:
    def __init__(self):
        self._state = State.OFF

    def toggle(self):
        self._state = State.ON if self._state == State.OFF else State.OFF
        print(f"Switch is {'OFF' if self._state == State.OFF else 'ON'}")


# %%
s = Switch()

# %%
for i in range(3):
    s.toggle()


# %%

# %%

# %%

# %%

# %%
def print_fib(n):
    a = 0
    b = 1
    for i in range(n):
        print(f"fib({i}) = {b}")
        tmp = a
        a = b
        b = tmp + b


# %%
print_fib(5)

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop: Tests für die Einkaufslisten-Implementierung
#
# Fügen Sie zur Implementierung einer Einkaufsliste in `examples/ShoppingListPytestSK`
# geeignete Unit-Tests hinzu.
#
# Beachten Sie, dass Sie manche der Tests auch als Doctests schreiben können.
#
# (Falls Sie die Einkaufsliste in einem vorherigen Workshop bereits implementiert haben,
# ist es besser, Sie verwenden stattdessen Ihre eigene Implementierung.)
