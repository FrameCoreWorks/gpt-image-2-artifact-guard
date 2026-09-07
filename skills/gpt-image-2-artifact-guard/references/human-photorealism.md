# Photographic people

Use when the brief asks for photographic people or reports waxy skin, plastic faces, CGI-like rendering or identity drift. These are review criteria, not an automatic detector or a claim that every listed issue is specific to GPT Image 2.

## Establish the intended photograph

Keep the user's subject, age, identity, body, expression, makeup, styling, crop and lighting. Explicitly describe a photographic medium when that is the goal. Ground the action, gaze, framing, light and person/object interaction in the scene.

"100% real" is a demanding appearance target, not a guarantee, an authenticity claim or a numerical score. A convincing invented person need not correspond to an existing individual.

Do not turn every brief into a candid phone snapshot. Studio, beauty, fashion, cinematic light, shallow depth of field and polished photography can be intentional. Preserve them while checking plausibility. Do not impose this profile on requested CGI, a doll, illustration or stylized anatomy.

## Review only what can actually be seen

| Region | Check | Do not assume |
| --- | --- | --- |
| Skin | Plausible tonal transitions and detail scale; avoid unrequested waxy smoothing, granular plaques, oversharpened pores and periodic microtexture | More pores, grain, wrinkles or blemishes always means more realism |
| Eyes and face | Gaze, eyelids, iris boundaries, reflections and expression work together under the depicted light | Catchlights must be identical or facial symmetry perfect |
| Mouth and teeth | Lip, tooth, gum and jaw relationships are coherent at the visible scale | Every person has ideal white teeth or a conventional smile |
| Hair and facial hair | Hairline, volume, direction and occlusion fit the head and scene | Every strand must be sharply resolved |
| Body and contact | Pose, perspective, grip, support and object contact are consistent | Disability, asymmetry or an unusual body feature is an error |
| Person in scene | Exposure, shadows, focus, scale, motion and color fit the surroundings | All lighting must be flat, neutral or uniform |
| Identity in edits | Source likeness, apparent age, skin tone, features, hair, expression and body are preserved unless intentionally changed | A photorealistic but different face is an acceptable replacement |

Not every feature is assessable in a small face or an occluded pose. State those limits; do not force visible pores into a full-body wide shot.

For edits, inspect the person against the actual source even if the requested change concerns only a jacket, product or background. Good texture does not compensate for changed identity. A waxy face can fail without any checker pattern.

## Prompt construction

Use the shortest relevant combination:

1. Photographic medium and the requested style.
2. Person, action, framing, gaze, and important object interaction.
3. Motivated lighting and natural detail at the actual shot scale.
4. Identity and other invariants when a source is attached.
5. A specific exclusion only for the observed or relevant failure.

Avoid generic "no AI slop" as the only correction. Translate the concern into observable requirements. Do not request CGI render-engine aesthetics in the same photographic brief without resolving that style conflict.

Do not add age, freckles, dirt, scars or other traits simply to "make it real." Do not erase intentional makeup or skin differences. Preserve the person's natural features.

## Recovery decision

- For a prompt-only request, return a complete prompt and do not generate.
- For localized unnatural skin, propose the least disruptive source-based edit with preservation checks; do not assume the generator can hold every other pixel fixed.
- For broad rendering failure, offer a new generation only with the identity/composition tradeoff made explicit.
- Do not sharpen, blur, denoise or increase grain automatically. Both oversmoothing and excessive texture can reduce plausibility.
- Stop on changed identity, serious regression, missing references or exhausted authorized attempts.

Keep three assessments separate: periodic texture, human photographic plausibility, and preservation. These criteria are a design contract. Their effectiveness in reducing generation failures has not been benchmarked.

Evidence: official photographic prompting guidance and firsthand face-quality reports are distinguished in the [evidence register](evidence-register.md).
