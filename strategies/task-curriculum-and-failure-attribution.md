# Task curriculum and failure attribution

## Strategy

Order tasks by the prerequisites needed to fail for the intended reason, then
classify the failure before increasing complexity.

## Audience and context

Use this for courses, labs, and workshops that teach evaluation, coding-agent
workflows, or multi-step technical tasks. It is especially useful when learners
can fail because the task is too difficult, the environment is incomplete, or
the evaluator measures the wrong thing.

## Teaching problem

When every failed task is treated as evidence that the learner or agent lacks
the target capability, the course teaches the wrong lesson. A difficult task can
produce a missing-prerequisite failure, a tool failure, or an evaluator failure
before the intended skill is ever tested.

## Facilitator move

Build a small ordered task set. For each task, declare:

- the prerequisite capability;
- the target capability;
- the checkpoint that shows the prerequisite was reached;
- the expected terminal evidence; and
- the failure mechanism the task is intended to expose.

After a failure, classify the cause as task or prerequisite, model, prompt or
scaffolding, tool or environment, orchestration or handoff, or evaluator and
rubric. If the evidence cannot distinguish the causes, keep the result
`not_evaluated` and reduce the task or add the missing observation before
advancing.

## Learner evidence

The learner produces a task map that names the prerequisite, target capability,
checkpoint, observed failure point, evidence available, and next task decision.
For repeated runs, the learner keeps task-level outcomes and distinguishes
reaching the protocol checkpoint from passing the substantive domain check.

## Feedback and adaptation

If a learner fails before the intended checkpoint, teach or reduce the
prerequisite before adding complexity. If the checkpoint is reached but the
target behavior fails, preserve the case for focused practice or regression
testing. If the evaluator cannot distinguish the causes, repair the evidence
contract before changing the learner path.

## Accessibility

Offer the curriculum as a table, diagram, narrated walkthrough, and runnable
smallest path. Let learners choose a lower-complexity task that tests the same
construct, and provide static synthetic fixtures when a live environment is not
available.

## Responsible-use boundary

Task difficulty is evidence about the declared exercise, not a general ranking
of a learner, model, or team. Keep learner records, raw production traces,
private prompts, credentials, and provider-restricted material out of public
teaching examples.

## Verification

Review the task map against a short rubric. Run one positive case and one
negative control, then verify that the negative control fails for the intended
reason and that a missing prerequisite is not misreported as target-skill
failure.

## What this does and does not prove

It proves that the learning path makes prerequisites, intended capability, and
failure attribution visible for the included tasks. It does not prove that the
task difficulty generalizes to another audience, model, environment, or
production workflow.
