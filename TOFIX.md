# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `tera.snippets/main.md.tera:15-29` - every CLI example in the README is wrong: `pypathutil add $PATH /usr/games/bin` fails with "free args are not allowed ... missing parameters [folder,path]", and `--tail` fails with "unknown flags [tail]" (pytconf needs `--path ... --folder ...`, and tail mode is `--head=false`); rewrite the examples to the real syntax (and regenerate `README.md`).

## Medium

- `tera.snippets/main.md.tera:37-45` - install instructions use `pip3 install --user` and `sudo -H pip3 install`, which fail on current Debian/Ubuntu (PEP 668 externally-managed environment); recommend `pipx install pypathutil` or `uv tool install pypathutil`.
- `pyproject.toml:97` - the mypy override sets `ignore_missing_imports` for `pypathutil.*`, the package's own first-party module (comment says "Third-party libraries without type stubs"); remove that entry.
- `rsconstruct.toml:28` and `rsconstruct.toml:32` - `ruff` and `mypy` list `config` in `src_dirs`, but `config/` holds only `.lua` files; drop `config`.

## Low

- `src/pypathutil/common.py:10` and `src/pypathutil/common.py:32` - `# pylint: disable=too-many-positional-arguments` leftovers; pylint is not run by this repo (ruff/mypy only), so delete the suppressions.
- `doc/TODO.txt:1` - "add find_in_path utility" is already done (`src/pypathutil/common.py:110`, `find_in_standard_path` at `:129`); remove the item, or reword it to "expose find_in_path as a CLI endpoint" if that is what is meant.
- `src/pypathutil/common.py:121-122` - `strict` mode validates with `assert`, which is stripped under `python -O`, so `strict=True` silently stops checking; raise `ValueError` instead.
- `pyproject.toml:89` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist; reduce it to `src`.
- `tera.snippets/main.md.tera:59` - "for it's API" should be "for its API".
