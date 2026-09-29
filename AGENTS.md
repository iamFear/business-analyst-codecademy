# Repository Guidelines

This repo is a **playground** and a **store for business analyst course projects**. It is not a single application. Expect small experiments, homework exercises, and one-off analyses in Python (scripts and notebooks). Do not refactor unrelated files into a shared package unless the user asks.

## Project Structure

- **Root `.py` files**: short, standalone exercises (insurance cost drills, string/list practice, NumPy experiments). Run them directly; they usually print sample output.
- **Subfolders**: one course project or analysis per folder (for example `fridakahlo/`). Keep related notebooks, solutions, and data together. Use a descriptive folder name, not a generic `project/` or `src/`.
- **Do not** introduce `src/`, `tests/`, or app scaffolding unless the current project actually needs it.

When adding work:

- Put a tiny experiment in a new root file with a descriptive `snake_case` name.
- Put a multi-file or notebook assignment in its own folder.
- Leave other exercises alone; do not “standardize” old medical or Frida files to match a new project.

## Commands

Use Python 3 from the repository root (or from a project folder for notebook-local files). There is no build step and no required virtualenv.

```sh
python3 <script>.py
```

Notebooks (`.ipynb`) live with their project. Prefer editing the existing notebook rather than converting it to a script unless the user wants a `.py` solution.

Third-party libraries (for example NumPy) appear only where that exercise uses them. Do not add dependencies to unrelated files. If a new analysis needs a package, import it in that file and keep the rest of the repo unchanged.

Scripts often run top-level examples on import. Do not import another exercise just to reuse a helper unless the user wants that.

## Coding Style

- `snake_case` for files, functions, and variables.
- Existing course files often use **two-space** indentation. Match the file you are editing. Use **four spaces** for brand-new modules unless the user is following a course template that specifies otherwise.
- Prefer readable operator spacing and f-strings for printed messages.
- Wrap multiline arithmetic in parentheses so the formula stays one expression.
- Preserve exercise-specific formulas, coefficients, rounding, and print wording unless the task is to change them.
- No formatter or linter is configured. Do not mass-reformat.

## Course Work vs Playground

- Follow the assignment’s steps and data. Do not replace a course solution with a more “production-ready” design unless asked.
- Keep commented-out course hints and step comments when they are part of the learning file.
- For playground files, keep the script short and focused on one idea.

## Testing

There is no test suite. After changing a script, run it and check printed results against the expected values (or the course’s sample output). For conditionals, check both branches. For random/simulation scripts, check that output is sensible, not bit-identical.

If you add tests, use `test_*.py` next to the work they cover, and note how to run them. Do not add a repo-wide test harness for unrelated exercises.

## Git

Commits are short and lowercase (for example `conditions project added`). One commit should cover one exercise or one behavior change. Do not mix unrelated playground edits with a course project.

## String Manipulation Project Tracker

This section tracks the educational Python string manipulation project steps and solutions.

### Step 1: Print medical_data
- **Request**: Take a look at the code in script.py. The string medical_data stores medical records for ten individuals. Each record is separated by a `;` and contains name, age, BMI, and insurance cost. Print medical_data to see the output in the terminal.
- **Solution**: Added `print(medical_data)` call at the end of `/Users/ibrejcha/Documents/Python/medical_strings.py` and executed the script. The medical_data string was printed successfully to the terminal, showing all ten records separated by `;`.

**Next step**: Continue with subsequent string manipulation steps.
