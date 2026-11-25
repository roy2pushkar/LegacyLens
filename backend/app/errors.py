ERRORS = {
    "-811": {"system": "DB2", "title": "More than one row returned", "meaning": "A singleton SELECT or scalar subquery returned multiple rows.", "checks": ["Confirm the predicate is unique", "Use a cursor or FETCH FIRST 1 ROW ONLY only if business logic permits", "Check joins for duplicate matches"]},
    "-805": {"system": "DB2", "title": "Package not found", "meaning": "The requested DBRM/package/plan combination was not found or is not valid for execution.", "checks": ["Verify collection, package name and consistency token", "Confirm the package was bound in the target subsystem", "Check plan/package deployment sequence"]},
    "-904": {"system": "DB2", "title": "Resource unavailable", "meaning": "A required DB2 resource is unavailable.", "checks": ["Check resource name and type", "Review DB2 messages and resource status", "Coordinate with DBA for locks or utility state"]},
    "-911": {"system": "DB2", "title": "Rollback due to deadlock or timeout", "meaning": "The unit of work was rolled back after deadlock or timeout handling.", "checks": ["Review SQLCODE and reason code", "Check transaction duration and lock order", "Retry only when application design supports safe retry"]},
    "-913": {"system": "DB2", "title": "Deadlock or timeout", "meaning": "The statement could not complete due to a deadlock or timeout.", "checks": ["Review DB2 messages and reason code", "Inspect locking and concurrent transactions", "Consider a bounded retry for transient cases"]},
    "-905": {"system": "DB2", "title": "Resource limit exceeded", "meaning": "The statement or process exceeded a DB2 resource limit.", "checks": ["Review SQLERRD values and DB2 accounting", "Check query access path and row volume", "Discuss applicable limits with DBA"]},
    "S0C7": {"system": "z/OS", "title": "Data exception", "meaning": "A data operation encountered invalid numeric or packed-decimal data.", "checks": ["Inspect the failing instruction and dump", "Validate input fields and numeric formats", "Check field definitions and data overlays"]},
    "S0C4": {"system": "z/OS", "title": "Protection exception", "meaning": "The program attempted an invalid memory access.", "checks": ["Inspect PSW and failing offset", "Check subscripts, pointers and linkage parameters", "Review storage overlays and initialization"]},
    "SB37": {"system": "JCL", "title": "Dataset space exhausted", "meaning": "A data set ran out of allocated space.", "checks": ["Review primary/secondary allocation", "Check volume and storage constraints", "Use appropriate space parameters after capacity review"]},
}

def lookup(code: str):
    return ERRORS.get(code.strip().upper().replace("SQLCODE ", ""))
