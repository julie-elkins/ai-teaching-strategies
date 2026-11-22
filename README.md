# AI Teaching Strategies

Reusable teaching and adoption strategies for AI engineering, evaluation, and
agent-systems learning.

This repository is the teaching-design layer in Julie Elkins' public portfolio.
It explains how to turn a technical idea into a learner path with a clear
audience, a hands-on demonstration, observable evidence, and an honest
limitation. It does not replace the courses, labs, design guides, or research
artifacts linked below.

## Start here

Read the [strategy card template](STRATEGY_CARD_TEMPLATE.md), then choose a
card:

- [Audience calibration](strategies/audience-calibration.md)
- [Demonstration-first instruction](strategies/demonstration-first-instruction.md)
- [Failure-driven labs](strategies/failure-driven-labs.md)
- [Assessment and feedback](strategies/assessment-and-feedback.md)
- [Domain evidence and source trust](strategies/domain-evidence-and-source-trust.md)
- [Evaluate the control path](strategies/evaluate-the-control-path.md)
- [Instructor calibration](strategies/instructor-calibration.md)
- [Learner adoption evidence](strategies/learner-adoption-evidence.md)

The [course crosswalk](COURSE_CROSSWALK.md) maps these strategies to the
public learning repositories. The [YouTube crosswalk](YOUTUBE_CROSSWALK.md)
turns the same cards into video planning prompts without treating views as
evidence of learning.

## The design contract

Every strategy card answers:

1. Who is the learner or facilitator?
2. What decision or behavior should change?
3. What failure occurs when the strategy is missing?
4. What does the instructor or author do?
5. What observable learner evidence is collected?
6. What accessibility and responsible-use boundary applies?
7. What does the evidence prove, and what does it not prove?

The key distinction is between *delivery evidence* and *outcome evidence*.
Delivery evidence shows that a lesson, lab, rubric, or feedback step was
provided. Outcome evidence shows a bounded change in learner performance or
decision quality. A view count, completion click, or positive comment is not
by itself evidence that a learner can perform the target task.

## How this fits the portfolio

- [Agent Evaluation Learning Path](https://github.com/julie-elkins/agent-evaluation-learning-path)
  sequences the learner route.
- [Claude Evaluation Lab](https://github.com/julie-elkins/claude-evaluation-lab)
  supplies the learner-facing lessons and synthetic labs.
- [Agent Systems Design Guide](https://github.com/julie-elkins/agent-systems-design-guide)
  supplies reusable design decisions and evidence vocabulary.
- [Agent Assurance Harness](https://github.com/julie-elkins/agent-assurance-harness)
  supplies runnable, metadata-only assurance controls.
- [AI Design Guides](https://github.com/julie-elkins/ai-design-guides)
  provides the public directory.

The public examples are synthetic or metadata-only. Do not add private learner
records, unpublished exam material, raw production traces, credentials,
provider-private prompts, or internal project identifiers.

## Use in courses and videos

Use one card to plan one learner outcome, workshop segment, or video. Keep the
technical implementation in its owning repository and link to it rather than
copying it here. A strategy is ready to reuse when another facilitator can
identify the audience, run the demonstration, inspect the evidence, and state
the limitation without the original author present.

## Verification

Run the standard-library contract check:

```bash
python3 scripts/check_strategy_cards.py
```

The check verifies that every card contains the required headings and that
public-facing links use approved repository surfaces.

## License

The strategy text is licensed under the MIT License. Adaptations should retain
the attribution in the repository history.
