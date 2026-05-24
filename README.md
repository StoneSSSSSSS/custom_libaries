# custom_libaries

A toolkit for managing custom Python libraries that can be imported globally from anywhere on your machine. Instead of copying library folders into Python's `site-packages` directory by hand, you store all your custom libraries in this repository and use the provided scripts to install, update, rename, or delete them.

---

## How It Works

This repo acts as a central store for your custom Python packages. Each subfolder in this repo (like `Example_Lib`) is a Python package. The scripts copy those folders into your Python `site-packages` directory, making them available for import in any Python project.

The path to your `site-packages` directory is stored in `python_path.txt`.

---

## Setup

1. **Clone this repository** to your local machine.

2. **Set your Python path** — open `python_path.txt` and make sure the path points to your Python `site-packages` folder. For example:
   ```
   C:\Users\YourName\AppData\Local\Programs\Python\Python310\Lib\site-packages
   ```
   You can find your `site-packages` path by running:
   ```python
   import site
   print(site.getsitepackages())
   ```

3. **Add your custom libraries** — create a subfolder in this repo for each library you want. Each folder should be a valid Python package (i.e., it must contain an `__init__.py` file).

---

## Usage

### Install / Update All Libraries — `update.py`

Copies all library folders from this repo into `site-packages`. If a library already exists there, it will be replaced with the latest version from this repo.

```
python update.py
```

Run this whenever you add a new library or make changes to an existing one.

---

### Delete a Library — `delete_library.py`

Removes a library from your `site-packages` directory.

```
python delete_library.py
```

You will be prompted to enter the library name and confirm the deletion.

---

### Rename a Library — `rename_library.py`

Renames a library both in this repo folder and in `site-packages`, keeping them in sync.

```
python rename_library.py
```

You will be prompted for the original name and the new name.

---

## Example Library

The `Example_Lib` folder is included as a template to show the expected structure:

```
Example_Lib/
└── __init__.py
```

After running `update.py`, you can import it in any Python script:

```python
import Example_Lib
```

Replace `Example_Lib` with your own package folder to get started.

---

## Project Structure

```
custom_libaries/
├── Example_Lib/          # Example custom library (template)
│   └── __init__.py
├── delete_library.py     # Script to delete a library from site-packages
├── rename_library.py     # Script to rename a library
├── update.py             # Script to install/update all libraries
├── python_path.txt       # Path to your Python site-packages directory
└── .gitignore
```
