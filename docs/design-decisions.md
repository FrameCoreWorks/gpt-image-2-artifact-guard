# Design decisions

Date: 2026-09-07. Version: 1.0.0, ready to test.

## Scope

One standalone instruction product, distributed as a skill and as a plugin containing that same skill. It does not change the owner's global skill pipeline, install external tools or run an image-cleaning model.

## Decisions and tradeoffs

| Decision | Reason | Limitation |
| --- | --- | --- |
| One skill, two package formats | Hosts support different installation paths | Each actual importer must still be tested |
| Four modes: onboarding, preflight, review, recovery | Separate help, prompt work, diagnosis and execution permissions | A mode name does not authorize a generator or installation |
| Separate periodic texture, human plausibility and preservation | Grid-free skin can still look waxy; a realistic face can depict the wrong person | Requires visible evidence and context, not a single smoothness score |
| Conditional morphology and human references | Target tiny diagonal clusters without confusing them with large tiles or intentional patterns | Written guidance is not a trained detector |
| Positive, task-specific prompt requirements | Protect materials and people while making the desired result concrete | Exact wording has not been benchmarked |
| No fixed exclusion quota | Relevant constraints matter more than an arbitrary count | Avoid redundant negative lists through judgment, not a one-item rule |
| Context isolation only as an optional experiment | First-generation failures are also reported | Missing references can destroy identity continuity |
| At most two additional authorized attempts by default | Bound time and generation cost | This is a workflow policy, not a model success threshold |
| No bundled cleaner, detector or API integration | Keep host portability and avoid new runtime, privacy and licensing obligations | Generation and viewing depend on the authorized host |
| Version-pinned setup prompts with explicit status reporting | Make installation and onboarding reproducible | Host approvals cannot be bypassed; an attached file is not an install |

## Photographic people

Realism must preserve age, makeup, lighting style and intended framing. It does not mean adding pores, wrinkles, dirt or grain to every face. Studio and cinematic photography remain valid. Intentional dolls, cartoons and CGI must not be converted to photography unless requested.

Edits protect the source person even when only clothing or background changes. A credible but different face is a preservation failure. “100% real” is a quality target, not a guarantee or an authenticity claim.

## Existing work and prior art

The initial local review found an anti-artifact module in an existing image-prompt skill. It remains unchanged. This repository is a separate distributable product requested by its owner, not a second global installation.

The public review considered `codex-image-skill` and `gpt-image-2-artifact-cleaner`. Neither is a dependency. The cleaner is a different post-processing method with detail-loss and licensing constraints. Source links and evidence limits are retained in the [evidence register](../skills/gpt-image-2-artifact-guard/references/evidence-register.md).

No private pipeline paths, permanent named-agent dependencies or third-party model files are required by the installed skill. Repository tests and packaging scripts are not bundled in the skill ZIP.

## What changed after the v0.1 audit

The [audit](skill-audit-2026-09-07.md) led to separate morphology and human-photorealism profiles, stronger source-person checks and additional test cases. Version 1.0 also adds installation/onboarding prompts and English documentation. It does not turn community hypotheses into confirmed mechanisms.

The previous default of one local exclusion was removed. A concise set of justified constraints is permitted; necessary user requirements must not be erased to satisfy a quota.

## Distribution and permissions

The GitHub repository stays private, and no public-distribution license has been chosen. Skill and plugin assets derive from the same source. The generated banner is cover artwork, not evidence of artifact removal.

The Codex setup prompt targets a project-local `.agents/skills/` folder. Work setup uses its actual supported importer and approval process. Neither setup prompt authorizes image generation, external providers, credential searches, uploads, global installation or overwriting a modified installation.

## Verification levels

Structural validity, a useful text response, a successful file copy, host discovery and a visual improvement are different outcomes. The [verification record](verification.md) identifies which were observed. A ready-to-test release is not an install-tested or efficacy-validated release.
