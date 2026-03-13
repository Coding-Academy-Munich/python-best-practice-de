# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Clean Code: Funktionen (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Clean Code: Funktionen
#
# Fasse Operationen, die logisch zusammengehören, als sorgfältig benannte
# Funktionen zusammen
#
# - Besser lesbar
# - Einfacher zu testen
# - Wird eher wiederverwendet
# - Fehler sind weniger wahrscheinlich

# %% [markdown]
#
# ## Die 1. Clean Code Regel für Funktionen
#
# - Funktionen sollten kurz sein
# - Kürzer als man meint!
# - Maximal 4 Zeilen!

# %% [markdown]
#
# ## Weniger strikte Regeln
#
# (Aus den C++ Core Guidelines)
#
# - Funktionen sollten auf einen Bildschirm passen
# - Große Funktionen sollten in kleinere, zusammenhängende und benannte
#   Funktionen aufgeteilt werden
# - Funktionen mit einer bis fünf Zeilen sollten als normal angesehen werden

# %% [markdown]
#
# ## Konzentration auf eine Aufgabe
#
# - Funktionen sollten eine Aufgabe erfüllen ("do one thing")
# - Sie sollten diese Aufgabe gut erfüllen
# - Sie sollten nur diese Aufgabe erfüllen

# %%
def do_stuff(a: int, b: int, results: list[int]):
    # Get measurement from sensors based on config data...
    measurement = a + b
    # ... and perform a complex computation
    new_result = measurement + 1
    # ... save the result to the list of results
    if new_result > 0:
        results.append(new_result)
    # ... print all results
    for result in results:
        print(result)
    # ... and return the result
    return new_result


# %%
all_results = [12, 43]
new_result = do_stuff(2, 4, all_results)
print(f"new_result = {new_result}, all_results = {all_results}")


# %% [markdown]
#
# Wir können die Implementierung verbessern, indem wir die Funktion in mehrere
# Funktionen aufteilen, die jeweils eine Aufgabe erfüllen:

# %%
def get_measurement(a: int, b: int) -> int:
    return a + b


# %%
def compute_data_for_next_timestep(measurement: int) -> int:
    return measurement + 1


# %%
def is_valid_result(result: int) -> bool:
    return result > 0


# %%
def save_result(new_result: int, results: list[int]):
    results.append(new_result)


# %%
def print_results(results: list[int]):
    for result in results:
        print(result)


# %% [markdown]
#
# Die resultierende Funktion ist besser:

# %%
def perform_measurement_and_process_result(a: int, b: int, results: list[int]):
    measurement = get_measurement(a, b)
    new_result = compute_data_for_next_timestep(measurement)
    if is_valid_result(new_result):
        save_result(new_result, results)
    print_results(results)
    return new_result


# %%
all_results = [12, 43]
new_result = perform_measurement_and_process_result(2, 4, all_results)
print(f"new_result = {new_result}, all_results = {all_results}")


# %% [markdown]
#
# ### Fragen
#
# - Ist die Funktion `perform_measurement_and_process_result()` wirklich besser?
# - Konzentriert sie sich auf eine Aufgabe?
# - Unterscheiden sich Ihre Aufgaben von `do_stuff()`?
# - Warum (nicht)?

# %% [markdown]
#
# ## Hilfsmittel: Änderungsgründe
#
# - Welche möglichen Änderungsgründe gibt es?
# - Wie viele davon betreffen die jeweilige Funktion?

# %% [markdown]
#
# | Änderungsgrund        | `do_stuff()` | `perform_measurement_and_process_result()` |
# | --------------------- | :----------- | :----------------------------------------- |
# | Messung               | ✓           | ❌ `get_measurement()`                    |
# | Berechnung            | ✓           | ❌ `compute_data_for_next_timestep()`     |
# | Speichern             | ✓           | ❌ `save_result()`                        |
# | Drucken               | ✓           | ❌ `print_results()`                      |
# | Neue/andere Tätigkeit | ✓           | ✓                                         |

# %% [markdown]
#
# # Abstraktionsebenen
#
# - Alles, was die Funktion in ihrem Rumpf tut, sollte eine (und nur eine)
#   Abstraktionsebene unterhalb der Funktion selbst sein.
# - Beispiel: `perform_measurement_and_process_result()`
# - Gegenbeispiel: `create_and_distribute_exam()`:

# %%
def create_and_distribute_exam(subject):
    # high level abstraction
    exam = create_exam_using_chatgpt(subject)

    # low level abstraction
    with open(f"{subject}_exam.pdf", "w") as file:
        # Code to write the PDF header...
        for question in exam.questions:
            # Code to convert the question to PDF...
            file.write(f"{question}\n")


# %% [markdown]
#
# ## Kontrolle der Abstraktionsebenen: "Um-Zu"-Absätze
#
# `perform_measurement_and_process_result()`:
#
# Um eine Messung durchzuführen und das Ergebnis zu verarbeiten:
# - Hole ein Messergebnis
# - Berechne die Daten für den nächsten Zeitschritt
# - Speichere das Ergebnis, falls es gültig ist
# - Drucke alle Ergebnisse, unabhängig davon, ob das neue Ergebnis gültig ist

# %% [markdown]
#
# ## Kommentare als "Um-Zu"-Absätze
#
# - Beim Schreiben von Code können wir das "Um-Zu"-Muster verwenden, um die
#   Abstraktionsebenen zu kontrollieren
# - Wir können die "Um-Zu"-Absätze als Kommentare schreiben bevor wir den Code
#   schreiben
# - Meistens wird jeder Absatz zu einer Funktion

# %%
def process_order(order_id: str) -> None:  # type: ignore
    pass

# %% [markdown]
#
# ## Funktionen als "Um-Zu"-Absätze
#
# Wir können die "Um-Zu"-Absätze auch gleich als Funktionsaufrufe schreiben:


# %%
def process_user_registration(username: str, password: str, email: str) -> None:  # type: ignore
    pass

# %% [markdown]
#
# ## Die Step-Down-Regel
#
# - Wir wollen, dass sich der Code wie eine Erzählung von oben nach unten liest
# - Auf jede Funktion sollten die Funktionen eine Abstraktionsebene darunter
#   folgen

# %% [markdown]
#
# ## Mini-Workshop: Do one Thing
#
# Die Funktion `handle_money_stuff()` macht mehr als eine Sache.
#
# Teilen Sie sie in mehrere Funktionen auf, so dass jede nur eine Sache tut.
# Stellen Sie sicher, dass
# - jede Funktion ihre Aufgabe gut erfüllt und sich auf einer einzigen
#   Abstraktionsebene befindet,
# - alle Namen angemessen sind, und
# - der Code leicht zu verstehen ist.
#
# *Tipp:* Beginnen Sie damit, die Variablen gemäß den Kommentaren umzubenennen,
# um den Rest der Arbeit zu vereinfachen.


# %%
# Name der Wochentage
lst_dns = ["Mon", "Tue", "Wed", "Thu", "Fri"]


# %% [markdown]
#
# Die Funktion `handle_money_stuff()` hat folgende Parameter:
#
# - den Wochentag (`i_dow`, day of week),
# - das Gehalt pro Tag (`f_spd`, salary per day),
# - den Namen des Angestellten (`str_n`, name) und
# - einen Liste der bisher gezahlten Gehälter (`lst_slrs`, salaries).
#
# Das neue Gehalt wird an die Liste `lst_slrs` angehängt.
#
# Die Funktion gibt die zu zahlende Steuer zurück.

# %%
def handle_money_stuff(i_dow: int, f_spd: float, str_n: str, lst_slrs: list):
    # Get the day of week from the list of days.
    # We count Sunday as 1, Monday as 2, etc. but the work week starts on Monday.
    str_dow = lst_dns[i_dow - 1]
    # Compute the salary so far based on the day
    f_ssf = (i_dow - 1) * f_spd
    # The tax
    f_t = 0.0
    if f_ssf > 500.0 and f_ssf <= 1000.0:
        f_t = f_ssf * 0.05
    elif f_ssf > 1000.0 and f_ssf <= 2000.0:
        f_t = f_ssf * 0.1
    else:
        f_t = f_ssf * 0.15
    # Update salary based on the tax to pay
    f_ssf = f_ssf - f_t
    # Add the salary to the list of all salaries paid
    lst_slrs.append(f_ssf)
    print(f"{str_n} worked till {str_dow} and earned ${f_ssf} this week.")
    print(f"Their taxes were ${f_t}.")
    return f_t


# %%
_salaries = [2345, 1234]
_result = handle_money_stuff(4, 200, "Joe", _salaries)
print(_result)

# %%
assert _salaries == [2345, 1234, 570]
assert _result == 30

# %%
