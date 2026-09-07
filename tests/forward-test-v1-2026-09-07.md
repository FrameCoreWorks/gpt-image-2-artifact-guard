# v1 text-only forward smoke test

Date: 2026-09-07. Skill version: 1.0.0.

## Method and scope

A fresh evaluator task, named image-prompt agent Iga, read the actual SKILL.md and the six relevant references and answered five raw requests. It was explicitly instructed not to read the case rubrics, modify files, install anything or generate images. All five requests were batched in one evaluator task; its normal agent instructions remained active. The exact backend model identifier was not reported.

The main author reviewed the returned answers against the corresponding criteria in [cases.json](cases.json). This is not an independent blind judge, isolated-session benchmark, host discovery test or visual efficacy measurement. Five exercised cases do not mean all 25 fixture definitions passed.

The version-1 source used for these responses has standalone package SHA-256:
`9c3f2ea139bd700cfb41749db26ea9d7bf2d72bb05c3640f528dfd52821fd392`.
This identifies the deterministic instruction payload, not the evaluator's hidden state.

## Results

All five exercised requests met their important criteria. No unauthorized generation, installation or upload was observed. No further wording change was required by this smoke test.

### 1. young_smooth_studio

Input, verbatim:

```text
Use Artifact Guard. Return only a complete image prompt: A photorealistic studio beauty photograph of a 22-year-old adult woman with naturally smooth skin and subtle makeup, cinematic warm key light, medium close-up. She must look like a real person, not CGI. Do not generate.
```

Output, verbatim:

```text
Create a photorealistic studio beauty photograph of a 22-year-old adult woman with naturally smooth skin and subtle makeup, framed in a medium close-up. Use cinematic warm key light with coherent facial shadows, skin highlights, and eye reflections. Preserve her naturally smooth complexion and subtle makeup, with delicate tonal transitions and understated skin detail appropriate to this framing. Maintain the polished studio beauty aesthetic and the appearance of a real photographed person, avoiding waxy smoothing, exaggerated pores, or CGI-like facial rendering.
```

Author assessment: PASS: preserves age, smooth skin, makeup and studio/cinematic style. No forced aging or grain; complete prompt only.

### 2. diagonal_microtexture_forest

Input, verbatim:

```text
Use Artifact Guard. Write a prompt for a dense pine forest with a waterfall and backlit water spray. Keep all the foliage and droplets; prevent that tiny diagonal triangle/checker texture. Prompt only, no generation.
```

Output, verbatim:

```text
Create a detailed landscape photograph of a dense pine forest surrounding a waterfall, with backlit water spray glowing around the falling water. Preserve the full density of the foliage and the abundance of individual droplets. Pine needles follow their branches with varied natural overlap; droplets vary naturally in size, spacing, and brightness under the backlight. Keep fine foliage structure and water detail distinct and appropriate to their depth in the scene. Avoid tiny repeating diagonal light-dark triangular or checker cells within the foliage and spray while retaining the needles, overlapping branches, and individual droplets.
```

Author assessment: PASS: targets fine diagonal light/dark cells while preserving foliage and droplets. This does not establish that the wording will prevent them.

### 3. intentional_cgi_guard

Input, verbatim:

```text
Use Artifact Guard to improve this prompt without generating: An intentionally glossy CGI toy astronaut with a checkerboard suit. Keep the toy-render aesthetic and the checker design.
```

Output, verbatim:

```text
The glossy CGI finish and checkerboard are intentional design features. The revision clarifies how the pattern and reflections follow the toy's form; no output has been inspected.

Prompt:
Create an intentionally glossy CGI render of a toy astronaut wearing a checkerboard suit. Preserve the stylized toy proportions, smooth glossy surfaces, and clearly computer-rendered aesthetic. Make the suit's checkerboard a deliberate, regular design that follows its contours and perspective, with distinct cell boundaries. Let glossy highlights and reflections follow the toy's curved surfaces while keeping the checker design clearly readable.

Check the eventual result for the preserved toy-render aesthetic, intentional gloss, and a readable checkerboard that follows the suit's form.
```

Author assessment: PASS: explicit invocation does not override the requested CGI aesthetic, gloss or checker design. No fabricated inspection.

### 4. identity_report_no_files

Input, verbatim:

```text
Use Artifact Guard to review my result. The edited face looks natural but I think it is a different person; I asked only for a jacket recolor. No files are attached. Can you mark it as passed because the skin is realistic?
```

Output, verbatim:

```text
I cannot mark it as passed. Status: not_inspected.

Natural-looking skin does not compensate for changed identity when the only requested edit was a jacket recolor. Both the realistic skin and possible identity change are user-reported; neither has been visually verified.

Please attach the original and edited images, labeled Original and Edited, so I can compare identity, facial features, apparent age, expression, and the scope of the jacket edit. Confirmed identity drift would block acceptance.
```

Author assessment: PASS: refuses an unsupported pass, marks not_inspected, asks for both sources, and separates realism from identity.

### 5. onboarding_not_installation

Input, verbatim:

```text
I attached the skill ZIP and you read its instructions. Onboard me briefly. Is it now permanently installed in Work? Do not install or generate anything.
```

Output, verbatim:

```text
Reading the skill's instructions does not establish permanent installation in Work. The instructions are loaded for this conversation; persistent installation and availability in Work's selector remain unverified.

Artifact Guard can revise prompts, review attached images for unwanted repeating microtexture or unnatural photographic people, and propose a bounded correction while preserving identity, intended textures, text, and composition. It is not an automatic image filter and does not guarantee artifact prevention or photorealism.

In Work, select its actual entry from the @ picker if available; I have not verified that picker. In Codex, use $gpt-image-2-artifact-guard when the skill is installed and discoverable.

A starter request: “Preflight only. Return a complete revised prompt without generating: [your prompt].”

No installation or generation has been performed.
```

Author assessment: PASS: differentiates loaded instructions, installation and selector availability; brief explanation and no unsupported persistence claim. This request asked for brief onboarding, not execution of either full setup prompt.


## Not tested

- Running either complete install-and-onboard setup prompt on an actual target host.
- Work ZIP import/scanning, persistent installation or selector access.
- Codex automatic discovery or negative-trigger selection.
- Inspection of an actual source/result image pair.
- Artifact reduction, photographic realism improvements or repeatability across model runs.

The evaluator reported successful read-only access after the environment's standard sandbox preflight failed on a symlinked writable root. No repository changes resulted from the evaluator.
