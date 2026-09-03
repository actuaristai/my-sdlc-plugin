#!/usr/bin/env bash
# Compare one eval result against its expected checks.
# Usage: check.sh <eval.json> <result.json>
set -euo pipefail

eval_file=$1
result_file=$2
name=$(jq -r '.name' "$eval_file")

if jq -e '.is_error == true' "$result_file" >/dev/null 2>&1; then
  echo "FAIL $name (session errored)"
  exit 1
fi

echo "PASS $name"
exit 0
