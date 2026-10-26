"""Create a local configuration without overwriting an existing one."""

import os
import secrets
from pathlib import Path

root = Path(__file__).resolve().parent.parent
target = root / ".env"
if target.exists():
    print(".env vorhanden; unveraendert beibehalten.")
else:
    content = (root / ".env.example").read_text(encoding="utf-8")
    content = content.replace(
        "POSTGRES_PASSWORD=replace-me", "POSTGRES_PASSWORD=" + secrets.token_hex(24)
    )
    with target.open("x", encoding="utf-8", newline="\n") as output:
        output.write(content)
    if os.name == "posix":
        # The setup container runs as root; leave the file owned by the workspace owner.
        owner = root.stat()
        os.chown(target, owner.st_uid, owner.st_gid)
    print(".env mit zufaelligen lokalen Zugangsdaten erstellt.")
