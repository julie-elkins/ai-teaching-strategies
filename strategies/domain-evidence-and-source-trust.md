# Domain evidence and source trust

## Strategy

Teach learners to distinguish a domain-specific evidence source from a
generic model capability and to keep original observations separate from
model-generated interpretations.

## Audience and context

Use this with learners designing AI applications, evaluations, or teaching
workflows that use domain data. It is most useful after learners can name the
decision a system should support but before they propose a data integration or
claim that the system is differentiated.

## Teaching problem

Learners may assume that adding data makes a system valuable or trustworthy.
They may also treat a generated label, summary, or prediction as if it were the
original evidence. That can produce a polished demo that cannot support the
decision it claims to inform.

## Facilitator move

Give learners a synthetic case with three records:

1. a public course description;
2. an original learner answer; and
3. an AI-generated “understood” label.

Ask them to identify the decision, name the source owner and permitted use,
record provenance (where the evidence came from) and freshness, distinguish
the observation from the interpretation, and define the response to missing,
stale, or conflicting evidence. Require `not_evaluated` or human review when a
required observation is unavailable.

## Learner evidence

The learner produces a one-page source contract containing the decision, source
owner, authority, provenance, freshness, retention and access boundary, original
observation, derived interpretation, missing-data behavior, and limitation.
The learner also explains why the AI-generated label is not automatically ground
truth (a trusted reference for correctness).

## Feedback and adaptation

If the learner lists data but cannot name the decision it changes, return to
decision-first scoping. If the learner treats the generated label as the source
of truth, ask them to identify the underlying observation and design a
calibration or human-review step. If the learner ignores missing data, add a
degraded case before introducing more data or model complexity.

## Accessibility

Offer the case as a short text, table, or screen-reader-friendly structured
record. Let learners submit a written contract, annotated diagram, or spoken
explanation. Keep the identifiers synthetic and provide a completed example
with the fields labeled.

## Responsible-use boundary

The exercise does not require private learner records, production traces, or
protected characteristics. Do not infer learner identity, ability, grades, or
future performance from sparse behavior. A model-generated status must not
replace an authorized human or domain decision.

## Verification

Use a rubric that checks whether the learner named the decision, source owner,
provenance, freshness, original observation, derived interpretation, and
missing-data behavior. Include a negative control where the generated label
conflicts with the original answer and verify that the learner routes the case
to review rather than silently accepting the label.

## What this does and does not prove

It proves that the learner can describe a bounded domain evidence contract and
identify a derived interpretation. It does not prove that the source is
correct, that the model label is valid, that the system is more useful than a
general model, or that the exercise predicts production or learner outcomes.
