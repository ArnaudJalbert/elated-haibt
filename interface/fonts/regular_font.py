from PySide6.QtGui import QFont


class RegularFont(QFont):
    def __init__(self):
        super().__init__()
        self.setFamily("Helvetica")
        self.setPointSize(12)
        self.setBold(False)
