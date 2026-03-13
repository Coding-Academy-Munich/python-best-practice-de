# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Clean Code: Kommentare und Dokumentation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ## Docstrings
#
# Aus [PEP-257](https://peps.python.org/pep-0257/):
#
# Ein Docstring ist ein String-Literal, das als erste Anweisung in einer Modul-,
# Funktions-, Klassen- oder Methodendefinition auftritt. Ein solcher Docstring
# wird zum `__doc__`-Attribut dieses Objekts.
#
# Alle Module sollten normalerweise Docstrings haben, und alle Funktionen und
# Klassen, die von einem Modul exportiert werden, sollten ebenfalls Docstrings
# haben. Öffentliche Methoden (einschließlich des `__init__` Konstruktors)
# sollten auch docstrings haben. Ein Package kann im Modul-Docstring der Datei
# `__init__.py` im Package-Verzeichnis dokumentiert werden.


# %% [markdown]
#
# ## Docstring-Konventionen
#
# - Einzeilige Docstrings
#   - Verwende dreifache Anführungszeichen
#   - Keine Leerzeile davor oder danach
#   - Eine Phrase, die mit einem Punkt endet
#   - Geschrieben als ein Befehl: "Tu dies", "Gib diesen Wert zurück"
#   - Ist nicht die Signatur der Funktion (die kann durch Introspektion
#     ermittelt werden)
#   - Mehr Informationen in
#     [PEP-257](https://peps.python.org/pep-0257/#one-line-docstrings)

# %% [markdown]
#
# ## Docstring-Konventionen
#
# - Mehrzeilige Docstrings
#   - Zusammenfassungszeile wie ein einzeiliger Docstring
#   - Auf die Zusammenfassungszeile folgt eine Leerzeile
#   - Dann folgt eine ausführlichere Beschreibung, möglicherweise mit Doctests
#   - Auf den Docstring folgt eine Leerzeile
#   - Mehr Informationen in
#     [PEP-257](https://peps.python.org/pep-0257/#multi-line-docstrings)

# %% [markdown]
#
# ## Kommentare
#
# - Kommentare kompensieren unser Unvermögen, uns in Code auszudrücken.
# - Wenn möglich, drücke dich in Code aus, nicht in Kommentaren!
#   - Wann immer du einen Kommentar schreiben willst, prüfe, ob du es nicht im
#     Code tun kannst.
#   - Schreibe lieber Assertions oder Doctests, wenn möglich.
#   - Verwende erklärende Variablen

# %%
# Compute the root of the quadratic equation with coefficients a, b, c.
def root(a, b, c):
    # Use the formula -b +- sqrt(b^2 - 4ac) / 2a to compute the roots
    return (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a), (
        -b - (b**2 - 4 * a * c) ** 0.5
    ) / (2 * a)


# %%
root(1, 0, -1)

# %%
root(1, -5, 6)


# %%
def solve_quadratic_equation(a, b, c):
    """Compute the solution of the equation ax^2 + bx + c == 0.

    >>> solve_quadratic_equation(1, 0, -1)
    (1.0, -1.0)
    >>> solve_quadratic_equation(1, -5, 6)
    (3.0, 2.0)
    """
    root = (b**2 - 4 * a * c) ** 0.5
    d = 2 * a
    return (-b + root) / d, (-b - root) / d


# %%
from doctest import testmod

# %%
testmod()

# %%
# Multiply the seconds in a day times the days of work.
ds = 60 * 60 * 24 * 4

# %%
DAYS_OF_WORK = 4
SECONDS_PER_DAY = 60 * 60 * 24
duration_in_seconds = SECONDS_PER_DAY * DAYS_OF_WORK


# %% [markdown]
#
# ## Wie Kommentare scheitern
#
# - Kommentare sind schwer zu pflegen
# - Deshalb lügen sie oft
# - Sie werden nicht geändert, wenn der Code aktualisiert wird
# - Sie werden nicht verschoben, wenn der Code verschoben wird

# %% [markdown]
# ```python
# # Check to see if the employee is eligible for full benefits
# if (employee.flags & HOURLY_FLAG) and (employee.age > 65):
#     ...
# ```
#
# versus
#
# ```python
# if employee.is_eligible_for_full_benefits():
#     ...
# ```

# %% [markdown]
#
# ## PEP-8 Regeln für Kommentare
#
# Befolge die [PEP-8](https://peps.python.org/pep-0008/#comments) Richtlinien
# für Kommentare:
#
# - Halte die Kommentare aktuell, wenn sich der Code ändert.
# - Kommentare sollten aus vollständigen Sätzen bestehen.
#   - Das erste Wort wird großgeschrieben, es sei denn, es ist ein Bezeichner.
#   - Bezeichner sollten niemals geändert werden
#   - Verwende in Kommentaren, die aus mehreren Sätzen bestehen, zwei
#     Leerzeichen nach einem Punkt am Satzende.
# - Die Kommentare müssen klar und leicht verständlich sein.
# - Python-Coder aus nicht englischsprachigen Ländern: Bitte schreibe deine
#   Kommentare auf Englisch, es sei denn, du bist 120% sicher, dass der Code
#   niemals von Leuten gelesen wird, die deine Sprache nicht sprechen.


# %% [markdown]
#
# ## Gute Kommentare
#
# Kommentare sind gut, wenn sie
#
# - aus juristischen Gründen notwendig sind
# - Konzepte erklären, die nicht im Code ausgedrückt werden können
# - den Zweck des Codes erklären
# - Code erklären, den man nicht bereinigen kann (z.B. eine veröffentlichte
#   Schnittstelle)
# - veröffentlichte Schnittstellen dokumentieren (z.B. mit Doxygen)
# - `TODO`-Kommentare sind (wenn sie sparsam verwendet werden)
# - wichtige Aspekte betonen ("Dies ist sehr wichtig, weil...")

# %% [markdown]
#
# ## Schlechte Kommentare
#
# - Unklare Kommentare (Nuscheln)
#
# Angenommen, der folgende Kommentar ist tatsächlich richtig. Was sagt er uns?

# %%
try:
    with open("my-app.cfg", mode="r", encoding="utf-8"):
        ...
except FileNotFoundError:
    # Somebody else has already loaded the defaults.
    pass


# %% [markdown]
#
# - Redundante Kommentare (dauern länger als der Code zu lesen, ohne klarer zu
#   sein)

# %%
def read_and_apply_configuration(file):
    ...


# %%
# Read the configuration from file `my-app.cfg`. The file has to be readable and
# in UTF-8 encoding. If the file cannot be found we simply ignore the attempt.
# If the file is indeed found, we read it and apply the configuration to the
# system.
try:
    with open("my-app.cfg", mode="r", encoding="utf-8") as file:
        read_and_apply_configuration(file)
except FileNotFoundError:
    pass


# %% [markdown]
#
# - Irreführende Kommentare

# %%
# Return a new list that is the concatenation of the elements in `list_1` and
# `list_2`.
def concatenate_lists(list_1, list_2):
    if not list_1:
        return list_2
    elif not list_2:
        return list_1
    else:
        return list_1 + list_2


# %%
assert concatenate_lists([1, 2], [3, 4]) == [1, 2, 3, 4]

# %% [markdown]
#
# Aufgrund des Kommentars würde man folgendes Verhalten nicht erwarten:

# %%
x = [1, 2]
assert concatenate_lists(x, []) is x
assert concatenate_lists([], x) is x


# %% [markdown]
#
# - Vorgeschriebene Kommentare (durch Style-Guides, nicht durch Gesetze)
# - Journal-Kommentare (Geschichte der Datei)

# %%
# file: widget.py
#
# Changes made to the file:
#
# 2022-08-10: Added a frobnicator as proposed by Jane
# 2022-08-11: Twiddled the frobnicator's parameters
# 2022-08-12: Further tweaks to the frobnicator settings
# 2022-08-13: Added flux compensation to the frobnicator
# 2022-08-14: Improved flux compensation
# 2022-09-03: Revisited flux compensation after discussion with Joe
#
class Frobnicator:
    pass


# %% [markdown]
#
# - Inhaltsfreie Kommentare (Noise comments)

# %%
class FluxCompensator:
    # The `__init__()` method of the flux compensator.
    def __init__(self) -> None:
        ...


# %%
# Hourly wage in US$
HOURLY_WAGE_IN_USD = 80


# %% [markdown]
#
# - Positions-Markierungen

# %%
class MyVeryLargeClass:
    ####################################################
    # Initialization Methods
    ####################################################
    def init(self):
        ...

    def init_in_another_way(self):
        ...

    ####################################################
    # Computations
    ####################################################
    def compute_this(self):
        ...

    def compute_that(self):
        ...

    ####################################################
    # State Updates
    ####################################################
    def set_some_state(self, x):
        ...


# %% [markdown]
#
# - Zuschreibungen und Namensnennungen

# %%
# Added by Jack <jack@example.org> on 2018-03-12
def some_function(x, y):
    return x + y


# %% [markdown]
#
# - Auskommentierter Code
#   - Neigt dazu, nie gelöscht zu werden
#   - Unklar, warum er da ist: sollte er gelöscht oder wieder einkommentiert
#     werden?
#   - Sollte lieber gelöscht und bei Bedarf aus dem Versionskontrollsystem
#     wiederhergestellt werden

# %%
# def some_function(x, y):
#     return x + y


# %%
def some_other_function(x, y):
    # z = x + y
    # return z
    return 123


# %% [markdown]
#
# - HTML-Kommentare
#
# In Python werden Formatierungen in Kommentaren entweder in Markdown oder in
# reStructuredText (RST) geschrieben:

# %%
# <p><strong>Important:</strong></p>
# <ul>
#   <li>
#     Don&#39;t use <code>frobnicator_1</code> to tweak
#     <code>flux_compensator_2</code> because they are not
#     coherent!
#   </li>
#   <li>
#     Make sure that <code>fuzzbox_2</code> is turned to
#     at least 11 before plugging in the guitar.
#   </li>
# </ul>


# %%
# **Important:**
#
# - Don't use `frobnicator_1` to tweak `flux_compensator_2` because they are not
#   coherent!
# - Make sure that `fuzzbox_2` is turned to at least 11 before plugging in the
#   guitar.

# %% [markdown]
#
# - Nichtlokale Information

# %%
# This is set to its correct value by `frob_foo()` in file `frobnicator.py`.
foo = 123

# %% [markdown]
#
# - Zu viel Information

# %%

# Implement protocol handling according to ABC Standard 212-3.
#
# This was first proposed by Steve in a meeting in 2013, but at the time we had
# no compatible implementation of the support libraries available. We therefore
# shelved the discussion until Tina brought the topic up in the famous all-hands
# meeting of October 2019. There were some initial problems, but we finally
# succeeded in getting a running implementation working in 2021. This contains a
# bug that is still present in the current code base that causes the system to
# crash when talking to a client that implements variant /4 of the protocol.
# Finally, in early 2022 we also adapted this implementation for the XYZ device
# series.

# %% [markdown]
#
# - Unklarer Bezug zum Code

# %%
# Adjust for target endianness and buffer size
foo = max((foo + 7) * 2, 256)
