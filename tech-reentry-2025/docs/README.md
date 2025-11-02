# Tech Comeback Journey — Week 1

**Goal:** Reboot hands-on engineering skills (Windows • AWS + GCP • Python fresh start).

## Repo Layout
```
tech-reentry-2025/
  week1-setup-check/
  week1-file-automation/
  week1-api-client/
  README.md
```

## Week 1 Objectives
- Install full dev environment
- Write & run 3 small projects (setup, automation, API)
- Commit daily to GitHub
- Document with screenshots

## Quickstart (PowerShell)
```powershell
python -m venv venv
.env\Scripts\Activate.ps1
pip install -r requirements.txt
python week1-setup-check\hello.py
```

## Projects
### 1) week1-setup-check
- `hello.py` — first script
- `sysinfo.py` — prints OS, Python version, CPU counts

### 2) week1-file-automation
- `file_sorter.py` — sorts files into subfolders by type (images/docs/videos/other)

### 3) week1-api-client
- `api_client.py` — CLI to call an API (demo: Open-Meteo or placeholder) and print formatted output

## Daily Cadence
Mon: init repo → push hello  
Tue: file sorter  
Wed: finish sorter + docs  
Thu: API client  
Fri: README polish + screenshots

## Screenshots
- Add screenshots of terminal runs here.

## Next Steps
- Optional: try deploying a simple Lambda hello-world
- Begin Week 2 plan (Python for automation + tests)
