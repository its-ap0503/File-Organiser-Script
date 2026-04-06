# File Organizer

A simple Python script that automatically sorts files in a directory into organized folders based on their file type.

---

## What it does

Tired of messy folders? Just run this script, point it to a directory, and it will automatically move your files into neatly organized subfolders like:

```
Downloads/
├── images/
├── videos/
├── audio/
├── documents/
├── coding/
├── archives/
├── executables/
├── fonts/
├── databases/
└── 3d_models/
```

---

## Prerequisites

- **Python 3.x** — that's it! No third-party libraries needed.

Check your Python version:
```bash
python --version
```

---

##How to Use

**1. Clone the repository**
```bash
git clone https://github.com/its-ap0503/File-Organiser-Script.git
cd File-Organizer-Script
```

**2. Run the script**
```bash
python File_Organizer.py
```

**3. Enter the path to the folder you want to organize**
```
Enter the Directory path: /home/aptuf/Downloads
```
The script will sort all files and show you what was moved.

---

##Supported File Types

| Category | Extensions |
|---|---|
|Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.tiff`, `.heic`, `.raw`, `.psd`, `.ai` |
|Audio | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.wma`, `.m4a`, `.aiff`, `.midi` |
|Videos | `.mp4`, `.mov`, `.mkv`, `.avi`, `.wmv`, `.flv`, `.webm`, `.3gp`, `.mpeg` |
|Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.epub`, `.xls`, `.xlsx`, `.ppt`, `.csv` |
|Coding | `.py`, `.js`, `.ts`, `.html`, `.css`, `.java`, `.cpp`, `.go`, `.sql`, `.json`, `.yaml` |
|Archives | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`, `.iso` |
|Executables | `.exe`, `.msi`, `.apk`, `.dmg`, `.deb`, `.bat` |
|Fonts | `.ttf`, `.otf`, `.woff`, `.woff2` |
|Databases | `.db`, `.sqlite`, `.sqlite3`, `.mdb`, `.sql` |
|3D Models | `.obj`, `.fbx`, `.stl`, `.blend`, `.gltf` |

---

##Notes

- The script only organizes files **directly inside** the given folder — it won't touch subfolders
- You need **read/write permission** on the folder you're organizing
- Files with **unknown extensions** are skipped and listed in the output
- Works on **Windows, macOS, and Linux**

---

##License

This project is licensed under the **MIT License** — feel free to use, modify, and share it.
