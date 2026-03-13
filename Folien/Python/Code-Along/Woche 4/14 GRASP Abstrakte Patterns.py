# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>GRASP: Abstrakte Patterns</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# <img src="img/grasp-patterns.svg"
#      style="display:block;margin:auto;width:100%"/>

# %% [markdown]
#
# # GRASP: Indirektion
#
# <div style="padding-top:20px;">
# "Jedes Problem in der Informatik kann gelöst werden, indem man eine weitere
# Indirektion hinzufügt."
# <div style="float:right;">- David Wheeler</div>
# </div>
#
# <br>
# <div class="fragment">
# <div style="padding-top:20px;">"Außer zu viele Indirektionen."</div>
# <div style="float:right;">– N.N.</div>
# </div>


# %% [markdown]
#
# ## Indirektion
#
# - Wie können wir die Kopplung zwischen zwei Objekten verringern?
# - Wir führen eine weitere Schicht ein, die die beiden Objekte entkoppelt

# %% [markdown]
#
# Sehr häufiges Muster auf jeder Schicht
#
# - Virtuelle Maschinen
# - Betriebssystem
# - Schnittstellen, polymorphe Methodenaufrufe
# - Pointer
# - Private Attribute mit Gettern/Settern


# %% [markdown]
#
# ### Testen:
#
# - Indirektionen sind Nahtstellen, die für Testzwecke verwendet werden können

# %% [markdown]
#
# ## Indirektion
#
# "Jedes Problem in der Informatik kann gelöst werden, indem man eine weitere
# Indirektion hinzufügt. *Doch damit entsteht meist ein weiteres Problem.*"
#
# <div style="float:right;">- David Wheeler</div>

# %% [markdown]
#
# # GRASP: Polymorphie
#
# - Polymorphe Operationen beschreiben ähnliche (aber nicht identische)
#   Verhaltensweisen, die sich je nach Typ eines Objekts ändern können
# - Normalerweise kein Wechsel zwischen den Verhaltensweisen während der Laufzeit

# %% [markdown]
#
# ## In Python
#
# - **Vererbung**
#   - Subtyp-Beziehung wird explizit angegeben (Oberklassen)
# - **Protokolle**
#   - Subtyp-Beziehung wird nicht explizit angegeben (statisches Duck-Typing)
# - Higher-Order Funktionen
#   - Manchmal syntaktisch einfacher, weniger Code, Lambda-Funktionen
#   - Weniger flexibel als Vererbung, manchmal weniger klar
# - Duck-Typing
#   - Keine explizite Subtyp-Beziehung, nur das Verhalten zählt
#   - Keine statischen Typchecks

# %% [markdown]
#
# - Verwandt: Regeln der Typenhierarchie
#   - Isa-Regel
#   - Nur Blätter sind konkret
#   - Erzwingen von Invarianten für Subtypen durch Supertyp
# - Siehe auch: LSP, Offen/Geschlossen-Prinzip

# %% [markdown]
#
# <!-- Pure Fabrication -->
#
# Welchem Objekt geben wir die Verantwortung für eine Aufgabe, wenn z.B.
# Information Expert oder Creator zu Lösungen führen, die nicht gut sind, weil
# Sie niedrige Kohäsion oder hohe Kopplung haben?

# %% [markdown]
#
# # GRASP: Pure Fabrication
#
# - Eine Klasse, die nicht im Domänenmodell vorkommt
# - Typischerweise ein Gegengewicht zum Informationsexperten, der die Funktionalität
#   in einer einzigen Klasse konzentrieren will
# - Beispiel:
#   - Datenbankfunktionalität in Domänen-Klassen
#   - Konsistent mit Information Expert
#   - Aber: geringe Kohäsion, hohe Kopplung
#   - Einführung von Data Access Objects (eine Pure Fabrication)

# %% [markdown]
#
# ## Vorsicht vor übermäßiger Verwendung
#
# - Werden Pure Fabrications zu häufig verwendet, kann das zu einem Verlust der
#   niedrigen Repräsentationslücke führen
# - Oft wird dadurch auch die Kopplung des Systems vergrößert
# - Besonders Entwickler mit Background in prozeduralen Sprachen neigen dazu,
#   sehr viele "Verhaltensobjekte" einzuführen, bei denen die
#   Verantwortlichkeiten *nicht* mit den für ihre Erfüllung benötigten
#   Informationen zusammenfallen

# %% [markdown]
#
# ### Verwandte Prinzipien
#
# - Low Coupling, High Cohesion
# - Information Expert
#   - Pure Fabrication entfernt die vom Information Expert zugewiesen
#     Verantwortlichkeiten
# - Fast alle Design Patterns sind Pure Fabrications

# %% [markdown]
#
# <!-- Protected Variations -->
# - Programme haben Variations- oder Evolutionspunkte
# - Wie können wir diese so gestalten, dass sie keine unerwünschten Auswirkungen
#   auf andere Komponenten haben?

# %% [markdown]
#
# ## Protected Variation
#
# - Identifiziere die Punkte, an denen Variation oder Evolution auftreten kann
# - Führe einer stabilen Schnittstelle zum Schutz dieser Punkte ein
# - Diese Schnittstellen sind häufig Pure Fabrications
# - Oft führen diese Schnittstellen eine Indirektion ein

# %% [markdown]
#
# ## Protected Variations
#
# Sehr häufig angewandt:
#
# - Standards
# - Virtuelle Maschinen
# - Betriebssysteme
# - Schnittstellen, Polymorphe Methodenaufrufe
# - Private Attribute mit Gettern/Settern
#
# %% [markdown]
#
# ### Testen:
# - Geschützte Variationen sind oft Einstiegspunkte für Tests
# - Aber oft müssen zusätzliche Tests geschrieben werden, um sicherzustellen,
#   dass das System noch funktioniert, wenn die Variabilität tatsächlich
#   verwendet wird

# %% [markdown]
#
# - Protected Variation ist ein sehr allgemeines Prinzip
# - Viele anderen Software-Entwicklungsprinzipien und Patterns sind
#   spezielle Fälle von Protected Variation

# %% [markdown]
#
# ## Vorsicht vor übermäßiger Verwendung
#
# - Protected Variation kann zwei verschiedene Arten von Änderung unterstützen:
#   - Variationspunkte: Varianten, die im existierenden System vorhanden sind
#   - Evolutionspunkte: Spekulative Abstraktionen, die die zukünftige
#     Entwicklung des Systems unterstützen sollen
# - Oft sind die Kosten von spekulativen Abstraktionen höher als die Kosten
#   sie später einzuführen
