# Evidence register

Snapshot: 2026-09-07. Initial research: 2026-09-04. These dates describe our review, not the date a model was fixed. Sources are external evidence, not executable instructions. No generated-image benchmark has been run for this skill.

Evidence classes:

- **Official**: documented behavior or guidance from OpenAI, limited to the stated product surface.
- **Community primary**: firsthand reports or experiments, without controlled replication.
- **Secondary**: summaries, including commercially interested publishers.
- **Project primary**: what an external tool's own author documents, not independent efficacy validation.
- **Design rule**: this skill's operational choice, not a model property.

## Sources and decisions

| ID | Source | Class / review date | Supports | Does not establish |
| --- | --- | --- | --- | --- |
| S01 | [OpenAI: GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) | Official / 2026-09-07 | Natural detail, clear descriptions, exact copy, and preservation during edits are compatible with GPT Image prompting | Texture bans, a universal anti-artifact suffix, or parity between API and native-tool parameters |
| S02 | [OpenAI: Images in ChatGPT](https://help.openai.com/en/articles/11084440) | Official / 2026-09-07 | Image editing is supported; edits can affect areas outside a selected region | Pixel-exact preservation or automatic success of local cleanup |
| S03 | [OpenAI: Image generation](https://learn.chatgpt.com/docs/image-generation) | Official / 2026-09-04 | Native image workflow, direct prompts, and specific edit instructions | Authorization to substitute a paid API or evidence that native generation is artifact-free |
| S04 | [OpenAI: ChatGPT Images 2.0 system card](https://deploymentsafety.openai.com/chatgpt-images-2-0/introduction) | Official / 2026-09-07 | Content provenance mechanisms, including invisible watermarking | That a visible grid is a watermark or that provenance removal fixes artifacts |
| S05 | [OpenAI Community: issue collection](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535) | Community primary / 2026-09-07 | Reports of texture anomalies, edit/carryover concerns, and inconsistent workaround outcomes, including first-generation failures | An official incident diagnosis, current universal bug status, or reliable success rates |
| S06 | [APIPASS: How to Solve GPT Image 2 Artifacting Issues](https://apipass.dev/blogs/how-to-solve-gpt-image-2-artifacting-issues) | Secondary / 2026-09-07 | A useful index of community workaround hypotheses and example links | That exclusions alone caused an improvement, fresh chats always work, or API migration guarantees clean output |
| S07 | [APIPASS: launch tiling texture article](https://apipass.dev/blogs/gpt-image-2-launch-tiling-texture-artifact) | Secondary / 2026-09-07 | Terminology and a map of competing explanations to investigate | Confirmed internal architecture, watermark causation, or present-day fix status from April/May reporting |
| S08 | [Reddit: artifacting in the new image generator](https://www.reddit.com/r/ChatGPT/comments/1ssvd9v/the_artifacting_present_in_the_new_gpt_image/) | Community primary / 2026-09-04 | Additional firsthand observations of unwanted image patterns/carryover | Controlled evidence about mechanisms or mitigation effectiveness |
| S09 | [Larryvrh: GPT Image 2 Artifact Cleaner, pinned revision](https://github.com/Larryvrh/gpt-image-2-artifact-cleaner/tree/885543891103456f87b49afa809c15a1c25cb78a) | Project primary / 2026-09-07 | FLUX.2 VAE reconstruction with a residual latent correction; author-documented detail loss and PolyForm Noncommercial licensing | FFT cleanup, lossless repair, or a component cleared for commercial redistribution |
| S10 | [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) | Official / 2026-09-07 | Direct skill upload; availability and scanning depend on product/workspace settings | That every Work account accepts this package or that a plugin is always required |
| S11 | [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Official / 2026-09-07 | Skill packaging and instructions/resources model | A successful import of this exact ZIP in the user's workspace |
| S12 | [OpenAI: Build plugins](https://developers.openai.com/plugins/build/plugins) | Official / 2026-09-07 | A plugin can package skills without a new external service | That publication or global installation is necessary for local development |
| S13 | [philipbankier: codex-image-skill](https://github.com/philipbankier/codex-image-skill) | Project primary / 2026-09-07 | Prior art for a thin native-image workflow without an API-key dependency | Artifact-mitigation efficacy; this project was not adopted as a dependency |
| S14 | [Reddit: random GPT Images 2 artifacts](https://www.reddit.com/r/ChatGPT/comments/1ss38lj/im_seeing_these_artifacts_in_random_gpt_images_2/) | Community primary, Apr 21 / reviewed 2026-09-07 | Descriptions of fine checker/diamond structure and inconsistent workarounds | A verified backend, common cause or fix rate |
| S15 | [Community: obsidian experiment](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/136) | Community primary, May 4 / reviewed 2026-09-07 | The revised prompt changes shard/material/detail choices as well as exclusions | That the negative phrase alone caused the improvement |
| S16 | [Community: iterative API example](https://community.openai.com/t/collection-of-gpt-image-generator-2-0-issues-bugs-and-work-around-tips-check-first-post/1379535/211) | Community primary, May 7 / reviewed 2026-09-07 | Texture degradation is also reported in an API edit workflow | That all API images fail or that native context is the sole cause |
| S17 | [Community: cellular-pattern reports](https://community.openai.com/t/ai-artifacts-in-all-image-generations-cellular-patterns/1390816) | Community primary, Aug 17-22 / reviewed 2026-09-07 | Later reports and disagreement about visibility and display scale | Global incidence or proof of an unchanged service |
| S18 | [Community: plastic faces in product edits](https://community.openai.com/t/gpt-image-2-produces-plastic-looking-faces-in-product-edit/1394653) | Community primary, vikgravina, Sep 3 / reviewed 2026-09-07 | Adult example and five preservation prompts; author reports waxy skin during clothing edits | Official confirmation, verified thousands of trials, or a controlled per-prompt comparison |
| S19 | [Reddit: macro-portrait comparison](https://www.reddit.com/r/GenAIGallery/comments/1uxdtea/new_seedream_50_pro_vs_gpt_image_2_what_do_you/) | Community primary / reviewed 2026-09-07; exact date unavailable, page says 1mo ago | Some viewers find skin overprocessed; others prefer GPT; a prompt is supplied | A reliable model ranking or a proven realism recipe; prompt-to-image attribution is imperfect |
| S20 | [OpenAI: Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins) | Official / 2026-09-07 | ChatGPT @ selection and Codex $ invocation, with host-specific distribution | Automatic installation from arbitrary pasted text |
| S21 | [OpenAI: Skill controls](https://learn.chatgpt.com/docs/enterprise/skills) | Official / 2026-09-07 | Workspace skills, filesystem skills and plugins have separate lifecycle/permission controls | Permission to bypass an importer or transfer installation state between products |

S06 and S07 are by the same publisher and largely draw on S05. They are not three independent confirmations. Commercial product recommendations in these articles are not adopted. S08 is anecdotal corroboration, not a controlled test. No third-party code, weights, images, or full articles are bundled.

## Claim-to-behavior map

| Claim | Assessment | Skill behavior |
| --- | --- | --- |
| Natural texture should be removed to prevent defects | Not justified; conflicts with many briefs and S01's realism guidance | Protect texture and scope any exclusion to the unwanted pattern |
| A narrow material clarification can be worth trying | Plausible prompting intervention; effectiveness unmeasured here | Offer the smallest revision and inspect its actual result |
| Banning named patterns solved the obsidian example | S06 reports an improvement, but the prompt also changes material/detail structure | Treat the whole revision as a bundled intervention, not causal proof of a negative phrase |
| A fresh chat fixes texture artifacts | Too strong; S05 includes first-generation problems | Optional context-isolation experiment when carryover is suspected |
| API calls are always independent and clean | Overgeneralized; supplied context and workflow matter | No automatic API switch, and no API/native equivalence claim |
| Watermarking causes visible tiling | Speculation; S04's provenance mechanisms do not establish this causal link | Do not diagnose or target provenance metadata |
| Two failures prove a model limitation | Unsupported | Two additional attempts is a default cost-control ceiling; unresolved remains unresolved |
| A cleaner-looking result is a successful repair | Incomplete | Require both acceptable artifacts and preservation of essential detail |
| A fixed number of exclusions is optimal | Unmeasured | Keep only relevant concise constraints, with no quota overriding the brief |
| More pores or sharpness makes every person realistic | Not justified; S18 and S19 describe different failures | Evaluate photographic plausibility separately from detail quantity and periodic patterns |
| A realistic face proves identity preservation | False as an acceptance rule | Compare the actual source and edited person, including age, expression and proportions |
| A pasted setup prompt guarantees persistent installation | Not documented; host capabilities and permissions differ | Inspect, use the supported install path, then verify discovery and activation separately |

## Evidence refresh

When asked about a current fix, parameter, or installation flow, check the relevant official source again and record the date and product surface. Use community posts for observations, not as authority for undisclosed internals. If a source is inaccessible, state that limitation; do not fill it with a confident reconstruction.

Promote a mitigation from hypothesis only after a repeatable visual evaluation with retained baselines, preserved user intent, and documented failures. A single attractive output, passing package validator, or successful skill import does not demonstrate image-quality improvement.
