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
The first cross-repository portable seam is now installed:

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

Merged evidence currently includes:

- `StegVerse-org/LLM-adapter` PR #121 — initial portable packet fixtures.
- `StegVerse-org/LLM-adapter` PR #122 — deterministic binding to canonical `simple_query.json` and `action_commit_candidate.json`; merged commit `12eefc095479b325ccb5551c7279b7ecec1d0283`.
- `AdmittedCode/provider-harness` PR #1 — initial portable StegVerse review demo.
- `AdmittedCode/provider-harness` PR #2 — canonical source-snapshot verification before review; merged commit `c4eb15c63f4d0869080f59a57207449a8bf629e7`.
- `StegVerse-org/StegVerse-SDK` PR #11 — portable non-authorizing receipt consumer; merged.
- `StegVerse-org/StegVerse-SDK` PR #12 — source-verified ALLOW and DENY receipt fixtures; validation in progress at handoff update time.

## Semantic Separation Proven
The first refusal path intentionally preserves three different meanings:

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
Priority order after the portable seam is complete:

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
- `StegVerse-org/LLM-adapter/docs/ADMITTEDCODE_EVIDENCE_DEMO_MIRROR_HANDOFF.md` — canonical source packet production.
- `StegVerse-org/StegVerse-SDK/docs/ADMITTEDCODE_PORTABLE_CONSUMER_MIRROR_HANDOFF.md` — non-authorizing portable receipt consumption.

## Current Next Task
Finish and merge SDK PR #12, then create a compact reviewer package in `AdmittedCode/provider-harness` that binds the exact merged LLM-adapter, AdmittedCode, and SDK commits and gives an external reviewer one short path through source fixture -> packet -> source verification -> ALLOW/DENY -> receipt -> independent SDK verification.

After that portable reviewer package is validated, integrate the same evidence contract into `StegVerse-Labs/Site` only through Site's current orchestration/admission path, then propagate release-facing semantics to Publisher and the two governance wikis.

## Release Propagation Rule
When an AdmittedCode repository reaches tagging/release readiness, verify that pertinent semantics, receipts, status, or integration guidance are reflected where applicable in:

- `StegVerse-Labs/Site`
- `GCAT-BCAT-Engine/Publisher`
- `StegVerse-Labs/admissibility-wiki`
- `StegVerse-002/stegguardian-wiki`

## Status
Portable cross-repository proof: IMPLEMENTED through canonical packet generation, independent source verification, provider-harness ALLOW/DENY, portable receipt generation, and SDK hash verification. Final reviewer packaging and downstream Site integration remain active.
