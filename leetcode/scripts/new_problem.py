#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from datetime import datetime

TEMPLATE_README = """# {id}. {title}

**Difficulty:** {difficulty}  
**Link:** [LeetCode](https://leetcode.com/problems/{slug}/)

## Problem Description

[Paste problem description here]

## Approach

[Explain your approach]

## Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

## Notes

[Your notes]
"""

TEMPLATE_SOLUTION = """\"\"\"
LeetCode #{id}: {title}
Difficulty: {difficulty}
Link: https://leetcode.com/problems/{slug}/
\"\"\"

class Solution:
    def methodName(self):
        pass

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
"""

def get_slug(title):
    return title.lower().replace(' ', '-').replace("'", "").replace('"', '')

def normalize_category(category):
    """Convert category to kebab-case plural format (e.g., 'Hash Table' -> 'hash-tables')."""
    # Common singular to plural mappings
    plurals = {
        "array": "arrays",
        "tree": "trees",
        "graph": "graphs",
        "string": "strings",
        "linked-list": "linked-lists",
        "hash-table": "hash-tables",
        "stack": "stacks",
        "queue": "queues",
        "heap": "heaps",
        "trie": "tries",
        "matrix": "matrices",
        "bit": "bits",
        "interval": "intervals",
    }
    # Convert to kebab-case
    normalized = category.strip().lower().replace(' ', '-').replace('_', '-')
    # Apply plural mapping if exists, otherwise add 's' if not already plural
    if normalized in plurals:
        return plurals[normalized]
    # Handle already plural or special cases
    if normalized.endswith('s') or normalized in ['dynamic-programming', 'searching', 'sorting', 'backtracking', 'greedy', 'math']:
        return normalized
    return normalized + 's'

def parse_categories(categories_str):
    """Parse comma-separated categories and normalize them."""
    if not categories_str:
        return ["arrays"]
    categories = [normalize_category(c) for c in categories_str.split(',')]
    return categories

def create_problem(problem_id, title, difficulty="Medium", categories_str=None):
    slug = get_slug(title)
    dir_name = f"{problem_id:04d}-{slug}"
    base_dir = Path(__file__).parent.parent
    problem_dir = base_dir / "problems" / dir_name
    if problem_dir.exists():
        print(f"Problem already exists: {problem_dir}")
        return False
    problem_dir.mkdir(parents=True)
    readme_content = TEMPLATE_README.format(id=problem_id, title=title, difficulty=difficulty, slug=slug)
    (problem_dir / "README.md").write_text(readme_content)
    solution_content = TEMPLATE_SOLUTION.format(id=problem_id, title=title, difficulty=difficulty, slug=slug)
    (problem_dir / "solution.py").write_text(solution_content)

    categories = parse_categories(categories_str)

    metadata_path = base_dir / "metadata.json"
    with open(metadata_path, "r") as f:
        data = json.load(f)
    new_entry = {
        "id": problem_id,
        "title": title,
        "difficulty": difficulty,
        "categories": categories,
        "link": f"https://leetcode.com/problems/{slug}/",
        "notes": "",
        "date_solved": datetime.now().strftime("%Y-%m-%d")
    }
    data["problems"].append(new_entry)
    data["problems"].sort(key=lambda x: x["id"])
    with open(metadata_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Created: {problem_dir}")
    print(f"Categories: {', '.join(categories)}")
    print("\nNext steps:")
    print(f"  1. Write solution in: {problem_dir}/solution.py")
    print("  2. Run: python scripts/generate_indexes.py (updates leetcode/README.md + categories/)")
    print("  3. Run: python ../scripts/generate_topic_problems.py (updates cross-platform topics/)")
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: python new_problem.py <id> \"<title>\" [difficulty] [categories]")
        print("\nArguments:")
        print("  id          Problem number")
        print("  title       Problem title (in quotes)")
        print("  difficulty  Easy, Medium, or Hard (default: Medium)")
        print("  categories  Comma-separated list (default: arrays)")
        print("\nExamples:")
        print('  python new_problem.py 1 "Two Sum" Easy "arrays,hash-tables"')
        print('  python new_problem.py 42 "Trapping Rain Water" Hard "arrays,dynamic-programming"')
        print('  python new_problem.py 100 "Same Tree" Easy "trees"')
        sys.exit(1)
    problem_id = int(sys.argv[1])
    title = sys.argv[2]
    difficulty = sys.argv[3] if len(sys.argv) > 3 else "Medium"
    categories_str = sys.argv[4] if len(sys.argv) > 4 else None
    if difficulty not in ["Easy", "Medium", "Hard"]:
        print(f"Invalid difficulty: {difficulty}")
        print("Must be: Easy, Medium, or Hard")
        sys.exit(1)
    create_problem(problem_id, title, difficulty, categories_str)

if __name__ == "__main__":
    main()
