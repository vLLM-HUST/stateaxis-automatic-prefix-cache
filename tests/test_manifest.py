import hashlib
import json
from pathlib import Path

from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_automatic_prefix_cache


def test_policy_is_discoverable_and_experimentally_activatable() -> None:
    manifest = load_manifest(
        Path(stateaxis_automatic_prefix_cache.__file__).with_name(
            "vllm-hust-extension-v0.3.json"
        )
    )
    assert manifest.bundle_id == "org.vllm-hust.stateaxis-automatic-prefix-cache"
    assert manifest.bundle_version == "0.2.0"
    assert manifest.schema_version == "0.3-experimental"
    assert activation_blocker(manifest) is None
    assert dict(manifest.implementation[0].attributes)["status"] == "active"
    assert manifest.resource_claims[0].resource == (
        "stateaxis.runtime.prefix-state-ownership"
    )
    additional = dict(manifest.activation.additional_config)
    research_manifest = (
        Path(stateaxis_automatic_prefix_cache.__file__).parents[2]
        / "RESEARCH_MANIFEST.json"
    )
    assert (
        additional["stateaxis_mod"]["manifest_sha256"]
        == hashlib.sha256(research_manifest.read_bytes()).hexdigest()
    )
    assert additional["stateaxis_mod"]["performance_qualified"] is False
    assert additional["stateaxis_automatic_prefix_cache"] == {
        "enabled": True,
        "max_entries": 2,
        "block_tokens": 128,
        "lease_safe": True,
        "verify_tokens_after_hash": True,
        "fail_closed": True,
    }


def test_research_manifest_and_python_contract_match() -> None:
    research_manifest = (
        Path(stateaxis_automatic_prefix_cache.__file__).parents[2]
        / "RESEARCH_MANIFEST.json"
    )
    payload = json.loads(research_manifest.read_text())
    assert payload["mod_id"] == stateaxis_automatic_prefix_cache.MOD_ID
    assert payload["version"] == "0.2.0"
    assert payload["mechanism"] == {
        "name": "lease-safe-content-addressed-prefix-cache",
        "enabled": True,
        "max_entries": 2,
        "block_tokens": 128,
        "lease_safe": True,
        "verify_tokens_after_hash": True,
        "fail_closed": True,
    }
    assert payload["qualification"]["performance_qualified"] is False
    assert (
        payload["qualification"]["evidence_label"]
        == "historical-matched-real-online-no-harm-scoped"
    )
    provenance = json.loads((research_manifest.parent / "PROVENANCE.json").read_text())
    assert provenance["implementation_extracted"] is True
    assert (
        provenance["implementation_boundary"]["research_manifest_sha256"]
        == hashlib.sha256(research_manifest.read_bytes()).hexdigest()
    )


def test_only_bounded_contract_is_constructible() -> None:
    config = stateaxis_automatic_prefix_cache.automatic_prefix_cache()
    assert config.max_entries == 2
    assert config.block_tokens == 128
    assert config.fail_closed is True

    try:
        stateaxis_automatic_prefix_cache.AutomaticPrefixCacheConfig(max_entries=3)
    except ValueError as error:
        assert "bounded two-entry" in str(error)
    else:
        raise AssertionError("broader APC capacity must fail closed")
