import sys
import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QDialog
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont, QIcon
from input import TimeInputDialog
from about import AboutDialog


class CountdownTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown TImer")
        self.setGeometry(100, 100, 400, 200)

        # Set application icon
        app_icon = QIcon("C:\\Users\\KinoBeddiez\\Documents\\qt\\icon.ico")
        QApplication.setWindowIcon(app_icon)

        layout = QVBoxLayout()
        self.timer_label = QLabel()
        font = QFont("Inter", 48, QFont.Weight.Bold)
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.timer_label)

        self.set_time_button = QPushButton("ตั้งเวลา")
        self.set_time_button.clicked.connect(self.show_time_input_dialog)
        layout.addWidget(self.set_time_button)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.show_about_dialog)
        layout.addWidget(self.about_button)

        self.setLayout(layout)

        self.end_time = datetime.datetime.now().replace(hour=19, minute=0, second=0)  # 7:00 PM
        self.update_timer()

        # Update timer every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def show_time_input_dialog(self):
        dialog = TimeInputDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            selected_time_str = dialog.get_selected_time()
            selected_time = datetime.datetime.strptime(selected_time_str, "%H:%M").time()
            current_date = datetime.datetime.now().date()
            self.end_time = datetime.datetime.combine(current_date, selected_time)
            self.update_timer()
    
    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def update_timer(self):
        current_time = datetime.datetime.now()
        if current_time >= self.end_time:
            self.timer_label.setText("Time's up!")
        else:
            time_left = self.end_time - current_time
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.timer_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the Fusion style
    app.setStyle("fusion")

    timer = CountdownTimer()
    timer.show()

    sys.exit(app.exec())
