# pennywise

A personal budgeting application.

## Development

### Work Environments

1. [Python 3.11.1](https://www.python.org/downloads/release/python-3111/).
1. [Sublime 4143](https://www.sublimetext.com/download)
	1. [Pretty JSON](https://packagecontrol.io/packages/Pretty%20JSON)
1. Git 2.39.0.windows.2
1. Github (repo)

### Setup

1. Clone the repo from https://github.com/mbloom88/pennywise.git.
1. Create a new virtual environment (venv) outside of the clone repo by entering `python -m venv my-venv`.
	1. `my-venv` is the desired name for the new venv.
1. Activate the new venv by entering `.\my-venv\Scripts\activate` (Windows OS only).
	1. The venv can be deactivated by entering `deactivate`.
1. Navigate to the cloned repo and enter `python setup.py install` to install supporting Python packages.

### Project Directory

```
.
├───sandbox: for development and testing purposes only
├───pennywise: scripts
├──────db: sqlite3 database directory
├──────json: JSON files 
├──────ui: UI files to create QT Designer GUIs
├───CHANGELOG.md: project changelog
├───README.md: this document
└───setup.py: setuptools installation script
```

#### GUI Creation
QT Designer is used to create UI (.ui) files for the project GUI. The EXE is located in the venv at `Lib/site-packages/qt5_applications/Qt/bin/designer.exe`.

New UI files are to be saved in the `pennywise/pennywise/ui/` directory.

All UI files must be converted to a PY (.py) file prior to use. To create a PY files from a UI file:

1. Navigate to the `pennywise/src/ui/` directory.
1. Enter `pyuic5 -x -o DesignerUi.py DesignerUi.ui`.
	1. DesignerUi.py is the desired PY file to create.
	1. DesignerUi.ui is the source UI file.
