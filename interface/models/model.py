from dataclasses import fields
from typing import Optional, List

from PySide6.QtCore import Qt, QAbstractTableModel, Signal

from transfer_objects import MediaItems, MediaItemDTO


class MediaTableModel(QAbstractTableModel):
    """Model for the Media Items."""

    _media_items: MediaItems
    _headers: List[str] = [f.name for f in fields(MediaItemDTO)]

    def __init__(self, media_items: Optional[MediaItems] = None, parent=None) -> None:
        """Initialize the model with the media items.

        Args:
            media_items: The media items to display. Defaults to None.
            parent: The parent object. Defaults to None.

        """
        super(MediaTableModel, self).__init__(parent)
        self._media_items = media_items

    def get_media_item(self, index: int) -> MediaItemDTO:
        """Return the media item for the given index.

        Args:
            index: The index of the media item.

        Returns:
            MediaItemDTO: The media item.

        """
        return self._media_items[index]

    def rowCount(self, parent=...) -> int:
        """Return the number of rows in the model.

        Args:
            parent: The parent object.

        Returns:
            int: The number of rows.

        """
        return len(self._media_items)

    def columnCount(self, parent=...) -> int:
        """Return the number of columns in the model.

        Args:
            parent: The parent object.

        Returns:
            int: The number of columns.

        """
        return len(self._headers)

    def headerData(self, section, orientation, role=...):
        """Return the header data for the given section, orientation and role.

        Args:
            section: The section of the header.
            orientation: The orientation of the header.
            role: The role of the header.

        Returns:
            Any: The header data.

        """
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]

    def data(self, index, role=...):
        """Return the data for the given index and role.

        Args:
            index: The index of the data.
            role: The role of the data.

        Returns:
            Any: The data.

        """
        if role == Qt.DisplayRole:
            return getattr(
                self._media_items[index.row()], self._headers[index.column()]
            )
