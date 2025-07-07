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
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color="black"):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"ColorPoint({self.x:.1f}, {self.y:.1f}, {self.color!r})"

    def randomize(self):
        super().randomize()
        self.color = random.choice(["black", "red", "green", "blue", "yellow", "white"])


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
from dataclasses import dataclass


# %%
@dataclass
class Mitarbeiter:
    name: str
    pers_nr: str
    grundgehalt: float

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %%
@dataclass
class Arbeiter(Mitarbeiter):
    überstunden: float = 0.0
    stundensatz: float = 0.0

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %%
@dataclass
class Manager(Mitarbeiter):
    bonus: float

    def gehalt(self):
        return super().gehalt() + self.bonus


# %% [markdown]
#
# Erzeugen Sie einen Arbeiter mit Namen Hans, Personalnummer 123, einem
# Grundgehalt von  36000.0 Euro, der 3.5 Überstunden zu je 40.0 Euro gearbeit
# hat. Drucken Sie das Gehalt aus.

# %%
a = Arbeiter("Hans", "123", 36_000, 3.5, 40.0)
print(a.gehalt())
a

# %% [markdown]
#
# Schreiben sie Assertions, die die Funktionalität der Klasse `Arbeiter` testen.

# %%
# Diese Assertions sind überflüssig!
assert a.name == "Hans"
assert a.pers_nr == "123"
assert a.grundgehalt == 36_000
assert a.überstunden == 3.5
assert a.stundensatz == 40.0

# Diese Assertion sollte vorhanden sein
assert a.gehalt() == 39_140.0

# %% [markdown]
#
# Erzeugen Sie einen Manager mit Namen Sepp, Personalnummer 843, der ein
# Grundgehalt von 60000.0 Euro und einen Bonus von 30000.0 Euro hat. Drucken Sie
# das Gehalt aus.

# %%
m = Manager("Sepp", "843", 60_000.0, 30_000.0)
print(m.gehalt())
m

# %% [markdown]
# Testen Sie die Funktionalität der `Manager` Klasse.

# %%
assert m.gehalt() == 95_000.0


# %% [markdown]
# ## Lösungsvorschlag ohne Dataclasses:

# %%
class Mitarbeiter:
    def __init__(self, name, pers_nr, grundgehalt):
        self.name = name
        self.pers_nr = pers_nr
        self.grundgehalt = grundgehalt

    def gehalt(self):
        return 13 / 12 * self.grundgehalt


# %%
class Arbeiter(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, überstunden, stundensatz):
        super().__init__(name, pers_nr, grundgehalt)
        self.überstunden = überstunden
        self.stundensatz = stundensatz

    def __repr__(self):
        return (
            f"Arbeiter({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.überstunden}, {self.stundensatz})"
        )

    def gehalt(self):
        return super().gehalt() + self.überstunden * self.stundensatz


# %%
class Manager(Mitarbeiter):
    def __init__(self, name, pers_nr, grundgehalt, bonus):
        super().__init__(name, pers_nr, grundgehalt)
        self.bonus = bonus

    def __repr__(self):
        return (
            f"Manager({self.name!r}, {self.pers_nr!r}, {self.grundgehalt}, "
            f"{self.bonus})"
        )

    def gehalt(self):
        return super().gehalt() + self.bonus


# %%
a = Arbeiter("Hans", 123, 36_000, 3.5, 40)

# %%
assert a.gehalt() == 39_140.0


# %%
m = Manager("Sepp", 843, 60_000, 30_000)

# %%
assert m.gehalt() == 95_000.0


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

# %% [markdown]
#
# ### Lösungsvorschlag mit Dataclasses


# %%
from dataclasses import dataclass, field


# %%
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


# %%
@dataclass
class Fahrzeug:
    hersteller: str
    modell: str
    baujahr: int
    maximale_geschwindigkeit: float
    aktuelle_geschwindigkeit: float = field(default=0.0, repr=False)

    def __post_init__(self):
        self.aktuelle_geschwindigkeit = clamp(
            self.aktuelle_geschwindigkeit, 0, self.maximale_geschwindigkeit
        )

    def beschleunige(self, wert: float):
        if wert < 0:
            raise ValueError("Beschleunigungswert muss positiv sein.")
        self.aktuelle_geschwindigkeit += wert
        if self.aktuelle_geschwindigkeit > self.maximale_geschwindigkeit:
            self.aktuelle_geschwindigkeit = self.maximale_geschwindigkeit

    def bremse(self, wert: float):
        if wert < 0:
            raise ValueError("Bremswert muss positiv sein.")
        self.aktuelle_geschwindigkeit -= wert
        if self.aktuelle_geschwindigkeit < 0:
            self.aktuelle_geschwindigkeit = 0

    def details(self) -> str:
        return (
            f"{self.hersteller} {self.modell} ({self.baujahr}), "
            f"Max Geschwindigkeit: {self.maximale_geschwindigkeit} km/h, "
            f"Aktuelle Geschwindigkeit: {self.aktuelle_geschwindigkeit:.1f} km/h"
        )


# %%
@dataclass
class Auto(Fahrzeug):
    anzahl_tueren: int = 4
    kraftstoffart: str = "Benzin"

    def details(self) -> str:
        basis_details = super().details()
        return f"{basis_details}, Türen: {self.anzahl_tueren}, Kraftstoff: {self.kraftstoffart}"


# %%
@dataclass
class Fahrrad(Fahrzeug):
    anzahl_gaenge: int = 12
    rahmentyp: str = "Mountainbike"

    def details(self) -> str:
        basis_details = super().details()
        return f"{basis_details}, Gänge: {self.anzahl_gaenge}, Rahmen: {self.rahmentyp}"

    def klingle(self):
        print("Klingeling!")


# %% [markdown]
# Erzeugen Sie ein Auto-Objekt und testen Sie seine Methoden.

# %%
mein_auto = Auto("VW", "Golf", 2021, 220.0, 0.0, 4, "Benzin")
print(mein_auto.details())
mein_auto.beschleunige(50)
print(mein_auto.details())
mein_auto.beschleunige(200)  # Versucht über Max Speed zu gehen
print(mein_auto.details())
mein_auto.bremse(100)
print(mein_auto.details())
mein_auto.bremse(200)  # Versucht unter 0 zu gehen
print(mein_auto.details())


# %% [markdown]
# Erzeugen Sie ein Fahrrad-Objekt und testen Sie seine Methoden.

# %%
mein_fahrrad = Fahrrad("Cube", "Nature", 2023, 35.0, 0.0, 24, "Crossbike")
print(mein_fahrrad.details())
mein_fahrrad.beschleunige(15)
print(mein_fahrrad.details())
mein_fahrrad.klingle()


# %% [markdown]
# ### Lösungsvorschlag ohne Dataclasses

# %%
class FahrzeugOhneDC:
    def __init__(
        self,
        hersteller: str,
        modell: str,
        baujahr: int,
        maximale_geschwindigkeit: float,
        aktuelle_geschwindigkeit: float = 0.0,
    ):
        self.hersteller = hersteller
        self.modell = modell
        self.baujahr = baujahr
        self.maximale_geschwindigkeit = maximale_geschwindigkeit
        self.aktuelle_geschwindigkeit = clamp(
            aktuelle_geschwindigkeit, 0, maximale_geschwindigkeit
        )

    def __repr__(self):
        return (f"FahrzeugOhneDC(hersteller={self.hersteller!r}, modell={self.modell!r}, "
                f"baujahr={self.baujahr}, "
                f"maximale_geschwindigkeit={self.maximale_geschwindigkeit})")

    def beschleunige(self, wert: float):
        if wert < 0:
            raise ValueError("Beschleunigungswert muss positiv sein.")
        self.aktuelle_geschwindigkeit += wert
        if self.aktuelle_geschwindigkeit > self.maximale_geschwindigkeit:
            self.aktuelle_geschwindigkeit = self.maximale_geschwindigkeit

    def bremse(self, wert: float):
        if wert < 0:
            raise ValueError("Bremswert muss positiv sein.")
        self.aktuelle_geschwindigkeit -= wert
        if self.aktuelle_geschwindigkeit < 0:
            self.aktuelle_geschwindigkeit = 0

    def details(self) -> str:
        return (f"{self.hersteller} {self.modell} ({self.baujahr}), "
                f"Max Geschwindigkeit: {self.maximale_geschwindigkeit} km/h, "
                f"Aktuelle Geschwindigkeit: {self.aktuelle_geschwindigkeit:.1f} km/h")


# %%
class AutoOhneDC(FahrzeugOhneDC):
    def __init__(
        self,
        hersteller: str,
        modell: str,
        baujahr: int,
        maximale_geschwindigkeit: float,
        anzahl_tueren: int,
        kraftstoffart: str,
        aktuelle_geschwindigkeit: float = 0.0,
    ):
        super().__init__(
            hersteller,
            modell,
            baujahr,
            maximale_geschwindigkeit,
            aktuelle_geschwindigkeit,
        )
        self.anzahl_tueren = anzahl_tueren
        self.kraftstoffart = kraftstoffart

    def __repr__(self):
        return (
            f"AutoOhneDC(hersteller={self.hersteller!r}, modell={self.modell!r}, "
            f"baujahr={self.baujahr}, "
            f"maximale_geschwindigkeit={self.maximale_geschwindigkeit}, "
            f"anzahl_tueren={self.anzahl_tueren}, kraftstoffart={self.kraftstoffart!r})"
        )

    def details(self) -> str:
        basis_details = super().details()
        return (
            f"{basis_details}, Türen: {self.anzahl_tueren}, Kraftstoff: {self.kraftstoffart}"
        )


# %%
class FahrradOhneDC(FahrzeugOhneDC):
    def __init__(
        self,
        hersteller: str,
        modell: str,
        baujahr: int,
        maximale_geschwindigkeit: float,
        anzahl_gaenge: int,
        rahmentyp: str,
        aktuelle_geschwindigkeit: float = 0.0,
    ):
        super().__init__(
            hersteller,
            modell,
            baujahr,
            maximale_geschwindigkeit,
            aktuelle_geschwindigkeit,
        )
        self.anzahl_gaenge = anzahl_gaenge
        self.rahmentyp = rahmentyp

    def __repr__(self):
        return (
            f"FahrradOhneDC(hersteller={self.hersteller!r}, modell={self.modell!r}, "
            f"baujahr={self.baujahr}, "
            f"maximale_geschwindigkeit={self.maximale_geschwindigkeit}, "
            f"anzahl_gaenge={self.anzahl_gaenge}, rahmentyp={self.rahmentyp!r})"
        )

    def details(self) -> str:
        basis_details = super().details()
        return f"{basis_details}, Gänge: {self.anzahl_gaenge}, Rahmen: {self.rahmentyp}"

    def klingle(self):
        print("Klingeling!")


# %%
mein_auto_ohne_dc = AutoOhneDC("BMW", "X5", 2022, 250.0, 5, "Diesel")
print(mein_auto_ohne_dc.details())
mein_auto_ohne_dc.beschleunige(100)
assert mein_auto_ohne_dc.aktuelle_geschwindigkeit == 100.0
print(mein_auto_ohne_dc.details())

# %%
mein_fahrrad_ohne_dc = FahrradOhneDC("Scott", "Scale", 2023, 30.0, 12, "Mountainbike")
print(mein_fahrrad_ohne_dc.details())
mein_fahrrad_ohne_dc.klingle()
assert mein_fahrrad_ohne_dc.aktuelle_geschwindigkeit == 0.0

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


# %% [markdown]
# ### Lösungsvorschlag mit Dataclasses

# %%
@dataclass
class Form:
    farbe: str

    def flaeche(self) -> float:
        raise NotImplementedError("Unterklassen müssen diese Methode implementieren")

    def umfang(self) -> float:
        raise NotImplementedError("Unterklassen müssen diese Methode implementieren")

    def beschreibung(self) -> str:
        return f"Farbe: {self.farbe}"


# %%
@dataclass
class Rechteck(Form):
    breite: float
    hoehe: float

    def __post_init__(self):
        if self.breite <= 0 or self.hoehe <= 0:
            raise ValueError("Breite und Höhe müssen positiv sein.")

    def flaeche(self) -> float:
        return self.breite * self.hoehe

    def umfang(self) -> float:
        return 2 * (self.breite + self.hoehe)

    def beschreibung(self) -> str:
        basis_beschreibung = super().beschreibung()
        return f"Rechteck: {basis_beschreibung}, Breite: {self.breite}, Höhe: {self.hoehe}"


# %%
@dataclass
class Kreis(Form):
    radius: float

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("Radius muss positiv sein.")

    def flaeche(self) -> float:
        return math.pi * self.radius**2

    def umfang(self) -> float:
        return 2 * math.pi * self.radius

    def beschreibung(self) -> str:
        basis_beschreibung = super().beschreibung()
        return f"Kreis: {basis_beschreibung}, Radius: {self.radius}"


# %% [markdown]
# Erzeugen Sie ein Rechteck-Objekt und testen Sie seine Methoden.

# %%
mein_rechteck = Rechteck("Blau", 10.0, 5.0)
print(mein_rechteck.beschreibung())
print(f"Fläche: {mein_rechteck.flaeche():.2f}")
print(f"Umfang: {mein_rechteck.umfang():.2f}")

# %% [markdown]
# Erzeugen Sie ein Kreis-Objekt und testen Sie seine Methoden.

# %%
mein_kreis = Kreis("Rot", 7.0)
print(mein_kreis.beschreibung())
print(f"Fläche: {mein_kreis.flaeche():.2f}")
print(f"Umfang: {mein_kreis.umfang():.2f}")


# %% [markdown]
# ### Lösungsvorschlag ohne Dataclasses

# %%
class FormOhneDC:
    def __init__(self, farbe: str):
        self.farbe = farbe

    def __repr__(self):
        return f"FormOhneDC(farbe={self.farbe!r})"

    def flaeche(self) -> float:
        raise NotImplementedError("Unterklassen müssen diese Methode implementieren")

    def umfang(self) -> float:
        raise NotImplementedError("Unterklassen müssen diese Methode implementieren")

    def beschreibung(self) -> str:
        return f"Farbe: {self.farbe}"


# %%
class RechteckOhneDC(FormOhneDC):
    def __init__(self, farbe: str, breite: float, hoehe: float):
        super().__init__(farbe)
        if breite <= 0 or hoehe <= 0:
            raise ValueError("Breite und Höhe müssen positiv sein.")
        self.breite = breite
        self.hoehe = hoehe

    def __repr__(self):
        return f"RechteckOhneDC(farbe={self.farbe!r}, breite={self.breite}, hoehe={self.hoehe})"

    def flaeche(self) -> float:
        return self.breite * self.hoehe

    def umfang(self) -> float:
        return 2 * (self.breite + self.hoehe)

    def beschreibung(self) -> str:
        basis_beschreibung = super().beschreibung()
        return f"Rechteck: {basis_beschreibung}, Breite: {self.breite}, Höhe: {self.hoehe}"


# %%
class KreisOhneDC(FormOhneDC):
    def __init__(self, farbe: str, radius: float):
        super().__init__(farbe)
        if radius <= 0:
            raise ValueError("Radius muss positiv sein.")
        self.radius = radius

    def __repr__(self):
        return f"KreisOhneDC(name={self.name!r}, farbe={self.farbe!r}, radius={self.radius})"

    def flaeche(self) -> float:
        return math.pi * self.radius**2

    def umfang(self) -> float:
        return 2 * math.pi * self.radius

    def beschreibung(self) -> str:
        basis_beschreibung = super().beschreibung()
        return f"Kreis: {basis_beschreibung}, Radius: {self.radius}"


# %%
rechteck_plain_de = RechteckOhneDC("Grün", 3.0, 4.0)
print(rechteck_plain_de.beschreibung())
assert rechteck_plain_de.flaeche() == 12.0
print(f"Fläche: {rechteck_plain_de.flaeche()}, Umfang: {rechteck_plain_de.umfang()}")

kreis_plain_de = KreisOhneDC("Gelb", 1.0)
print(kreis_plain_de.beschreibung())
assert kreis_plain_de.flaeche() == math.pi
print(f"Fläche: {kreis_plain_de.flaeche():.2f}, Umfang: {kreis_plain_de.umfang():.2f}")


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

# %% [markdown]
# ### Lösungsvorschlag mit Dataclasses

# %%
@dataclass
class BankKonto:
    konto_nummer: str
    saldo: float
    konto_inhaber: str

    def __post_init__(self):
        if self.saldo < 0:
            raise ValueError("Anfangssaldo darf nicht negativ sein, es sei denn, es ist ein Girokonto mit Überziehung.")

    def zahle_ein(self, betrag: float):
        if betrag <= 0:
            raise ValueError("Einzahlungsbetrag muss positiv sein.")
        self.saldo += betrag
        print(f"{betrag:.2f} EUR eingezahlt. Neuer Saldo: {self.saldo:.2f} EUR.")

    def hebe_ab(self, betrag: float) -> bool:
        if betrag <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")
        if self.saldo >= betrag:
            self.saldo -= betrag
            print(f"{betrag:.2f} EUR abgehoben. Neuer Saldo: {self.saldo:.2f} EUR.")
            return True
        else:
            print(
                f"Abhebung von {betrag:.2f} EUR fehlgeschlagen. Nicht genügend Guthaben."
            )
            return False

    def get_saldo(self) -> float:
        return self.saldo

    def konto_info(self) -> str:
        return f"Kontonr: {self.konto_nummer}, Inhaber: {self.konto_inhaber}, Saldo: {self.saldo:.2f} EUR"


# %%
@dataclass
class SparKonto(BankKonto):
    zinssatz: float  # z.B. 0.02 für 2%
    abhebegebuehr: float = 1.50

    def addiere_zinsen(self):
        zinsen = self.saldo * self.zinssatz
        self.saldo += zinsen
        print(
            f"Zinsen ({self.zinssatz*100:.2f}%) in Höhe von {zinsen:.2f} EUR angewendet. Neuer Saldo: {self.saldo:.2f} EUR."
        )

    def hebe_ab(self, betrag: float) -> bool:
        if betrag <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")

        gesamtkosten = betrag + self.abhebegebuehr
        if self.saldo >= gesamtkosten:
            self.saldo -= gesamtkosten
            print(
                f"{betrag:.2f} EUR abgehoben (plus {self.abhebegebuehr:.2f} EUR Gebühr). Neuer Saldo: {self.saldo:.2f} EUR."
            )
            return True
        else:
            print(
                f"Abhebung von {betrag:.2f} EUR (plus Gebühr) fehlgeschlagen. Nicht genügend Guthaben für Betrag + Gebühr."
            )
            return False


# %%
@dataclass
class GiroKonto(BankKonto):
    ueberziehungs_limit: float

    def hebe_ab(self, betrag: float) -> bool:
        if betrag <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")
        if self.saldo + self.ueberziehungs_limit >= betrag:
            self.saldo -= betrag
            print(f"{betrag:.2f} EUR abgehoben. Neuer Saldo: {self.saldo:.2f} EUR.")
            return True
        else:
            print(
                f"Abhebung von {betrag:.2f} EUR fehlgeschlagen. Überziehungslimit überschritten."
            )
            return False

    def ziehe_monatliche_gebuehr_ab(self, gebuehr: float):
        if gebuehr <= 0:
            raise ValueError("Gebühr muss positiv sein.")
        self.saldo -= gebuehr
        print(
            f"Monatliche Gebühr von {gebuehr:.2f} EUR abgebucht. Neuer Saldo: {self.saldo:.2f} EUR."
        )


# %% [markdown]
# Erzeugen Sie ein Sparkonto-Objekt und testen Sie seine Methoden.

# %%
mein_sparkonto = SparKonto("SK123", 1000.0, "Max Mustermann", 0.025)
print(mein_sparkonto.konto_info())
mein_sparkonto.zahle_ein(500.0)
mein_sparkonto.addiere_zinsen()
print(mein_sparkonto.konto_info())
mein_sparkonto.hebe_ab(200.0)  # Erfolgreich mit Gebühr
print(mein_sparkonto.konto_info())
mein_sparkonto.hebe_ab(1400.0)  # Sollte fehlschlagen

# %% [markdown]
# Erzeugen Sie ein Girokonto-Objekt und testen Sie seine Methoden.

# %%
mein_girokonto = GiroKonto("GK789", 200.0, "Erika Mustermann", 500.0)
print(mein_girokonto.konto_info())
mein_girokonto.zahle_ein(100.0)
print(mein_girokonto.konto_info())
mein_girokonto.hebe_ab(400.0)  # Geht in Überziehung
print(mein_girokonto.konto_info())
mein_girokonto.hebe_ab(500.0)  # Sollte fehlschlagen (Limit überschritten)
mein_girokonto.ziehe_monatliche_gebuehr_ab(5.0)
print(mein_girokonto.konto_info())


# %% [markdown]
# ### Bankkonten-Lösung ohne Dataclasses

# %%
class BankKontoOhneDC:
    def __init__(self, konto_nummer: str, saldo: float, konto_inhaber: str):
        self.konto_nummer = konto_nummer
        self.saldo = saldo
        self.konto_inhaber = konto_inhaber
        if self.saldo < 0:
            print(
                f"Warnung: Konto {self.konto_nummer} mit negativem Saldo initialisiert: {self.saldo}"
            )

    def __repr__(self):
        return f"BankKontoOhneDC(konto_nummer={self.konto_nummer!r}, saldo={self.saldo}, inhaber={self.konto_inhaber!r})"

    def zahle_ein(self, betrag: float):
        if betrag <= 0:
            raise ValueError("Einzahlungsbetrag muss positiv sein.")
        self.saldo += betrag
        print(f"{betrag:.2f} EUR eingezahlt. Neuer Saldo: {self.saldo:.2f} EUR.")

    def hebe_ab(self, betrag: float) -> bool:
        if betrag <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")
        if self.saldo >= betrag:
            self.saldo -= betrag
            print(f"{betrag:.2f} EUR abgehoben. Neuer Saldo: {self.saldo:.2f} EUR.")
            return True
        else:
            print(
                f"Abhebung von {betrag:.2f} EUR fehlgeschlagen. Nicht genügend Guthaben."
            )
            return False

    def get_saldo(self) -> float:
        return self.saldo

    def konto_info(self) -> str:
        return f"Kontonr: {self.konto_nummer}, Inhaber: {self.konto_inhaber}, Saldo: {self.saldo:.2f} EUR"


# %%
class SparKontoOhneDC(BankKontoOhneDC):
    abhebegebuehr: float = 1.50

    def __init__(
        self, konto_nummer: str, saldo: float, konto_inhaber: str, zinssatz: float
    ):
        super().__init__(konto_nummer, saldo, konto_inhaber)
        self.zinssatz = zinssatz

    def __repr__(self):
        return f"SparKontoOhneDC(konto_nummer={self.konto_nummer!r}, saldo={self.saldo}, inhaber={self.konto_inhaber!r}, zinssatz={self.zinssatz})"

    def addiere_zinsen(self):
        zinsen = self.saldo * self.zinssatz
        self.saldo += zinsen
        print(
            f"Zinsen ({self.zinssatz*100:.2f}%) in Höhe von {zinsen:.2f} EUR angewendet. Neuer Saldo: {self.saldo:.2f} EUR."
        )

    def hebe_ab(self, betrag: float) -> bool:
        if betrag <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")
        gesamtkosten = betrag + self.abhebegebuehr
        if self.saldo >= gesamtkosten:
            self.saldo -= gesamtkosten
            print(
                f"{betrag:.2f} EUR abgehoben (plus {self.abhebegebuehr:.2f} EUR Gebühr). Neuer Saldo: {self.saldo:.2f} EUR."
            )
            return True
        else:
            print(
                f"Abhebung von {betrag:.2f} EUR (plus Gebühr) fehlgeschlagen. Nicht genügend Guthaben für Betrag + Gebühr."
            )
            return False


# %%
class GiroKontoOhneDC(BankKontoOhneDC):
    def __init__(
        self,
        konto_nummer: str,
        saldo: float,
        konto_inhaber: str,
        ueberziehungs_limit: float,
    ):
        super().__init__(konto_nummer, saldo, konto_inhaber)
        self.ueberziehungs_limit = ueberziehungs_limit

    def __repr__(self):
        return f"GiroKontoOhneDC(konto_nummer={self.konto_nummer!r}, saldo={self.saldo}, inhaber={self.konto_inhaber!r}, limit={self.ueberziehungs_limit})"

    def hebe_ab(self, betrag: float) -> bool:
        if betrag <= 0:
            raise ValueError("Abhebungsbetrag muss positiv sein.")
        if self.saldo + self.ueberziehungs_limit >= betrag:
            self.saldo -= betrag
            print(f"{betrag:.2f} EUR abgehoben. Neuer Saldo: {self.saldo:.2f} EUR.")
            return True
        else:
            print(
                f"Abhebung von {betrag:.2f} EUR fehlgeschlagen. Überziehungslimit überschritten."
            )
            return False

    def ziehe_monatliche_gebuehr_ab(self, gebuehr: float):
        if gebuehr <= 0:
            raise ValueError("Gebühr muss positiv sein.")
        self.saldo -= gebuehr
        print(
            f"Monatliche Gebühr von {gebuehr:.2f} EUR abgebucht. Neuer Saldo: {self.saldo:.2f} EUR."
        )


# %%
sparkonto_plain_de = SparKontoOhneDC("SPPlain1", 2000.0, "Anna Alt", 0.03)
print(sparkonto_plain_de.konto_info())
sparkonto_plain_de.addiere_zinsen()
assert math.isclose(sparkonto_plain_de.saldo, 2060.0, rel_tol=1e-9)
sparkonto_plain_de.hebe_ab(250.0)
print(sparkonto_plain_de.konto_info())

# %%
girokonto_plain_de = GiroKontoOhneDC("zahle_ein", 100.0, "Peter Alt", 200.0)
girokonto_plain_de.hebe_ab(250.0)  # Geht hebe_ab Überziehung
print(girokonto_plain_de.konto_info())

# %%
