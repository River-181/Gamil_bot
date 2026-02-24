#!/usr/bin/env sh
set -eu
cat <<JSON
{
  "status": "ok",
  "audits": [
    "schema_contract_exists",
    "policy_contract_exists",
    "hooks_contract_exists",
    "skills_contract_exists"
  ],
  "risk_tags": []
}
