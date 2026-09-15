# Repository Guidelines

## Project Structure & Module Organization

This repository contains standalone Python exercises about estimating medical insurance costs. All source files live in the repository root:

- `medical_insurance.py`: variables, arithmetic, and changes to estimated costs.
- `functions_medical.py`: reusable cost calculations and example function calls.
- `conditions_medical.py`: conditional advice based on smoking status.
- `list_medical.py`: lists, paired data with `zip()`, and comparisons of actual and estimated costs.

There are no separate source, test, or asset directories. Keep new exercises focused and use descriptive filenames consistent with the existing medical theme.

## Build, Test, and Development Commands

Use Python 3 from the repository root. No build step or third-party packages are required.

```sh
python3 medical_insurance.py
python3 functions_medical.py
python3 conditions_medical.py
python3 list_medical.py
```

Each command executes that exercise and prints its sample results. Scripts also execute their top-level examples when imported; account for this when reusing functions.

## Coding Style & Naming Conventions

Use `snake_case` for filenames, functions, and variables, such as `estimate_insurance_cost` and `num_of_children`. Existing function bodies use two-space indentation; preserve surrounding indentation in small edits and use four spaces for new modules. Prefer readable operator spacing and f-strings for new output messages.

Wrap multiline arithmetic in parentheses to keep the entire formula in one expression. Preserve exercise-specific coefficients and rounding behavior unless the change explicitly targets them. No formatter or linter is configured.

## Testing Guidelines

No automated test framework or coverage threshold is configured. Run every changed script and compare printed costs with independently calculated expected values; successful execution alone does not verify arithmetic. For conditional changes, check both smoker and nonsmoker examples.

If adding automated tests, use descriptive `test_*.py` filenames and document the test command alongside the change.

## Commit & Pull Request Guidelines

Existing commits use short, lowercase descriptions, such as `conditions project added`; no formal commit convention is enforced. Keep commits focused and describe the affected exercise or behavior.

Pull requests should explain the change, identify affected scripts, and list validation commands and results. Include before-and-after output for calculation or message changes, and link related issues when applicable.
