import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent.parent
print(f"Root directory: {root_dir}")
sys.path.insert(0, str(root_dir))
