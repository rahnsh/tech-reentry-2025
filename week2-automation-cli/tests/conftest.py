# Make the parent folder (where app.py lives) importable in tests
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
