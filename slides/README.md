# Tutorial slides

Quarto (reveal.js) slides for the DINGO tutorial (CCA, Flatiron Institute, 13 November 2026). The HTML is built by CI (`.github/workflows/slides.yml`) and uploaded as a workflow artifact.

## Editing

- Text and layout: `index.qmd`; styling: `theme.scss`. Preview with `quarto preview slides` from the repository root.
- Executed code cells are frozen in `_freeze/`, so CI renders with [Quarto](https://quarto.org) alone. Note that the cache stores the whole executed document: after **any** edit to `index.qmd` (text included), re-render locally with the tutorial environment and commit the updated `_freeze/`, or CI will fail. Run the notebook first so that its outputs exist:

  ```sh
  DINGO_TUTORIAL_RUN_DIR=/path/where/the/notebook/ran QUARTO_PYTHON=/path/to/venv/bin/python quarto render slides
  ```

  and commit the updated `_freeze/`.

## Config excerpts

The YAML/INI panels are generated from the examples of a tagged dingo release, not copied by hand:

```sh
python slides/make_snippets.py /path/to/dingo/clone v0.10.3
```

This writes `snippets/*.md`, which `index.qmd` includes. To update the slides for a new release, rerun with the new tag and re-render.
