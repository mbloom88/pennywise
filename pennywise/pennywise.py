# ==============================================================================
# Name:     pennywise.py
# Author:   Bloom, Matthew 
# Created:  12/31/2022
# Modified: 12/31/2022
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# Main Pennywise application script.
#
# ==============================================================================
# History
# ------------------------------------------------------------------------------
# Revision on https://github.com/mbloom88/pennywise.
#
# ==============================================================================

# ==============================================================================
# PACKAGES
# ==============================================================================

# Standard
import os
import sqlite3
import sys

# 3rd-Party
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow)

# Local
from ui.Pennywise import Ui_Pennywise

# ==============================================================================
# CLASSES
# ==============================================================================

class Pennywise(QMainWindow, Ui_Pennywise):
    """
    Main class for creating a Pennywise application object.
    """
    
    # ==========================================================================
    # CONSTRUCTORS
    # ==========================================================================

    def __init__(self, parent=None):
        super(Pennywise, self).__init__(parent)
        self.setupUi(self)
        self.show()

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == '__main__':

    # Enable high-dpi scaling and high-dpi icons
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) 
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)

    pennywise = Pennywise()

    sys.exit(app.exec_())
