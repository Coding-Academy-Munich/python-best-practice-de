# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Test-Driven-Development</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Idee
#
# - Verwende Tests, um das Design und die Feature-Entwicklung des Programms
#   voranzutreiben
# - Jeder neue Test beschreibt ein Feature-Inkrement des Programms
# - (Gut testbarer Code entsteht dabei quasi als Nebenprodukt)

# %% [markdown]
#
# ## Problem
#
# Wie können Tests das Design des Programms vorantreiben?

# %% [markdown]
#
# ## Mögliche Antworten
#
# - Tests verwenden die Funktionalität und zeigen komplizierte Interfaces auf
# - Tests ermöglichen Refactoring

# %% [markdown]
#
# ## Refactoring
#
# - Verbessern der Code-Struktur ohne Änderung des Verhaltens
# - Vorgehen in kleinen Schritten
#   - Nach jedem Schritt ist der Code wieder ausführbar
# - Ziele:
#   - Verbessern des Codes
#   - Verbesserung des Designs

# %% [markdown]
#
# ## Refactoring und Tests
#
# - Durch Refactoring wird das Design des Programms in kleinen Schritten verbessert
# - Die Korrektheit dieser Schritte wird durch Tests abgesichert


# %% [markdown]
#
# ## So what???
#
# <img src="img/dev-velocity.png"
#      style="display:block;margin:auto;width:70%"/>


# %% [markdown]
#
# ## Test-Driven Development
#
# - Ziel beim TDD ist nicht in erster Linie, eine hohe Testabdeckung zu erreichen
#   - Typischerweise schreibt man keine Tests für Methoden, von denen man überzeugt
#     ist, dass sie nicht fehlschlagen können
# - Ziel beim TDD ist es, durch Tests ein gutes Design zu entdecken
#   - Beim Schreiben der Tests versucht man, das Interface von Klassen und Funktionen
#     so zu gestalten, dass es leicht zu benutzen ist
#   - Dadurch, dass alle wesentlichen Teile des Programms durch Tests abgesichert
#     sind, kann man das Design durch Refactoring permanent an das aktuelle Feature-Set
#     anpassen


# %% [markdown]
#
# ## Der TDD-Zyklus
#
# - Schreibe einen (minimalen) Test
#   - Der Test testet nur ein einziges neues (Teil-)Feature: **Baby Steps**
#   - Dieser Test schlägt fehl
# - Implementiere die minimale Funktionalität, um den Test zum Laufen zu bringen
#   - Dabei muss man nicht auf sauberen Code oder gutes Design achten
#   - Aber: **Solve Simply**
# - Verbessere den Code
#   - Entferne die unsauberen Konstrukte, die im vorhergehenden Schritt eingefügt wurden
#   - Generalisiere die Implementierung, wenn zu viel Wiederholung entstanden ist
#   - **Dieser Schritt ist nicht optional!!!**


# %% [markdown]
#
# ## Der TDD-Zyklus
#
# - <span style="color: red"><b>Red (fehlschlagender Test)</b></span>
# - <span style="color: green"><b>Green (alle Tests sind wieder grün)</b></span>
# - <span style="color: blue"><b>Clean/Refactor (der Code ist wieder sauber)</b></span>

# %% [markdown]
#
# ## Baby-Steps
#
# - Das System ist nicht stunden- oder tagelang in einem Zustand, in dem es nicht
#   baubar, testbar oder ausführbar ist
# - Dadurch bekommt man bei jeder Änderung schnell Feedback vom Code
# - Häufiges Mergen und CI wird möglich

# %% [markdown]
#
# ## Warum Solve Simply?
#
# - Eine flexible, generische Lösung erhöht oft die Komplexität des Systems
# - Das lohnt sich nur, wenn die Flexibilität auch benötigt wird
# - Entwickler können meist schlecht vorhersehen, an welchen Stellen
#   Flexibilität/Erweiterbarkeit benötigt wird
# - Eine flexible, generische Lösung ist oft sehr viel schwerer zu implementieren
#   als eine einfache Lösung für einen spezielleren Anwendungsfall
# - Die naheliegendste flexible, generische Lösung ist oft nicht der sauberste und
#   wartbare Code

# %% [markdown]
#
# ## Annahmen von Solve Simply
#
# - Es ist durch Refactoring möglich, Code in einen sauberen, wartbaren Zustand zu
#   bekommen, ohne dadurch die Funktionalität zu verändern
# - Es ist möglich, Code iterativ zu erweitern und flexibler zu machen,
#   wenn das erforderlich ist
# - Es ist einfacher, die Refactoring- und Iterations-Schritte durchzuführen, als
#   gleich die endgültige Lösung zu entwickeln
# - Diese Annahmen sind nur dann erfüllt, wenn hinreichend viele, gute
#   Unit-Tests vorliegen

# %% [markdown]
#
# ## Noch besser: TDD + Vorbereitungsschritt
#
# - Refactore den Code, sodass die Änderung einfach wird
#   - Das ist oft nicht so einfach…
#   - Wenn beim Refactoring klar wird, dass Tests fehlen, so werden diese hinzugefügt
# - Führe die einfache Änderung mit dem TDD-Zyklus durch
# - Wiederhole diese Schritte immer wieder

# %% [markdown]
#
# ## Geleitetes Kata: Primfaktorzerlegung
#
# - Eine Übung zu TDD, die zeigt, wie man durch Tests auf eine einfache
#   Implementierung eines Algorithmus geführt werden kann
# - Wichtig ist die Vorgehensweise: Tests sollen das Design treiben
# - Ziel: Lernen inkrementell und iterativ zu arbeiten!

# %% [markdown]
#
# ## Geleitetes Kata: Primfaktorzerlegung
#
# Schreiben Sie eine Funktion
#
# ```python
# compute_prime_factors(n: int) -> list[int]
# ```
# die die Primfaktoren von n in aufsteigender Reihenfolge zurückgibt.
#
# Mehrfach vorkommende Primfaktoren sind in der Liste mehrmals enthalten.
#
# Sie können dazu das Programmgerüst `examples/PrimesStarterKit` hernehmen.

# %%
def compute_prime_factors(n: int) -> list[int]:  # noqa
    return []


# %%
assert compute_prime_factors(1) == []


# %%
def compute_prime_factors(n: int) -> list[int]:
    if n == 2:
        return [2]
    else:
        return []


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]


# %%
def compute_prime_factors(n: int) -> list[int]:
    if n == 2:
        return [2]
    if n == 3:
        return [3]
    return []


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]


# %%
def compute_prime_factors(n: int) -> list[int]:
    result = []
    if n == 2:
        result.append(2)
    elif n == 3:
        result.append(3)
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]


# %%
def compute_prime_factors(n: int) -> list[int]:
    result = []
    if n == 2:
        result.append(2)
    elif n == 3:
        result.append(3)
    elif n == 4:
        result.append(2)
        result.append(2)
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]
assert compute_prime_factors(4) == [2, 2]


# %%
# Generalization/refactoring 1
def compute_prime_factors(n: int) -> list[int]:
    result = []
    if n % 2 == 0:
        result.append(2)
        if n == 4:
            result.append(2)
    elif n == 3:
        result.append(3)
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]
assert compute_prime_factors(4) == [2, 2]


# %%
# Generalization/refactoring 2
def compute_prime_factors(n: int) -> list[int]:
    result = []
    if n % 2 == 0:
        result.append(2)
        n //= 2
        if n % 2 == 0:
            result.append(2)
    elif n == 3:
        result.append(3)
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]
assert compute_prime_factors(4) == [2, 2]


# %%
# Generalization/refactoring 3
def compute_prime_factors(n: int) -> list[int]:
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    while n % 3 == 0:
        result.append(3)
        n //= 3
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]
assert compute_prime_factors(4) == [2, 2]


# %%
def compute_prime_factors(n: int) -> list[int]:
    result = []
    while n % 2 == 0:
        result.append(2)
        n //= 2
    while n % 3 == 0:
        result.append(3)
        n //= 3
    while n % 5 == 0:
        result.append(5)
        n //= 5
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]
assert compute_prime_factors(4) == [2, 2]
assert compute_prime_factors(5) == [5]


# %%
# Final Cleanup
def compute_prime_factors(n: int) -> list[int]:
    result = []
    for factor in range(2, n + 1):
        while n % factor == 0:
            result.append(factor)
            n //= factor
    return result


# %%
assert compute_prime_factors(1) == []
assert compute_prime_factors(2) == [2]
assert compute_prime_factors(3) == [3]
assert compute_prime_factors(4) == [2, 2]
assert compute_prime_factors(5) == [5]


# %% [markdown]
#
# ## Kata: FizzBuzz
#
# Schreiben Sie eine Funktion `fizz_buzz(n)`, die die Zahlen von 1 bis `n`
# ausgibt aber dabei
#
# - jede Zahl, die durch 3 teilbar ist, durch `Fizz` ersetzt
# - jede Zahl, die durch 5 teilbar ist, durch `Buzz` ersetzt
# - jede Zahl, die durch 3 und 5 teilbar ist, durch `FizzBuzz` ersetzt
#
# Zum Beispiel soll `fizz_buzz(31)` die folgende Ausgabe erzeugen:
#
# ```
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# ```

# %%
def fizz_buzz(n):
    for n in range(1, n + 1):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


# %%
fizz_buzz(31)


# %%
def fizzbuzz_number(n: int) -> str:
    return str(n)


# %%
assert fizzbuzz_number(1) == "1"


# %%
def fizzbuzz_number(n: int) -> str:
    if n == 3:
        return "Fizz"
    return str(n)


# %%
assert fizzbuzz_number(1) == "1"
assert fizzbuzz_number(3) == "Fizz"


# %%
def fizzbuzz_number(n: int) -> str:
    if n == 3:
        return "Fizz"
    if n == 5:
        return "Buzz"
    return str(n)


# %%
assert fizzbuzz_number(1) == "1"
assert fizzbuzz_number(3) == "Fizz"
assert fizzbuzz_number(5) == "Buzz"


# %%
def fizzbuzz_number(n: int) -> str:
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# %%
assert fizzbuzz_number(1) == "1"
assert fizzbuzz_number(3) == "Fizz"
assert fizzbuzz_number(5) == "Buzz"
assert fizzbuzz_number(6) == "Fizz"


# %%
def fizzbuzz_number(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# %%
assert fizzbuzz_number(1) == "1"
assert fizzbuzz_number(3) == "Fizz"
assert fizzbuzz_number(5) == "Buzz"
assert fizzbuzz_number(6) == "Fizz"
assert fizzbuzz_number(15) == "FizzBuzz"


# %% [markdown]
#
# ### Implementierungsvariante

# %%
def fizzbuzz_number(n: int) -> str:
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)


# %%
assert fizzbuzz_number(1) == "1"
assert fizzbuzz_number(3) == "Fizz"
assert fizzbuzz_number(5) == "Buzz"
assert fizzbuzz_number(6) == "Fizz"
assert fizzbuzz_number(15) == "FizzBuzz"

# %%
from sys import stdout


# %%
def fizzbuzz(n: int, file=stdout):
    for i in range(1, n + 1):
        print(fizzbuzz_number(i), file=file)


# %%
FIZZBUZZ_RESULTS = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
    "16",
]

# %%
from io import StringIO

# %%
_file = StringIO()
fizzbuzz(16, _file)
assert _file.getvalue().strip() == "\n".join(FIZZBUZZ_RESULTS)


# %%
def fizzbuzz_numbers(n: int) -> list[str]:
    return [fizzbuzz_number(i) for i in range(1, n + 1)]


# %%
assert fizzbuzz_numbers(16) == FIZZBUZZ_RESULTS


# %%
def fizzbuzz_str(n: int) -> str:
    return "\n".join(fizzbuzz_numbers(n))


# %%
assert fizzbuzz_str(16) == "\n".join(FIZZBUZZ_RESULTS)


# %%
def fizzbuzz(n: int) -> None:
    print(fizzbuzz_str(n))
