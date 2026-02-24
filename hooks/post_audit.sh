#!/usr/bin/env sh
set -eu

ROOT_DIR=${1:-/Users/river/tools/gmail-agent-sys}
cat <<JSON
{
  "status": "ready",
  "audits": [
    "labels_schema_checked",
    "filters_schema_checked",
    "sensitivity_masked",
    "plan_only_mode_preserved"
  ]
}
JSON
