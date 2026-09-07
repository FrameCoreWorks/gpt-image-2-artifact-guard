# Evaluation protocol

Version 0.1 separates four kinds of evidence. Passing one does not imply passing the others.

## 1. Structural checks

Run the repository unit tests, the available skill/plugin validators, and the package comparison. Check local links, required resources, portable paths, identical skill contents in both ZIPs, checksums, deterministic outputs, no hidden runtime, and refusal to overwrite a differing archive. Record actual commands and results.

These checks do not measure prompt behavior, import acceptance, or image quality.

## 2. Instruction behavior

Use the requests in `cases.json`. Give the evaluator the skill and one raw request, not the rubric or an expected answer. Each case should start in an independent context when feasible. Read the actual returned prompt/review and compare it to the rubric afterward.

A case passes only if all its important criteria hold. Any unauthorized execution/upload, invented visual inspection, missing-reference claim, or removal of an essential feature is a blocking failure. Keep raw responses, judge notes, model/host identity if available, and limitations of the test method.

Do not equate keyword matching with behavioral success. The negative-trigger cases require a host-level discovery test without explicitly forcing skill use. A directly instructed dry run cannot validate automatic skill selection. Testing several separate requests inside one evaluator turn is a useful smoke test, not a fully isolated benchmark.

## 3. Live import and activation

On the user's target account, after authorization:

1. Import one package variant using the current UI, recording package hash and product/date.
2. Record scanner result, displayed name, resource access, and any warnings.
3. Invoke the skill explicitly on a prompt-only case. Confirm the references load and the response preserves detail.
4. Test relevant positive and negative triggers without explicit invocation.
5. If both distribution variants are tested, do not leave duplicate active installations in the same scope.

Do not record import as passed merely because the ZIP opens locally. No bypass of workspace restrictions or scanner failures.

## 4. Visual pilot, not yet run

Obtain explicit generation authorization and a total attempt budget. No provider API is required by this protocol; use only a surface the user authorized. Record model name/version only when actually exposed.

Suggested small pilot: six scene classes (skin/grain, woven fabric, foliage, smooth product wall, glass/particles, text on a textured poster), with two unchanged-prompt baselines and two guard-prompt outputs per class: 24 generations in total. This is a proposal, not a preauthorized spend. A smaller budget produces exploratory examples, not a reliable success-rate claim.

For each scene:

- Freeze a user-approved brief, essential detail, exact copy, references, surface, and output settings.
- Compare the original prompt to one documented minimal intervention. Randomize/interleave the execution order where practical, and log actual order.
- Hold available controls and reference inputs constant. Do not invent a seed or assume hidden state is identical. Test context isolation separately from material wording; do not bundle it into the prompt comparison.
- Retain original output files, exact prompts, and observations. Do not cherry-pick only favorable images.
- Inspect both native-pixel areas and intended use size. Randomize presentation labels for a human reviewer where feasible.
- Judge artifact severity and protected-detail fidelity independently. A smoother output that loses required pores, weave, text, identity, or scene content fails preservation.

Report counts and uncertainty, not a general cure rate. Separate cases that had no baseline defect from actual repair opportunities. Review disagreement should be recorded. The pilot is too small to establish universal behavior across subjects or future model updates.

Then, only if useful, run a separately authorized local-edit experiment and a context-carryover experiment. Compare both target region and untouched areas; generative edits can introduce regressions.

## Release gates

- Local candidate: source/package checks pass; critical instruction failures fixed; untested layers clearly marked.
- Install-tested candidate: actual target imports and explicit invocations pass.
- Evidence-backed mitigation release: visual evaluation retained and reported, including failure cases and detail-loss tradeoffs.
- Public repository: user chooses repo identity, visibility, license, and publication scope.
