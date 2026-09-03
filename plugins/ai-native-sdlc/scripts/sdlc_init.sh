#!/usr/bin/env bash
# Copy the SDLC artifact scaffolding into the current repository.
# Never overwrites an existing file — the repo's own version always wins.
set -euo pipefail

assets="${CLAUDE_PLUGIN_ROOT:-$(dirname "$0")/..}/assets"
[ -d "$assets" ] || { echo "Cannot find plugin assets at $assets" >&2; exit 1; }

copy_if_absent() {
  local src=$1 dest=$2
  if [ -e "$dest" ]; then
    echo "skip   $dest (already exists)"
    return 0
  fi
  mkdir -p "$(dirname "$dest")"
  cp "$src" "$dest"
  echo "create $dest"
}

copy_if_absent "$assets/CLAUDE.md" "CLAUDE.md"
copy_if_absent "$assets/REVIEW.md" "REVIEW.md"
copy_if_absent "$assets/intent/README.md" "intent/README.md"
copy_if_absent "$assets/intent/TEMPLATE.md" "intent/TEMPLATE.md"
copy_if_absent "$assets/docs-sdlc/spec-template.md" "docs/sdlc/spec-template.md"
copy_if_absent "$assets/docs-sdlc/plan-template.md" "docs/sdlc/plan-template.md"

echo
echo "Scaffolding in place. Next: cut CLAUDE.md down to what is true here."
