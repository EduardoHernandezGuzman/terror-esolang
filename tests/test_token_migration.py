import subprocess
import sys
from pathlib import Path


def run_source(tmp_path, source):
    repo_root = Path(__file__).resolve().parents[1]
    terror = repo_root / "terror.py"
    program = tmp_path / "programa.bolsi"
    program.write_text(source, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(terror), str(program)],
        check=True,
        capture_output=True,
        text=True,
    )


def test_frank_caudett_is_the_canonical_output_token(tmp_path):
    result = run_source(tmp_path, "SILVER KANE FRANK CAUDETT")
    assert result.stdout == "\x01"
    assert result.stderr == ""


def test_frank_caudwell_is_a_deprecated_output_alias(tmp_path):
    result = run_source(tmp_path, "SILVER KANE FRANK CAUDWELL")
    assert result.stdout == "\x01"
    assert "FRANK CAUDWELL está obsoleto" in result.stderr
