# Verification record

Date: 2026-09-07. Version: 0.1.0 local candidate.

This record reports local source checks and text-only evaluation. It is not evidence of a successful import or image-quality improvement.

## Source checks

Commands below were run from the project directory. The two creator validators were invoked from the installed OpenAI system-skill directories; those installation-specific absolute paths are intentionally not embedded in this portable project.

| Check | Result |
| --- | --- |
| `python3 -m unittest discover -s tests -v` | PASS: 10 tests, covering metadata/resources, local links, portability, fixture IDs, deterministic ZIPs/checksums, identical skill payloads, overwrite refusal, unexpected runtime files, and symlink rejection |
| OpenAI skill-creator `quick_validate.py skills/gpt-image-2-artifact-guard` | PASS: `Skill is valid!` |
| OpenAI plugin-creator `validate_plugin.py .` | PASS: plugin validation passed |
| Source scan for unfinished scaffold markers, private machine paths, and common credential markers in Markdown/JSON/YAML | No matches; this is a limited hygiene scan, not a security audit |

## Instruction smoke test

[Retained responses and assessment](../tests/forward-test-2026-09-07.md): 12 distinct positive scenarios and one focused retest, evaluated by the named image-prompt agent Iga without access to the answer rubrics. The main author assessed actual outputs against the rubrics.

No blocking failure was observed in the exercised scenarios. A formatting ambiguity around “only the prompt” was identified, fixed, and retested. All tests were text-only, batched in two turns of one evaluator task, with its normal agent instructions active. This does not validate isolated-session reliability or host-level automatic triggering.

The fixture suite contains 14 scenarios in total. The two negative-trigger scenarios have not been executed in a real installation. The number of fixture definitions is not the number of tests passed.

## Built artifacts

| Check | Result |
| --- | --- |
| `python3 scripts/package.py` | PASS: skill ZIP, plugin ZIP, and versioned SHA-256 manifest created |
| `python3 scripts/package.py --check` | PASS: both archives and checksum manifest match the current source snapshot |
| `shasum -a 256 -c SHA256SUMS-0.1.0.txt` from `dist/` | PASS: both ZIPs reported `OK` |
| Extract standalone skill to an isolated temporary directory, run `quick_validate.py` on extracted skill | PASS: `Skill is valid!` |
| Extract plugin to a separate isolated temporary directory, run `validate_plugin.py` on extracted plugin | PASS: plugin validation passed |

Archives contain instructions and metadata only. The plugin adds its manifest to an identical skill payload. Repository scripts, tests, private paths, environment values, user images, and third-party code/models are not bundled. Archive sizes at this build were approximately 35 KiB for the skill and 37 KiB for the plugin. These checks prove local packaging consistency, not acceptance by a remote importer.

## Not run

- Import/scanning on the user's ChatGPT/Work account.
- Installation and automatic trigger evaluation in the user's Codex environment.
- Image generation, image editing, or a paired visual benchmark.
- External generation-provider/API calls, image uploads, or global registry changes.

## Private GitHub distribution

The user subsequently requested a separate GitHub repository. Both the connected GitHub account and the authenticated CLI identified `FrameCoreWorks`. Repository creation was verified as `PRIVATE` at [FrameCoreWorks/gpt-image-2-artifact-guard](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard).

Only this skill project's source is in scope for the initial push. Generated ZIPs and checksums are distributed as prerelease assets rather than committed build files. This distribution step does not change the unverified live-import and image-quality status above.
