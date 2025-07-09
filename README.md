# 📁 File Organizer Script

A simple yet effective Python script that automatically organizes files in a given folder into subfolders based on file types — like Images, Documents, Music, and Videos. It also maintains a log of all operations performed.

---

## ✨ Features

- Automatically categorizes files into:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`
  - **Documents**: `.pdf`, `.docx`, `.doc`, `.txt`, `.xls`, `.ppt`, `.epub`
  - **Music**: `.mp3`, `.wav`, `.aac`, `.flac`
  - **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`
- Creates folders for each category if not already present.
- Skips unknown file types gracefully.
- Generates a `organizer_log.txt` file with a detailed log of what was moved and when.

---

## 📦 Requirements

This script only uses Python's built-in modules:

- `os`
- `shutil`
- `datetime`

No external libraries needed.

---

## 🚀 Usage

1. Run the script:
    ```bash
    python file_organizer.py
    ```
   

2. Enter the path to the folder you want to organize when prompted:
    ```
    Enter the path to the folder: /your/folder/path
    ```

    
---

## 📝 Example
```
Before:
/Downloads
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mkv
```

After running the script:
```
/Downloads
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Music/
│   └── song.mp3
├── Videos/
│   └── movie.mkv
├── organizer_log.txt
```
