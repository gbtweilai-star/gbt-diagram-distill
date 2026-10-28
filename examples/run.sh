#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_diagram_distill info
PYTHONPATH=src python -m gbt_diagram_distill check --payload '{}'
PYTHONPATH=src python -m gbt_diagram_distill run   --payload '{}'
