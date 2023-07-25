import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from window import janela










app = QApplication(sys.argv)

# Create and show the window
window = janela()
window.show()

# Start the event loop
sys.exit(app.exec_())