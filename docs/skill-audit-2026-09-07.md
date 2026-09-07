# Audit: microtexture and photographic people

Date: 2026-09-07. Baseline reviewed: 0.1.0. This English record preserves the audit findings and records their disposition in 1.0.0; it is not a new visual benchmark.

## Conclusion

The small preflight/review/recovery core did not need replacement. The user's examples and new requirement justified two more precise profiles: fine triangular/diamond checker microtexture and photographic plausibility of people.

Lack of a checker pattern does not establish human realism. More pores do not necessarily help. A realistic face that no longer matches the original person fails preservation.

## Findings and v1 disposition

| Finding against the earlier scope | v1 response | Remaining test |
| --- | --- | --- |
| Human realism was only partially covered by skin-detail preservation | Added [human photorealism](../skills/gpt-image-2-artifact-guard/references/human-photorealism.md), conditional routing and photographic-person triggers | Image-based assessment and controlled generation tests |
| The checker category did not clearly distinguish microtexture from large displaced tiles | Added [pattern morphology](../skills/gpt-image-2-artifact-guard/references/pattern-morphology.md), local-pattern guidance and false positives | Native-resolution examples and difficult counterexamples |
| A smoothness-led review could miss a changed face | Review separately assesses periodic texture, plausibility and preservation, including source comparison after clothing edits | Paired original/edited image tests |
| Text scenarios did not establish image recognition or mitigation efficacy | Expanded cases and retained separate evaluation gates | Live host activation and a visual pilot remain unverified |
| The earlier smoke test was batched and had no recorded backend model identifier | Preserve exact new inputs/outputs and identify evaluator context where available | Independent-session repetition on target hosts |
| Installation help needed to be a usable first-run path | Added version-pinned setup prompts, onboarding and a first-test checklist | Real Work import and host-level discovery |

These are scope and evidence findings, not proof that every listed defect occurs in every model run.

## Research interpretation

Firsthand reports describe fine repeating bright/dark clusters, diagonal checker or scale-like structures, and unnatural skin in some edits. They do not establish a single shared cause or a universal fix.

The official prompting guide supports explicit photographic framing, lighting, material behavior and preservation instructions. Community reports are observations, not manufacturer confirmation or controlled efficacy measurements. Relevant sources are recorded with dates, confidence and caveats in the [evidence register](../skills/gpt-image-2-artifact-guard/references/evidence-register.md).

Two human-realism examples informed the added scope:

- [Plastic-looking faces during a clothing edit](https://community.openai.com/t/gpt-image-2-produces-plastic-looking-faces-in-product-edit/1394653), a firsthand September 3 report with example prompts. It does not provide a controlled success/failure rate.
- [Macro-portrait comparison discussion](https://www.reddit.com/r/GenAIGallery/comments/1uxdtea/new_seedream_50_pro_vs_gpt_image_2_what_do_you/), a gallery and mixed aesthetic reactions. Exact publication date and complete prompt mapping were not verified; it is not a model ranking.

The [OpenAI prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) is guidance, not a promise that the adapted prompts will solve these reports. API examples do not grant access to hidden controls in a native ChatGPT or Codex tool.

## Banner correction

The selected [v6 banner](../assets/readme-banner-v6-microtexture.png) illustrates fine diagonal tonal repetition in a continuous forest scene. An earlier large-tile interpretation did not represent the user's intended problem and was not selected.

The final artwork was generated natively with its title in one pass. It deliberately depicts a defect and is not a naturally occurring failure or a repair result. [Prompt and provenance](readme-banner-v6.md)

## Validation disposition

The baseline audit observed 10 structural tests passing and the v0.1 packages matching their source. Those historical results do not validate modified v1 files.

For v1 commands, smoke-test outputs and untested gates, use the [verification record](verification.md). Do not count a generated banner as an evaluation of either morphology recognition or realistic people.
