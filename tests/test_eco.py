import subprocess
import sys
from pathlib import Path

def test_eco():
    repo_root = Path(__file__).resolve().parents[1]
    terror = repo_root / "terror.py"
    eco = repo_root / "examples" / "eco.bolsi"
    out = subprocess.check_output(
        [sys.executable, str(terror), str(eco), "--input", "hola"]
    ).decode("latin-1", "ignore")
    assert out.strip() == "hola"