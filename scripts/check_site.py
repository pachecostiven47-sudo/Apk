#!/usr/bin/env python3
"""Dependency-free sanity checks for the NekoNexa static site."""
from html.parser import HTMLParser
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.ids = set()
        self.links = []
        self.inputs = set()
        self.forms = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "input":
            self.inputs.add(attrs.get("id", ""))
        if tag == "form":
            self.forms.add(attrs.get("id", ""))

html_path = ROOT / "index.html"
manifest_path = ROOT / "manifest.webmanifest"
icon_path = ROOT / "icon.svg"
sw_path = ROOT / "sw.js"

for path in (html_path, manifest_path, icon_path, sw_path):
    if not path.is_file():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")

if html_path.is_file():
    source = html_path.read_text(encoding="utf-8")
    parser = SiteParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:
        errors.append(f"HTML parser error: {exc}")
    for required_id in ("searchForm", "animeSearch", "searchResults", "instalar", "android-remoto"):
        if required_id not in parser.ids:
            errors.append(f"Missing expected HTML id: {required_id}")
    if "Kawaii Animes" not in source:
        errors.append("Kawaii Animes entry is missing")
    if "class=\"search-submit\"" not in source:
        errors.append("Search submit button is missing")
    if "navigator.serviceWorker.register" not in source:
        errors.append("Service worker registration is missing")
    for href in parser.links:
        if href.startswith("./") and not (ROOT / href[2:].split("#", 1)[0]).exists():
            errors.append(f"Broken local link: {href}")

if manifest_path.is_file():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("short_name") != "NekoNexa":
            errors.append("Manifest short_name must be NekoNexa")
        if not manifest.get("icons"):
            errors.append("Manifest has no app icon")
        for icon in manifest.get("icons", []):
            src = icon.get("src", "")
            if src.startswith("./") and not (ROOT / src[2:]).is_file():
                errors.append(f"Manifest icon not found: {src}")
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"Invalid manifest: {exc}")

if icon_path.is_file() and "<svg" not in icon_path.read_text(encoding="utf-8")[:300]:
    errors.append("icon.svg does not appear to be an SVG")

if errors:
    print("NekoNexa checks FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("NekoNexa checks passed: required files, app manifest, icon, local links and core UI are present.")
