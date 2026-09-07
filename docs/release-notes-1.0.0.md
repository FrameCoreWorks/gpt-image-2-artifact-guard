# GPT Image 2 Artifact Guard 1.0.0

Ready-to-test prerelease for ChatGPT / Work and Codex.

## What's included

- Fine triangular/diamond checker microtexture guidance and false-positive checks.
- A photographic-human profile covering skin, eyes, hair, pose/contact, lighting and identity preservation.
- Complete prompt creation with a task-specific anti-artifact/realism layer.
- Onboarding plus English copy-ready installation prompts and starter requests.
- One standalone skill ZIP and one plugin ZIP containing the same skill.
- A native one-pass README banner illustrating the targeted microtexture.

## Start here

Download one package variant and its matching setup prompt. The repository is private, so authorized access or an owner-supplied ZIP is required.

- Work: `gpt-image-2-artifact-guard-skill-1.0.0.zip` plus `INSTALL-CHATGPT-WORK-1.0.0.txt`.
- Codex: paste `INSTALL-CODEX-1.0.0.txt` in the intended project. It requests installation from tag `v1.0.0`, not main.
- Use the plugin ZIP only when the chosen host workflow requires it. Do not install both variants in the same scope.
- Verify downloaded assets with `SHA256SUMS-1.0.0.txt`.

[Setup guide](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/blob/v1.0.0/docs/getting-started.md) · [Starter prompts](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/blob/v1.0.0/docs/starter-prompts.md) · [Test checklist](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/blob/v1.0.0/docs/ready-to-test.md)

## Verification and limits

15 structural/package tests passed, both creator validators passed, ZIPs passed isolated extraction checks, and five new text-only smoke cases met their criteria. An independent technical audit found no blocking issue in its reviewed scope.

Live Work import, host automatic discovery and visual mitigation efficacy have not been verified. The setup prompts respect host approvals and report unfinished steps instead of pretending that reading a ZIP creates a persistent installation. They do not authorize generation or a global install.

This is an instruction-and-review workflow, not an automatic image filter or model fix. It cannot guarantee artifact-free output or 100% photorealistic people. The banner is illustrative, not a repair result.

[Full verification record](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/blob/v1.0.0/docs/verification.md). No new runtime dependencies, external generation providers or public-distribution license are included. The repository stays private.
