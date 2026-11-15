# Failure-driven labs

## Strategy

Make the most important failure observable, repeatable, and safe to inspect.

## Audience and context

Use this for hands-on learning about evaluations, agent workflows, tool use,
traces, retries, permissions, or release decisions.

## Teaching problem

A lab with only a passing path teaches learners to confuse execution with
correctness. They may not learn what evidence is missing or when a workflow
should stop.

## Facilitator move

Pair every positive fixture with a bounded negative control. Give the failure a
clear terminal state and preserve enough metadata to explain the result without
exporting prompts, raw traces, or sensitive content.

## Learner evidence

The learner records the declared decision, expected failure, observed status,
missing evidence, and next action. A successful retry must also show that the
failed attempt did not leave unintended repository or state changes.

## Feedback and adaptation

Use the learner's failure analysis to decide whether the next step is a concept
clarification, a smaller fixture, a changed rubric, or a new safety boundary.

## Accessibility

Make the lab runnable from a clean checkout with standard tools, bounded output,
and a written expected result. Offer a static walkthrough when execution is not
possible.

## Responsible-use boundary

Synthetic failures teach control behavior; they do not authorize testing against
live systems, private data, or destructive repositories.

## Verification

Run the positive and negative cases from a fresh environment and verify that the
negative case still fails when the control is deliberately weakened.

## What this does and does not prove

It proves that the declared control catches the included failure. It does not
prove that the control catches every failure or that a retry is safe outside the
tested state boundary.
