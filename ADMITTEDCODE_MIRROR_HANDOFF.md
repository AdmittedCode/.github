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
- `StegVerse-org/LLM-adapter/docs/ADMITTEDCODE_EVIDENCE_DEMO_MIRROR_HANDOFF.md` — canonical source packet production; completed and merged.
- `StegVerse-org/StegVerse-SDK/docs/ADMITTEDCODE_PORTABLE_CONSUMER_MIRROR_HANDOFF.md` — non-authorizing portable receipt consumption; completed and merged.

## Machine-owned Site Integration Continuation

The portable reviewer-package goal is COMPLETE. The next integration goal is `StegVerse-Labs/Site`, but Site currently denies external task and external session ownership. No Site branch or path is claimed by this workstream.

Durable blocked task:

`data/tasks/ADMITTEDCODE-SITE-REVIEW-INTEGRATION.json`

Machine observer:

- workflow: `.github/workflows/site-admission-watch.yml`
- script: `scripts/check_site_admission.py`
- persisted state: `data/site-admission-watch.json` when the scheduled/main workflow observes a state change.

Observer PR #1 merged as `0d30496950ea89a7e483d6ab67efa4bd05b45997`. PR workflow run `31186953791`, job `92893798545`, completed PASS and directly observed Site status `BLOCKED` from live Site orchestration/heartbeat files.

Release condition is machine-observable: `ADMITTEDCODE-SITE-REVIEW-INTEGRATION` appears in Site `machine_admission.admitted_tasks`, or both `external_tasks_allowed` and `external_session_ownership_allowed` become true. Until then, do not create a competing Site branch.

## Session Consolidation

Complete durable execution inventory:

`SESSION_CONSOLIDATION_ADMITTEDCODE_PORTABILITY_2026-08-07.md`

The originating ChatGPT session's unique requirements are transferred there and into the task/observer above. The session does not own the repository's separate API/browser product-interface milestones in `provider-harness`; those remain independent repository work unless another durable claim assigns them.

Publisher and downstream wiki propagation are MERGED INTO their existing canonical Site -> Publisher -> wiki workstream rather than duplicated here. `GCAT-BCAT-Engine/Publisher/PUBLISHER_MIRROR_HANDOFF.md` remains authoritative for that projection chain.

## Release Propagation Rule
When an AdmittedCode repository reaches tagging/release readiness, verify that pertinent semantics, receipts, status, or integration guidance are reflected where applicable in:

- `StegVerse-Labs/Site`
- `GCAT-BCAT-Engine/Publisher`
- `StegVerse-Labs/admissibility-wiki`
- `StegVerse-002/stegguardian-wiki`
- `master-records/orchestration` when custody/reconstruction is authorized.

## Current Next Task

No ChatGPT session owns the blocked Site mutation. The next executable action is machine-owned observation through `.github/workflows/site-admission-watch.yml`. When Site releases the admission condition, a future execution lane must first reread Site's current handoff/orchestration/heartbeat state and use the exact Site-admitted claim before mutating any Site path.

## Status
Portable cross-repository proof and compact reviewer package: COMPLETE, merged, and hosted-validated. Session-specific implementation/consolidation: COMPLETE. StegVerse-wide integration remains active as machine-owned blocked work with a durable owner, release condition, collision boundary, and next action.
