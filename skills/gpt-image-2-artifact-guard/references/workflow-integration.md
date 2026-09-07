# Workflow integration

This skill is standalone and instruction-only. It requires no named agent, other installed skill, local absolute path, API key, script runtime, MCP server, or cloud storage. The host may provide image viewing and generation; without those, prompt review and recovery planning remain available, while visual inspection/generation must be reported unavailable.

## Composition with another image skill

Use the existing creative brief and reference roles as inputs. Return a small risk note, protected features, a revised prompt if warranted, and acceptance checks. Let the host's authorized image workflow own execution. Do not add a second generation call just because this guard is active.

If another prompt skill already contains an anti-artifact check, run one combined check. Do not concatenate duplicate exclusions, competing style directions, or retry budgets. The user's brief and permissions remain authoritative; preserve stricter relevant safety boundaries.

## Optional named-pipeline mapping

In a workspace that already uses these roles:

- Reference curator (for example Renata): supplies actual assets, roles, and continuity anchors.
- Image prompt author (for example Iga): applies the preflight correction in the complete prompt.
- Output reviewer (for example Olga): inspects returned images and records preservation failures.
- Orchestrator (for example Oskar): owns approval, budget, and routing decisions.

These names are examples of optional integration, not dependencies or permission to spawn agents. Do not create permanent agents or modify workspace registries during normal skill use.

## Output contract

- Mode and inspection status.
- Relevant assessment axes: periodic texture, photographic plausibility, and preservation. Omit irrelevant axes instead of inventing scores.
- User intent and protected features.
- Up to three relevant risks or observed defects, with evidence status.
- Complete generator-ready prompt if requested, or a bounded recovery recommendation.
- Actual reference roles, if attachments are required.
- Acceptance checks and any remaining authorized attempts.

Keep this contract short for simple cases. Do not force a research report on every invocation. Use a full review record only for repeated attempts or a complex handoff.

For onboarding, use the shorter onboarding reference instead. Loading these instructions in a conversation does not prove persistent installation. A local file copy, host discovery, explicit activation, automatic matching, and visual effectiveness are separate outcomes.

For iterative work, keep acceptance criteria, actual evidence, the failed region or requirement, one repair target, regression checks, and the stopping condition. The host or existing orchestrator owns approval and budget. Stop when the requested criteria pass in the inspected scope; otherwise return one bounded next action or the missing input, not an endless loop.
