"""Lightweight deterministic dependency extraction for a hackathon MVP."""
import re
from pathlib import Path
from typing import Any

SUPPORTED = {".cbl", ".cob", ".jcl", ".cpy", ".copy", ".sql", ".txt"}

def _unique(items: list[str]) -> list[str]:
    return sorted({x.strip().upper() for x in items if x and x.strip()})

def parse_source(filename: str, source: str) -> dict[str, Any]:
    ext = Path(filename).suffix.lower()
    if ext not in SUPPORTED:
        raise ValueError(f"Unsupported file type: {ext or '(no extension)'}")
    upper = source.upper()
    name = Path(filename).stem.upper()
    programs: list[str] = []
    copybooks: list[str] = []
    jobs: list[str] = []
    tables: list[str] = []
    files: list[str] = []
    calls: list[str] = []

    if ext in {".cbl", ".cob", ".cpy", ".copy", ".txt"}:
        programs += re.findall(r"(?im)^\s*PROGRAM-ID\.?\s+([A-Z0-9-]+)", upper)
        copybooks += re.findall(r"(?im)^\s*COPY\s+([A-Z0-9-]+)", upper)
        calls += re.findall(r"(?im)\bCALL\s+['\"]?([A-Z0-9-]+)", upper)
        tables += re.findall(r"(?is)\b(?:FROM|JOIN|INTO|UPDATE)\s+([A-Z0-9_.]+)", upper)
        files += re.findall(r"(?im)^\s*SELECT\s+([A-Z0-9-]+)\s+ASSIGN", upper)
    if ext == ".jcl":
        jobs += re.findall(r"(?im)^\s*//([A-Z0-9@$#]+)\s+JOB\b", upper)
        programs += re.findall(r"(?im)\bPGM\s*=\s*([A-Z0-9@$#]+)", upper)
        copybooks += re.findall(r"(?im)\bDSN\s*=\s*[^,\s]*\.([A-Z0-9@$#]+)", upper)
        files += re.findall(r"(?im)\bDSN\s*=\s*([A-Z0-9.@#$-]+)", upper)
    # SQL can appear in .sql files or embedded in COBOL/JCL.
    tables += re.findall(r"(?is)\b(?:FROM|JOIN|INTO|UPDATE)\s+([A-Z][A-Z0-9_.$#-]*(?:\.[A-Z][A-Z0-9_.$#-]*)?)", upper)
    tables = [t for t in tables if t not in {"SQLCA", "SYSIBM.SYSDUMMY1"}]
    return {
        "filename": filename,
        "file_type": ext,
        "programs": _unique(programs) or ([name] if ext in {".cbl", ".cob"} else []),
        "jobs": _unique(jobs),
        "copybooks": _unique(copybooks),
        "calls": _unique(calls),
        "tables": _unique(tables),
        "files": _unique(files),
        "line_count": len(source.splitlines()),
    }
