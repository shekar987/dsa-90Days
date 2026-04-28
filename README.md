# 90-Day DSA Learning Project

A focused workspace for practicing data structures and algorithms for 90 days with a hints-first mentor workflow.

## Project Structure

```text
.
|-- problems/
|   |-- day01.py
|   |-- day02.py
|   |-- ...
|   `-- day90.py
|-- journal/
|   `-- journal.md
|-- templates/
|   `-- template.py
|-- tests/
|   `-- test_day01.py
|-- INSTRUCTIONS.md
`-- README.md
```

## Daily Workflow: 30 Minutes

1. Minutes 0-5: Read the problem and rewrite it in your own words.
2. Minutes 5-10: Identify constraints, examples, edge cases, and the likely pattern.
3. Minutes 10-20: Work through the approach and implement it in the day's file.
4. Minutes 20-25: Test manually, then add or update automated tests.
5. Minutes 25-30: Log the pattern, mistakes, complexity, and review plan in `journal/journal.md`.

## How To Use Each Day File

Open the matching file in `problems/`, such as `problems/day01.py`. Copy structure from `templates/template.py` when you want a fuller prompt, then implement only after you can explain the approach.

## How To Use Codex Properly

Use Codex as a mentor first and an answer key last.

Good prompts:

- "Give me one hint, not the solution."
- "What pattern does this problem look like?"
- "Review my approach before I code."
- "Find the bug in my solution using a failing test case."
- "Ask me questions that lead me to the recurrence."
- "Check my time and space complexity."

Avoid starting with:

- "Solve this for me."
- "Give me the full code immediately."

The best loop is: attempt, ask for a hint, revise, test, explain, then log.

## Running Tests

From the repository root, run:

```bash
pytest
```

The sample test proves the day file imports cleanly and gives you a place to add real assertions once Day 01 has a problem.
