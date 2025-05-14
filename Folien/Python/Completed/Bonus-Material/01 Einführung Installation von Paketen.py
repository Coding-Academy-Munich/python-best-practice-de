# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung: Installation von Paketen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Pakete in Python
#
# Verschiedene Bedeutungen von "Paket" oder "Package" in Python:
#
# - Sammlung von Python Dateien wie im Kapitel über Module und Packages
#   beschrieben (*Import-Paket*)
# - Distribution einer installierbaren Version einer Bibliothek ("wheel"),
#   die dann importiert werden kann (*Distributions-Paket* oder *installierbares
#   Paket*)
#
# In diesem Abschnitt beschäftigen wir uns mit installierbaren Paketen.

# %% [markdown]
#
# ## Lebenszyklus eines Pakets
#
# - Quellcode (typischerweise in einem Git-Repository)
#   - Python-Dateien
#   - Metadaten-Dateien: `pyproject.toml`
#   - Bei älteren Paketen: `setup.py`, `setup.cfg`
# - Distribution
#   - sdist: Quellcode-Archiv zum selber kompilieren
#   - wheel: installierbares, "Binär"-Archiv
# - Installation
#   - Von Quellcode, lokaler Distribution oder von PyPI

# %% [markdown]
#
# ## Wheels
#
# - Wheels sind das Standardformat für installierbare Pakete
# - Archive im ZIP-Format
# - Enthalten alle Dateien, die für die Installation benötigt werden
# - Haben Metadaten wie Versionsnummer und Abhängigkeiten
# - Können mit `pip` installiert werden
# - Erstellung mit Tools wie `setuptools`, `hatchling`, `poetry` oder `flit`

# %% [markdown]
#
# ## PyPI
#
# - Python Package Index
# - Zentrale Datenbank für Python-Pakete
# - Enthält Metadaten für viele Pakete und Links zu den Wheels
# - `pip` kann Pakete von PyPI herunterladen und installieren

# %% [markdown]
#
# ## Versionsnummern
#
# - Beschreiben die Version eines Pakets
# - [Offizielle Spezifikation](
#   https://packaging.python.org/en/latest/specifications/version-specifiers/)
# - Besteht oft aus drei Zahlen, getrennt durch Punkte: `MAJOR.MINOR.PATCH`
#   - `MAJOR`: Große Änderungen, die nicht abwärtskompatibel sind
#   - `MINOR`: Neue Features, die abwärtskompatibel sind
#   - `PATCH`: Bugfixes, die abwärtskompatibel sind
# - Beispiel: `1.0.3`

# %% [markdown]
#
# ## Versions-Spezifikationen
#
# - Pakete können von anderen Paketen abhängen
# - Abhängigkeiten werden durch Namen und eine [Versions-Spezifikation](
#   https://packaging.python.org/en/latest/specifications/version-specifiers/#id4)
#   angegeben
# - Wird keine Versions-Spezifikation angegeben, so ist jede Version erlaubt

# %% [markdown]
#
# ### Beispiele
#
# - `>= 2.25.1`: Mindestens Version 2.25.1
# - `== 1.0.3`: Genau Version 1.0.3
# - `>= 1.0.3, < 2.0.0`: Mindestens Version 1.0.3, aber kleiner als 2.0.0
# - `~= 1.0.3`: Mindestens Version 1.0.3, aber kleiner als 1.1.0
# - `>= 1.0.3, == 1.0.*`: Äquivalent zu `~= 1.0.3`
# - `~= 1.1`: Mindestens Version 1.1, aber kleiner als 2.0.0
# - `>= 1.1, == 1.*`: Äquivalent zu `~= 1.1`
# - `~= 1.0.3, != 1.0.4, != 1.0.5`: Mindestens Version 1.0.3, kleiner als 1.1.0,
#   aber nicht 1.0.4 oder 1.0.5

# %% [markdown]
#
# ## Requirements-Dateien
#
# - Dateien, die mehrere Pakete und Versions-Spezifikationen enthalten
# - Format:
#   - Eine Zeile pro Paket
#   - Paket-Name, gefolgt von Versions-Spezifikationen
# - Mit `pip` können alle Pakete in einer Requirements-Datei installiert werden
#   - Dabei versucht `pip` Abhängigkeiten so aufzulösen, dass sie für alle
#     Pakete erfüllt werden
#   - Das kann fehlschlagen, wenn Pakete inkompatible Abhängigkeiten haben
#   - Oft kann man durch Abschwächen der Versions-Spezifikationen das Problem
#     lösen

# %% [markdown]
#
# ### Beispiel
#
# - `requirements.txt`:
#
#   ```
#   requests>=2.25.1
#   fastapi~=0.63.2
#   ```
#
# - Installiert `requests` und `fastapi` in den angegebenen Versionen


# %% [markdown]
#
# ## Installation von Paketen
#
# - `pip install <package>`: Installiert ein Paket
# - `pip install <package><version-spec>`: Installiert ein Paket, das die angegebene
#   Versions-Spezifikation erfüllt
# - `pip install <p1> <p2> ...`: Installiert mehrere Pakete (potenziell mit
#   unterschiedlichen Versions-Spezifikationen)
# - `pip install -r <requirements-file>`: Installiert alle Pakete, die in der
#   angegebenen Datei aufgelistet sind

# %% [markdown]
#
# ## Auflisten der installierten Pakete
#
# - `pip list`: Gibt alle installierten Pakete mit Versionsnummern aus
# - `pip freeze`: Gibt alle installierten Pakete mit Versionsnummern aus, so dass
#   sie in einer Requirements-Datei verwendet werden können

# %% [markdown]
#
# ## Virtuelle Umgebungen
#
# - Python-Pakete werden normalerweise systemweit installiert
# - Das kann zu Problemen führen, wenn verschiedene Versionen von Paketen
#   benötigt werden
# - Virtuelle Umgebungen ermöglichen die Installation von Paketen in einem
#   abgeschlossenen Bereich
# - `pip` kann virtuelle Umgebungen erstellen und Pakete darin installieren
# - Die Pakete in jedem virtuellen Environment können unabhängig von anderen
#   virtuellen Umgebungen verwaltet werden

# %% [markdown]
#
# ### Erstellen eines virtuellen Environments
#
# ```shell
# python -m venv <path>
# ```
#
# - Erstellt ein virtuelles Environment im angegebenen Verzeichnis
# - Dieses Verzeichnis
#   - enthält alle für das virtuelle Environment benötigten Dateien
#   - soll nicht ins Versionskontrollsystem aufgenommen werden
#   - kann nicht verschoben oder an eine andere Stelle kopiert werden
#   - darf keine Projektdateien enthalten

# %% [markdown]
#
# ### Aktivieren eines virtuellen Environments
#
# - Linux/OS X: `source <path>/bin/activate`
# - Windows (CMD): `<path>\Scripts\activate.bat`
# - Windows (PowerShell): `<path>\Scripts\Activate.ps1`

# %% [markdown]
#
# ### Deaktivieren eines virtuellen Environments
#
# - `deactivate`

# %% [markdown]
#
# ```shell
# python -c "import requests; print(requests.__version__)"
# python -m venv venv
# source ./venv/bin/activate # Linux
# ./venv/Scripts/activate.bat # Windows CMD
# ./venv/Scripts/Activate.ps1 # Windows PowerShell
# pip install requests~=2.28.1
# python -c "import requests; print(requests.__version__)"
# pip freeze > requirements.txt
# deactivate


# %% [markdown]
#
# ## Beispiel für Versionskonflikt
#
# In einem neuen virtuellen Environment schlägt folgende Installation fehl:
#
# ```shell
# pip install requests==2.31.0 urllib3==1.21.0
# ```
#
# Auflösung durch flexiblere Versions-Spezifikationen:
#
# ```shell
# pip install requests~=2.31.0 urllib3~=1.26.0
# ```

# %% [markdown]
#
# ### Beispiel für anderes Installationsproblem
#
# Installation von `numpy` in Version `1.20.0` in einem neuen Environment schlägt
# unter manchen Windows-Versionen fehl:
#
# ```shell
# pip install numpy==1.20.0
# ```
#
# Auch hier lässt sich durch eine flexiblere Versions-Spezifikation das Problem
# lösen:
#
# ```shell
# pip install numpy~=1.20
# python -c "import numpy; print(numpy.__version__)"
# ```

# %% [markdown]
#
# ## Workshop: Installation von Paketen in virtuellen Umgebungen
#
# - Erstellen Sie ein virtuelles Environment in einem Verzeichnis `venv-workshop`
# - Aktivieren Sie das virtuelle Environment
# - Installieren Sie das `requests` Paket in der Version `~= 2.0`
# - Installieren Sie das Paket `Pillow` in der Version `~= 10.0.0`
# - Bestimmen Sie die installierten Versionen von `requests` und `Pillow`

# %% [markdown]
#
# - Erstellen Sie eine Datei `requirements.txt` mit den installierten Paketen
# - Führen Sie das folgende Skript im virtuellen Environment aus:

# %%
import requests
from PIL import Image
from PIL.ImageShow import show

response = requests.get("https://www.python.org/static/img/python-logo.png")
with open("python-logo.png", "wb") as file:
    file.write(response.content)
image = Image.open("python-logo.png")
show(image)

# %% [markdown]
#
# - Deaktivieren Sie das virtuelle Environment
# - Löschen Sie das Verzeichnis `venv-workshop`
# - Erstellen Sie ein neues virtuelles Environment in einem Verzeichnis `venv2`
# - Installieren Sie die Pakete aus der Datei `requirements.txt` in das neue
#   virtuelle Environment
# - Führen Sie das Skript im neuen virtuellen Environment erneut aus

# %% [markdown]
#
# ```shell
# echo 'import requests
# from PIL import Image
# from PIL.ImageShow import show
#
# response = requests.get("https://www.python.org/static/img/python-logo.png")
# with open("python-logo.png", "wb") as file:
#     file.write(response.content)
# image = Image.open("python-logo.png")
# show(image)
# ' > script.py
# ```

# %% [markdown]
#
# ```shell
# python -m venv venv-workshop
# source ./venv-workshop/bin/activate # Linux
# ./venv-workshop/Scripts/activate.bat # Windows CMD
# ./venv-workshop/Scripts/Activate.ps1 # Windows PowerShell
# pip install requests~=2.28.1
# pip install Pillow~=10.0.0
# python -c "import requests; print(requests.__version__)"
# python -c "import PIL; print(PIL.__version__)"
# python script.py
# pip freeze > requirements.txt
# cat requirements.txt
# deactivate

# %% [markdown]
#
# ```shell
# rm -rf venv-workshop # Linux/OS X
# rmdir /s venv-workshop # Windows CMD
# rm -Recurse -Force venv-workshop # Windows PowerShell
# python -m venv venv2
# source ./venv2/bin/activate # Linux
# ./venv2/Scripts/activate.bat # Windows CMD
# ./venv2/Scripts/Activate.ps1 # Windows PowerShell
# pip install -r requirements.txt
# python script.py
# deactivate
# ```
