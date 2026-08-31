# ORG_BOUNDARY_MIRROR_HANDOFF.md

Status: ACTIVE
Updated: 2026-08-31

## Goal
Make AdmittedCode/.github the canonical organizational ingress/egress definition for AdmittedCode while preserving the existing non-authoritative review semantics and the independent heartbeat-response implementation lane.

## Existing authority preserved
- ADMITTEDCODE_MIRROR_HANDOFF.md remains authoritative for AdmittedCode review semantics and the Site-review integration boundary.
- HEARTBEAT_RESPONSE_MIRROR_HANDOFF.md remains authoritative for its claimed heartbeat-response surfaces.
- This handoff claims only org-boundary/* and this file.

## Boundary semantics
- Cross-organization packets enter and leave AdmittedCode through the organization boundary contract defined here.
- The boundary may validate, normalize, route, and bind evidence, but it does not turn review output into execution authority.
- HB/HB-derived carrier presence grants no admission, execution, routing, transition, receiving, publication, or release authority.
- AdmittedCode service endpoints remain responsible only for their application-specific review behavior.

## Immediate files
- org-boundary/README.md
- org-boundary/schemas/intr-envelope.schema.json
- org-boundary/evidence/receipt-chain.schema.json
- org-boundary/registry/services.json
- org-boundary/profiles/review-services.json

## Completion semantics
Source presence, CI, merge, deployment, packet receipt, dispatch, consumption, and same-execution reconstruction remain distinct evidence states.


## Canonical resident-runtime activation rule — 2026-08-31
- Every AdmittedCode resident runtime activation surface MUST be kept in `AdmittedCode/.github`.
- No application repository is the organization resident-runtime activation authority.
- Application repositories expose capabilities/endpoints to the organizational boundary; the organization `.github` owns activation, ingress, egress, and organization-crossing transport behavior.
- All communication crossing the AdmittedCode organizational boundary MUST be generated through this `.github` boundary using Interlock/InTr semantics.
- Ingress responsibilities: carrier observation, InTr envelope validation, provenance binding, transition-context binding, destination/profile resolution, dispatch evidence.
- Egress responsibilities: result/evidence validation, destination-org resolution, InTr envelope generation, egress evidence, reconstruction linkage.
- HB/HB-derived carrier presence remains non-authorizing. Authority is determined by applicable transition elements.
- GitHub Actions may validate or transport evidence, but GitHub-hosted workflow execution is not required as sovereign runtime authority.
- Canonical implementation paths: `org-boundary/runtime/`, `org-boundary/registry/`, `org-boundary/schemas/`, `org-boundary/evidence/`, `resident-runtime/`.
- Any legacy resident activation implementation outside `AdmittedCode/.github` becomes an endpoint/provider to this boundary or must be migrated here; it must not remain a competing organizational activation point.
