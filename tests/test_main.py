import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import main


def test_main_runs(capsys):
    assert main() is None
    captured = capsys.readouterr()
    assert "Hello, CSE103 Lab 3" in captured.out





