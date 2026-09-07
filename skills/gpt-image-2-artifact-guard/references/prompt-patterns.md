# Prompt patterns

These are original, unbenchmarked examples of the workflow, not proven magic phrases. Preserve the user's scene and language preferences. Do not copy an example's scene, lens, mood, or anti-pattern clause into an unrelated brief.

## Construction

Write a complete prompt: subject and action; composition; style and light; surface-specific material or photographic requirements; exact visible text when applicable; protected details; concise local exclusions only if justified. Use as few sentences as the task allows. Do not repeat a long QA report in the prompt.

For an edit, identify the image by its role in the current call and describe the permitted region/change. Referencing an actually attached image is valid; referencing a missing image or conversation history is not. For an independent new image, omit attachment and history language entirely.

## Example A: portrait without erasing skin texture

User intent: candid portrait with freckles, wrinkles, natural skin, and fine film grain. No observed output yet.

> Create a photorealistic candid close-up photograph of an adult woman with freckles and fine smile lines, wearing a cream linen shirt beside a window. Use soft side daylight, a quietly blurred interior, natural skin tones, and subtle fine film grain. Keep pores and freckles varied at a believable scale, with the linen weave confined to the shirt and following its folds.

The positive material description is sufficient here. No invented defect, blanket smooth-skin instruction, or universal ban is needed.

## Example B: dense foliage remains the subject

User intent: dense humid jungle; a prior inspected output had a diamond grid on leaves.

> Create a wide photograph of a dense tropical jungle at dawn, with overlapping broad leaves, hanging vines, humid mist in the distance, and a narrow muddy path through the center. Preserve the richness and fine variety of the vegetation; leaf veins follow each leaf's form and nearer leaves remain distinct while distant foliage softens with atmospheric depth. Avoid a repeating diagonal light-dark micro-lattice in the foliage while retaining its natural veins and weathering.

Do not replace the jungle with a sparse garden. If complexity remains unresolved, discuss an optional compositional change rather than imposing it.

## Example C: local wall repair with an attached source

Precondition: the actual source image is attached to this edit call and has been inspected. The affected region is the plain wall behind a bottle, not the bottle's label.

> Edit the attached product photograph only to remove the unwanted diagonal grid on the plain wall behind the bottle. Render that wall as matte warm-gray painted plaster with its subtle irregular texture and existing light falloff. Preserve the bottle's exact silhouette, label lettering, reflections, position, tabletop, framing, and color balance; keep changes confined to the wall as closely as possible.

A natural-language boundary is not a pixel-exact guarantee. Inspect the label, silhouette, and other protected areas after the edit, even if a mask was available.

## Example D: an intentional grid is not an artifact

> Create a three-quarter studio photograph of a red-and-white gingham cotton shirt on a neutral mannequin. Preserve the regular woven check pattern as it curves with the fabric, visible fine cotton threads, seams, and soft folds. Use diffuse neutral light and a plain pale-gray background.

Do not append “no grids,” “no repeating patterns,” or “texture-free.” If moiré is reported, examine the original and display scale before altering the pattern design.

## Example E: visible text is protected

> Generate a vertical Polish exhibition poster with the exact headline “ŚWIATŁO I MATERIA” and the exact date “12–28 października”. Place the headline in large clear dark type above a photograph of a softly side-lit sandstone sculpture on a warm off-white background, with the date below. Preserve the sculpture's irregular fine stone grain and readable Polish diacritics; keep the type edges clean and the lettering separate from the photographed stone texture.

For a requested raster output, generate the text in the image. Do not substitute an HTML/SVG poster or add a later text layer without the user's request. Verify the actual spelling and accents afterward.

## Example F: photographic person without exaggerated pores

User intent: a believable waist-up workshop photograph, not a macro skin study.

> Create a photorealistic waist-up photograph of an adult man checking a bicycle handlebar in a daylight workshop. Show a believable grip and gaze directed at the bicycle. Keep skin detail subtle and varied at this framing, with coherent facial features and lighting shared by the person and room. Preserve a photographic appearance without beauty-filter smoothing.

Do not add age, blemishes, extreme sharpness or grain as a universal realism trick. Review only features the crop and resolution can show.

## Example G: clothing edit protects the person

Precondition: the original photograph is actually attached and has been inspected.

> Edit the attached photograph only to change the jacket to dark blue. Preserve the person's face, skin detail, age, expression, hair, body proportions, pose, lighting and background. Do not retouch the person.

Compare the face and exposed skin against the source afterward. This is a preservation instruction, not a pixel-lock or identity guarantee.

## Example H: studio photography stays studio photography

> Create a photorealistic full-body fashion photograph of an adult model in a tailored gray suit against a light-gray studio background. Use a large softbox from camera left with a restrained fill and coherent floor contact shadows. Keep the requested makeup, natural proportions and a relaxed standing pose. Skin detail should remain believable at full-body framing; the suit's weave follows its folds. Preserve the polished studio style without turning the person into a plastic-looking render.

Do not replace this with a candid phone snapshot. Polished lighting is not itself an artifact.

## Avoid these transformations

| Temptation | Better action |
| --- | --- |
| Append “no noise, no grain, no texture, no detail” to everything | Name only the observed unwanted pattern and protect intended detail |
| Delete smoke, glitter, grass, or fabric because they are complex | Preserve essential subject matter; explain optional tradeoffs |
| Treat “soft atmosphere, crisp subject” as contradictory | Apply each quality to its intended region |
| Set seed, CFG, denoise, or `negative_prompt` for a tool lacking them | Use ordinary material language and only exposed controls |
| Add “ignore the earlier image” to a standalone prompt | Select correct inputs at the host level; provide a complete scene description |
| Promise “artifact-free 4K” from prompt wording | Request the desired output and disclose control/verification limits |

The examples demonstrate instruction behavior. Their visual effectiveness remains to be tested on actual outputs.
