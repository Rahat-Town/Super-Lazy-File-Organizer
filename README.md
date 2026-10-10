# Lazy File Organizer

A simple Python project that automatically organizes files into separate folders based on their file extensions.

Instead of keeping all your files in one folder, this program creates folders such as `pdf`, `jpg`, `png`, and `py`, then moves each file into its corresponding folder.

## Features

- Automatically detects file extensions.
- Creates folders for different file types.
- Moves files into their corresponding folders.
- Reuses existing folders when available.
- Simple and beginner-friendly Python code.


The project uses Python's built-in `os` and `shutil` modules.

## How to Run

### Step 1: Download the Project

Clone the repository using Git:

```bash
git clone https://github.com/Rahat-Town/Foolish-File-Explorer.git
```

Alternatively, download the project as a ZIP file from GitHub and extract it.

### Step 2: Open the Project

Open the project folder in VS Code, then open the terminal.

### Step 3: Run the Program

Execute the following command:

```bash
python3 LazyFileOrganizer.py
```

enter the full path of the folder you want to organize.

Example:

```text
Enter the Folder Path to Organize: C:\Users\YourName\Downloads\TestFolder
```

The program will create folders based on file extensions and move the files automatically.
