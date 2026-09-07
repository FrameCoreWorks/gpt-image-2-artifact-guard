# Risk taxonomy

These are practical review categories, not diagnoses of the model's internals. A prompt can suggest where to inspect; it cannot prove that an image contains a defect. Classify the most relevant category instead of listing every possible failure.

| Category | Evidence to look for | Intended look or alternative explanation | Minimal next step |
| --- | --- | --- | --- |
| Periodic microtexture | Fine light/dark clusters repeat diagonally as tiny triangular, diamond, checker, or scale-like cells within detail; may be local or cross materials | Weave, droplets, grain, masonry, halftone, resampling | Use the morphology profile; inspect scale and material fit, not regularity alone |
| Macro tiling or duplication | Large image patches repeat, move, or break object contours at seams | Patchwork, collage, panel layout | Separate this from fine microtexture and identify the discontinuity |
| False microdetail | Brittle specks, worm-like noise, invented cracks, or sharpening halos that compete with coherent form | Grain, pores, freckles, patina, brush marks, fine particles | Specify detail scale and location; avoid global smoothing |
| Material leakage | Skin inherits wall texture, cloth looks like scales, glass becomes cellular | Deliberate hybrid material or fantasy design | Separate material boundaries and protect the requested hybrid if intentional |
| Unnatural photographic person | Unrequested waxy smoothing, exaggerated pores, incoherent facial detail, pose/contact or person/scene lighting | Makeup, naturally smooth skin, physical variation, intended CGI or stylization | Use the human profile; preserve identity, intended lighting and age; judge the actual visible evidence |
| Edit drift | New image changes protected face, shape, lettering, framing, or palette | Changes the user actually requested | Compare against the actual source; narrow the edit and lock invariants |
| Suspected context carryover | Unrequested object/style appears and corresponds to an earlier input the user identifies | Shared brief, intentional continuity, chance similarity | Audit the inputs actually supplied; consider a controlled context experiment |
| Display/encoding ambiguity | Pattern appears only in a screenshot, thumbnail, or at certain zoom levels | Preview checkerboard, resampling moiré, lossy encoding | Inspect an original file at native pixels when available; avoid diagnosing from preview alone |

## Protected detail

- Portrait: pores, wrinkles, freckles, facial hair, age, identity, and requested grain.
- Textile: weave direction, thread scale, seams, folds, logo, and requested pattern.
- Nature: leaf variation, bark, rock strata, fog structure, water, and weathering.
- Product: material finish, silhouette, proportions, joints, label, and reflections.
- Illustration: brushwork, paper, halftone, pixel grid, deliberate distortion, and style.
- Text-bearing graphics: exact copy, accents, line hierarchy, glyphs, and alignment.

Do not label an image defective because the design uses a repeated texture. Evaluate whether the repetition belongs to the depicted object, follows form/perspective, and matches the brief. A screenshot of an alpha-preview checkerboard does not establish that those squares were baked into the image.

## Severity, only after inspection

- `minor`: visible in an inspected region but does not materially harm the stated use.
- `material`: distracts at intended use size or compromises an important surface.
- `blocking`: makes a required face, product, text, or material unusable.
- `unknown`: inspection or intended use is insufficient.

No numeric probability or automatic frequency threshold is supplied. The same high-frequency pattern may be a defect in skin and an essential feature in fabric.
