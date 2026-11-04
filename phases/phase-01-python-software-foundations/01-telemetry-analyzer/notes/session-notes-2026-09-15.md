# Session Notes — 2026-09-15 (Week 1, Python Basics)

## What happened

Picked up right where Saturday's EOF session left off: the `while` loop using
`.readline()` and the `''` EOF check finally got written and tested. First run worked
functionally — the loop correctly stopped at end of file — but the console output had an
extra blank line between every printed line, which was annoying enough to chase down
properly instead of ignoring it.

## Starting point and approach

Instead of guessing at a fix, the debugging started with two targeted questions: does
`.readline()` include the trailing newline character in what it returns, and does
`print()` add its own newline on top of that? Both were checked rather than assumed —
the second one by re-running a quick REPL test from a completely different angle
(`print('Hello'); print('World!')` with no `\n` inside either string, and watching them
still land on separate lines). That confirmed `print()` adds its own newline unconditionally,
which meant `.readline()`'s trailing `\n` plus `print()`'s own newline were stacking into
two line breaks per loop iteration.

## The path from first draft to final version

1. **First fix attempt**: strip the newline off the line before printing it, using
   `str.strip()`.
2. **The catch, caught before writing code**: a look back at Saturday's EOF work — where
   the whole point was that `''` (true EOF) and `'\n'` (a real blank line) are
   distinguishable *only* if you check the raw, unstripped value. Stripping first and
   *then* checking for `''` would make a legitimate blank line look identical to EOF,
   silently truncating the file on the first blank line it hit.
3. **Fix applied**: reordered the logic so the EOF check runs on the raw `.readline()`
   output first; only after confirming it's *not* EOF does the code strip the newline
   and print. This is the same "check on the trustworthy raw signal, strip only for
   display" pattern — check-then-transform, not transform-then-check.
4. **Verified**: re-ran against `foo` (which contains an em-dash quote and a trailing
   line) — clean single-line-per-log-line output, `===== End of file reached =====`
   printed correctly at the true end.

## How the pieces connect

This is a direct continuation of Saturday's EOF investigation, not a new topic — the
blank-line bug and its fix are the EOF concept being *applied* under real pressure
(cosmetics finally gave a reason to care about the ordering) rather than being tested in
isolation in the REPL. The design spec's next step (keyword search per line) was also
scoped today: talked through using `str.find()`, its `-1`-vs-real-index return contract,
and the design decision to defer case-insensitive matching to a later week rather than
scope-creep the current script.

## Tools/methods used, and why

- **REPL experiments** to verify `print()`'s newline behavior and `str.find()`'s
  return contract (`.find()` returns `-1` on no-match, and a real match returns an
  index — including a valid `0` for "found at the very start," which matters for the
  `if` condition's design), continuing the "test, don't assume" habit from Saturday.
- **Order-of-operations reasoning** applied to code logic, not just arithmetic — checking
  EOF before transforming the string, specifically because the transform (`.strip()`)
  produces a value that could collide with the EOF sentinel.

## Tradeoffs

Chose to defer case-insensitive keyword matching (e.g. matching `"Error"` or `"ERROR"`
when searching for `"error"`) rather than solve it now. Explicitly named as a scoping
decision, not an oversight — the goal was avoiding "analysis paralysis," a pattern
recognized in hindsight as something that has stalled past sessions. Getting a working,
if limited, script beats a perfect script that never ships.

## Mistakes, dead ends, and how they were fixed

- Initial fix (`strip()` before the EOF check) would have silently broken the EOF
  detection for real blank lines in the middle of a file — caught *before* writing the
  code, by connecting it back to Saturday's EOF work rather than after debugging a
  mysterious early-truncation bug later. Fixed by reordering: check raw value for `''`
  first, strip only the confirmed-non-EOF value before printing.

## Pitfalls to watch for next time

- **A fix that removes a "duplicate-looking" character can quietly erase the exact
  signal a downstream check depends on.** Stripping `\n` looks purely cosmetic, but it
  destroys the one feature (`'\n'` vs `''`) that another piece of the code was relying on
  to distinguish two very different situations (blank line vs. end of file). Before
  transforming a value, ask what else in the code reads that same value in its raw form.
- **`if index:` vs `if index >= 0:` is a real trap with `.find()`.** Because `0` is
  falsy in Python, a truthiness check would treat "keyword found at position 0" the same
  as "not found at all" — a match at the very start of a line would be silently missed.
  Always check the actual return contract of a method rather than assuming falsy-means-
  not-found.

## What an expert would notice that a beginner might miss

An expert immediately asks "does this value get read anywhere else, in its current
(unmodified) form, before I transform it?" before applying a cleanup transform like
`.strip()`. A beginner tends to reason about a transform in isolation ("this makes the
output look nicer") without tracing where else the *pre-transform* value is load-bearing.
The bug here wasn't in the strip itself — it was in not asking that question before
moving the strip earlier in the sequence than the EOF check.

## Lessons that generalize beyond this project

- When a value gets both **checked** (for a sentinel/special case) and **transformed**
  (for display or further processing), the check should almost always run on the raw
  value, with the transform applied afterward — not the other way around. This shows up
  far beyond file parsing: input validation before sanitization, raw vs. normalized data
  in general.
- Recognizing a personal failure pattern (analysis paralysis / over-scoping a "simple"
  script) in the moment, and explicitly deferring the tempting refinement with a written
  note rather than either solving it immediately or forgetting it existed, is itself a
  practiced skill worth calling out — not just a throwaway aside.
