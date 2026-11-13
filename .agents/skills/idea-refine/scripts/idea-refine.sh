#!/bin/sh
set -eu

# Resolve this helper from the installed skill directory; run in the target workspace.
exec python3 - "$@" <<'PY'
import json
import os
import sys

if len(sys.argv) > 2:
    print("usage: idea-refine.sh [directory]", file=sys.stderr)
    sys.exit(2)

ideas_dir = (sys.argv[1] if len(sys.argv) == 2 else "") or "docs/ideas"
try:
    os.makedirs(ideas_dir, exist_ok=True)
except OSError as error:
    print(f"cannot create idea directory: {error}", file=sys.stderr)
    sys.exit(1)

print(json.dumps({"status": "ready", "directory": ideas_dir}))
PY
