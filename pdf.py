from itertools import chain
import os
import subprocess
from pathlib import Path

for p in Path('.').rglob("*.tex"):
    if not p.with_suffix(".pdf").exists():
        # print(p)
        os.chdir(p.absolute().parent)
        try:
            subprocess.run(["lualatex", "-interaction=nonstopmode", "-file-line-error", "-shell-escape", p.name], stdout=subprocess.DEVNULL ,timeout=3)
        except:
            print(p)

        os.chdir(Path(__file__).parent)

for p in chain(*map(lambda x: Path('.').rglob(f"*.{x}"), ["aux", "log", "out"])):
    p.unlink()
