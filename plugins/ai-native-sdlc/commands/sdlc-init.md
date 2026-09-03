---
description: Scaffold the SDLC artifact files into the current repository
---

Set up this repository for the AI-native SDLC loop.

1. Run `bash ${CLAUDE_PLUGIN_ROOT}/scripts/sdlc_init.sh` to copy the
   artifact scaffolding in: `CLAUDE.md`, `REVIEW.md`, `intent/` and
   `docs/sdlc/` templates. Existing files are never overwritten.
2. Read the generated `CLAUDE.md` and cut it down to what is actually
   true here. Run `/init` first if the repo has no conventions written
   down yet, then merge the two — keep it under a page.
3. Read `REVIEW.md` and set the exclusions and the nit cap to match how
   this team actually reviews.
4. Tell me what you changed and what still needs a human decision,
   specifically: who the product owner is, who owns each policy, and what
   the higher-risk classification is here.

Do not commit. Show me the diff.
