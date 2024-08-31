from PySide6.QtGui import QFont


class TitleFont(QFont):
    """Font for titles in the application."""

    def __init__(self):
        super().__init__()

        self.setFamily("Helvetica")
        self.setPointSize(16)
        self.setBold(True)