# LegacyLens — Mainframe Intelligence MVP

LegacyLens is a hackathon starter for analyzing COBOL/JCL/copybook/SQL source, extracting a dependency graph, and checking change impact.

## Stack
- Next.js + TypeScript
- React + @xyflow/react
- FastAPI + Python
- Deterministic starter parser (regex-based)
- 

## Run on Windows

### 1. Backend
Open CMD or PowerShell:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

If PowerShell blocks activation, run in CMD using `.venv\Scripts\activate.bat`, or run `.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000` without activating.

### 2. Frontend (second terminal)
Install Node.js LTS if needed, then:

```powershell
cd frontend
copy .env.example .env.local
npm install
npm run dev
```

Open http://localhost:3000. API docs: http://localhost:8000/docs.

## Demo
Upload the sample files in `backend/data/samples` together:
- `CUSTPROC.cbl`
- `CUSTCOPY.cpy`
- `CUSTJOB.jcl`
- `CUSTSQL.sql`

Then try impact analysis for `CUSTOMER` and knowledge lookup for `-811` or `S0C7`.

## Notes
- This is a hackathon MVP, not a production parser. It does not fully understand COBOL continuation rules, fixed-format columns, nested SQL, JCL PROC expansion, DB2 bind/package metadata, or runtime control flow.
- Do not upload confidential production code or data to a public deployment.
- No cloud resources or AI API keys are required for this local starter.
