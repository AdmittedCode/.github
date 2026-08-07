#!/usr/bin/env python3
"""Observe StegVerse-Labs/Site admission state for the AdmittedCode integration task.

This observer is non-authorizing. It never mutates Site. It persists a deterministic
state document in this repository so ChatGPT sessions are not required to poll the
Site orchestration boundary manually.
"""
from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
from urllib.request import Request, urlopen

SITE = "StegVerse-Labs/Site"
CANDIDATE_TASK = "ADMITTEDCODE-SITE-REVIEW-INTEGRATION"
STATE_PATH = "data/site-orchestration-state.json"
HEARTBEAT_PATH = "data/ecosystem-heartbeat-state.json"


def fetch_json(path: str) -> tuple[dict, str]:
    url = f"https://api.github.com/repos/{SITE}/contents/{path}?ref=main"
    req = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "AdmittedCode-site-admission-watch"})
    with urlopen(req, timeout=20) as response:
        payload = json.load(response)
    raw = base64.b64decode(payload["content"]).decode("utf-8")
    return json.loads(raw), payload["sha"]


def derive(orchestration: dict, heartbeat: dict, orchestration_blob: str, heartbeat_blob: str) -> dict:
    active = orchestration.get("active_sequence", {})
    admission = active.get("machine_admission", {})
    admitted = admission.get("admitted_tasks") or []
    admitted_ids = []
    for item in admitted:
        if isinstance(item, str):
            admitted_ids.append(item)
        elif isinstance(item, dict):
            admitted_ids.append(str(item.get("task_id") or item.get("id") or ""))

    task_claimed = CANDIDATE_TASK in admitted_ids
    external_allowed = bool(admission.get("external_tasks_allowed"))
    external_session_allowed = bool(admission.get("external_session_ownership_allowed"))
    active_state = str(active.get("state") or "UNKNOWN")
    work_state = str(heartbeat.get("work_state") or "UNKNOWN")

    if task_claimed:
        status = "CLAIMED_FOR_INTEGRATION"
        next_action = "Execute only the Site paths and role granted by the admitted Site task record."
    elif external_allowed and external_session_allowed:
        status = "READY_FOR_SITE_ADMISSION"
        next_action = "Create or admit the Site integration task through Site's canonical orchestration lane before claiming files."
    else:
        status = "BLOCKED"
        next_action = "Wait for Site machine admission to name this task or permit external task/session ownership; do not create a competing Site branch."

    return {
        "schema_version": "1.0.0",
        "task_id": CANDIDATE_TASK,
        "owner_repository": "AdmittedCode/.github",
        "target_repository": SITE,
        "status": status,
        "source": {
            "site_orchestration_path": STATE_PATH,
            "site_orchestration_blob_sha": orchestration_blob,
            "site_heartbeat_path": HEARTBEAT_PATH,
            "site_heartbeat_blob_sha": heartbeat_blob,
            "site_active_sequence_state": active_state,
            "site_work_state": work_state,
            "external_tasks_allowed": external_allowed,
            "external_session_ownership_allowed": external_session_allowed,
            "admitted_task_ids": admitted_ids,
        },
        "authority_effect": "NONE",
        "activation_effect": "NONE",
        "publication_effect": "NONE",
        "release_effect": "NONE",
        "release_condition": {
            "machine_observable": True,
            "condition": f"{CANDIDATE_TASK} appears in Site machine_admission.admitted_tasks OR both external_tasks_allowed and external_session_ownership_allowed become true",
        },
        "next_executable_action": next_action,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="data/site-admission-watch.json")
    args = ap.parse_args()
    output = Path(args.output)
    try:
        orchestration, orchestration_blob = fetch_json(STATE_PATH)
        heartbeat, heartbeat_blob = fetch_json(HEARTBEAT_PATH)
        result = derive(orchestration, heartbeat, orchestration_blob, heartbeat_blob)
    except Exception as exc:
        result = {
            "schema_version": "1.0.0",
            "task_id": CANDIDATE_TASK,
            "owner_repository": "AdmittedCode/.github",
            "target_repository": SITE,
            "status": "RETRY",
            "error": f"{type(exc).__name__}: {exc}",
            "authority_effect": "NONE",
            "activation_effect": "NONE",
            "next_executable_action": "Retry observation; do not infer Site admission while source state is unavailable.",
        }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
