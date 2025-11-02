import os, shutil, argparse, pathlib

CATEGORIES = {
    "images": {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"},
    "docs": {".pdf", ".docx", ".doc", ".txt", ".md", ".pptx", ".xlsx", ".csv"},
    "videos": {".mp4", ".mov", ".avi", ".mkv"},
    "audio": {".mp3", ".wav", ".m4a", ".flac"},
}

def categorize(ext: str) -> str:
    ext = ext.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "other"

def sort_folder(path: str, dry_run: bool=False) -> int:
    path = pathlib.Path(path)
    moved = 0
    for item in path.iterdir():
        if item.is_file():
            target_cat = categorize(item.suffix)
            target_dir = path / target_cat
            target_dir.mkdir(exist_ok=True)
            dest = target_dir / item.name
            if dry_run:
                print(f"[DRY] {item.name} -> {target_cat}/")
            else:
                shutil.move(str(item), str(dest))
                print(f"MOVED {item.name} -> {target_cat}/")
            moved += 1
    return moved

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Sort files in a folder into subfolders by type.")
    ap.add_argument("folder", nargs="?", default=".", help="Folder to sort (default: current directory)")
    ap.add_argument("--dry-run", action="store_true", help="Show what would happen without moving files")
    args = ap.parse_args()
    total = sort_folder(args.folder, args.dry_run)
    print(f"Done. Processed {total} files.")
