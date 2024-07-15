# DataConverterProject

## Opis projektu
Projekt `DataConverterProject` służy do konwersji danych między formatami `.xml`, `.json` i `.yaml`.

## Wymagania
- Python 3.x
- `pyinstaller`
- `lxml`
- `pyyaml`

## Instalacja
Aby zainstalować wymagane zależności, uruchom skrypt `installResources.ps1`:
```powershell scripts/installResources.ps1```

## Użycie
Uruchomienie programu:
```python src/main.py input.json output.json```

Przykład:
```python src/main.py input.json output.json```

## Budowanie pliku .exe
Automatyczne budowanie pliku .exe odbywa się za pomocą GitHub Actions. Plik .exe można pobrać z artefaktów po zakończeniu workflow.

## GitHub Actions
Plik konfiguracyjny `build.yml` w folderze .github/workflows konfiguruje GitHub Actions do:

- Instalacji zależności
- Budowania pliku .exe za pomocą PyInstaller
- Przesyłania zbudowanego pliku jako artefakt

## Zawartość pliku build.yml:
```yaml
name: Build and upload artifact

on:
  push:
    branches:
      - master
  schedule:
    - cron: '0 0 * * 1'  # Co tydzień w poniedziałek
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install pyinstaller
        pip install lxml pyyaml
      shell: bash

    - name: Run pyinstaller
      run: pyinstaller --onefile --noconsole src/main.py
      shell: bash

    - name: Upload artifact
      uses: actions/upload-artifact@v2
      with:
        name: my-executable
        path: dist/main.exe
        
