---
name: add-primitive
description: Create a canonical Python template file for a coding-interview primitive (a technique from templates/interview-primitives.md) in this repo's house style. Use when the user wants to add a topic/primitive, create a template for a technique (BFS, topological sort, union-find, binary search, etc.), or types /add-primitive <topic-folder> "<primitive name>".
---

# Add a primitive template

Produce a `templates/<topic>/<primitive>.py` file teaching one interview
primitive: canonical, runnable Python reference implementations in this repo's
house style, plus a practice ladder. Match the two existing exemplars exactly —
`templates/graphs/bfs.py` and `templates/graphs/topological_sort.py`. Read at
least one of them before writing, and mirror its structure.

## Inputs

- **topic folder** — the subdirectory under `templates/` (e.g. `graphs`,
  `arrays-and-strings`, `dynamic-programming`). Create it if missing.
- **primitive name** — the technique, from `templates/interview-primitives.md`.

If either is unclear, ask which primitive and which topic folder before writing.

## File conventions (non-negotiable — this is the house style)

- **Path:** `templates/<topic>/<snake_case_name>.py` (e.g. `bfs.py`,
  `topological_sort.py`, `union_find.py`).
- **Language:** Python only, idiomatic for interviews — `collections.deque`,
  `heapq`, `@lru_cache`, direction arrays. No type annotations; keep it terse.
- **Top banner** for the whole file: a `=`-ruled comment naming the primitive,
  one line on **when to use it**, and the **trigger words** that should make a
  reader reach for it in a disguised problem.
- **"THE ONE RULE" hook:** call out the single classic bug for this primitive in
  an uppercase comment (e.g. BFS: "mark visited on ENQUEUE, not dequeue").
- **Numbered `===` sections**, ordered simplest variant → payoff variant. Each
  section: a `=`-ruled header, a short comment explaining the idea and when to
  reach for it, then a clean function. Later variants should visibly reuse the
  earlier skeleton and the comment should say so.
- **Cross-link** to sibling primitives when one is a special case of another
  (e.g. "Kahn's algorithm = multi-source BFS seeded on in-degree-0 nodes").
- **Practice ladder** as the final trailing comment block, `=`-ruled header
  `PRACTICE LADDER  (do them in this order)`. Group as: *direct use* →
  *disguised / sub-step* → the payoff/harder variant. Each line:
  `#   N. LC <num>  <Title> — <one-line why>`. End with a
  `# Checkpoint: if you nail A -> B -> C, you own this pattern.` line.

## Steps

1. Read `templates/graphs/bfs.py` (and `topological_sort.py` if the primitive is
   graph-ish) to lock in the exact formatting before writing anything.
2. Write `templates/<topic>/<name>.py` following the conventions above.
3. **Verify it runs.** Write a scratch test (in the scratchpad, not the repo)
   that imports the file via `importlib` and exercises every function on known
   inputs, including edge/failure cases (empty, cycle, unreachable). Run it with
   the repo's Python interpreter and confirm outputs are correct. Do NOT declare
   done until the test passes. If a `__pycache__/` appears in the topic folder
   from importing, delete it.
4. Report: the file path, a one-line list of the variants included, the single
   most important mental hook, and the checkpoint problems.

## LeetCode numbers caveat

You cannot query LeetCode live, so problem numbers/titles in the practice ladder
come from memory. Tell the user to sanity-check them, and never invent a problem
you are unsure exists — prefer well-known canonical problems for the primitive.

## Keep it focused

One primitive per file. One file per invocation unless the user asks for a
batch. Don't pad with variants that aren't interview-relevant.
