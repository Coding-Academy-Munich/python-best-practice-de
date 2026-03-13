# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Refactoring: Kapsle Variable</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
# ### Kapsle Variable

# %%
class ProductV0:
    def __init__(self, name: str):
        self.name = name


# %%
class ProductV1:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


# %% [markdown]
# #### Motivation
#
# - Erleichtert zukünftige Refactorings
#   - Forwarding ist bei Funktionen einfacher als bei Daten
#   - Durch Kapselung kann man Techniken zum Refactoring von Funktionen
#     anwenden
# - Verhindert ungewollte Änderungen an Daten
# - Ermöglicht Validierung, Monitoring, ...
# - In Python weniger relevant als in anderen Sprachen

# %% [markdown]
# #### Mechanik
#
# - Implementiere Getter (und nur bei Bedarf Setter)
# - Ersetze Zugriffe auf die Variable durch Getter (und Setter)
# - Teste nach jeder solchen Änderung
# - Schränke die Sichtbarkeit der Variable ein
# - Falls die Variable einen Record-Typ hat, ziehe *Encapsulate Record* in
#   Betracht
