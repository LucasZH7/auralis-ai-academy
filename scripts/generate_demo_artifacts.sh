#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$ROOT_DIR/scripts/generate_artifact.py" \
  --template "$ROOT_DIR/templates/certificate-template.md" \
  --data "$ROOT_DIR/examples/artifacts/demo-certificate-data.yaml" \
  --output "$ROOT_DIR/out/CERT-2026-000001.md"

python3 "$ROOT_DIR/scripts/generate_artifact.py" \
  --template "$ROOT_DIR/templates/certificate-template.svg" \
  --data "$ROOT_DIR/examples/artifacts/demo-certificate-data.yaml" \
  --output "$ROOT_DIR/out/CERT-2026-000001.svg"

python3 "$ROOT_DIR/scripts/generate_artifact.py" \
  --template "$ROOT_DIR/templates/student-card-template.svg" \
  --data "$ROOT_DIR/examples/artifacts/demo-student-card-data.yaml" \
  --output "$ROOT_DIR/out/STU-2026-000001.svg"

echo "Generated demo artifacts in $ROOT_DIR/out"
