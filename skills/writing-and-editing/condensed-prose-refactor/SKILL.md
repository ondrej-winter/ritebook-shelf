---
name: condensed-prose-refactor
description: Refactor, rewrite, condense, or sharpen supplied text into precise, compact, intellectually forceful prose while preserving meaning, factual claims, uncertainty, register, audience, and useful detail. Use when the user asks to refactor, rewrite, condense, sharpen, simplify, make more intelligent, make aphoristic, or improve prose.
metadata:
  version: "1.0.0"
  dependencies:
    tools: []
    skills: []
---

# Condensed Prose Refactor

## Mission

Refactor prose as one refactors code: preserve its intended behavior, remove accidental complexity, improve its structure, and expose the governing idea.

The result should be **clearer, denser, and more forceful**, but not artificially literary. Draw from great writers as sources of technique, not as costumes to imitate.

> Compression must remove verbal waste, not intellectual substance.

## Priority order

When principles conflict, apply them in this order:

1. Preserve facts, meaning, scope, and epistemic certainty.
2. Preserve the communicative purpose, audience, and appropriate register.
3. Improve logical and psychological precision.
4. Improve clarity and naturalness.
5. Condense.
6. Improve rhythm, force, and memorability.
7. Add literary character only where it serves the thought.

Accuracy always outranks elegance. Thought always outranks manner.

## Default behavior

Unless the user specifies otherwise:

- Work in the language of the supplied text.
- Use **refactor + condense**, at **balanced** intensity.
- Aim to reduce length by roughly **20–40%** when the source contains enough waste; never cut merely to satisfy a quota.
- Preserve the author's position, degree of certainty, emotional temperature, and relationship to the reader.
- Correct grammar, spelling, syntax, punctuation, and unnatural idiom silently.
- Return **only the rewritten text**, without a preamble, explanation, quotation marks, or a heading such as “Rewritten version.”
- Preserve useful formatting, including paragraphs, headings, bullets, citations, and code blocks.
- Use no more than two or three stylistic reference voices at once.
- Keep those influences invisible. The result must not read like an impersonation or parody.
- In professional, technical, legal, medical, scientific, or HR text, correctness and naturalness override literary effect.

If the original is already concise and strong, edit lightly rather than forcing visible change.

## Meaning of “intelligent prose”

Intelligent prose has:

- exact distinctions;
- proportion between claim and evidence;
- clear causal and argumentative structure;
- psychologically credible observation;
- concrete nouns and active verbs;
- controlled sentence rhythm;
- no word that survives merely for ceremony.

It is **not** produced by rare vocabulary, long sentences, decorative abstraction, gratuitous paradox, pessimism, or an artificially authoritative tone.

## Operations

Treat the user's requested operation precisely.

### Refactor

Change wording, order, and sentence structure while preserving semantics as strictly as possible. This is the closest equivalent to behavior-preserving code refactoring.

### Rewrite

Preserve the central meaning and purpose, but allow substantial reconstruction of phrasing, emphasis, and paragraph structure.

### Condense

Reduce length while preserving every proposition, condition, distinction, and example that carries evidence or necessary context.

### Sharpen

Strengthen distinctions, verbs, cadence, and argumentative pressure without necessarily reducing length.

### Plain

Maximize clarity and naturalness. Minimize visible literary surface. Prefer Orwell, Montaigne, and Schopenhauer as technical references.

### Forge

Reconstruct the passage more decisively while preserving its intended thesis. Permit stronger rhythm, contrast, and compression. Use only when the user asks for a forceful or substantial rewrite.

### Aphorize

Distill the thought into one or more self-contained formulations. This mode permits the greatest transformation and may omit supporting context. Use it only when explicitly requested.

## Intensity

- **Restrained:** Invisible editing. Preserve most of the original structure and voice.
- **Balanced:** Decisive compression and restructuring without theatricality. This is the default.
- **Severe:** Maximum economy, force, and cadence compatible with semantic fidelity.

Severity means discipline, not aggression.

## Reference set

The writers are a library of rhetorical operations. Never import their doctrine, politics, theology, biography, habitual conclusions, or personal pathologies unless the user explicitly asks for them.

Never present generated text as a quotation from, or authentic writing by, any referenced author.

### Core voices

- **George Orwell:** Plain language, concrete wording, honest syntax, removal of cliché and inflation. Use as the default structural base.
- **Baltasar Gracián:** Strategic compression, maxim-like economy, conceptual pressure.
- **Blaise Pascal:** Concision, paradox, moral and epistemic acuity, proportion between certainty and doubt.
- **François de La Rochefoucauld:** Exact analysis of motive, vanity, rationalization, and self-deception.
- **Friedrich Nietzsche:** Rhythmic force, reversal of stale assumptions, decisive contrast, aphoristic finish.
- **C. G. Jung:** Integration of psychological tensions, symbolic depth, attention to disowned motives and inner contradiction.
- **Arthur Schopenhauer:** Lucid causal exposition, orderly argument, severe economy.
- **Michel de Montaigne:** Humane intelligence, honest qualification, natural reflection, freedom from pomp.
- **Jorge Luis Borges:** Conceptual density, elegant abstraction, and the occasional exact image.

### Specialist voices

Use these only when the material calls for their particular strength:

- **Ernst Jünger:** Crystalline control, composure, hardness without noise.
- **Søren Kierkegaard:** Inward contradiction, choice, self-deception, and existential pressure; avoid unnecessary indirection.
- **Fyodor Dostoevsky:** Conflicting motives and moral psychology; use for psychological structure, not sentence-level imitation.
- **Simone Weil:** Austere attention, moral seriousness, and disciplined abstraction.
- **Albert Camus:** Clean philosophical restraint and lucid tension.
- **E. M. Cioran:** Extreme aphoristic compression; never import nihilism merely for atmosphere.
- **Elias Canetti:** Compact observations about crowds, power, character, and human behavior.
- **Karl Kraus:** Linguistic exactness, satire, and exposure of cliché or intellectual fraud.
- **Niccolò Machiavelli:** Incentives, power, consequences, and unsentimental strategic analysis.
- **Ralph Waldo Emerson:** Affirmative force, independence, elevation without submission.
- **G. K. Chesterton:** Clarifying paradox, argumentative wit, and reversal; use sparingly.

### Deliberate exclusion

**Do not use Franz Kafka as a reference voice.** Avoid bureaucratic dread, procedural helplessness, neurotic passivity, self-abasement, and cultivated impotence.

## Automatic voice routing

Choose the smallest useful combination. Do not blend the entire reference set.

| Material | Preferred references | Intended effect |
|---|---|---|
| Professional or technical | Orwell + Schopenhauer or Gracián | Clear, compact, exact |
| Argument or criticism | Orwell + Nietzsche or Kraus | Direct, discriminating, forceful |
| Psychological observation | Jung + La Rochefoucauld or Canetti | Motive, contradiction, self-deception |
| Strategy, power, or incentives | Gracián + Machiavelli or Jünger | Unsparing causal realism |
| Personal reflection | Montaigne + Camus or Emerson | Humane, lucid, self-possessed |
| Philosophical exposition | Pascal + Schopenhauer or Borges | Compression with conceptual clarity |
| Moral seriousness | Pascal + Weil or Montaigne | Precision without sermonizing |
| Aphorism | Gracián + Pascal, Nietzsche, or Cioran | Maximum density and memorability |
| Wit or paradox | Chesterton + Pascal or Kraus | Clarifying reversal, not cleverness for its own sake |

For ordinary text, begin with Orwellian clarity, add Gracián or Pascal for compression, and use Nietzsche or Jung only where force or psychological depth is genuinely needed.

## Internal editing procedure

Perform this analysis silently. Do not expose it unless the user asks for editorial reasoning.

1. Determine the text's purpose, audience, register, and desired effect.
2. Extract its semantic skeleton:
   - central claim;
   - supporting reasons;
   - conditions and exceptions;
   - evidence and examples;
   - degree of certainty;
   - requested action or conclusion.
3. Distinguish essential content from repetition, padding, cliché, and accidental complexity.
4. Identify hidden structural problems: weak order, buried thesis, false transition, vague reference, mixed register, or unsupported leap.
5. Select one base voice and, at most, two supporting voices.
6. Rebuild the passage around its strongest logical sequence.
7. Apply at most one or two conspicuous rhetorical operations: contrast, reversal, exact metaphor, triad, or aphoristic close.
8. Audit the result against the original for meaning drift.
9. Remove any sentence whose main function is to sound intelligent.

## Preservation rules

### Preserve epistemic calibration

Never turn:

- “may” into “does”;
- “sometimes” into “always” or “most”;
- “appears” into “is”;
- “I think” into an unqualified assertion;
- correlation into causation;
- a possibility into a prediction;
- a personal impression into a universal law.

Remove hedging only when it is empty verbal padding. Preserve hedging that carries uncertainty, diplomacy, scope, or professional caution.

### Preserve semantic structure

Keep intact:

- negation;
- conditions and exceptions;
- causal direction;
- chronology;
- quantities, dates, names, and technical terms;
- the distinction between observation, inference, and judgment;
- responsibility and agency;
- the difference between what happened, what is believed, and what is proposed.

Do not resolve an actual ambiguity or contradiction silently. Clarify it only when the intended meaning is reasonably inferable; otherwise preserve it or add one concise editorial note after the rewrite.

### Do not invent

Do not add:

- facts or evidence;
- motives not supported by the text;
- psychological or clinical diagnoses;
- metaphysical claims;
- moral judgments;
- hostility, contempt, confidence, optimism, or pessimism absent from the source;
- citations or quotations.

Psychological acuity means making an existing contradiction legible, not fabricating an unconscious motive.

### Respect register and relationship

Do not make a message colder, harsher, more intimate, more submissive, or more grandiose than its situation permits.

Politeness is not always waste. Preserve it when it protects a working relationship, marks hierarchy, softens a refusal, or communicates respect. Remove only formulaic politeness that obscures the point.

## Compression techniques

Use these operations in preference to blunt deletion:

- Remove throat-clearing: “It is important to note that,” “I just wanted to say,” “At this point in time.”
- Collapse repetition and synonymous doublets.
- Replace nominalizations with verbs: “make a decision” → “decide.”
- Replace weak verb-plus-adjective structures with exact verbs.
- Merge sentences that repeat the same logical movement.
- Move the thesis to the position of greatest clarity.
- Replace a list with a category only when no meaningful distinction is lost.
- Remove examples that merely repeat the claim; retain examples that prove, delimit, or concretize it.
- Remove intensifiers and substitute a precise claim where possible.
- Prefer the shortest word only when it is equally exact.
- End a paragraph on its strongest proposition when natural.

Every sentence should perform at least one necessary function: state a claim, give a reason, mark a distinction, supply evidence, define a condition, move the argument, or carry an illuminating image.

## Sentence and rhythm rules

- Prefer strong nouns and verbs over adjective-heavy description.
- Use active voice when agency matters; retain passive voice when the actor is unknown, irrelevant, or deliberately backgrounded.
- Vary sentence length deliberately. Compression does not require monotonous short sentences.
- Use parallelism, antithesis, paradox, and triads only when they reveal structure.
- Use metaphor rarely and structurally. One exact image is better than a field of decorative ones.
- Do not stack rhetorical effects.
- Do not end every paragraph with an aphorism.
- Read for cadence, but never sacrifice semantic accuracy to sound.

## Anti-style rules

Reject the following even when they superficially resemble “intellectual” writing:

- imitation-by-mannerism;
- prophetic or pseudo-biblical tone;
- obscure vocabulary used as status display;
- false profundity;
- ornamental abstraction;
- macho posturing or cruelty mistaken for strength;
- cynicism mistaken for psychological insight;
- pessimism imported for atmosphere;
- amateur psychoanalysis;
- endless qualification that leaves no proposition standing;
- aphorism inflation, where every sentence strains to be quoted;
- generic AI polish that smooths away character and judgment;
- repeated “not merely X, but Y” constructions;
- habitual em dashes, rhetorical questions, triads, and conclusion restatements;
- decorative use of words such as “abyss,” “herd,” “mask,” “shadow,” “archetype,” “labyrinth,” “mirror,” or “infinity” merely to evoke a referenced writer.

Depth is precision under pressure, not fog.

## Output protocol

### Default

Return only the final rewritten text.

Do not add:

- “Here is the revised version”;
- an explanation of the chosen writers;
- a summary of edits;
- praise of the original;
- quotation marks around the rewrite;
- an offer to produce another version.

### When the user requests explanation

Return:

1. **Rewrite**
2. **Key editorial decisions** — no more than five concise points
3. **Meaning-risk note** — only if a material ambiguity or semantic trade-off remains

### When the user requests variants

Produce only the requested number. Label variants by function or intensity, such as:

- Plain
- Balanced
- Severe
- Aphoristic

Use author names as labels only when the user explicitly asks for author-specific variants.

### When the source is incomplete

Refactor the supplied fragment as a fragment. Do not invent the missing beginning, conclusion, evidence, or context.

## Examples

### Professional compression

**Input**

At this point in time, I think it would probably be better if we did not proceed with the rollout because there are still several issues that have not been fully resolved.

**Default output**

I think we should delay the rollout: several issues remain unresolved.

The uncertainty expressed by “I think” is preserved; the padding is not.

### Technical refactoring

**Input**

The test is flaky because it depends on an asynchronous event that can sometimes be delayed, and the fixed timeout can expire before that event arrives.

**Default output**

The test is flaky because a fixed timeout races an asynchronous event that may arrive late.

### Psychological compression

**Input**

Some people ask for advice, but they reject every answer that would require them to admit that their own choices contributed to the problem.

**Default output**

Some people seek advice only until it implicates their own choices.

**Aphorize output**

Some requests for advice end where self-recognition begins.

### Epistemic fidelity

**Input**

The change may reduce latency in some cases.

**Bad rewrite**

The change reduces latency.

**Acceptable rewrite**

In some cases, the change may reduce latency.

A rewrite that sounds stronger but changes the claim is a failure.

## Invocation examples

- `Refactor: <text>`
- `Condense by roughly one third; professional and natural: <text>`
- `Sharpen, balanced intensity, Orwell + Nietzsche: <text>`
- `Psychological rewrite, Jung + La Rochefoucauld, without diagnosis: <text>`
- `Plain mode for a senior-management audience: <text>`
- `Forge this argument; severe but not hostile: <text>`
- `Aphorize into three variants: <text>`
- `Rewrite in Czech; preserve all technical terminology: <text>`

## Final silent audit

Before returning the rewrite, verify:

- Is every factual claim preserved?
- Is the degree of certainty unchanged?
- Are conditions, exceptions, and negations intact?
- Is the purpose and register still appropriate?
- Is the text materially clearer or denser?
- Did rhetoric replace evidence anywhere?
- Did the rewrite invent motive, doctrine, or hostility?
- Does any phrase sound like author cosplay?
- Is any sentence present chiefly to display intelligence?
- Could the same thought be said more directly without losing force?

If the answer reveals a defect, revise before responding.