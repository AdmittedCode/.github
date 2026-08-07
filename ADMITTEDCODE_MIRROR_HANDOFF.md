# AdmittedCode Mirror Handoff

## Role
AdmittedCode is the StegVerse review and verification lane for repository and governed-action admissibility. It is not the execution authority and does not replace source repositories, product owners, policy authorities, or deployment controls.

## Current Objective
Integrate AdmittedCode as a recurring review layer across StegVerse so material repository, governance, provider-access, and release transitions can be independently checked and leave portable evidence.

## Canonical Review Sequence
1. `code-admit-gate` — declared-structure and forbidden-pattern conformance.
2. `coherency-scanner` — governance-role artifact completeness and coherence.
3. `admissibility-receipt` — portable decision/evidence receipt generation and independent verification.
4. `provider-harness` — pre-provider consent, budget, replay, and admissibility gating for AI-provider actions.
5. `fleet-status` — continuous public status surface for the review tools.

## StegVerse Integration Contract
For a StegVerse repository or governed transition under review:

- Review MUST be non-authoritative: AdmittedCode may ALLOW, DENY, FAIL_CLOSED, or report PARTIAL/INCOMPLETE according to its declared checks, but it does not grant business, deployment, publication, or policy authority by itself.
- Review MUST occur before execution where the evaluated condition can still prevent the transition.
- Review results MUST be reproducible from repository state, canonical inputs, and declared rules.
- Material decisions SHOULD emit or reference an admissibility receipt.
- Denial or incomplete review MUST preserve evidence and remediation information rather than silently disappearing.
- Browser, API, CLI, workflow, or SDK entry points MUST converge on the same decision semantics when they represent the same governed operation.
- Provider access MUST remain downstream of governance checks; inadmissible requests must not request provider credentials.
- Review artifacts MUST state scope assertions and scope disclaimers.

## Initial Cross-Ecosystem Review Targets
Priority order:

1. StegVerse-Labs/Sit — system integration and activation state.
2. GCAT-BCAT-Engine/Publisher — publication and governed release path.
3. admissibility-wiki — public admissibility semantics and verification guidance.
4. stegguardian-wiki — guardian/review boundary documentation.
5. StegVerse-Labs/Site — public proof/status representation where applicable.

## Review Triggers
AdmittedCode review should be invoked for at least these classes of change:

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
A review is not complete merely because analysis exists. Completion requires directly inspectable evidence from the strongest available path, such as passing tests, workflow runs, receipt verification, canonical hashes, release artifacts, or reproducible local execution.

## Failure Handling
- `DENY` is a valid governance outcome when the proposed action is inadmissible.
- `FAIL_CLOSED` is required when required governance evidence is absent or a live path cannot be safely evaluated.
- `PARTIAL`/`INCOMPLETE` must identify missing artifacts and must not be converted into an implicit ALLOW.
- Review-tool failure must not silently become execution permission.

## Adjacent Handoffs
`AdmittedCode/provider-harness/PROVIDER_HARNESS_MIRROR_HANDOFF.md` governs provider-harness implementation details. This org-level handoff governs AdmittedCode's StegVerse-wide review role.

## Current Next Task
Install the smallest viable StegVerse review integration beginning with `StegVerse-Labs/Sit`: define a machine-readable review manifest/contract, execute the available AdmittedCode checks against the repo or representative transition, preserve results, then propagate the same pattern to Publisher and the two governance wikis.

## Release Propagation Rule
When an AdmittedCode repository reaches tagging/release readiness, verify that pertinent semantics, receipts, status, or integration guidance are reflected where applicable in:

- `StegVerse-Labs/Sit`
- `GCAT-BCAT-Engine/Publisher`
- `admissibility-wiki`
- `stegguardian-wiki`

## Status
Created as the canonical organization-level handoff for the StegVerse review integration objective.
