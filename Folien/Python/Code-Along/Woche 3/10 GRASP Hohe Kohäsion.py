# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Hohe Kohäsion</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# ### Problem
#
# - Wie können wir objekte fokussiert, verständlich und wartbar gestalten?
#
# ### Lösung
#
# - Weise Verantwortlichkeiten so zu, dass die Kohäsion hoch bleibt.
# - Evaluiere Designalternativen anhand ihrer Kohäsion.
#
# Dadurch erreichen wir als Nebenprodukt oft auch niedrige Kopplung.

# %% [markdown]
#
# ## Was ist Kohäsion?
#
# - Maß dafür
#   - wie gut verschiedene Teile eines Artefakts zusammenpassen
#   - wie fokussiert die Funktionalität eines Artefakts ist

# %% [markdown]
#
# ## Konsequenzen
#
# - Hohe Kohäsion vereinfacht Entwicklung, Wiederverwendung, Testen, Performance
# - Niedrige Kohäsion macht es schwierig, den Code zu verstehen oder herauszufinden,
#   wo Änderungen vorgenommen werden sollen
# - Der **negative Effekt** niedriger Kohäsion ist **immer groß**
# - Es ist **schwer**, ein System mit niedriger Kohäsion in einen Zustand mit mehr
#   Kohäsion zu überführen

# %% [markdown]
#
# ### Wie können wir feststellen, ob die Kohäsion hoch ist?
#
# - Relativ geringe Anzahl von Methoden
# - Stark zusammenhängende Funktionalität
# - Übernimmt nicht zu viel Arbeit
# - Arbeitet mit anderen Objekten zusammen, um komplexere Aufgaben zu erledigen

# %% [markdown]
#
# ## Kohäsion und Kopplung
#
# - Geringe Kohäsion führt dazu, dass die Systemfunktionalität über das gesamte
#   System "verschmiert" wird
# - Dies führt oft zu einer *hohen Kopplung*
# - Das System lässt sich nur schwer in einen gewünschten Zustand versetzen
# - Testen wird schwierig
#   - Unit-Tests werden groß und schwerfällig
#   - Erzwingen die Verwendung vieler Testdoubles
#   - Verringern den Wert von Unit-Tests als Dokumentation

# %% [markdown]
#
# ## Was können wir tun?
#
# - Extraktion von Klassen (wie bei SRP)
# - Verwendung von Entwurfsmustern
