#!/usr/bin/env python3

import argparse
import pathlib
import re
import sys


PLACEHOLDER_RE = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")


def parse_simple_yaml(path: pathlib.Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
            value = value[1:-1]
        data[key] = value
    return data


def render_template(template_text: str, values: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        return values.get(key, match.group(0))

    return PLACEHOLDER_RE.sub(replace, template_text)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a Markdown or SVG academy template using a simple YAML data file."
    )
    parser.add_argument("--template", required=True, help="Path to the template file")
    parser.add_argument("--data", required=True, help="Path to the flat YAML data file")
    parser.add_argument("--output", required=True, help="Path to write the rendered artifact")
    args = parser.parse_args()

    template_path = pathlib.Path(args.template)
    data_path = pathlib.Path(args.data)
    output_path = pathlib.Path(args.output)

    values = parse_simple_yaml(data_path)
    rendered = render_template(template_path.read_text(encoding="utf-8"), values)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    print(f"Rendered {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
