import subprocess
import sys
from pathlib import Path

def test_hola_world():
    repo_root = Path(__file__).resolve().parents[1]
    terror = repo_root / "terror.py"
    hola = repo_root / "examples" / "hola.bolsi"
    out = subprocess.check_output([sys.executable, str(terror), str(hola)]).decode("latin-1", "ignore")
    assert out.strip() == "Hello World!"