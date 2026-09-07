# Ready-to-test checklist

Version 1.0.0 packages a complete instruction workflow, examples and onboarding. It does not claim proven visual mitigation or universal installation compatibility.

Use this checklist on the target account. Preserve actual outcomes, including failed and ambiguous cases. [Verification record](verification.md) distinguishes what the author ran from tests for the recipient.

## Installation and onboarding

- Obtain the intended release asset, not the source-code ZIP. Record its SHA-256 and source/tag.
- Paste the appropriate [setup prompt](getting-started.md).
- Confirm the package name/version, destination and absence of conflicting copies.
- Record importer/scanner status in Work or source-to-installed-file comparison in Codex.
- Verify host discovery and explicit selection separately.
- Request onboarding: it should explain invocation, modes, expected outputs and limits briefly in your language, without generating an image.
- Start a fresh conversation and repeat explicit invocation. Then try a relevant request without mentioning the skill.
- Try an unrelated coding-artifact request without mentioning the skill. It should not attract an image workflow.

## Prompt-only acceptance

Use the [starter prompts](starter-prompts.md):

- Photographic people: preserve the scene, age and style; no universal pore, wrinkle or grain recipe.
- Fine checker pattern: target periodic microtexture, not large pasted triangles or missing objects.
- Gingham/CGI: preserve intentional pattern or stylization.
- Missing image: report `not_inspected`, not a fabricated diagnosis.
- Recovery plan: no execution without permission; required references stay attached.
- Prompt-only output: complete prompt, no unsolicited image generation or long report.

These are behavioral criteria. A structural script cannot judge them from keyword counts.

## Existing-image review

Start with images you have permission to use. Include true repetitive materials, smooth skin and resized previews as counterexamples. Record actual file/preview access, region, intended display size, status and uncertainty. Do not publish private or identifiable images in an issue without permission.

The author-provided banner intentionally illustrates microtexture. It is not a natural failure sample, an effectiveness test or a before/after pair.

## Optional visual pilot

Generation is a separate opt-in step with a total attempt budget. Follow [the evaluation protocol](../tests/evaluation-protocol.md): fixed brief and available settings, comparable baseline, one documented intervention, repetitions, retained failures, and blinded/randomized review where feasible.

Score periodic texture, human plausibility and preservation separately. A plausible but different face fails an identity-sensitive edit. A smoother image that loses required detail fails preservation. Report counts and limitations, not a universal cure rate.

## Report a result

Use this compact record, omitting personal or sensitive material:

```text
Version / source / checksum:
Host and date:
Install/import result:
Discovery and explicit invocation:
Request and authorized actions:
Input provenance and actual view:
Observed result:
Expected criterion:
Preserved details / regressions:
Status: pass / repair_candidate / regenerate_candidate / uncertain / not_inspected
Reproduction steps and remaining limitations:
```

For installation failures use pending, blocked or unverified rather than an image-review status. Keep raw screenshots and original images local unless you choose to share them.
