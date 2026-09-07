# Verification record

Date: 2026-09-07. Version: 1.0.0, ready to test.

## Summary

Local source/package checks passed. Five new text-only cases passed their important criteria. An independent technical review found no blocking problem in the reviewed scope. This is not evidence of live Work import, host-level automatic activation or improved generated-image quality.

| Layer | Observed result |
| --- | --- |
| Source and deterministic release packaging | PASS |
| Isolated archive extraction/file-copy roundtrip | PASS, not a live host installation |
| New text-only instruction smoke test | 5 exercised cases passed; method limits below |
| Work import/scanning and persistent installation | Not run |
| Codex host discovery and automatic triggers | Not run |
| Controlled visual mitigation/realism benchmark | Not run |

## Commands and checks

Commands were run from the repository root unless stated otherwise. Creator validators were invoked from the installed OpenAI system-skill locations; machine-specific paths are intentionally omitted from this portable record.

| Check | Actual result |
| --- | --- |
| `python3 -B -m unittest discover -s tests -v` | PASS: 15 tests, also independently rerun by Eryk |
| OpenAI skill-creator `quick_validate.py skills/gpt-image-2-artifact-guard` | PASS: `Skill is valid!` |
| OpenAI plugin-creator `validate_plugin.py .` | PASS: plugin validation passed |
| `python3 -B scripts/package.py` | PASS: two ZIPs, two setup prompts and a checksum manifest built |
| `python3 -B scripts/package.py --check` | PASS: all five release files match current sources |
| `shasum -a 256 -c SHA256SUMS-1.0.0.txt` from `dist/` | PASS: all four covered assets reported OK |
| Extract each ZIP into a separate isolated temporary directory, run its respective creator validator | PASS for standalone skill and plugin |
| `git diff --check` | PASS |
| Export only the staged source into a fresh temporary directory, then run unit tests and build/check | PASS: 15 tests and all five deterministic release files; no dependency on unpublished local variants |
| Limited staged-text scan for private machine paths and recognizable credential formats | No matches; not a full security audit |
| README banner reference and PNG header/dimensions | PASS in the source tests: selected PNG is 1983 × 793 |
| GitHub repository identity and visibility via `gh repo view` | Verified FrameCoreWorks/gpt-image-2-artifact-guard, PRIVATE, main |

The unit tests cover required resources, version consistency, portable paths, local links, fixture structure, deterministic ZIPs/checksums, exact setup-prompt copies, identical skill payloads, isolated file-copy roundtrip, overwrite refusal, unexpected runtime files and symlink rejection. They do not execute the natural-language fixtures or score image quality.

The independent reviewer inspected the setup prompts, onboarding, README, readiness checklist, manifest, skill core, packager and tests. It checked the local installer's support for `--ref` and `--dest` without performing an installation. It found no material release blocker. This does not validate every possible host/account configuration.

## Instruction behavior

[Exact v1 inputs, outputs and author assessment](../tests/forward-test-v1-2026-09-07.md) retain five requests covering:

- Naturally smooth young skin with makeup and studio/cinematic lighting.
- Fine diagonal microtexture while preserving dense foliage and droplets.
- Intentional glossy CGI and checker design.
- An unseen identity-sensitive edit that must not be passed.
- Onboarding without a false permanent-installation claim.

A fresh named image-prompt evaluator, Iga, read the skill and relevant references without access to the rubrics. All five requests ran in one evaluator task with its normal instructions active. The main author judged the returned outputs; this was not a blind independent judge. The exact backend model identifier was not reported.

There are 25 scenario definitions in the fixture suite, including historical Polish inputs for language coverage. Only the five v1 cases above were executed in this new run. Do not call all 25 cases passed, or treat directly requested skill use as automatic trigger validation.

The [historical v0.1 smoke record](../tests/forward-test-2026-09-07.md) retains 12 positive scenarios and one focused retest. Those earlier results are not a fresh regression run of the modified v1 instructions. Polish raw inputs and outputs remain untranslated to preserve evidence; current product documentation is English.

## Release payload identity

The standalone instruction ZIP used to identify the v1 smoke-test source has SHA-256:

```text
9c3f2ea139bd700cfb41749db26ea9d7bf2d72bb05c3640f528dfd52821fd392
```

The versioned checksum manifest covers both ZIPs and both copy-ready setup prompts. Archives contain instructions and metadata only. The plugin adds its manifest to an otherwise identical skill payload. Tests, packaging scripts, the cover artwork, user reference images, credentials and third-party code/models are not installed by either ZIP.

The repository remains private. Versioned release files are distributed as assets of the [v1.0.0 test release](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/releases/tag/v1.0.0), not as committed build files. This delivery mechanism is separate from importer acceptance.

## Not established

- Real Work import/scanning, account availability or selector activation.
- Running either entire install-and-onboard prompt on a target account.
- Automatic positive/negative trigger behavior in a live Codex or Work installation.
- Image-based diagnosis accuracy on user originals, or paired identity preservation.
- Artifact reduction, photographic-realism improvements, a cure rate or universal failure mechanism.
- Live mobile/README viewport QA or quantitative fidelity of the banner's deliberately illustrated pattern.

No external image provider/API, third-party cleaner, user-image upload, global skill installation or registry change was performed for these tests. The banner was generated separately with the native image tool and is not an evaluation run of Artifact Guard.

Next steps are in the [first-test checklist](ready-to-test.md) and [evaluation protocol](../tests/evaluation-protocol.md).
