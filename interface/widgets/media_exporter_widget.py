from PySide6.QtWidgets import QWidget, QHBoxLayout

from interface.views import MediaTableView


class MediaExporterWidget(QWidget):

    _main_layout: QHBoxLayout

    def __init__(self, parent=None):
        super(MediaExporterWidget, self).__init__(parent)
        self._main_layout = QHBoxLayout()

        self._media_table_view = MediaTableView()
