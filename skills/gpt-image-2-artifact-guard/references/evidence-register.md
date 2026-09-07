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
| S09 | [Larryvrh: GPT Image 2 Artifact Cleaner](https://github.com/Larryvrh/gpt-image-2-artifact-cleaner) | Project primary / 2026-09-07 | A separate post-processing approach whose author documents texture loss, global VAE reconstruction, and noncommercial licensing | A lossless repair method or a component cleared for our commercial distribution |
| S10 | [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) | Official / 2026-09-07 | Direct skill upload; availability and scanning depend on product/workspace settings | That every Work account accepts this package or that a plugin is always required |
| S11 | [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Official / 2026-09-07 | Skill packaging and instructions/resources model | A successful import of this exact ZIP in the user's workspace |
| S12 | [OpenAI: Build plugins](https://learn.chatgpt.com/docs/build-plugins) | Official / 2026-09-07 | A plugin can package skills without a new external service | That publication or global installation is necessary for local development |
| S13 | [philipbankier: codex-image-skill](https://github.com/philipbankier/codex-image-skill) | Project primary / 2026-09-07 | Prior art for a thin native-image workflow without an API-key dependency | Artifact-mitigation efficacy; this project was not adopted as a dependency |

S06 and S07 are by the same publisher and largely draw on S05. They are not three independent confirmations. Commercial product recommendations in these articles are not adopted. S08 is anecdotal corroboration, not a controlled test. No third-party code, weights, images, or full articles are bundled.

## Claim-to-behavior map

| Claim | Assessment | v0.1 behavior |
| --- | --- | --- |
| Natural texture should be removed to prevent defects | Not justified; conflicts with many briefs and S01's realism guidance | Protect texture and scope any exclusion to the unwanted pattern |
| A narrow material clarification can be worth trying | Plausible prompting intervention; effectiveness unmeasured here | Offer the smallest revision and inspect its actual result |
| Banning named patterns solved the obsidian example | S06 reports an improvement, but the prompt also changes material/detail structure | Treat the whole revision as a bundled intervention, not causal proof of a negative phrase |
| A fresh chat fixes texture artifacts | Too strong; S05 includes first-generation problems | Optional context-isolation experiment when carryover is suspected |
| API calls are always independent and clean | Overgeneralized; supplied context and workflow matter | No automatic API switch, and no API/native equivalence claim |
| Watermarking causes visible tiling | Speculation; S04's provenance mechanisms do not establish this causal link | Do not diagnose or target provenance metadata |
| Two failures prove a model limitation | Unsupported | Two additional attempts is a default cost-control ceiling; unresolved remains unresolved |
| A cleaner-looking result is a successful repair | Incomplete | Require both acceptable artifacts and preservation of essential detail |
| One surface-specific exclusion is optimal | Unmeasured | Use as an editing default to avoid clutter, not a performance claim |

## Evidence refresh

When asked about a current fix, parameter, or installation flow, check the relevant official source again and record the date and product surface. Use community posts for observations, not as authority for undisclosed internals. If a source is inaccessible, state that limitation; do not fill it with a confident reconstruction.

Promote a mitigation from hypothesis only after a repeatable visual evaluation with retained baselines, preserved user intent, and documented failures. A single attractive output, passing package validator, or successful skill import does not demonstrate image-quality improvement.
