# stateaxis-automatic-prefix-cache

Extension ID: `org.vllm-hust.stateaxis-automatic-prefix-cache`

Automatic content-addressed prefix reuse with lease-safe bounded LRU residency.

This repository is the independent MOD boundary for StateAxis issues [#55](https://github.com/Qixin-Gaoke/stateaxis/issues/55), [#95](https://github.com/Qixin-Gaoke/stateaxis/issues/95).
It is deliberately `import_only`, default-off, and cannot be enabled. The split does
not inherit correctness, device, performance, or publication qualification from the
aggregate StateAxis repository.

## Evidence boundary

Status: **scoped-positive**.

Repeated-prefix benefit is positive; the measured 3+3 default-path overhead was 0.0256%. Scope does not transfer beyond the frozen repeated-prefix cell.

The copied evidence and its SHA-256 are recorded in `PROVENANCE.json`. Negative,
failed, and inconclusive results are retained. Microbenchmarks and component results
must not be restated as online end-to-end gains.

## Install and inspect

```bash
python -m pip install .
vllm-hust-ext extension inspect org.vllm-hust.stateaxis-automatic-prefix-cache
vllm-hust-ext extension check org.vllm-hust.stateaxis-automatic-prefix-cache
```

Discovery does not enable the MOD. A future active revision must extract an
independently reviewable implementation, declare exclusive resources where needed,
and pass exactness, lifecycle, release, failure-recovery, and matched real-online
gates.

## Validate

```bash
python -m pip install -e '.[test]'
pytest -q
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
