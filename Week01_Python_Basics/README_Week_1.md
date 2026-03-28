# Week 01 – Python Fundamentals & Secure File Processing
## Overview
### Week 1 focus
Build foundational Python skills while applying them to a small, security-relevant problem. The goal this week was not to build a “production-ready” tool, but to:
* Refresh Python fundamentals
* Practice reading and understanding unfamiliar code
* Apply basic secure coding habits early
* Begin documenting design and learning decisions clearly

### Learning Objectives
By the end of this week, I aimed to be comfortable with:

* Python syntax and control flow
* Reading from and writing to files safely
* Basic string processing
* Structuring a small CLI-style script
* Thinking about security implications even in simple tools

### Resources Used
**Primary Resources**
* Automate the Boring Stuff with Python
  * Chapters 1–3 (Python basics, flow control, functions)
**Supplementary**
* Personal notes and experimentation
* Python documentation (as needed)

## Project: Simple Log Parser

**Project Goal**
Build a small Python script that:
* Reads input from a log file
* Processes each line safely
* Produces a useful output (filtered results or stored data)

### Design Notes
**Input Handling**

* File paths are provided explicitly rather than hard-coded
* File access errors are handled gracefully

**Data Processing**

* Simple string operations (split, in, etc.)
* No assumptions that input data is well-formed

**Output**

* Human-readable console output
* Clear indication of what the script is doing

**Security Considerations (Even at This Stage)**

Although this is an introductory project, I made a point to think about:

* Failing safely (no crashes on bad input)
* Avoiding assumptions about file contents
* Clear boundaries between input, processing, and output

These habits scale directly into product security work.

### What I Learned
**Technical**

* ...
* ...

**Conceptual**

* ...
* ...


**Challenges & Open Questions**

* ...
* ...

These questions will guide improvements in later weeks.

### Next Steps (Week 2 Preview)

**Introduce:**

* Functions and modularization
* Better error handling
* Cryptographic primitives (hashing)


Begin turning this script into a more security-focused tool


### Feedback Welcome
I’m actively learning and would appreciate feedback on:

* Code structure
* Security assumptions
* Documentation clarity

Feel free to open an issue or reach out.