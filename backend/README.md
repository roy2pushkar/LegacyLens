# LegacyLens API

## Run locally

```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# If PowerShell blocks activation, use CMD: .venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs
Health: http://localhost:8000/health

This MVP uses deterministic regex-based extraction. It is a demo parser, not a complete COBOL/JCL compiler. Review its findings before using them for real production impact decisions.
