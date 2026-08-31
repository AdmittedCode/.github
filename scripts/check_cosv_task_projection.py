#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
idx=json.loads((ROOT/"data/cosv/task-vector-index.json").read_text())
watch=json.loads((ROOT/"data/site-admission-watch.json").read_text())
row=idx["tasks"][0]
rec=json.loads((ROOT/row["vector_ref"]).read_text())
m=rec["exact_metrics"]
assert idx["profile"]=="task.v1" and idx["width"]==14
assert row["task_id"]==watch["task_id"]=="ADMITTEDCODE-SITE-REVIEW-INTEGRATION"
assert rec["vector"]==row["vector"]=="60000000101000"
assert watch["status"]=="BLOCKED"
assert m["lifecycle"]=="BLOCKED"
assert m["blocker_count"]==1
assert m["activated"] is False and m["propagated"] is False
assert watch["authority_effect"]=="NONE"
assert watch["activation_effect"]=="NONE"
assert watch["publication_effect"]=="NONE"
assert idx["coverage"]["repository_active_task_surface_audit_complete"] is True
assert idx["coverage"]["repository_vector_present_claimed"] is False
print("ADMITTEDCODE_COSV_PROJECTION_PASS tasks=1 repository_vector_present=false")
