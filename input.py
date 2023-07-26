from PyQt6.QtWidgets import QDialog, QLabel, QTimeEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QApplication
from PyQt6.QtCore import Qt, QTime


class TimeInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Countdown Time")
        self.resize(300, 100)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm")
        self.time_edit.setTime(QTime.currentTime())

        self.confirm_button = QPushButton("ตกลง")
        self.confirm_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow(QLabel("เวลานับถอยหลัง:"), self.time_edit)
        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.confirm_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_selected_time(self):
        return self.time_edit.time().toString("hh:mm")


if __name__ == "__main__":
    app = QApplication([])
    dialog = TimeInputDialog()
    app.setStyle("fusion")
    if dialog.exec() == QDialog.DialogCode.Accepted:
        selected_time = dialog.get_selected_time()
        print(f"Selected Time: {selected_time}")
    app.quit()
