# Session Notes — 2026-09-11 (Week 1, Python Basics)

## What happened

First real session picking the curriculum back up after it sat untouched since
2026-08-09. New pace going forward: 15 minutes/day, deliberately small, no fixed
schedule for ramping that up yet — the point right now is just showing up daily. This
session ran long (till about 1:30am), which is fine for a first night back, but the plan
is to keep future sessions tighter to the 15-minute box.

## Starting point and approach

The design spec for the Simple Log Parser (`designSpec_LogParser.md`) calls for reading
a log file, searching for a keyword, and handling edge cases gracefully — missing file,
empty file, invalid path, corrupted lines. Rather than jumping straight to the full
parser, tonight scoped down to the smallest useful slice: **open a file without crashing
the program if it doesn't exist.** Everything else (keyword search, output, counts) is
deliberately deferred to later sessions.

## The path from first draft to final version

1. **First draft**: a `try`/`except` around `open()`, but with a bare `except:` (no
   exception type named) and no `with` block — meaning the file handle, once opened,
   was never explicitly closed.
2. **First fix attempt**: named the exception, but picked `FileExistsError` — which is
   actually for the opposite situation (e.g. `os.mkdir()` on a directory that already
   exists), not for a missing file. Caught by checking the actual failure mode wanted
   ("this path does not exist") against what the exception name literally means, rather
   than trusting IDE autocomplete's first suggestion.
3. **Correct exception**: switched to `FileNotFoundError`, confirmed by testing directly
   in the Python REPL — `open('C:\\Users\\MWADA\\poop')` reliably raises
   `FileNotFoundError: [Errno 2] No such file or directory`.
4. **Resource cleanup**: introduced the `with open(...) as fooFile:` context manager to
   replace the plain `fooFile = open(...)` with no `.close()`. This guarantees the file
   gets closed even if an exception happens partway through reading it — the cleanup
   isn't dependent on execution reaching a `.close()` line at the end.
5. **Verified both paths**: ran the script against a real file (`foo`, printed its
   contents) and a nonexistent one (`poo`, printed the friendly error) — confirmed no
   traceback in either case.

## Why this order (plan -> draft -> structure)

Design spec first, then smallest possible slice of it, then iterate on that slice until
it's actually correct — rather than writing the whole parser and debugging exceptions
across the whole thing at once. Each fix targeted exactly one gap (wrong exception name,
then missing cleanup) instead of rewriting from scratch.

## Tools/concepts used, and why

- **`pathlib.Path`** instead of raw string concatenation for building the file path —
  cross-platform-safe and more idiomatic than string-gluing directory + filename.
- **`try`/`except`** for the recoverable failure (missing file) instead of letting an
  unhandled exception crash the script — matches the design spec's "fail safely, no
  crashes on bad input" requirement.
- **Named exception (`FileNotFoundError`)** instead of a bare `except:` — a bare except
  would also silently swallow unrelated bugs (e.g. a typo elsewhere in the try block,
  or a `PermissionError`) and misreport them as "file does not exist," sending future
  debugging down the wrong path.
- **`with` / context manager** instead of manual `open()` + `.close()` — removes the
  need to remember cleanup, and Python still closes the file even on an uncaught
  exception, not just on a clean exit.

## Tradeoffs

Kept the script deliberately narrow — one file path, one exception type, no keyword
search or output logic yet — to fit a short session and build the habit of shipping a
correct small piece rather than a half-working big one.

## Mistakes and how they were fixed

- Bare `except:` → named exception, once it was clear a bare except hides bugs instead
  of just handling the intended case.
- Wrong exception name (`FileExistsError`) → verified the actual exception via a live
  REPL test against a real nonexistent path, rather than guessing or trusting
  autocomplete blindly.
- No cleanup → `with` block, once the "what if you never close a file" question
  connected to a real security/reliability concept (resource exhaustion).

## Pitfalls to watch for next time (the "I wish someone told me this" list)

- **IDE autocomplete on exception names is not a decision — it's a suggestion.** Look up
  what an exception actually means before catching it; two exceptions can sound similar
  (`FileExistsError` vs `FileNotFoundError`) and mean opposite things.
- **A bare `except:` is a footgun.** It doesn't just "catch errors" — it catches
  *everything*, including bugs you didn't anticipate, and can produce a misleading error
  message that sends you debugging the wrong problem entirely.
- **Checking a condition and then acting on it are two separate moments in time.** Even
  if you verify a file exists, it can vanish (or get swapped) before you actually open
  it. This is a real, named class of bug — TOCTOU (time-of-check-to-time-of-use) — not
  just an academic curiosity; it shows up in real-world CVEs involving files,
  permissions, and symlinks.

## What an expert would notice that a beginner might miss

An expert wouldn't just ask "does this code handle the error?" — they'd ask "does this
error handling actually match the failure mode I expect, and does it fail *loudly and
specifically* rather than *quietly and generically*?" A script that always prints "file
not found" regardless of what actually went wrong looks correct in the happy path and
in the one failure case you tested, but silently misdiagnoses everything else.

## Lessons that generalize beyond this project

- Prefer language constructs that make correctness the default (context managers,
  guaranteed cleanup) over constructs that rely on the programmer remembering a step
  every single time.
- Name failure modes as specifically as the language allows. Vague catch-alls trade
  short-term convenience for long-term debugging pain.
- Verify behavior empirically (a REPL, a quick test run) rather than trusting a name or
  an autocomplete suggestion at face value — especially for anything security- or
  correctness-relevant.
