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
