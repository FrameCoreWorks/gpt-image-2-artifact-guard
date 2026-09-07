# Onboarding

Use when asked how to start, what this skill does, how to invoke it, or what results to expect. Do not generate, edit, install, upgrade or upload as a side effect of onboarding.

## Verify the status first

Report only the state you can observe:

- Instructions loaded in this conversation.
- Skill files installed at a known location.
- Skill available in the host selector.
- Explicit invocation and required reference access verified.

These are different states. Loading an attached SKILL.md is not proof of persistent installation. If discovery needs a new turn, chat or restart, give the host-supported next step and keep activation unverified until checked. Do not ask for credentials.

If installation is requested, use the host's actual installation capability and approval flow. Inspect the supplied package, source, version and existing copies first. Do not overwrite a different or modified installation blindly. Do not infer installation authority from a request for help.

## Brief introduction

After the status, explain in the user's language, normally within 150 words:

- Select the actual skill entry with @ in ChatGPT/Work, or use $gpt-image-2-artifact-guard in Codex. If the picker is unavailable, say so rather than pretending the mention worked.
- Preflight checks a prompt and can return a complete revised prompt with a task-specific anti-artifact/realism layer.
- Review inspects an attached image for fine repeating triangular/diamond texture and, where relevant, photographic people.
- Recovery proposes one bounded intervention while protecting identity, intended textures, exact text and composition.
- Expected outputs are usable prompts, evidence-based reviews and correction plans. No guaranteed artifact prevention, automatic pixel filter, or guaranteed photorealism is provided.

Use a short explanation, not a full research report. Do not show every mode-specific reference unless it is relevant.

## Starter requests

In ChatGPT/Work, select the skill before sending one. In Codex, prefix it with $gpt-image-2-artifact-guard.

### Prompt check, no attachment needed

> Preflight only. Return a complete revised prompt, without generating: A waist-up photograph of an adult repairing a bicycle in a daylight workshop. Preserve natural skin, a believable grip, and lighting shared by the person and room.

### Image review, attach the image

> Review the attached image for fine triangular or diamond-shaped repeating microtexture. Distinguish unwanted patterns from intentional texture. State the regions inspected and any uncertainty. Do not edit or regenerate.

### Identity check, attach Original and Edited

> Review the two attached images, labeled Original and Edited. The intended change was the jacket color only. Check identity, age, expression, skin, eyes, anatomy and lighting. If there is drift, propose one targeted recovery prompt. Do not execute it.

If the user wants only a prompt, output only that complete prompt, except when missing essential input or unsupported controls require clarification.
