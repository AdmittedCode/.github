# AdmittedCode

**Governance you can verify, not just trust.**

AdmittedCode builds small, composable tools that gate code and AI actions through
explicit, checkable admissibility rules — and hand back a receipt you can
re-verify yourself. Every tool is open source, runs anywhere, and proves its own
behavior in CI before it asks you to believe anything.

The principle the name encodes: an action is *admitted* only when it passes a
declared rule, and the admission leaves evidence. Nothing here asks for trust it
hasn’t earned with a re-verifiable artifact.

-----

## The line

Four products, each standalone and free, sharing one manifest convention and one
canonical-hashing core. They move from *structure* → *posture* → *proof* →
*governed execution*:

|Product                                                                           |What it does                                                                                                                                                                                                   |Form         |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
|**[code-admit-gate](https://github.com/AdmittedCode/code-admit-gate)**            |Validates a repo against its declared structure and blocks forbidden patterns (e.g. secrets). Manifest-driven; produces repair plans and secret-excluding snapshots.                                           |GitHub Action|
|**[coherency-scanner](https://github.com/AdmittedCode/coherency-scanner)**        |Reads a repo’s declared governance role and reports whether the artifacts that role requires are present — OK, partial, or missing, with evidence.                                                             |CLI          |
|**[admissibility-receipt](https://github.com/AdmittedCode/admissibility-receipt)**|Generates, verifies, and fleet-audits portable admissibility receipts. The verifier independently re-derives every claim — no dependency on the generator.                                                     |CLI          |
|**[provider-harness](https://github.com/AdmittedCode/provider-harness)**          |Governs access to AI providers: consent, budget, and admissibility checks before any call — and refuses *before the API key is ever requested* when governance is incomplete. Includes governance-bound replay.|CLI          |

Live status of all four: **[fleet-status](https://github.com/AdmittedCode/fleet-status)**.

-----

## What ties them together

- **One manifest convention.** Each tool reads the same declared-governance
  manifest, so a repo describes its rules once and every tool understands it.
- **One canonical-hashing core** (`stegverse.jcs.v1`). Every receipt is hashed
  the same deterministic way, so any party can re-verify any receipt without
  trusting — or even contacting — the tool that produced it.
- **Portable receipts.** A decision and its evidence travel together and can be
  re-checked offline. The receipt is the unit of trust, not the service.
- **Honest scope.** Every receipt states what it asserts *and what it does not*.
  A tool claims only what it actually evaluated.

-----

## How to read a green badge here

Every product runs a `self-test` in GitHub Actions on each commit. A green badge
means the tool’s own tests pass on its current `main`, on a clean runner — not
“passed once on a laptop.” The proof is continuous and public. If a badge is
broken, the tool’s workflow hasn’t run or is misconfigured — it does **not** mean
a silent failure. See [fleet-status](https://github.com/AdmittedCode/fleet-status).

-----

## The foundation

These tools are the working expression of a formal governance framework —
GCAT/BCAT admissibility, where a proposed action is permitted only if its induced
state stays inside an admissible region bounded by governance legitimacy, system
constraints, and trust continuity.

The public formalization (coupling-block structure, the admissibility invariant,
and dated proof status) lives at **[the StegVerse formalization site](https://stegverse-labs.github.io/Site/index.html)**.
The tools here are how that formalism shows up as something you can run, not just
read.

-----

## Design commitments

- **Open and portable.** MIT-licensed. No required service, no lock-in. Receipts
  are verifiable with the open tools alone.
- **Composable, not monolithic.** Each tool does one thing and stays small.
  Routing, pricing, and execution policy live *outside* the governance gate, so
  the gate stays provider-agnostic and stable.
- **Verify, don’t assert.** Inclusion here means a tool ships a reproducible
  proof of its own behavior, survives independent re-verification, and states its
  scope honestly. That standard is the product.

-----

## Using these together

A typical flow: `code-admit-gate` confirms a repo conforms to its declared
structure → `coherency-scanner` confirms it carries what its governance role
requires → actions emit `admissibility-receipt`s that anyone can re-verify →
`provider-harness` governs any AI provider call along the way, refusing before
the key when governance is incomplete and replaying instead of re-paying when an
identical admissible request recurs.

Each is useful alone. Together they form a single conformance-to-execution path
where every step leaves verifiable evidence.

-----

## Scope, stated plainly

These tools govern, check, and produce evidence. They do **not** assert the
security or compliance of any third-party provider, the correctness of any AI
model’s output, or any guarantee beyond what each receipt explicitly claims. The
value is that the boundary of every claim is written down and re-checkable.

-----

*Every tool here can be self-hosted, read in full, and verified independently.
That is the point.*
