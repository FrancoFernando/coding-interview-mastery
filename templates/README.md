# Templates

Canonical, runnable Python reference implementations for the interview
primitives in [interview-primitives.md](interview-primitives.md). Each file
teaches **one** primitive: read it, type it once, then drill it from a blank
canvas until it's automatic.

## Layout

```
templates/
  <topic>/<primitive>.py    e.g. graphs/bfs.py, graphs/topological_sort.py
```

One primitive per file, grouped by topic folder.

## House style

Every template file follows the same shape:

- **Top banner** — names the primitive, says *when to use it*, and lists the
  **trigger words** that should make you reach for it in a disguised problem.
- **"THE ONE RULE"** — an uppercase comment flagging the single classic bug for
  this primitive (e.g. BFS: *mark visited on enqueue, not dequeue*).
- **Numbered `===` sections** — ordered simplest variant → payoff variant, each
  with a short "why / when" comment. Later variants reuse the earlier skeleton.
- **Practice ladder** — a trailing comment block of LeetCode problems ordered
  *direct use → disguised → checkpoint*, so you know exactly what to drill.

## How to drill (from interview-primitives.md)

1. **Day 1:** read the canonical implementation, type it once.
2. **Day 2–3:** solve the *direct-use* problems from the ladder.
3. **Day 4–5:** solve the *disguised / sub-step* problems (recognize the trigger).
4. **End of week:** type it from a blank canvas, no reference. Stuck? Restart
   from the canonical version and try again.

Nail the ★ primitives first.

## Adding a new template

Use the `add-primitive` skill: `/add-primitive <topic-folder> "<primitive name>"`.
It scaffolds a new file in the house style, wires up a practice ladder, and
verifies the code runs before finishing.
