from interface.models.model import MediaTableModel
from interface.views import MediaTableView
from transfer_objects import MediaItemDTO

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    media_items = [
        MediaItemDTO(
            title="a_qt.mov",
            source="/path/to/a_qt.mov",
            resolution="1920x1080",
            format="mov",
            size="100MB",
            rate="24 Mbit/s",
            fps="24",
        ),
        MediaItemDTO(
            title="another_qt.mov",
            source="/path/to/another_qt.mov",
            resolution="1000x1000",
            format="mov",
            size="50MB",
            rate="12 Mbit/s",
            fps="30",
        ),
    ]

    model = MediaTableModel(media_items)
    view = MediaTableView()
    view.setModel(model)
    view.show()

    view.media_item_selected.connect(lambda media_items: print(media_items))

    sys.exit(app.exec())
