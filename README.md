# 🐼 Pandas — Bro Code 1-Hour Practice Repository

A chapter-by-chapter Pandas practice repository based on the topics covered in Bro Code's
**"Learn Pandas in 1 hour!"** video.

## Chapters

1. `01_series/series.py` — Series
2. `02_dataframes/dataframes.py` — DataFrames
3. `03_importing/importing.py` — CSV / Excel / JSON importing and exporting
4. `04_selection/selection.py` — selecting rows and columns
5. `05_filtering/filtering.py` — filtering data
6. `06_aggregation/aggregation.py` — aggregation and grouping
7. `07_data_cleaning/data_cleaning.py` — missing/duplicate/invalid data
8. `08_mini_project/mini_project.py` — combine the concepts

## Setup in VS Code (Windows)

Open this repository folder in VS Code terminal:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

You can also run Python without activating:

```powershell
.\.venv\Scripts\python.exe 01_series\series.py
```

## Run a chapter

```powershell
python 01_series\series.py
python 02_dataframes\dataframes.py
python 03_importing\importing.py
python 04_selection\selection.py
python 05_filtering\filtering.py
python 06_aggregation\aggregation.py
python 07_data_cleaning\data_cleaning.py
python 08_mini_project\mini_project.py
```

## Important Git note

`.venv/` is intentionally ignored by Git. A virtual environment is machine-specific and
should not be uploaded to GitHub. Anyone cloning this repo can recreate it with:

```powershell
python -m venv .venv
pip install -r requirements.txt
```
