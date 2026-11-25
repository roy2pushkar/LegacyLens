from collections import defaultdict
from typing import Any


def build_graph(parsed_files: list[dict[str, Any]]) -> dict[str, Any]:
    nodes: dict[str, dict[str, str]] = {}
    edges: set[tuple[str, str, str]] = set()
    for parsed in parsed_files:
        source = parsed["filename"]
        nodes[source] = {"id": source, "label": source, "type": "source"}
        for key, kind in [("programs", "program"), ("jobs", "job"), ("copybooks", "copybook"), ("tables", "table"), ("files", "dataset")]:
            for item in parsed.get(key, []):
                target = f"{kind}:{item}"
                nodes.setdefault(target, {"id": target, "label": item, "type": kind})
                edges.add((source, target, key))
        for called in parsed.get("calls", []):
            target = f"program:{called}"
            nodes.setdefault(target, {"id": target, "label": called, "type": "program"})
            edges.add((source, target, "calls"))
    return {"nodes": list(nodes.values()), "edges": [{"source": a, "target": b, "relation": r} for a,b,r in sorted(edges)]}


def impact_analysis(graph: dict[str, Any], changed_component: str) -> dict[str, Any]:
    key = changed_component.strip().upper()
    matched = [n for n in graph["nodes"] if n["label"].upper() == key or n["id"].upper() == key]
    if not matched:
        matched = [n for n in graph["nodes"] if key in n["label"].upper()]
    impacted = set()
    for node in matched:
        impacted.add(node["id"])
        # Reverse traversal: find source components that depend on the changed item.
        frontier = [node["id"]]
        while frontier:
            current = frontier.pop()
            for edge in graph["edges"]:
                if edge["target"] == current and edge["source"] not in impacted:
                    impacted.add(edge["source"])
                    frontier.append(edge["source"])
    impacted_nodes = [n for n in graph["nodes"] if n["id"] in impacted]
    return {
        "changed_component": key,
        "matched": bool(matched),
        "matched_nodes": matched,
        "impact_count": len(impacted_nodes),
        "risk": "HIGH" if len(impacted_nodes) >= 5 else "MEDIUM" if len(impacted_nodes) >= 2 else "LOW",
        "impacted": impacted_nodes,
        "recommendation": "Review dependent programs and jobs, then run regression tests for impacted flows." if matched else "No matching component found. Check spelling or analyze the uploaded source files first.",
    }
