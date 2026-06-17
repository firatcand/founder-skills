"""Repo sanity tests for the founder-skills collection.

This is a markdown/skills repo, not a Python package, so these tests give the
CI "Python package" workflow something meaningful to run instead of failing on
"no tests collected":

  1. every shipped .py file byte-compiles (guards Python syntax rot),
  2. every skill ships a SKILL.md with valid frontmatter (name + description),
  3. each skill's frontmatter `name` matches its directory (the routing key).

Dependency-free on purpose: CI installs only flake8 + pytest, so we parse the
YAML frontmatter by hand rather than importing PyYAML.
"""
import py_compile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _py_files():
    return [p for p in REPO.rglob("*.py") if ".git" not in p.parts]


def _skill_dirs():
    return sorted(p.parent for p in REPO.glob("*/SKILL.md"))


def _frontmatter(skill_md_text):
    """Return the text between the first two `---` fences, or None."""
    if not skill_md_text.startswith("---"):
        return None
    rest = skill_md_text[3:]
    end = rest.find("\n---")
    if end == -1:
        return None
    return rest[:end]


def _name_field(frontmatter):
    for line in frontmatter.splitlines():
        if line.strip().startswith("name:"):
            return line.split("name:", 1)[1].strip().strip('"\'')
    return None


def test_python_files_compile():
    files = _py_files()
    assert files, "expected at least one .py file in the repo"
    for f in files:
        py_compile.compile(str(f), doraise=True)


def test_every_skill_has_frontmatter():
    skills = _skill_dirs()
    assert skills, "expected at least one skill directory"
    for skill in skills:
        fm = _frontmatter((skill / "SKILL.md").read_text(encoding="utf-8"))
        assert fm is not None, f"{skill.name}: missing or unterminated frontmatter"
        assert "name:" in fm, f"{skill.name}: frontmatter missing name:"
        assert "description:" in fm, f"{skill.name}: frontmatter missing description:"


def test_skill_name_matches_directory():
    for skill in _skill_dirs():
        fm = _frontmatter((skill / "SKILL.md").read_text(encoding="utf-8"))
        assert fm is not None, f"{skill.name}: missing frontmatter"
        name = _name_field(fm)
        assert name == skill.name, (
            f"{skill.name}: frontmatter name '{name}' != directory '{skill.name}'"
        )
