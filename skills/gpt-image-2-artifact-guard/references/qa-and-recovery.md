# QA and bounded recovery

## Inspection order

1. Verify which file or preview is visible. Record source, available resolution, and intended use when known. Do not invent metadata.
2. Read the image at its intended display size. Inspect native-pixel regions only when the viewer actually allows it. Enlarging a thumbnail does not reveal original pixels.
3. Review high-value regions: face/hands, product edges, exact text, important fabric/stone/skin, plain surfaces, and boundaries between materials.
4. Distinguish observed defect from user report and hypothesis. Compare a suspected pattern across surfaces and zoom levels where possible.
5. Record the smallest useful repair target and protected features. Use `uncertain` if intentional texture and artifact cannot be separated.

## Recovery ladder

This is a choice of interventions, not a mandatory sequence of generation calls.

| Evidence | Candidate intervention | Preserve / check | Limit |
| --- | --- | --- | --- |
| Prompt gives incompatible properties to one surface | Clarify which property belongs where | Scene, style, intended complexity | Cannot establish the cause of a prior output by itself |
| Specific repeated pattern on one material | Positive material contract plus a narrow integrated exclusion | Real texture, object geometry | Prompt-only hypothesis until tested |
| Local defect in an otherwise acceptable image | Targeted edit using the actual source; mask only if supported | Identity, text, edges, untouched surfaces | Edits may extend beyond the requested region |
| Source itself carries heavy defects | Propose a clean reference or a new generation | Needed identity and composition anchors | Do not silently drop required references |
| Unrequested material/object resembles earlier input | Audit references and offer a context-isolation trial | Complete scene contract, clean necessary references | No guarantee of a backend reset or cure |
| Defect may be preview or compression related | Inspect original/native pixels before generation | Source pixels | PNG avoids further lossy encoding, not defects already present |
| Widespread degradation remains after allowed attempts | Stop with unresolved status and a documented next option | Best available version and traceability | Do not automatically buy, install, or switch providers |

## Trial protocol

Before an authorized attempt, state:

- Hypothesis and evidence status.
- The one main changed variable, or an explicit note that this is a bundled change.
- The actual input images and their roles.
- What must remain unchanged.
- What observation would justify acceptance.
- Remaining authorized attempts.

Keep a comparable baseline when available. A fresh prompt, different reference, larger shards, and new lighting all at once may yield a better image, but cannot establish which intervention worked. Stochastic variation also prevents treating one before/after pair as causal proof.

After the attempt, inspect the returned output. Accept only if the relevant artifact is reduced enough for the intended use AND protected detail is retained. If text changes or skin becomes waxy, record a regression even if the grid disappears. Do not overwrite or delete the user's originals.

Default maximum: two additional attempts after authorization, not two attempts automatically. A lower user limit wins. A larger explicit budget may supersede this default, but stop on serious regression or missing authority. Report unresolved outcomes without claiming a confirmed model fault.

## Context transfer

Use [clean handoff](../templates/clean-handoff.md) if the user chooses a fresh context. Transfer the full brief and only clean, authorized reference assets essential for continuity. Describe each attachment's role. If a necessary source is unavailable in the destination, request it there; do not write prompts referring to an absent file.

The handoff can record earlier observations as diagnostic notes outside the generator prompt. The generator prompt itself must stand alone. Neither a new chat nor text saying “fresh image” demonstrates that every internal service state has been reset.

## Out of scope for v0.1

No FFT-based automatic defect classifier, pixel filter, denoiser, upscaler, watermark removal, batch API runner, background monitor, or provider switch. Frequency patterns are not a sufficient classifier for real textures. External cleanup may sacrifice real detail and requires separate tool, privacy, and license review before any future integration.
