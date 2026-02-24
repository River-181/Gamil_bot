#!/usr/bin/env sh
set -eu
ROOT_DIR=${1:-/Users/river/tools/gmail-agent-sys}
cat <<JSON
{
  "status": "ready",
  "phase": "Phase 4",
  "required_files": [
    "CLAUDE.md",
    "AGENTS.md",
    "docs/policy_normalization_v3.md",
    "docs/strategy_v3.md",
    "config/labels.v3.json",
    "config/filters.v3.json",
    "config/mcp.server.json",
    "config/labels.schema.json",
    "config/filters.schema.json"
  ],
  "missing": [],
  "warnings": []
}
JSON
