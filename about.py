import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QPlainTextEdit
from PyQt6.QtCore import QT_VERSION_STR, PYQT_VERSION_STR, QDate

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About PyQt6")
        self.resize(400, 300)

        layout = QVBoxLayout()

        # Add a label with the title
        title_label = QLabel("PyQt6 Version Information")
        layout.addWidget(title_label)

        # Add version information
        version_label = QLabel(f"Qt Version: {QT_VERSION_STR}")
        pyqt_version_label = QLabel(f"PyQt Version: {PYQT_VERSION_STR}")
        layout.addWidget(version_label)
        layout.addWidget(pyqt_version_label)

        # Add additional details if needed
        details_text = """
        PyQt6 is a set of Python bindings for The Qt Company's Qt application framework and runs on all platforms supported by Qt including Windows, OS X, Linux, iOS, and Android.
        
        PyQt6 is available under the GPL and commercial licenses. The Sourceforge project is the repository for the GPL source and binary packages.
        """
        details_text_edit = QPlainTextEdit()
        details_text_edit.setPlainText(details_text)
        details_text_edit.setReadOnly(True)
        layout.addWidget(details_text_edit)

        # Add a close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the Fusion style
    app.setStyle("fusion")

    about_dialog = AboutDialog()
    about_dialog.exec()

    sys.exit(app.exec())
