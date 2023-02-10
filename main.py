import os
from pathlib import Path
import subprocess
import sys
from itertools import chain

dir = "/workspaces/tikz"
dir_pdf = "/workspaces/tikz-pdf"

# subprocess.run(["git", "config", "--global", "user.email", "qpfortier@gmail.com"])
# subprocess.run(["git", "config", "--global", "user.name", "Quentin Fortier"])

for p in chain(*map(lambda x: Path('.').rglob(f"*.{x}"), ["pdf", "png"])):
    p_pdf = dir_pdf / p
    p_pdf.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["cp", p, p_pdf])

def git(*args):
    return subprocess.run(["git", *args]) 
os.chdir(dir_pdf)
git("checkout", "--orphan", "new")
git("add", "-A")
git("commit", "-m", "Update")
git("branch", "-D", "main")
git("branch", "-m", "main")
git("push", "-f", f"https://fortierq:{sys.argv[1]}@github.com/fortierq/tikz-pdf.git", "--set-upstream", "main")
