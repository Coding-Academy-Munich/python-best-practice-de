# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>SOLID: Single Responsibility Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# - Problem: Zu viel Funktionalität in einer Klasse
# - Sowohl SOLID als auch GRASP haben jeweils ein Pattern dafür/dagegen

# %% [markdown]
#
# ## Single Responsibility Principle (SRP, SOLID)
#
# - Ein Modul sollte nur einen einzigen Grund haben, sich zu ändern
# - Alternative Formulierung: Ein Modul sollte nur gegenüber einem einzigen
#   Aktor verantwortlich sein
# - Der Name kann leicht falsch verstanden werden:
#   - Responsibility-Driven Design (RDD) ist ein etabliertes Vorgehen in der
#     Softwareentwicklung
#   - SRP besagt nicht, dass jede Klasse nur eine einzige Verantwortung (im RDD-Sinne)
#     haben darf

# %% [markdown]
#
# ### Wie entdecken wir eine Verletzung des SRP?
#
# - Analyse von Änderungen, die aus Anforderungen entstehen könnten
# - Betrachtung der Akteure, die die Klasse verwenden/Änderungen anfordern
# - Analyse des Codes auf mögliche Änderungen
# - Code Smell: Divergent Change

# %% [markdown]
#
# ### Beispiel: Verletzung des SRP
#
# Wir haben die folgende Funktion.
#
# - Verletzt sie das SRP?
# - Was können wir dagegen tun?

# %%
def compute_save_and_print_results(a: int, b: int, results: list) -> int:
    # complex computation...
    new_result = a + b
    # save result to persistent storage...
    results.append(new_result)
    # print report...
    for r in results:
        print(f"Result: {r}")
    # provide information about the new result...
    return new_result


# %%
my_results = []


# %%

# %%

# %% [markdown]
#
# ### Was sind die Gründe, dass sich diese Funktion ändert?
#
# - Die komplexe Berechnung
# - Das Speichern der Ergebnisse
# - Die Formatierung des Berichts
# - Die Information, die im Report enthalten ist
# - Die Teile oder Reihenfolge der Berechnung

# %%
def compute_result(a: int, b: int) -> int:
    return a + b


# %%
def save_result(result: int, results: list):
    results.append(result)


# %%
def print_report(results):
    for r in results:
        print(f"Result: {r}")


# %%
def process_new_sensor_data(a: int, b: int, results: list) -> int:
    new_result = compute_result(a, b)
    save_result(new_result, results)
    print_report(results)
    return new_result


# %%
my_sensor_data = []

# %%

# %%

# %% [markdown]
#
# - Wir haben die Menge an Code verdoppelt
# - Haben wir wirklich eine Verbesserung erreicht?

# %% [markdown]
#
# ### Was sind die Gründe, dass sich die neue Funktion ändert?
#
# - <del>Die komplexe Berechnung</del> $\rightarrow$ `compute_result()`
# - <del>Das Speichern der Ergebnisse</del> $\rightarrow$ `save_result()`
# - <del>Die Art, in der der Bericht ausgedruckt wird</del>
#   $\rightarrow$ `print_report()`
# - <del>Die Information, die im Report enthalten ist</del>
#   $\rightarrow$ `print_report()`
# - Die Teile oder Reihenfolge der Berechnung

# %% [markdown]
#
# - Die Funktion verletzt immer noch das Command-Query-Separation-Prinzip (CQS)
#   - Sie hat Seiteneffekte (Speichern und Drucken)
#   - Sie gibt einen Wert zurück (das neue Ergebnis)

# %% [markdown]
#
# ## Command-Query Separation (CQS)
#
# - Eine Funktion sollte entweder eine Abfrage (Query) oder eine Anweisung
#   (Command) sein, aber nicht beides
# - Eine Abfrage ist eine Funktion, die einen Wert zurückgibt, aber keine
#   beobachtbaren Seiteneffekte hat
# - Eine Anweisung ist eine Funktion, die keine Werte zurückgibt, aber
#   beobachtbare Seiteneffekte hat
# - Eine Funktion, die CQS nicht erfüllt verletzt meistens das SRP

# %%
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]

# %%

# %%

# %%

# %%

# %% [markdown]
#
# ## Workshop: CQS
#
# Ein Verkaufssystems für Veranstaltungstickets speichert die Anzahl der noch
# verfügbaren Tickets für verschiedene Veranstaltungen in einer Variable `events`
# und die Anzahl der erfolgreichen/fehlgeschlagenen Ticketkäufe in Variablen
# `tickets_sold` und `failed_purchases`.

# %%
events = {"Cats": 10, "Les Miserables": 1, "Phantom of the Opera": 8}
tickets_sold = 0
failed_purchases = 0

# %% [markdown]
#
# Die Klasse `User` wurde folgendermaßen implementiert:

# %%
from dataclasses import dataclass, field


# %%
@dataclass
class User:
    events: dict = field(default_factory=dict)

    def buy_ticket(self, event: str, number_of_tickets: int):
        if events.get(event, 0) < number_of_tickets:
            return f"Sorry, there are not enough tickets for {event}."
        else:
            events[event] = events.get(event, 0) - number_of_tickets
        self.events[event] = self.events.get(event, 0) + number_of_tickets

        return f"You have {self.events.get(event, 0)} tickets for {event}."

    @staticmethod
    def register_sale_and_print(sales_result):
        print(sales_result)
        if sales_result.startswith("Sorry"):
            global failed_purchases
            failed_purchases += 1
        else:
            number_of_tickets = int(sales_result.split()[2])
            print(f"Tickets sold: {number_of_tickets}")
            global tickets_sold
            tickets_sold += number_of_tickets


# %% [markdown]
#
# Das System wird folgendermaßen verwendet:
#
# - Ein Benutzer kauft Tickets für eine Veranstaltung

# %%
user = User()

# %%
result = user.buy_ticket("Cats", 2)
user.register_sale_and_print(result)

# %%
result = user.buy_ticket("Les Miserables", 2)
user.register_sale_and_print(result)

# %% [markdown]
#
# - Wir wollen wissen, wie viele Tickets ein Benutzer für eine Veranstaltung hat
#   und wie viele noch verfügbar sind:

# %%
print(user.buy_ticket("Cats", 0))
print(f"There are {events.get('Cats', 0)} tickets left for Cats.")

# %% [markdown]
#
# Es stellt sich heraus, dass das System sehr fehleranfällig ist.
#
# - Welche der besprochenen Prinzipien werden verletzt?
# - Implementieren Sie eine verbesserte Version des Systems.

# %% [markdown]
# *Antwort:* 

# %% [markdown]
#
# - Wir lassen die globalen Variablen unverändert, es wäre aber besser, sie zu
#   kapseln
# - Wir isolieren die Verantwortung zum Kaufen des Tickets in einer eigenen
#   Methode
# - Die neuen Methoden befolgen CQS

# %%

# %%

# %%

# %%

# %%
