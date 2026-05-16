#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path
from datetime import datetime

def load_metadata():
    metadata_path = Path(__file__).parent.parent / "metadata.json"
    with open(metadata_path, 'r') as f:
        return json.load(f)

def generate_category_indexes(data):
    if not data['problems']:
        print("No problems yet")
        return
    by_category = defaultdict(lambda: defaultdict(list))
    for problem in data['problems']:
        for category in problem['categories']:
            by_category[category][problem['difficulty']].append(problem)
    categories_dir = Path(__file__).parent.parent / "categories"
    categories_dir.mkdir(exist_ok=True)
    for category, difficulties in sorted(by_category.items()):
        slug = category.lower().replace(' ', '-')
        filename = categories_dir / f"{slug}.md"
        with open(filename, 'w') as f:
            f.write(f"# {category} Problems\n\n")
            f.write(f"[← Back to LeetCode](../README.md)\n\n")
            total = sum(len(probs) for probs in difficulties.values())
            f.write(f"**Total: {total} problems**\n\n")
            for diff in ['Easy', 'Medium', 'Hard']:
                if diff in difficulties:
                    problems = sorted(difficulties[diff], key=lambda x: x['id'])
                    f.write(f"## {diff} ({len(problems)})\n\n")
                    for p in problems:
                        problem_slug = p['title'].lower().replace(' ', '-').replace("'", "")
                        problem_dir = f"problems/{p['id']:04d}-{problem_slug}"
                        problem_path = Path(__file__).parent.parent / problem_dir
                        has_solution = (problem_path / "solution.py").exists()
                        solution_link = f"[Solution]({problem_dir}/solution.py)" if has_solution else "*No solution yet*"
                        f.write(f"- **[{p['id']}. {p['title']}](../{problem_dir})** - {solution_link}\n")
                        if p.get('notes'):
                            f.write(f"  - {p['notes']}\n")
                    f.write("\n")
            f.write(f"---\n\n*Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n")
    with open(categories_dir / "README.md", 'w') as f:
        f.write("# All Categories\n\n")
        f.write("[← Back to LeetCode](../README.md)\n\n")
        for category in sorted(by_category.keys()):
            slug = category.lower().replace(' ', '-')
            total = sum(len(probs) for probs in by_category[category].values())
            easy = len(by_category[category].get('Easy', []))
            medium = len(by_category[category].get('Medium', []))
            hard = len(by_category[category].get('Hard', []))
            f.write(f"## [{category}]({slug}.md)\n")
            f.write(f"**{total} problems** - Easy: {easy}, Medium: {medium}, Hard: {hard}\n\n")
    print(f"Generated {len(by_category)} category files")

def update_readme(data):
    problems = sorted(data['problems'], key=lambda x: x['id'])
    stats = {
        'total': len(problems),
        'easy': len([p for p in problems if p['difficulty'] == 'Easy']),
        'medium': len([p for p in problems if p['difficulty'] == 'Medium']),
        'hard': len([p for p in problems if p['difficulty'] == 'Hard'])
    }
    categories = sorted(set(cat for p in problems for cat in p['categories']))
    lines = []
    lines.append("# LeetCode Solutions\n\n")
    lines.append(f"![Problems Solved](https://img.shields.io/badge/solved-{stats['total']}-blue)\n\n")
    lines.append("## Statistics\n\n")
    lines.append("| Difficulty | Count |\n")
    lines.append("|------------|-------|\n")
    lines.append(f"| Easy       | {stats['easy']}     |\n")
    lines.append(f"| Medium     | {stats['medium']}     |\n")
    lines.append(f"| Hard       | {stats['hard']}     |\n")
    lines.append(f"| **Total**  | **{stats['total']}** |\n\n")
    lines.append("## Browse by Category\n\n")
    if categories:
        for category in categories:
            slug = category.lower().replace(' ', '-')
            lines.append(f"- [{category}](categories/{slug}.md)\n")
        lines.append("\n[View All](categories/)\n\n")
    else:
        lines.append("Categories will appear after you add problems.\n\n")
    lines.append("## Quick Actions\n\n")
    lines.append("### Add New Problem\n\n")
    lines.append("```bash\n")
    lines.append("python scripts/new_problem.py <id> \"<title>\" [difficulty] [categories]\n")
    lines.append("```\n\n")
    lines.append("| Arg          | Required | Default  | Notes                                                 |\n")
    lines.append("| ------------ | -------- | -------- | ----------------------------------------------------- |\n")
    lines.append("| `id`         | yes      | —        | LeetCode problem number                               |\n")
    lines.append("| `title`      | yes      | —        | Quote it; used to build the slug                      |\n")
    lines.append("| `difficulty` | no       | `Medium` | `Easy`, `Medium`, or `Hard`                           |\n")
    lines.append("| `categories` | no       | `arrays` | Comma-separated, quoted (e.g. `\"arrays,hash-tables\"`) |\n\n")
    lines.append("Category names are normalized to kebab-case and pluralized when needed (`Hash Table` → `hash-tables`, `array` → `arrays`). Words in the special list (`dynamic-programming`, `searching`, `sorting`, `backtracking`, `greedy`, `math`) are left as-is.\n\n")
    lines.append("Examples:\n")
    lines.append("```bash\n")
    lines.append("python scripts/new_problem.py 1 \"Two Sum\" Easy \"arrays,hash-tables\"\n")
    lines.append("python scripts/new_problem.py 42 \"Trapping Rain Water\" Hard \"arrays,dynamic-programming\"\n")
    lines.append("python scripts/new_problem.py 100 \"Same Tree\" Easy \"trees\"\n")
    lines.append("```\n\n")
    lines.append("### Regenerate Indexes\n\n")
    lines.append("LeetCode-only views (this README + `categories/*.md`):\n")
    lines.append("```bash\n")
    lines.append("python scripts/generate_indexes.py\n")
    lines.append("```\n\n")
    lines.append("Cross-platform topic pages (`topics/*/problems.md`), run from repo root:\n")
    lines.append("```bash\n")
    lines.append("python scripts/generate_topic_problems.py\n")
    lines.append("```\n\n")
    lines.append("To change a problem's categories after creation, edit its entry in [metadata.json](metadata.json) and re-run both scripts.\n\n")
    lines.append("## All Problems\n\n")
    if problems:
        lines.append("| # | Title | Difficulty | Categories |\n")
        lines.append("|---|-------|------------|------------|\n")
        for p in problems:
            problem_slug = p['title'].lower().replace(' ', '-').replace("'", "")
            problem_dir = f"problems/{p['id']:04d}-{problem_slug}"
            categories_str = ", ".join(p['categories'])
            lines.append(f"| {p['id']} | [{p['title']}]({problem_dir}) | {p['difficulty']} | {categories_str} |\n")
    else:
        lines.append("No problems yet. Add your first problem!\n")
    lines.append("\n---\n\n")
    lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d')}*\n")
    readme_path = Path(__file__).parent.parent / "README.md"
    with open(readme_path, 'w') as f:
        f.write(''.join(lines))
    print("Updated LeetCode README.md")

def main():
    print("Generating indexes...")
    try:
        data = load_metadata()
        generate_category_indexes(data)
        update_readme(data)
        print("\nDone!")
    except Exception as e:
        print(f"\nError: {e}")
        raise

if __name__ == "__main__":
    main()
