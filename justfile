# AI-native SDLC recipes.
# Import into an existing justfile with:  import 'sdlc.just'

set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

plugin_dir := "plugins/ai-native-sdlc"

# Register this repository as a plugin marketplace locally
sdlc-install:
    claude plugin marketplace add .
    claude plugin install ai-native-sdlc

# Validate the plugin and marketplace manifests parse
sdlc-check:
    Get-Content -Raw .claude-plugin/marketplace.json | ConvertFrom-Json | Out-Null
    Get-Content -Raw {{plugin_dir}}/.claude-plugin/plugin.json | ConvertFrom-Json | Out-Null
    Get-Content -Raw {{plugin_dir}}/hooks/hooks.json | ConvertFrom-Json | Out-Null
    py -m py_compile {{plugin_dir}}/scripts/sdlc_measure.py
    @echo "Manifests and scripts are valid."

# Show where every change in a target repo currently sits in the loop
sdlc-status:
    @echo "Intents:"; $i = Get-ChildItem intent/*.md -ErrorAction SilentlyContinue | Where-Object Name -notmatch 'TEMPLATE'; if ($i) { $i.Name -replace '^', '  ' } else { "  none" }
    @echo "Specs:";   $s = Get-ChildItem docs/sdlc/*/spec.md -ErrorAction SilentlyContinue; if ($s) { $s.FullName } else { "  none" }
    @echo "Plans:";   $p = Get-ChildItem docs/sdlc/*/plan.md -ErrorAction SilentlyContinue; if ($p) { $p.FullName } else { "  none" }

# Report the playbook's leading and lagging indicators from git history
sdlc-measure since="90.days":
    py {{plugin_dir}}/scripts/sdlc_measure.py --since {{since}}

# Scaffold the artifact directory for a new change
sdlc-new slug:
    New-Item -ItemType Directory -Force -Path docs/sdlc/{{slug}} | Out-Null
    Copy-Item docs/sdlc/spec-template.md docs/sdlc/{{slug}}/spec.md
    Copy-Item docs/sdlc/plan-template.md docs/sdlc/{{slug}}/plan.md
    @echo "Scaffolded docs/sdlc/{{slug}}/"

# The verification gate the agent must pass before claiming done
verify:
    just test
    just lint
