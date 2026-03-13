# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Vererbung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
#  ## Vererbung
#
# Wir haben folgende Klasse implementiert:

# %%
import random


# %%
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.1f}, {self.y:.1f})"

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def randomize(self):
        self.x = random.gauss(2, 0.5)
        self.y = random.gauss(3, 0.5)


# %%
p = Point(1, 1)
p

# %%
p.move(2, 3)
p

# %%
p.randomize()
p


# %% [markdown]
#
# Wie können wir farbige Punkte einführen, ohne die komplette Funktionalität
# von `Point` neu implementieren zu müssen?

# %%

# %%
cp = ColorPoint(2, 3)
assert isinstance(cp, Point)
# cp


# %%
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "black"

# %%
cp.color = "red"

# %%
assert cp.x == 2.0
assert cp.y == 3.0
assert cp.color == "red"

# %%
cp.move(2, 3)
# cp


# %%
assert cp.x == 4.0
assert cp.y == 6.0
assert cp.color == "red"

# %%
cp.randomize()
# cp

# %% [markdown]
#
# ## Workshop: Mitarbeiter
#
# Im Folgenden soll eine Klassenhierarchie für Mitarbeiter einer Firma erstellt
# werden:
#
# - Mitarbeiter können entweder Arbeiter oder Manager sein
# - Jeder Mitarbeiter der Firma hat einen Namen, eine Personalnummer und ein
#   Grundgehalt
# - Für jeden Arbeiter werden die angefallenen Überstunden und der Stundenlohn
#   gespeichert.
# - Das Gehalt eines Arbeiters berechnet sich als das 13/12-fache des
#   Grundgehalts plus der Bezahlung für die Überstunden
# - Jeder Manager hat einen individuellen Bonus
# - Das Gehalt eines Managers berechnet sich als das 13/12-fache des
#   Grundgehalts plus Bonus

# %% [markdown]
#
#
# Implementieren Sie Python Klassen `Mitarbeiter`, `Arbeiter` und `Manager` mit
# geeigneten Attributen und einer Methode `gehalt()`, die das Gehalt berechnet.
#
# Implementieren Sie in der Klasse `Mitarbeiter` eine Version der `gehalt()`
# Methode, die das 13/12-fache des Grundgehalts zurückgibt. Überschreiben Sie in
# den Klassen `Arbeiter` und `Manager` die Methode `gehalt()`, um das Gehalt
# entsprechend der angegebenen Formeln zu berechnen. Verwenden Sie dazu die Methode
# `gehalt()` der Basisklasse `Mitarbeiter` mit `super()`.

# %%

# %%

# %%

# %%

# %% [markdown]
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %%

# %% [markdown]
#
# Schreiben sie Assertions, die die Funktionalität der Klasse `Arbeiter` testen.

# %%

# %% [markdown]
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 843, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %%

# %% [markdown]
# Testen Sie die Funktionalität der `Manager` Klasse.

# %%

# %% [markdown]
#
# ## Workshop: Fahrzeuge
#
# In dieser Übung implementieren wir eine Hierarchie von Fahrzeugklassen.
#
# Erstellen Sie eine Basisklasse `Fahrzeug` mit den folgenden Attributen:
# - `hersteller` (string)
# - `modell` (string)
# - `baujahr` (int)
# - `maximale_geschwindigkeit` (float)
# - `aktuelle_geschwindigkeit` (float, Standardwert 0)

# %% [markdown]
#
# Die Klasse `Fahrzeug` soll folgende Methoden haben:
# - `beschleunige(self, wert)`: Erhöht die `aktuelle_geschwindigkeit` um `wert`,
#   aber nicht über `maximale_geschwindigkeit`.
# - `bremse(self, wert)`: Verringert die `aktuelle_geschwindigkeit` um `wert`,
#   aber nicht unter 0.
# - `details(self)`: Gibt einen String mit den allgemeinen Fahrzeuginformationen
#   zurück.

# %% [markdown]
#
# Erstellen Sie eine abgeleitete Klasse `Auto`, die von `Fahrzeug` erbt.
# - Zusätzliche Attribute: `anzahl_tueren` (int), `kraftstoffart` (string, z.B.
#   "Benzin", "Elektro").
# - Überschreiben Sie `details(self)`, um autospezifische Informationen
#   (inklusive der Basisinformationen via `super()`) anzuzeigen.
# - Die `repr()`-Funktion, angewandt auf ein Auto-Objekt, soll eine lesbare
#   Darstellung des Objekts zurückgeben, die dem Konstruktoraufruf ähnelt.

# %% [markdown]
#
# Erstellen Sie eine weitere abgeleitete Klasse `Fahrrad`, die von `Fahrzeug`
# erbt.
# - Zusätzliche Attribute: `anzahl_gaenge` (int), `rahmentyp` (string, z.B.
#   "Mountainbike", "Rennrad").
# - Überschreiben Sie `details(self)`, um fahrradspezifische Informationen
#   (inklusive der Basisinformationen via `super()`) anzuzeigen.
# - Fügen Sie eine Methode `klingle(self)` hinzu, die "Klingeling!" ausgibt.
# - Die `repr()`-Funktion, angewandt auf ein Fahrrad-Objekt, soll eine lesbare
#   Darstellung des Objekts zurückgeben, die dem Konstruktoraufruf ähnelt.

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# Erzeugen Sie ein Auto-Objekt und testen Sie seine Methoden.

# %%


# %% [markdown]
# Erzeugen Sie ein Fahrrad-Objekt und testen Sie seine Methoden.

# %%

# %% [markdown]
#
# ## Workshop: Geometrische Formen
#
# In dieser Übung implementieren wir eine Hierarchie von geometrischen Formen.
#
# - Erstellen Sie eine Basisklasse `Form` mit den folgenden Attributen:
#   - `farbe` (string)
# - Die Klasse `Form` soll folgende Methoden haben:
#   - `flaeche(self)`: Soll einen `NotImplementedError` auslösen, da die
#     Flächenberechnung formabhängig ist.
#   - `umfang(self)`: Soll einen `NotImplementedError` auslösen.
#   - `beschreibung(self)`: Gibt einen String mit Namen und Farbe der Form
#     zurück.

# %% [markdown]
#
# - Erstellen Sie eine Klasse `Rechteck`, die von `Form` erbt.
#   - Zusätzliche Attribute: `breite` (float), `hoehe` (float).
#   - Implementieren Sie `flaeche(self)`: $breite \times hoehe$.
#   - Implementieren Sie `umfang(self)`: $2 \times (breite + hoehe)$.
#   - Überschreiben Sie `beschreibung(self)`, um zusätzlich Breite und Höhe
#     anzuzeigen.
#   - Die `repr()`-Funktion, angewandt auf ein Rechteck-Objekt, soll eine
#     lesbare Darstellung des Objekts zurückgeben, die dem Konstruktoraufruf
#     ähnelt.

# %% [markdown]
#
# - Erstellen Sie eine abgeleitete Klasse `Kreis`, die von `Form` erbt.
#   - Zusätzliche Attribute: `radius` (float).
#   - Implementieren Sie `flaeche(self)`: $\pi \times radius^2$. (Verwenden Sie
#     `math.pi`)
#   - Implementieren Sie `umfang(self)`: $2 \times \pi \times radius$.
#   - Überschreiben Sie `beschreibung(self)`, um zusätzlich den Radius
#     anzuzeigen.
#   - Die `repr()`-Funktion, angewandt auf ein Kreis-Objekt, soll eine lesbare
#     Darstellung des Objekts zurückgeben, die dem Konstruktoraufruf ähnelt.

# %%
import math


# %%

# %%

# %%

# %% [markdown]
# Erzeugen Sie ein Rechteck-Objekt und testen Sie seine Methoden.

# %%

# %% [markdown]
# Erzeugen Sie ein Kreis-Objekt und testen Sie seine Methoden.

# %%

# %% [markdown]
#
# ## Workshop: Bankkonten
#
# In dieser Übung implementieren wir eine Hierarchie von Bankkonten.
#
# - Erstellen Sie eine Basisklasse `BankKonto` mit den folgenden Attributen:
#   - `konto_nummer` (string)
#   - `saldo` (float)
#   - `konto_inhaber` (string)
# - Die Klasse `BankKonto` soll folgende Methoden haben:
#   - `zahle_ein(self, betrag)`: Erhöht den `saldo`. Betrag muss positiv sein.
#   - `hebe_ab(self, betrag)`: Verringert den `saldo`. Betrag muss positiv sein. Gibt `True` zurück bei Erfolg, `False` sonst (z.B. nicht genug Guthaben).
#   - `get_saldo(self)`: Gibt den aktuellen `saldo` zurück.
#   - `konto_info(self)`: Gibt einen String mit Kontoinformationen zurück.

# %% [markdown]
#
# - Erstellen Sie eine abgeleitete Klasse `SparKonto`, die von `BankKonto` erbt.
#   - Zusätzliches Attribut: `zinssatz` (float, z.B. 0.02 für 2%).
#   - Fügen Sie eine Methode `addiere_zinsen(self)` hinzu, die Zinsen auf den
#     Saldo anrechnet ($saldo = saldo \times (1 + zinssatz)$).
#   - Überschreiben Sie `hebe_ab(self, betrag)`: Ein Sparkonto könnte eine
#     Abhebegebühr oder ein Limit haben (für diese Übung: Gebühr von 1.50, wenn
#     Abhebung erfolgreich).

# %% [markdown]
#
# - Erstellen Sie eine abgeleitete Klasse `GiroKonto`, die von `BankKonto` erbt.
#   - Zusätzliches Attribut: `ueberziehungs_limit` (float).
#   - Überschreiben Sie `hebe_ab(self, betrag)`: Erlaubt Abhebungen bis zum
#     $saldo + ueberziehungs\_limit$.
#   - Fügen Sie eine Methode `ziehe_monatliche_gebuehr_ab(self, gebuehr)` hinzu.

# %%

# %%

# %%

# %% [markdown]
# Erzeugen Sie ein Sparkonto-Objekt und testen Sie seine Methoden.

# %%

# %% [markdown]
# Erzeugen Sie ein Girokonto-Objekt und testen Sie seine Methoden.

# %%

# %%
