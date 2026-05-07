# Process Manager

A simple Python-based process manager for Windows that allows you to view, search, and terminate running processes.

---

## Features

- List all running processes
- Display process names with their PIDs
- Kill processes by PID or by name
- Group processes by application name

---

## Requirements

- Python 3.8+
- psutil

Install dependency:

```bash
pip install psutil
```

---

## Usage

```bash
python main.py
```

---

## Commands

- `show` → display all processes  
- `stop <pid>` → kill process by PID  
- `stop <name>` → kill all processes with that name  

Examples:

```bash
stop 1234
stop chrome.exe
show
```

---

## Notes

- Some system processes cannot be terminated due to permissions.
- Certain applications may restart background processes automatically.
- This tool is a simplified CLI alternative to Windows Task Manager.

---

## ⚠ Disclaimer

This tool is intended for educational purposes only.
