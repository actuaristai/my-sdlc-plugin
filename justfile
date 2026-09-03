# AI-native SDLC recipes.
# Import into an existing justfile with:  import 'sdlc.just'

plugin_dir := "plugins/ai-native-sdlc"

# Make the hook and helper scripts executable after a fresh clone
sdlc-init:
    chmod +x {{plugin_dir}}/hooks/*.sh
    chmod +x {{plugin_dir}}/scripts/*.sh
    chmod +x evals/check.sh
    @echo "Scripts are executable."

# Register this repository as a plugin marketplace locally
sdlc-install:
    claude plugin marketplace add .
    claude plugin install ai-native-sdlc

# Validate the plugin and marketplace manifests parse
sdlc-check:
    jq empty .claude-plugin/marketplace.json
    jq empty {{plugin_dir}}/.claude-plugin/plugin.json
    jq empty {{plugin_dir}}/hooks/hooks.json
    bash -n {{plugin_dir}}/hooks/format-on-edit.sh
    bash -n {{plugin_dir}}/hooks/protect-tests.sh
    bash -n {{plugin_dir}}/hooks/production-gate.sh
    python -m py_compile {{plugin_dir}}/scripts/sdlc_measure.py
    @echo "Manifests and scripts are valid."

# Show where every change in a target repo currently sits in the loop
sdlc-status:
    @echo "Intents:"; ls -1 intent/*.md 2>/dev/null | grep -v TEMPLATE || echo "  none"
    @echo "Specs:";   ls -1 docs/sdlc/*/spec.md 2>/dev/null || echo "  none"
    @echo "Plans:";   ls -1 docs/sdlc/*/plan.md 2>/dev/null || echo "  none"

# Report the playbook's leading and lagging indicators from git history
sdlc-measure since="90.days":
    python {{plugin_dir}}/scripts/sdlc_measure.py --since {{since}}

# Scaffold the artifact directory for a new change
sdlc-new slug:
    mkdir -p docs/sdlc/{{slug}}
    cp docs/sdlc/spec-template.md docs/sdlc/{{slug}}/spec.md
    cp docs/sdlc/plan-template.md docs/sdlc/{{slug}}/plan.md
    @echo "Scaffolded docs/sdlc/{{slug}}/"

# The verification gate the agent must pass before claiming done
verify:
    just test
    just lint
