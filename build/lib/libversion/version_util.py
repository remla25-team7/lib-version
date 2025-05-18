from pathlib import Path

def get_version():
    return (Path(__file__).parent / "version.txt").read_text().strip()
