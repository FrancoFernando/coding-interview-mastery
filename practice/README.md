# Practice

Blank-canvas drills for the primitives in [../templates/](../templates/). Each
file is one **variant** of one primitive: a spec, an empty stub, and a runnable
self-check. Fill in the stub without peeking, run the file, then drill again
from blank until it's automatic.

## Layout

This tree mirrors `templates/`, one level deeper — the practice unit is the
*variant*, not the whole primitive:

```
templates/graphs/bfs.py                 # one file, all variants — READ whole
practice/graphs/bfs/                     # folder named after the template stem
  multi_source.py                        # one file per variant — DRILL alone
  rotting_oranges.py
```

**Finding the answer key:** swap the top folder and drop the variant.
`practice/graphs/bfs/multi_source.py` → `templates/graphs/bfs.py`.

## House style

Every drill file is self-contained (~50–70 lines):

- **Top banner** — names the variant and the template it drills.
- **SPECIFICATION** — the signature, args, return contract, and the invariants
  the template cares about (e.g. BFS: *mark visited on enqueue*).
- **Stub** — the function to fill in, body `pass`.
- **`_run_tests()`** — a self-check under `if __name__ == "__main__":`, so
  `python practice/<topic>/<primitive>/<variant>.py` tells you if you're right.

Templates stay pure reference (no tests); the runnable tests live here.
