import argparse
import datetime
from pathlib import Path, PosixPath

parser = argparse.ArgumentParser()

parser.add_argument("path")

parser.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print(f"El directorio {sys.argv[1]} no existe")
    raise SystemExit(1)

def build_output(entry: PosixPath, long: bool = False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))