# Persistent CRUD Task Manager

A command-line interface (CLI) application designed for persistent task management. This project focuses on file I/O operations and maintaining data integrity during state changes.

## 🚀 Technical Highlights
- **Data Integrity Logic:** Developed a `number_assortment` algorithm that automatically re-indexes tasks following a deletion to prevent gaps in the data structure.
- **State Persistence:** Implemented a dual-file storage system (`text.txt` and `line_counter.txt`) to maintain application state across reboots.
- **Input Validation:** Features a duplicate-detection system that parses existing data to prevent redundant entry before appending to the filesystem.
- **Modular Design:** Segregated core logic (`todo_class.py`) from the user interface driver to follow clean code practices.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Development Workflow:** Fedora Linux / Neovim.
- **Storage:** Flat-file database (.txt).

## 📝 Developer Logs
The project includes a manual developer log tracking hours and version iterations, reflecting a commitment to documentation and project management.
