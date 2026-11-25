from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .parser import parse_source
from .analysis import build_graph, impact_analysis
from .errors import lookup

app = FastAPI(title="LegacyLens API", version="0.1.0", description="Mainframe code analysis MVP")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_origin_regex=r"https://.*\.vercel\.app", allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class ImpactRequest(BaseModel):
    changed_component: str
    graph: dict

@app.get("/health")
def health():
    return {"status": "ok", "service": "LegacyLens API"}

@app.post("/api/analyze")
async def analyze(files: list[UploadFile] = File(...)):
    parsed = []
    for file in files:
        content = await file.read()
        try:
            text = content.decode("utf-8", errors="replace")
            parsed.append(parse_source(file.filename or "uploaded.txt", text))
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
    graph = build_graph(parsed)
    return {"files": parsed, "graph": graph, "summary": {"file_count": len(parsed), "node_count": len(graph["nodes"]), "edge_count": len(graph["edges"]), "program_count": sum(len(p["programs"]) for p in parsed), "table_count": len({t for p in parsed for t in p["tables"]})}}

@app.post("/api/impact")
def impact(request: ImpactRequest):
    return impact_analysis(request.graph, request.changed_component)

@app.get("/api/errors/{code}")
def error_lookup(code: str):
    result = lookup(code)
    if not result:
        raise HTTPException(status_code=404, detail="Error code not in the starter catalogue. Add a verified entry to backend/app/errors.py.")
    return {"code": code.upper(), **result}
