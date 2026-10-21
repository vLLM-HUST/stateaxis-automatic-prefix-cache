# stateaxis-automatic-prefix-cache

Extension ID: `org.vllm-hust.stateaxis-automatic-prefix-cache`

Automatic content-addressed prefix reuse with lease-safe bounded LRU residency.

This repository is the independent MOD boundary for StateAxis issues [#55](https://github.com/Qixin-Gaoke/stateaxis/issues/55), [#95](https://github.com/Qixin-Gaoke/stateaxis/issues/95).
It is default-off and is admitted only through the vLLM-HUST Extension Manager
StateAxis provider in explicit experiment mode. The split does not inherit
correctness, device, performance, or publication qualification from the aggregate
StateAxis repository.

## Evidence boundary

Status: **historical no-harm in one cell; independent implementation unqualified**.

Original measured figures, raw records, failed attempts and limitations are now
maintained in [benchmark's frozen report](https://github.com/vLLM-HUST/vllm-hust-benchmark/blob/ddc4f6a3290e447260fc8f6c03ea36d3ca514e23/archive/mod-git-20261021/stateaxis-automatic-prefix-cache/snapshot/README.md) and
[original evidence index](https://github.com/vLLM-HUST/vllm-hust-benchmark/blob/ddc4f6a3290e447260fc8f6c03ea36d3ca514e23/archive/mod-git-20261021/stateaxis-automatic-prefix-cache/snapshot/EVIDENCE.md). See [EVIDENCE.md](EVIDENCE.md)
for immutable source links and verified external-cache retrieval.

The historical closure exercised no authoritative cache hits and does not
establish an online speedup. The independent implementation remains unqualified.
Negative, failed and inconclusive results remain unchanged in benchmark.

## Install and inspect

```bash
python -m pip install .
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-automatic-prefix-cache
vllm-hust-ext extension check org.vllm-hust.stateaxis-automatic-prefix-cache
```

Discovery alone does not enable the MOD. The active Manifest 0.3 contract is
accepted only with `experiment_mode=true`, the exact `RESEARCH_MANIFEST.json`
digest, and the matching StateAxis host identity. The independently reviewable
content-addressed, collision-verified, lease-safe LRU index lives under `native/`.
StateAxis remains responsible for resident-state validation, device eviction,
lifecycle cleanup, and fail-closed rollback.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
cargo test --manifest-path native/Cargo.toml
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
