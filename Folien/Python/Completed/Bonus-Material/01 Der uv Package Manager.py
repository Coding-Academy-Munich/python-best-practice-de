# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Der uv Package Manager</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Der uv Package Manager
#
# - Ein moderner, schneller Package-Manager für Python
# - Entwickelt von Astral, dem Team hinter Ruff
# - Geschrieben in Rust für maximale Performanz
# - Zwei APIs: die moderne Project API und die kompatible pip API
# - Open-Source auf GitHub verfügbar

# %% [markdown]
#
# # Warum uv?
#
# - **Geschwindigkeit**: Deutlich schneller als bestehende Alternativen
# - **Moderne API**: Intuitive Befehle für Projektmanagement
# - **Kompatibilität**: Unterstützt pyproject.toml und requirements.txt
# - **Workspace-Unterstützung**: Ideal für Monorepos
# - **Determinismus**: Reproduzierbare Builds durch konsequentes
#   Dependency-Locking
# - **Vereinfachung**: Ersetzt mehrere Tools durch eine einzige Lösung

# %% [markdown]
#
# # uv vs. andere Package Manager
#
# | Feature | uv | pip | poetry | pipenv |
# |---------|----|----|--------|--------|
# | Geschwindigkeit | ★★★★★ | ★★ | ★★★ | ★★ |
# | Virtuelle Umgebungen | ✅ | ❌ (braucht venv) | ✅ | ✅ |
# | Dependency Resolution | ✅ | ✅ (langsam) | ✅ | ✅ |
# | Abhängigkeits-Locking | ✅ | ❌ (braucht pip-tools) | ✅ | ✅ |
# | Workspace Support | ✅ | ❌ | ✅ | ❌ |
# | pyproject.toml | ✅ | ✅ (begrenzt) | ✅ | ❌ |
# | requirements.txt | ✅ | ✅ | ❌ | ❌ |

# %% [markdown]
#
# # Installation von uv
#
# - **Linux/macOS**:
#   ```bash
#   curl -LsSf https://astral.sh/uv/install.sh | sh
#   ```
#
# - **Windows** (PowerShell):
#   ```powershell
#   irm https://astral.sh/uv/install.ps1 | iex
#   ```
#
# - **Mit pip** (alle Betriebssysteme):
#   ```bash
#   pip install uv
#   ```

# %% [markdown]
#
# # Virtuelle Umgebungen mit uv
#
# - Erzeugen einer neuen virtuellen Umgebung:
#   ```bash
#   uv venv
#   ```
#
# - Mit spezifischem Python-Interpreter:
#   ```bash
#   uv venv --python=python3.11
#   ```
#
# - Aktivieren (je nach Shell unterschiedlich):
#   ```bash
#   # Bash/Zsh
#   source .venv/bin/activate
#   # Windows PowerShell
#   .venv\Scripts\Activate.ps1
#   ```

# %% [markdown]
#
# # uv Project API - Grundlagen
#
# - Die moderne API für Python-Projekte mit pyproject.toml
# - **Abhängigkeiten hinzufügen**:
#   ```bash
#   uv add numpy pandas
#   ```
#
# - **Mit Versionsbeschränkungen**:
#   ```bash
#   uv add "numpy>=1.20.0" "pandas>=1.3.0,<2.0.0"
#   ```
#
# - **Entwicklungsabhängigkeiten hinzufügen**:
#   ```bash
#   uv add --dev pytest black
#   ```

# %% [markdown]
#
# # Editable Installationen und Workspaces
#
# - **Editable Installation einer Abhängigkeit**:
#   ```bash
#   uv add --editable ./my-local-package/
#   ```

# %% [markdown]
#
# - **Workspace-Konfiguration** (pyproject.toml):
#   ```toml
#   [project]
#   name = "my-app-bundle"
#   dependencies = ["my-libraries"]
#   [tool.uv.sources]
#   my-libraries = { workspace = true }
#   [tool.uv.workspace]
#   members = ["packages/*"]
#   ```

# %% [markdown]
#
# # Abhängigkeiten verwalten mit Project API
#
# - **Abhängigkeiten synchronisieren** (installieren/aktualisieren):
#   ```bash
#   uv sync
#   ```
#
# - **Abhängigkeiten locken** (automatisch mit `uv run`):
#   ```bash
#   uv lock
#   ```
#
# - **Installation ohne Lockfile upzudaten (Fehler falls inkompatibel)**:
#   ```bash
#   uv sync --locked
#   ```

# %% [markdown]
#
# # Befehle ausführen mit uv run
#
# - **Python-Script ausführen**:
#   ```bash
#   uv run python script.py
#   ```
#
# - **Installierte Tools ausführen**:
#   ```bash
#   uv run pytest
#   uv run black .
#   ```
#
# - **In dev-Umgebung mit optionalen Abhängigkeiten**:
#   ```bash
#   uv run --dev pytest
#   ```
#
# - **Mit zusätzlichen Argumenten**:
#   ```bash
#   uv run pytest -xvs tests/
#   ```

# %% [markdown]
#
# # Neues Projekt mit uv erstellen
#
# - Projekt-Verzeichnis erstellen:
#   ```bash
#   mkdir mein-projekt && cd mein-projekt
#   ```
#
# - Virtuelle Umgebung erstellen:
#   ```bash
#   uv venv
#   ```
#
# - pyproject.toml erstellen:
#   ```bash
#   cat > pyproject.toml << EOF
#   [build-system]
#   requires = ["hatchling"]
#   build-backend = "hatchling.build"
#
#   [project]
#   name = "mein-paket"
#   version = "0.1.0"
#   description = "Ein Beispielprojekt"
#   requires-python = ">=3.8"
#   EOF
#   ```

# %% [markdown]
#
# # Projektabhängigkeiten mit Project API
#
# - **Hauptabhängigkeiten hinzufügen**:
#   ```bash
#   uv add numpy pandas matplotlib
#   ```
#
# - **Entwicklungsabhängigkeiten hinzufügen**:
#   ```bash
#   uv add --dev pytest black mypy
#   ```
#
# - **Dependencies für eigenes Projekt installieren**:
#   ```bash
#   uv add --editable .
#   ```
#
# - **Alle Abhängigkeiten synchronisieren**:
#   ```bash
#   uv sync --all
#   ```

# %% [markdown]
#
# # Dependency-Locking mit uv
#
# - **Lock-Datei erzeugen**:
#   ```bash
#   uv lock
#   ```
#
# - **Lock-Datei mit Entwicklungsabhängigkeiten**:
#   ```bash
#   uv lock --all
#   ```
#
# - **Abhängigkeiten aus Lock-Datei installieren**:
#   ```bash
#   uv sync --locked
#   ```
#
# - **Lock-Datei aktualisieren**:
#   ```bash
#   uv lock --refresh
#   ```

# %% [markdown]
#
# # Die pip API - für besondere Fälle
#
# - Kompatible API für bestehende Projekte ohne pyproject.toml
# - **Paket installieren**:
#   ```bash
#   uv pip install numpy
#   ```
#
# - **Pakete aus einer requirements.txt installieren**:
#   ```bash
#   uv pip install -r requirements.txt
#   ```
#
# - **Paketinformationen anzeigen**:
#   ```bash
#   uv pip show numpy
#   ```

# %% [markdown]
#
# # Projekt entwickeln und publizieren
#
# - **Tests ausführen**:
#   ```bash
#   uv run pytest
#   ```
#
# - **Code formatieren**:
#   ```bash
#   uv run black .
#   ```
#
# - **Build-Abhängigkeiten installieren**:
#   ```bash
#   uv add --dev build twine
#   ```
#
# - **Paket bauen und publizieren**:
#   ```bash
#   uv run build
#   uv run twine upload dist/*
#   ```

# %% [markdown]
#
# # Fazit: Vorteile von uv
#
# - **Geschwindigkeit**: Drastisch schnellere Installation und Abhängigkeitsauflösung
# - **Moderne API**: Intuitive Project API für effizientes Projektmanagement
# - **Workspaces**: Unterstützung für Monorepos mit mehreren Paketen
# - **Dual-API**: Modern (Project API) und kompatibel (pip API)
# - **Determinismus**: Zuverlässiges Dependency-Locking für reproduzierbare Builds
# - **Entwicklerfreundlich**: `uv run` für einfache Befehlsausführung

# %% [markdown]
#
# # Wann sollten Sie uv verwenden?
#
# - Bei neuen Projekten mit pyproject.toml
# - In Monorepos mit mehreren Python-Paketen
# - Für schnellere CI/CD-Pipelines
# - Wenn Sie von pip auf ein moderneres Tool umsteigen möchten
# - Bei großen Projekten mit vielen Abhängigkeiten
# - Wenn Sie Wert auf reproduzierbare Builds legen

# %% [markdown]
#
# # Ressourcen
#
# - [Offizielle uv-Dokumentation](https://docs.astral.sh/uv/)
# - [GitHub Repository](https://github.com/astral-sh/uv)
# - [uv vs. andere Package Manager-Benchmarks](https://astral.sh/blog/uv)
# - [Python Packaging User Guide](https://packaging.python.org)
# - [PEP 621 – Metadaten in pyproject.toml](https://peps.python.org/pep-0621)
# - [uv Tech Talk (Jane Street)](https://www.janestreet.com/tech-talks/uv-an-extremely-fast-python-package-manager/)
