from typing import List

from PySide6.QtCore import Signal, QModelIndex
from PySide6.QtWidgets import QTableView

from transfer_objects import MediaItems


class MediaTableView(QTableView):
    media_item_selected: Signal = Signal(object)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setSelectionBehavior(QTableView.SelectRows)

    def selectionChanged(self, selected, deselected) -> None:
        """Handle the selection change event.

        Args:
            selected: The selected items.
            deselected: The deselected items.

        """
        super().selectionChanged(selected, deselected)
        indexes = self.selectionModel().selectedRows()

        if not indexes:
            return

        self._emit_selected_media_items(indexes=indexes)

    def _emit_selected_media_items(self, indexes: List[QModelIndex]) -> None:
        """Emit the selected media items.

        Args:
            indexes: The selected indexes.
        """
        items: MediaItems = []
        for index in indexes:
            media_item = self.model().get_media_item(index.row())
            items.append(media_item)
        self.media_item_selected.emit(items)
