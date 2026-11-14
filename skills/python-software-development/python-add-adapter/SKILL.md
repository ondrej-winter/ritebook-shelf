---
name: python-add-adapter
description: Add an inbound or outbound adapter to the owning vertical slice in a Python hexagonal project while keeping business logic in the application layer.
metadata:
  version: "1.2.1"
  last-verified: "2026-11-14T19:06:34+00:00"
---

# Add an Adapter

Add an inbound or outbound adapter to the owning vertical slice in a Python
hexagonal project while keeping business logic in the application layer.

This skill owns adapter implementation. If the required application boundary
does not exist yet, define the port first with `python-add-port`.

## When to use this skill

Use this skill when you need to:

- add an inbound adapter that receives external input and calls an existing
  application port
- add an outbound adapter that implements an existing application port and talks
  to infrastructure
- wire a concrete adapter into dependency injection, routing, bootstrap, or the
  composition root without moving business logic out of the application layer

## Prerequisites

- The relevant port interface exists in
  `src/<app_name>/features/<feature_name>/application/ports/` or a documented
  shared application port location.
- The adapter technology has been chosen and any required library is installed,
  for example with `uv add <library>`.

If the port does not exist yet, use `python-add-port` before implementing the
adapter.

Inspect repository instructions, working-tree changes, the actual package root,
and neighboring adapters before creating files; adapt the example paths to the
project. Confirm prerequisites and any required specialist skill are available.
If a port, chosen library, or required capability is missing, report that
dependency and continue independent inspection or design. Label an unwired or
untested adapter as incomplete rather than claiming working integration.

## Steps

Choose the inbound or outbound path to match the boundary's direction.

Inspect the port, its callers, existing implementations, and contract tests first.
Record validation, defaults, omission/null handling, result ownership, and stable
failure categories. Preserve promised ordering, atomicity, concurrency, and
retry behavior; do not infer semantic conformance merely from matching methods.

## Inbound adapter

An inbound adapter receives external input, maps it into application boundary
types, and calls the application through an inbound port.

### 1. Create the module

```text
src/<app_name>/features/<feature_name>/adapters/inbound/<adapter_name>/
    __init__.py
    adapter.py
```

Keep `__init__.py` lightweight. Re-export the public symbol only when you want a
stable package-level API, and declare `__all__` when it adds clarity:

```python
from .adapter import router

__all__ = ["router"]
```

### 2. Implement

- Accept external input and map it to an application command or query DTO.
- Validate external shape, size and encoding before mapping; establish identity
  with the transport's authentication mechanism. Do not trust caller-supplied
  roles or tenant IDs as authority; application policy must authorize the use case.
- Call the application through its inbound port contract.
- Map the result or exception back to the external format.
- Keep credentials, private data and infrastructure diagnostics out of public
  responses and logs; use the project's safe error categories.
- Map domain or application exceptions to adapter-level error responses when
  they are part of the caller-visible boundary.
- Import domain types directly only when the port contract or exception mapping
  requires them; otherwise prefer application DTOs.
- Do not call domain services, repositories, or outbound adapters directly from
  the adapter.
- Keep all business logic in the application service.
- Update routing, framework registration, or other entry-point wiring so the
  adapter is reachable in the running system.

### 3. Test

Place transport-level tests under
`tests/integration/features/<feature_name>/adapters/inbound/<adapter_name>/`.
Test through the framework test client or transport boundary, injecting a fake
or stubbed inbound port implementation to keep tests focused on adapter behavior.

Add unit tests under
`tests/unit/features/<feature_name>/adapters/inbound/<adapter_name>/` only when the
adapter contains meaningful mapping or serialization helpers that warrant direct,
framework-free verification.

## Outbound adapter

An outbound adapter implements a port interface and talks to external infrastructure.

### 1. Create the module

```text
src/<app_name>/features/<feature_name>/adapters/outbound/<adapter_name>/
    __init__.py
    adapter.py
```

Keep `__init__.py` lightweight. Re-export the public symbol only when you want a
stable package-level API, and declare `__all__` when it adds clarity:

```python
from .adapter import <AdapterName>

__all__ = ["<AdapterName>"]
```

### 2. Implement

- Implement all port interface methods.
- Map infrastructure types to the domain or application types required by the
  port. Do not expose infrastructure types beyond the adapter boundary.
- Translate infrastructure exceptions into the domain or application exceptions
  expected by the port contract.
- Keep framework clients, ORM models, serializers, and transport-specific
  configuration inside the adapter package.
- Update dependency injection, bootstrap, or composition-root wiring when the
  new adapter becomes part of the runtime path.
- Define who creates and closes clients, sessions, streams, and transactions,
  including cleanup after failure or cancellation. Match synchronous/asynchronous
  behavior to the port; do not block an async caller with hidden synchronous I/O.
- Bound technical timeouts and retries according to the port contract. A lost
  response may follow a committed write; reconcile unknown outcomes or use the
  established idempotency mechanism before replaying effects.
- Keep data separate from SQL, subprocess, path and template syntax using the
  appropriate safe APIs. Constrain caller-selected network destinations and
  redirects; preserve tenant scope and use least-privilege credentials.

### 3. Test

Write unit tests under
`tests/unit/features/<feature_name>/adapters/outbound/<adapter_name>/` using fakes,
stubs, or mocks around the infrastructure boundary. Follow with integration
tests under
`tests/integration/features/<feature_name>/adapters/outbound/<adapter_name>/` when
adapter behavior depends on actual driver, network, or persistence integration.

## Validation

Run the narrowest unit or integration tests that cover the changed adapter,
including mapping and error translation. Then run the quality gate required by
the target project's `AGENTS.md` and executable task definitions. Use its
configured lint, type, architecture, and test commands; report any unavailable
checks and their limits.

Include malformed and oversized input, missing/forged identity, denied resource
access and redacted failure output where relevant. Pair adapter tests with the
real use-case enforcement path for authorization claims; a stubbed port cannot
prove the application denies access. Use isolated test services for effects.

## Related skills

- Use `python-add-port` when the required application boundary does not exist
  yet.
- Use `python-add-env-settings-adapter` for the dedicated environment settings
  adapter workflow.
- Use `add-hexagonal-feature` when the change is a complete feature slice that
  spans domain, application, adapters, and tests.
