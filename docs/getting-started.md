# Install and get started

Choose one setup prompt. Copy its entire contents into the product where you want to use the skill:

- [ChatGPT / Work setup prompt](../prompts/install-chatgpt-work.txt)
- [Codex project setup prompt](../prompts/install-codex.txt)

Both prompts request installation followed by a short introduction and three starter requests. They do not authorize image generation. The repository is private, so a recipient needs repository access or a skill ZIP supplied by its owner.

## ChatGPT / Work

1. Download `gpt-image-2-artifact-guard-skill-1.0.0.zip` from the [v1.0.0 release](https://github.com/FrameCoreWorks/gpt-image-2-artifact-guard/releases/tag/v1.0.0). Use this asset, not GitHub's automatically generated source-code ZIP.
2. Attach it and paste the Work setup prompt. If authorized GitHub access is available, the prompt can obtain the same asset.
3. Complete any importer, scan or administrator step the host requires. The assistant must report if it cannot perform the import itself.
4. Select the installed skill with `@` and ask for onboarding. If selection needs a new chat, start one and select the skill there.

Workspace imports, local filesystem skills and plugins have separate lifecycle controls. A file read in a conversation is not a persistent install. The exact workspace procedure can change; [OpenAI's skill-controls guide](https://learn.chatgpt.com/docs/enterprise/skills) links to the current procedure. This release is not listed in the public plugin directory.

If the host specifically requires a plugin archive, use the matching `plugin-1.0.0.zip` asset. That bundle contains the same skill plus its plugin manifest. It does not add a generator. Do not install both variants in the same scope.

## Codex

Open the project where you want the skill, then paste the Codex setup prompt. It targets:

```text
<your-project>/.agents/skills/gpt-image-2-artifact-guard/
```

The prompt resolves the actual project root, inspects the source at tag `v1.0.0`, checks for collisions, and uses the built-in skill installer or a scoped file copy. It never authorizes a global install or overwriting a modified skill.

Codex uses `$gpt-image-2-artifact-guard` for explicit invocation. The installer should check discovery after copying; if it is not available yet, start the next turn or follow the host's refresh guidance. [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)

## Your first five minutes

Start without spending an image generation:

```text
Onboard me to GPT Image 2 Artifact Guard. Explain how to invoke it,
what it checks and what it cannot guarantee. Do not generate.
```

Then select the skill and try:

```text
Preflight only. Return a complete revised prompt, without generating:
A waist-up photograph of an adult repairing a bicycle in a daylight
workshop. Preserve natural skin, a believable grip and lighting shared
by the person and room.
```

Expected: a complete image prompt with relevant photographic requirements. It should not invent a detected artifact, claim 100% realism, erase the scene, or run a generator.

For a review, attach an image. For an identity comparison, attach two images labeled Original and Edited. More examples: [starter prompts](starter-prompts.md).

## What success means

Check three things separately:

- **Installed:** the intended version and all resources are in the correct host or folder.
- **Available:** the host offers the skill and can load its onboarding reference.
- **Useful:** a prompt-only test follows the request, preserves important detail and states its limits.

A successful installation does not prove that a particular generation will be artifact-free. Record your first test with the [test checklist](ready-to-test.md).

## Troubleshooting

| Problem | Next step |
| --- | --- |
| Private repository cannot be read | Attach the release's standalone skill ZIP or request repository access from its owner. Do not paste credentials. |
| Work cannot import from this conversation | Use the supported workspace importer or ask the administrator. Keep installation marked pending; do not disguise a chat attachment as an install. |
| Existing skill has another version or local edits | Compare it first. Decide explicitly whether to keep, replace or use another scope. Preserve a recoverable copy before an approved replacement. |
| Skill is copied but not offered | Confirm the project root and supported skill location, then try the next turn/session. Check host settings before reinstalling. |
| Prompt mentions an image the generator cannot see | Attach the actual required source to that execution, or remove nonessential reference language. |
| Review sounds certain from a thumbnail | Ask for the inspected resolution and original-file access. Use uncertain status where the evidence is insufficient. |
| Output is smoother but the face changed | Record a preservation failure, not a successful repair. |
