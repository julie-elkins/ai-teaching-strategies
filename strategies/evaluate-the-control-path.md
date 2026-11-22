# Evaluate the control path

## Strategy

Teach learners to evaluate the control path around a model, not only the
model's final answer.

## Audience and context

Use this with learners who are building or reviewing agent workflows that
route between models, call tools, preserve state, request approval, retry work,
or hand results to another agent or person.

## Teaching problem

A fluent answer can hide an unsafe or unsupported workflow. Learners may treat
a fallback model, a successful retry, a local completion flag, or an approval
record as proof that the original failure was recovered safely.

## Facilitator move

Show one positive path and one interrupted synthetic path. In the interrupted
path, require learners to inspect:

- the selected model and reason for routing;
- the handoff evidence and uncertainty;
- approval binding to the current action and revision;
- stable operation identity and idempotency;
- authoritative state after an ambiguous result;
- capability, permission, privacy, cost, and quality differences on fallback;
- the final status: `recovered`, `unknown`, `unsafe_to_retry`, or
  `not_evaluated`.

An **orchestrator** is the workflow component that chooses models, delegates
work, applies policy, manages state, requests approval, retries actions, and
joins evidence. **Idempotency** means that repeating the same operation
identity does not create an additional unintended effect.

Connect the exercise to the
[Claude Evaluation Lab trajectory lesson](https://github.com/julie-elkins/claude-evaluation-lab/blob/main/course/lesson-scripts/lesson-25-agent-trajectories-and-recovery.md),
the [orchestrator trust-boundary pattern](https://github.com/julie-elkins/agent-systems-design-guide/blob/main/decisions/orchestrator-trust-boundary.md),
and the [Agent Assurance Harness workflow](https://github.com/julie-elkins/agent-assurance-harness/blob/main/docs/DEVELOPER_WORKFLOW_ASSURANCE.md).

## Learner evidence

The learner produces a bounded control-path annotation containing:

- the decision the workflow must support;
- the model route and fallback reason;
- the approval and revision evidence;
- the operation identity and authoritative postcondition;
- the missing or conflicting evidence;
- the terminal decision and why a retry is or is not safe.

## Feedback and adaptation

If the learner scores only the final answer, return them to the interrupted
path. If they call every model switch a failure, ask them to identify the
capability difference and the evidence needed to justify continuation. If they
cannot identify the authoritative state, narrow the exercise to one synthetic
side effect before adding more agents or tools.

## Accessibility

Provide the control path as a text table, a diagram, and a narrated walkthrough.
Let learners inspect metadata-only fixtures without requiring live provider
access or a real external action. Offer a static annotation path when running
the lab is not possible.

## Responsible-use boundary

Use synthetic or metadata-only examples. Do not connect the exercise to real
accounts, credentials, private data, destructive repositories, or live
side-effecting tools. A local approval record is not permission to test against
an external system.

## Verification

Use a rubric that checks whether the learner identified the decision, route,
approval binding, operation identity, authoritative state, missing evidence, and
terminal status. Include a negative control in which the fallback response is
fluent but the external state remains unknown.

## What this does and does not prove

It proves that the learner can inspect a bounded agent control path and explain
why a retry is or is not supported by the available evidence. It does not prove
live model equivalence, exactly-once execution, production safety, or that the
learner can operate a real external workflow.
