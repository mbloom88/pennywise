# pennywise

A personal budgeting application.

## Development

### Work Environments

1. Microsoft Windows 10 Home 10.0.19045 Build 19045
1. [Python 3.11.1](https://www.python.org/downloads/release/python-3111/).
1. [Sublime 4143](https://www.sublimetext.com/download)
	1. [Pretty JSON](https://packagecontrol.io/packages/Pretty%20JSON)
1. Git 2.39.0.windows.2
1. Github (repo)

### Setup

1. Clone the repo from https://github.com/mbloom88/pennywise.git.
1. Create a new virtual environment (venv) in the cloned repo by entering `python -m venv venv`.
1. Activate the new venv by entering `.\venv\Scripts\activate` (Windows OS only).
	1. The venv can be deactivated by entering `deactivate`.
	1. If a security error appears, enter `Set-ExecutionPolicy Unrestricted -Scope Process` and select Yes to allow for venv activation.
1. Enter `python setup.py install` to install supporting Python packages.

### Project Directory

```
.
├───sandbox: for development and testing purposes only
├───pennywise: scripts
├──────db: sqlite3 database directory
├──────ui: UI files to create QT Designer GUIs
├───CHANGELOG.md: project changelog
├───README.md: this document
└───setup.py: setuptools installation script
```

### Releases and Hotfixes

- The working development branch on Github is "develop".
- To prepare for a new release:
	- Create release branch: `git checkout -b release-X.Y.Z develop`
	- Push the new branch to Github: `"git push --set-upstream origin release-X.Y.Z`.
	- Checkout master branch: `git checkout master`
	- Merge the release to master: `git merge --no-ff release-X.Y.Z`
	- Tag master with the release version: `git tag -a vX.Y.Z -m "tag comments go here"`
	- Push everything to Github `git push --all`; `git push --tags`
- New hotfixes (e.g. hotfix-X.Y.Z) follow the same instructions as new releases, but generally branch from "master."

#### GUI Creation
QT Designer is used to create UI (.ui) files for the project GUI. The EXE is located in the venv at `Lib/site-packages/PyQt5Designer-5.14.1-py3.11-win-amd64.egg/QtDesigner/designer.exe`.

New UI files are to be saved in the `pennywise/pennywise/ui/` directory.

All UI files must be converted to a PY (.py) file prior to use. To create a PY files from a UI file:

1. Navigate to the `pennywise/src/ui/` directory.
1. Enter `pyuic5 -x -o DesignerUi.py DesignerUi.ui`.
	1. DesignerUi.py is the desired PY file to create.
	1. DesignerUi.ui is the source UI file.
