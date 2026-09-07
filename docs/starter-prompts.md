# Starter prompts

In ChatGPT/Work, select GPT Image 2 Artifact Guard with `@`. In Codex, prefix a request with `$gpt-image-2-artifact-guard`. These are requests to the assistant, not unsupported API parameters.

## Onboarding

```text
Onboard me to GPT Image 2 Artifact Guard in my language. Explain the
modes, invocation, expected outputs and limits. Give three starter
requests. Do not install anything or generate an image.
```

## Photographic person: prompt only

```text
Preflight only. Return only a complete generator-ready prompt.
I want a photorealistic waist-up photograph of an adult repairing a
bicycle in a daylight workshop. Preserve natural skin, a believable
grip, gaze toward the bicycle and coherent person/scene lighting.
Avoid a plastic-looking person without adding exaggerated pores.
Do not generate an image.
```

## Microtexture in a dense scene: prompt only

```text
Write a complete GPT Image 2 prompt for a dense pine forest with a
rocky stream, water spray and mist. I previously noticed repeating
diagonal triangular/diamond microtexture. Keep the dense foliage,
irregular spray and atmosphere. Add a relevant anti-artifact layer
without deleting these details. Do not generate.
```

## Visual review: attach the image

```text
Review the attached image for periodic triangular or diamond-shaped
microtexture and false microdetail. Distinguish these from real weave,
droplets, grain and display effects. State what you actually inspected,
the affected regions and uncertainty. Review only; do not edit or rerun.
```

## Clothing edit: attach Original and Edited

```text
Compare the two attached images, labeled Original and Edited. Only
the jacket color was meant to change. Assess identity, apparent age,
expression, skin, eyes, hair, pose and scene lighting separately from
repeated texture. If there is drift, provide one complete source-based
recovery prompt. Do not execute it.
```

## Preserve an intentional texture

```text
Preflight this GPT Image 2 prompt without generating: a studio photograph
of a red-and-white gingham cotton shirt. Keep the regular woven checks,
fine threads and seams. Protect the intended pattern while addressing
only a justified artifact risk.
```

## Bounded native generation, only when you want an image

```text
Use GPT Image 2 Artifact Guard to preflight and generate one image with
the built-in image generator, if available: a photorealistic waist-up
photograph of an adult reading a book beside a window, looking at the
page, natural skin and soft side daylight. Inspect the returned image.
No extra attempts, external providers or uploads. If built-in generation
is unavailable, return the complete prompt and explain that limitation.
```

The last request authorizes one native generation, not the local OpenAI API. The other requests are free of image-generation execution. Tool access and account limits still depend on the host.
