import subprocess
import sys
import sysconfig
from pathlib import Path


def main():
    if sys.version_info < (3, 11):
        raise SystemExit(
            "Python 3.11 or newer is required for the patched Pillow dependency."
        )

    root = Path(__file__).resolve().parent
    wheel_source = root.parent / "omnisynth-dev" / "omnisynth"

    subprocess.run([sys.executable, "-m", "build"], cwd=wheel_source, check=True)
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        cwd=root,
        check=True,
    )
    garden = Path(sysconfig.get_path("scripts")) / "garden"
    subprocess.run([sys.executable, str(garden), "install", "graph"], cwd=root, check=True)
    subprocess.run([sys.executable, str(garden), "install", "matplotlib"], cwd=root, check=True)


if __name__ == "__main__":
    main()
