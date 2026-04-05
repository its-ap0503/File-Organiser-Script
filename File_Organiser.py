# this script moves all the files,
# separated according to the types like mp4, mp3, pdf, jpg ... etc

import os

imgFileType = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".tif", ".ico", ".heic", ".raw", ".psd", ".ai")
audioFileType = (".aac", ".mp3", ".wav", ".flac", ".ogg", ".wma", ".m4a", ".opus", ".aiff", ".mid", ".midi")
videoFileType = (".mp4", ".mov", ".mkv", ".avi", ".wmv", ".flv", ".webm", ".m4v", ".3gp", ".mpeg", ".mpg", ".ts", ".vob")
codingFileType = (".sh", ".cpp", ".py", ".ipynb", ".go", ".js", ".ts", ".html", ".css", ".java", ".c", ".cs", ".rb", ".php", ".swift", ".kt", ".rs", ".r", ".sql", ".json", ".xml", ".yaml", ".yml", ".toml")
documentFileType = (".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".tex", ".md", ".epub", ".pages", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".ods", ".odp")
archiveFileType = (".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".tar.gz", ".tar.bz2", ".iso")
executableFileType = (".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm", ".bin", ".bat", ".cmd", ".appimage")
fontFileType = (".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon")
databaseFileType = (".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".dbf", ".sql")
threeDFileType = (".obj", ".fbx", ".stl", ".blend", ".3ds", ".dae", ".gltf", ".glb")

file_map = {
    "images":      imgFileType,
    "audio":       audioFileType,
    "videos":      videoFileType,
    "coding":      codingFileType,
    "documents":   documentFileType,
    "archives":    archiveFileType,
    "executables": executableFileType,
    "fonts":       fontFileType,
    "databases":   databaseFileType,
    "3d_models":   threeDFileType,
}

path = input("Enter the Directory path: ")

if not os.path.exists(path):
    print(f"Error: Path '{path}' does not exist.")
    exit(1)

moved_count = 0
skipped_count = 0

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if not os.path.isfile(full_path):
        continue

    moved = False

    for folder, extensions in file_map.items():
        if file.lower().endswith(extensions):
            folder_path = os.path.join(path, folder)

            # create folder if not exists
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # move file
            os.rename(full_path, os.path.join(folder_path, file))
            print(f"  Moved: {file}  →  {folder}/")
            moved = True
            moved_count += 1
            break

    if not moved:
        skipped_count += 1
        print(f"  Skipped (unknown type): {file}")

print(f"\nDone! {moved_count} file(s) moved, {skipped_count} file(s) skipped.")