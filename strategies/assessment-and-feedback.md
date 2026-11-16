# Assessment and feedback

## Strategy

Assess the decision the learner must make, then give feedback that points to the
next observable improvement.

## Audience and context

Use this for courses and workshops where learners must interpret evidence,
choose a control, or explain a release or escalation decision.

## Teaching problem

Completion, a passing average, or a polished final answer can hide an important
misconception. Feedback that only says “incorrect” does not show what to repair.

## Facilitator move

Use a small rubric with observable criteria, high-risk failure conditions, and
an explicit `not evaluated` state when evidence is missing. Keep automated
recommendation separate from human adjudication (a responsible person's
resolution of disagreement).

## Learner evidence

Collect the artifact, the decision rule used, the evidence cited, the
limitation, and the learner's next action. For repeated tasks, retain
task-level outcomes rather than only one aggregate score.

## Feedback and adaptation

Classify feedback as retain, clarify, revise, or retry. Use disagreement as a
signal to calibrate the rubric, not as permission to force a label.

## Attention-adjusted evidence value

Treat human attention as part of the evidence budget. Use this working
heuristic when deciding whether to ask for explicit feedback:

```text
attention-adjusted evidence value =
  P(usable feedback)
  × expected change in the decision
  ÷ attention cost
```

Here, `P(usable feedback)` is the likelihood that a person will provide an
answer that can be interpreted; expected change is the decision-relevant
information the answer may add; and attention cost includes time, effort,
context switching, and accessibility burden. This is a design heuristic, not a
universal score or a replacement for human judgment.

Implicit feedback—edits, retries, rejections, abandonment, or repeated
requests—can identify cases for review when explicit labeling is expensive. It
must remain a signal, not an automatic pass/fail label, because the same
behavior can have several explanations.

## Accessibility

Offer feedback in the same medium as the task when possible, with plain-language
explanations and enough time to revise. Keep the rubric readable without hidden
tool context.

## Responsible-use boundary

Learner evidence supports teaching decisions within the declared activity. It
does not justify predicting grades, employment outcomes, or personal traits.

## Verification

Run a calibration set (shared examples used to align reviewers) and inspect
disagreements before relying on labels at scale.

## What this does and does not prove

It proves that the assessment has a visible decision rule and feedback loop. It
does not prove that the rubric measures every aspect of competence or transfers
to a different audience.
