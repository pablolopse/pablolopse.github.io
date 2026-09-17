#!/usr/bin/env python3
"""Generates index.html from templates/index.html.j2 + data.py.

GitHub Pages only serves static files, so this script is the build step:
run it locally, commit the generated index.html, push. No Python runs
server-side.
"""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import data

ROOT = Path(__file__).parent

def main():
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True)
    template = env.get_template("index.html.j2")
    html = template.render(
        profile=data.PROFILE,
        projects=data.PROJECTS,
        education=data.EDUCATION,
        experience=data.EXPERIENCE,
        awards=data.AWARDS,
        skills=data.SKILLS,
        interests=data.INTERESTS,
    )
    out = ROOT / "index.html"
    out.write_text(html)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
