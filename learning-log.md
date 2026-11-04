# Learning Log

Quick daily entries for blog drafting. Longer teaching notes (with the full "why" behind
each session) live alongside each project, e.g.
`phases/phase-01-python-software-foundations/01-telemetry-analyzer/notes/session-notes-YYYY-MM-DD.md`.
(Entries dated before 2026-11-04 refer to the old `Week01_Python_Basics/` folder, now migrated there.)

> **Before writing a blog post from an entry below, go read that session's full
> teaching-notes file** (linked in each entry) — the log here is just a quick-scan
> summary; the real depth (alternatives considered, mistakes, expert-vs-beginner
> nuance) lives in the teaching notes.

---

## 2026-09-11 — Week 1: Safe file opening

**Time spent**: ~1 session (ran long — first night back after a stall)

**What I did**: Wrote `sample_file_open.py` — the first real slice of the Week 1 log
parser. It opens a file safely: no crash if the file's missing, and the file always
gets closed properly.

**What I learned**:
- `except:` with no error type named catches *everything*, which can hide real bugs
  behind a misleading error message. Name the specific exception you expect instead
  (`FileNotFoundError` for a missing file).
- `FileExistsError` and `FileNotFoundError` sound similar but mean opposite things —
  checked in the Python REPL rather than trusting autocomplete's first guess.
- `with open(...) as f:` (a context manager) closes the file automatically, even if
  an exception happens partway through — no need for a manual `.close()`.
- Checking "does this file exist?" and then opening it a moment later leaves a gap
  where the file could disappear in between. This is a real, named bug class:
  **TOCTOU** (time-of-check-to-time-of-use).

**Blog angle**: the gap between "looks handled" and "is actually handled" — bare
excepts and check-then-act patterns both look safe on the surface but hide real gaps.

**Full teaching notes**: `Week01_Python_Basics/session-notes-2026-09-11.md`

**Next**: keyword search over the file's lines.

---

## 2026-09-12 — Week 1: What EOF actually is

**Time spent**: ~short session (concept-only, no new code)

**What I did**: Before writing the keyword-search loop, worked out how a `while` loop
driven by `.readline()` should know to stop. Tested it live in the REPL rather than
guessing.

**What I learned**:
- `.readline()` returns `''` (true empty string, zero bytes) at real end-of-file — but a
  blank line in the middle of a file returns `'\n'` (one byte), not `''`. Confirmed by
  adding an actual blank line to the test file and re-reading it.
- EOF isn't a byte or marker stored in a file's contents — it's the OS/Python layer
  reporting "nothing left to read." That's why it can't collide with real data: there's
  no way to "write zero bytes" into the middle of a file.
- A worry can be reasonable in general (file-format EOF conventions vary at the raw-byte
  level) and still not apply at the abstraction layer you're actually coding at
  (Python's `.readline()` normalizes that away).

**Blog angle**: sentinel values and the "is this distinguishable from real data?"
question — same shape of question as null vs. empty vs. missing in other languages.

**Full teaching notes**: `Week01_Python_Basics/session-notes-2026-09-12.md`

**Next**: write the actual `while` loop using `.readline()` + the `''` EOF check, then
add keyword matching over each line.

---

## 2026-09-15 — Week 1: The blank-line bug (and why order matters)

**Time spent**: ~ran well over the 15-minute target, split across two topics

**What I did**: Finally wrote the `while`/`.readline()` loop planned since 9/12 — it
worked, but printed an extra blank line between every log line. Chased that down to a
real bug rather than papering over it with a quick strip. Then scoped (but didn't code
yet) the next slice: keyword search using `str.find()`.

**What I learned**:
- `print()` always adds its own newline, and `.readline()` keeps the line's trailing
  `\n` — combined, that's two newlines per iteration. Confirmed live in the REPL.
- Stripping the newline before checking for EOF would have broken EOF detection: a real
  blank line strips down to `''`, identical to true EOF. Fix was to check the raw
  `.readline()` value for `''` first, and only strip *after* confirming it's not EOF.
  Direct payoff from Saturday's EOF investigation.
- `str.find()` returns `-1` for no match and a real index (including `0`) for a match —
  so the found-check needs to be `>= 0`, not plain truthiness (`0` is falsy in Python).
- Made an explicit scoping call to defer case-insensitive keyword matching to later,
  naming "analysis paralysis" as a pattern to watch for in myself.

**Blog angle**: "check before you transform" — the same shape of bug (a cleanup step
accidentally destroying the raw signal another check depends on) shows up everywhere,
not just file parsing.

**Full teaching notes**: `Week01_Python_Basics/session-notes-2026-09-15.md`

**Next**: write the keyword-matching logic (line counter + per-keyword count using
`str.find()`) into the parser script.

---

## 2026-09-17 — Week 1: The `None` that came from a missing `return`

**Time spent**: ~short session, debugging-focused

**What I did**: Took the `str.find()`-based keyword-matching function prototyped in the
REPL and wired it into `sample_file_open.py`. First run crashed with
`TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'`. Traced it, fixed
it, verified the fix against `foo` — correct count (1 match on `'mag'`).

**What I learned**:
- A `return` statement placed only inside an `if` block means every other path through
  the function returns `None` implicitly — Python doesn't error on this, it just does it
  silently.
- In an accumulator pattern (`x = f(x)` inside a loop), an accidental `None` return
  doesn't crash on the iteration that causes it — it corrupts the accumulator quietly,
  and the crash shows up later, on a totally different (and totally correct) branch.
- The non-matching lines (3 of 4 in the test file) were the actual majority case, not an
  edge case — testing only the "keyword found" path left the more common path untested.

**Blog angle**: implicit `None` returns as a silent-failure pattern — the bug's symptom
(crash on match) was in a different place than its cause (three unhandled no-match
iterations before it), which is a good story about why traceback location isn't always
bug location.

**Full teaching notes**: `Week01_Python_Basics/session-notes-2026-09-17.md`

**Next**: keyword matching now works on `foo`. Next slice per todo: test against the real
Windows Event Log export, decide on the stray `foo`/`~$curriculum_plan.xlsx` files, and
fill in the Week 1 README's "What I Learned" section.

---
