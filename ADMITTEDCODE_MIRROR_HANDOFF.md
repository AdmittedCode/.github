# AdmittedCode Mirror Handoff

## Role
AdmittedCode is the StegVerse review and verification lane for repository and governed-action admissibility. It is not execution authority and does not replace source repositories, product owners, policy authorities, custody, publication, or deployment controls.

## Current Objective
Make AdmittedCode portable, independently verifiable, and reusable throughout StegVerse while preserving exact authority boundaries and source semantics.

## Canonical Review Sequence
1. `code-admit-gate` — declared-structure and forbidden-pattern conformance.
2. `coherency-scanner` — governance-role artifact completeness and coherence.
3. `admissibility-receipt` — portable decision/evidence receipt generation and independent verification.
4. `provider-harness` — pre-provider consent, budget, replay, source-evidence, and admissibility gating for AI-provider actions.
5. `fleet-status` — continuous public status surface for the review tools.

## Implemented Portable StegVerse Seam
The first cross-repository portable seam is installed and merged:

```text
StegVerse-org/LLM-adapter
  canonical end-to-end fixture
  -> deterministic stegverse.admittedcode.review_packet.v1

AdmittedCode/provider-harness
  source-snapshot hash verification
  -> consent / budget / GCAT-BCAT preflight
  -> ALLOW or DENY before any provider key
  -> stegverse.provider_harness_receipt.v1

StegVerse-org/StegVerse-SDK
  independent canonical receipt-hash verification
  -> ACCEPTED for non-authorizing SDK consumption
```

Merged evidence:

- `StegVerse-org/LLM-adapter` PR #121 — initial portable packet fixtures.
- `StegVerse-org/LLM-adapter` PR #122 — deterministic canonical-fixture binding; merged commit `12eefc095479b325ccb5551c7279b7ecec1d0283`; PR validation PASS.
- `AdmittedCode/provider-harness` PR #1 — initial portable StegVerse review demo.
- `AdmittedCode/provider-harness` PR #2 — canonical source-snapshot verification before review; merged commit `c4eb15c63f4d0869080f59a57207449a8bf629e7`; Self Test PASS.
- `StegVerse-org/StegVerse-SDK` PR #11 — portable non-authorizing receipt consumer; merged.
- `StegVerse-org/StegVerse-SDK` PR #12 — source-verified ALLOW and DENY receipt fixtures; merged commit `6227454a78b9c210a8ec0d3eb5be3f15b977c6e7`; all five SDK validation workflows PASS.
- `AdmittedCode/provider-harness` PR #3 — compact external reviewer packet; merged commit `b5b942d64cb7d7278b7a4137704fea75f325a77f`; Self Test PASS.

## External Reviewer Packet
Canonical path:

```text
AdmittedCode/provider-harness/demo/reviewer_packet/
```

Installed reviewer surfaces:

- `README_FIRST.md`
- `cross_repo_manifest.json`
- `run_reviewer_demo.py`
- `REVIEWER_PACKET_MIRROR_HANDOFF.md`
- `tests/test_reviewer_packet.py`

The packet binds exact merged implementations in LLM-adapter, provider-harness, and SDK. One command demonstrates source verification, ALLOW, correct DENY, `key_requested=false`, independent base receipt-hash verification, and `authority_effect=NONE`.

## Semantic Separation Proven
The refusal path preserves three different meanings:

```text
StegVerse canonical source expected_outcome = QUARANTINE
AdmittedCode provider-execution decision     = DENY
StegVerse SDK receipt-consumption status      = ACCEPTED
```

`SDK ACCEPTED` means the receipt is structurally and cryptographically acceptable for non-authorizing consumption. It does not convert the denied provider action into an allowed action. No layer silently rewrites another layer's authority class.

## StegVerse Integration Contract
For a StegVerse repository or governed transition under review:

- review MUST remain non-authoritative;
- review MUST occur before execution where the evaluated condition can still prevent the transition;
- review results MUST be reproducible from repository state, canonical inputs, source snapshots, and declared rules;
- material decisions SHOULD emit or reference a portable admissibility receipt;
- denial or incomplete review MUST preserve evidence and remediation information;
- browser, API, CLI, workflow, or SDK entry points MUST converge on the same decision semantics when they represent the same governed operation;
- provider access MUST remain downstream of governance checks;
- review artifacts MUST state scope assertions and scope disclaimers;
- source evidence hashes MUST be verified before a source-bound review is trusted;
- `ALLOW`, `DENY`, `FAIL_CLOSED`, `QUARANTINE`, `PARTIAL`, and downstream `ACCEPTED` statuses MUST not be collapsed into one generic success/failure bit.

## Initial Cross-Ecosystem Review Targets
Priority order after the portable seam:

1. `StegVerse-Labs/Site` — activation and public proof projection, subject to its own orchestration handoff.
2. `GCAT-BCAT-Engine/Publisher` — publication and governed release path.
3. `StegVerse-Labs/admissibility-wiki` — public admissibility semantics and verification guidance.
4. `StegVerse-002/stegguardian-wiki` — guardian/review boundary documentation.
5. `master-records/orchestration` — custody/reconstruction of portable review evidence where authorized.

`StegVerse-Labs/Sit` and `StegVerse-Labs/stegguardian-wiki` are not canonical destinations.

## Review Triggers
AdmittedCode review should be invoked for at least:

- new or materially changed governance manifests/schemas;
- new execution/provider/tool paths;
- release/tag candidates;
- activation-state changes;
- policy/delegation changes affecting admissibility;
- workflow changes that can mutate governed state;
- changes to receipt generation, canonicalization, replay, or verification;
- cross-org installation or ingestion events;
- changes that convert scaffolding/stubs into executable paths.

## Evidence Standard
A review is not complete merely because analysis exists. Completion requires directly inspectable evidence from the strongest available path, such as passing tests, workflow runs, independently verified receipts, canonical source hashes, release artifacts, or reproducible local execution.

## Failure Handling
- `DENY` is a valid governance result.
- `FAIL_CLOSED` is required when required governance evidence is absent or a live path cannot be safely evaluated.
- `PARTIAL`/`INCOMPLETE` must identify missing artifacts and must not become implicit ALLOW.
- review-tool failure must not silently become execution permission.
- a source hash mismatch must stop source-bound review before downstream gate evaluation.

## Adjacent Handoffs
- `AdmittedCode/provider-harness/PROVIDER_HARNESS_MIRROR_HANDOFF.md` — provider-harness implementation.
- `AdmittedCode/provider-harness/demo/stegverse/PORTABLE_STEGVERSE_DEMO_MIRROR_HANDOFF.md` — portable StegVerse demonstration.
- `AdmittedCode/provider-harness/demo/reviewer_packet/REVIEWER_PACKET_MIRROR_HANDOFF.md` — compact external-review package.
- `StegVerse-org/LLM-adapter/docs/ADMITTEDCODE_EVIDENCE_DEMO_MIRROR_HANDOFF.md` — canonical source packet production.
- `StegVerse-org/StegVerse-SDK/docs/ADMITTEDCODE_PORTABLE_CONSUMER_MIRROR_HANDOFF.md` — non-authorizing portable receipt consumption.

## Site Integration Admission Check — 2026-08-07
The next integration goal was started by reading the current Site handoff and both required orchestration-state files before claiming any Site path.

Observed Site state:

```text
Site handoff: current work task sequence 0001 remains RUNNING / OBSERVED_BLOCKED
machine_observation.active_task_count = 6
machine_observation.blocker_count = 6
machine_admission.admitted_tasks = []
machine_admission.external_tasks_allowed = false
machine_admission.external_session_ownership_allowed = false
heartbeat work_state = RUNNING
heartbeat system_health = ACTIVE_WITH_DECLARED_BLOCKER
active HIL upload owner = external-active-session
queued exclusive SITE-0002-HIL-LIVE remains blocked
```

Therefore the AdmittedCode Site projection is **NOT ADMITTED** at this time. No Site branch or file was claimed. This is a deliberate fail-closed result, not lack of progress.

The handoff requires local execution of `scripts/site_handoff_orchestrator.py` and `scripts/check_ecosystem_heartbeat_orchestration.py`. A read-only local clone/execution attempt from this session could not run because the container has no external DNS/network access to GitHub. The committed Site state itself already explicitly denies external task admission; that denial is preserved here rather than bypassed.

Publisher was also inspected. Its current handoff remains bound to Site activation and explicitly says Publisher's current blocker is that Site has not published `ACTIVATION_COMPLETE` with a hash-bound `READY_FOR_DOWNSTREAM_INGESTION` packet. No premature Publisher publication/release integration was installed.

## Current Next Task
Portable reviewer-package goal: COMPLETE.

Current ecosystem integration status:

```text
StegVerse-Labs/Site integration: WAITING_FOR_SITE_MACHINE_ADMISSION
GCAT-BCAT-Engine/Publisher projection: WAITING_FOR_SITE_ACTIVATION_CHAIN
admissibility-wiki propagation: DOWNSTREAM_OF_PUBLISHER
stegguardian-wiki propagation: DOWNSTREAM_OF_PUBLISHER
```

When Site state changes to admit external/parallel-safe work or otherwise explicitly admits an AdmittedCode task, install the smallest non-authorizing Site projection of the portable review evidence and bind it into Site's canonical validation path. Until then, do not bypass Site orchestration.

## Release Propagation Rule
When an AdmittedCode repository reaches tagging/release readiness, verify that pertinent semantics, receipts, status, or integration guidance are reflected where applicable in:

- `StegVerse-Labs/Site`
- `GCAT-BCAT-Engine/Publisher`
- `StegVerse-Labs/admissibility-wiki`
- `StegVerse-002/stegguardian-wiki`

## Status
Portable cross-repository proof and compact reviewer package: COMPLETE, merged, and validated. StegVerse-wide integration remains active but is currently blocked at the canonical Site admission boundary; no downstream authority boundary was bypassed.