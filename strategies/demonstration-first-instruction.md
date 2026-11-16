# Demonstration-first instruction

## Strategy

Show a complete, bounded workflow and its failure case before asking learners
to generalize or extend it.

## Audience and context

Use this for unfamiliar agent, evaluation, observability, or governance
concepts where the learner needs to see the relationship between components.

## Teaching problem

Starting with terminology or disconnected code encourages cargo-cult copying.
Learners may complete a command sequence without understanding what the result
can support.

## Facilitator move

Run a small positive path, then run a deliberately degraded path. Explain the
decision, evidence contract, stopping condition, and human handoff. Keep the
demo offline or synthetic when live access would add cost, privacy risk, or
irreproducibility.

When teaching competing architectures, show the smallest working mechanism
first, then compare it with one more complex variant on the same task. Use one
focused diagram or figure to show the boundary between components, and include
a small runnable or inspectable example so learners can connect the visual to
the behavior. For multi-agent workflows, make the independent read path and
the shared-write owner visible rather than presenting parallelism as an
automatic improvement.

## Learner evidence

The learner annotates the workflow, identifies the failure signal, and states
what the demonstration does and does not prove.

## Feedback and adaptation

If learners can describe the happy path but miss the degraded case, repeat the
failure demonstration and ask them to name the missing control before changing
the implementation.

## Accessibility

Provide a transcript, diagram, command output, and explanation of expected
states. Do not make timing or audio quality the only way to perceive the lesson.

## Responsible-use boundary

A demonstration is an example, not a production approval. Synthetic evidence
must remain visibly separate from live quality, safety, or business claims.

## Verification

Use an independent negative control (a known-bad case that should be caught) and
ask the learner to explain why it was blocked.

## What this does and does not prove

It proves that the learner can follow and interpret one declared workflow. It
does not prove generalization to unseen systems or production readiness.
