# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Setuptools und Installation</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Setuptools: Distribution von Python Paketen
#
# - Setuptools sind das "Standard"-Tool um installierbare Python-Pakete zu
#   erzeugen.
# - Es gibt eine Vielzahl von anderen Tools, die auch verwendet werden können, z.B.:
#   - [Flit](https://flit.pypa.io/en/latest/)
#   - [Poetry](https://python-poetry.org/)
#   - [Hatch](https://hatch.pypa.io/latest/)
#   - [uv](https://docs.astral.sh/uv/)
# - Viele dieser Tools haben zusätzliche Features, z.B. die Verwaltung von
#   Abhängigkeiten, die Verwaltung von virtuellen Umgebungen, etc.


# %% [markdown]
#
#  ### Beispiel: Erstellen einer Anwendung als Python-Paket
#
#  - Hinzufügen von einer `pyproject.toml`-Dateien mit Information über die zu
#    installierenden Packages und Skripte
#  - Hinzufügen einiger Hilfsdateien (`README.md`, `LICENSE`)
#  - Erstellen der Distribution mit `python -m build` (Benötigt das PyPA `build`
#    [package](https://github.com/pypa/build))
#  - Installation mit `pip` und dem generierten Wheel
#  - Installation während der Entwicklung: `pip install -e .`

# %% [markdown]
#
# ### Einfacheres Vorgehen: Verwendung einer Template
#
# - Es gibt eine Vielzahl von Templates, die verwendet werden können, um
#   Python-Pakete zu erstellen.
# - Diese Templates sind in der Regel auf GitHub verfügbar und können z.B. mit
#   [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) verwendet
#   werden.
# - `cookiecutter` ist ein Tool, um Projekte aus Templates zu erstellen.
#
# ```
# cookiecutter.exe https://github.com/hoelzl/trivial_python_project
# ```


# %% [markdown]
#
# ### Verwendung der `trivial_python_project`-Template
#
# - `cookiecutter.exe https://github.com/hoelzl/trivial_python_project`
# - Beantworten der Fragen
# - Wechseln in das Verzeichnis

# %% [markdown]
#
# - Erstellen einer virtuellen Umgebung
#   - `python -m venv .venv`
#   - `source .venv/bin/activate` (Linux/Mac)
#   - `.venv\Scripts\activate` (Windows)
# - Installieren der Build-Tools
#   - `pip install build setuptools wheel`
# - Erstellen der Distribution mit `python -m build`
# - Editierbare Installation mit `pip install -e . --group dev`

# %% [markdown]
#
# - Ausführen der Anwendung:
#   - `python -m my_awesome_project`
#   - `my-awesome-project[.exe]` (nach Installation)
# - Ausführen der Tests: `pytest`
# - Test mit verschiedenen Python-Versionen: `tox`
