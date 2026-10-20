# Repository Guidance

- This repository contains independent Python exercises and course projects, not one application. Keep changes within the requested exercise; do not introduce shared packages or repo-wide tooling.
- Preserve course datasets, formulas, rounding, print wording, step comments, and hints unless the task changes them. Match existing indentation; several exercises use two spaces.
- Edit notebooks in place rather than converting them to scripts.
- Scripts can execute examples on import; do not import unrelated exercises for helpers.
- No build or configured test/lint framework exists. Run the changed script with Python 3 and verify the requested behavior; successful execution alone does not check results.
- When the user approves a commit and push, include all pending repository changes, not just the current exercise. Check for secrets before staging; do not force-push.

## Hurricanes project

- Work in `hurricanes_project/hurricanes.py`. Read its project goals and numbered assignment comments before editing.
- Implement only the requirements the user supplies, then explain how the solution works in beginner-friendly terms. Do not complete later assignment steps preemptively.
- Add beginner-friendly code comments explaining each implementation's logic.
- After every implementation, finish by asking for the user's approval. Only after explicit approval, commit all pending repository changes and automatically push them to GitHub.
- Use built-in Python functionality only: no imports, including standard-library imports.
- The seven source lists describe the same hurricanes by matching index. Preserve their alignment and supplied values, including area spelling and capitalization.
- Damage strings use `M` and `B` suffixes or the sentinel `"Damages not recorded"`; account for the sentinel when converting or comparing damages.
- Preserve the supplied `conversion` and `damage_scale` values unless explicitly asked to change them.
- Run from the repository root with `python3 hurricanes_project/hurricanes.py`, or from the project folder with `python3 hurricanes.py`. The initial template only defines data and has no printed output; verify each implemented function with focused examples.
