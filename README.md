# DataConverterProject

## Opis projektu
Projekt `DataConverterProject` służy do konwersji danych między formatami `.xml`, `.json` i `.yaml`.

## Wymagania
- Python 3.x
- `pyinstaller`, `lxml`, `pyyaml`

## Instalacja
Aby zainstalować wymagane zależności, uruchom skrypt `installResources.ps1`:

```bash
powershell scripts/installResources.ps1

Użycie
Uruchomienie programu:

bash
Skopiuj kod
python src/main.py <input_file> <output_file>
Przykład:

bash
Skopiuj kod
python src/main.py input.json output.json
Budowanie pliku .exe
Automatyczne budowanie pliku .exe odbywa się za pomocą GitHub Actions. Plik .exe można pobrać z artefaktów po zakończeniu workflow.

GitHub Actions
Plik konfiguracyjny build.yml w folderze .github/workflows konfiguruje GitHub Actions do:

Instalacji zależności
Budowania pliku .exe za pomocą PyInstaller
Przesyłania zbudowanego pliku jako artefakt
