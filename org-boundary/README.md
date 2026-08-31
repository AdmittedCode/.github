# AdmittedCode Organizational Boundary

This directory defines the canonical organization-level ingress/egress contract for AdmittedCode.

## Processing model

```
HB or HB-derived carrier
  -> governed InTr envelope
  -> organization ingress
  -> normalization / provenance binding
  -> service resolution
  -> AdmittedCode review endpoint
  -> decision/evidence binding
  -> organization egress
  -> governed InTr envelope
```

The boundary is non-authoritative. It may validate, route, classify, and preserve evidence, but it must not transform AdmittedCode review output into execution permission.

## Required distinctions

- receipt != admission
- admission != execution
- dispatch != consumption
- consumption != same-execution reconstruction
- CI success != runtime proof
- carrier observation != transition authority

## Existing review semantics

The canonical internal review sequence remains:
1. code-admit-gate
2. coherency-scanner
3. admissibility-receipt
4. provider-harness
5. fleet-status

Each repository is an internal service endpoint. Cross-organization transport semantics are owned here.
