from dataclasses import dataclass, asdict
from typing import Optional, Tuple, List, Dict

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from interface.fonts import RegularFont, TitleFont

PLAY_ICON = "../icons/play.png"


@dataclass
class MediaCardDTO:
    """Data Transfer Object for Card widget."""

    title: str
    source: str
    resolution: Optional[str] = None
    format: Optional[str] = None
    size: Optional[str] = None
    rate: Optional[str] = None
    thumbnail: Optional[str] = None


class MediaCard(QWidget):
    """Card widget for media files."""

    _title_label: QLabel
    _source_label: QLabel
    _thumbnail: QPixmap

    _obligatory_labels: Tuple[str] = ("title", "source")
    _ignore_labels: List[str] = ["thumbnail"]

    _data_labels: Dict[str, QLabel]

    _data_layout: QVBoxLayout
    _main_layout: QVBoxLayout

    def __init__(self, media_card_dto: MediaCardDTO, parent=None):
        super().__init__(parent)

        self._main_layout = QVBoxLayout()

        self._set_title_label(media_card_dto.title)

        self._set_data_layout(media_card_dto)

        self.setLayout(self._main_layout)

    def _set_data_layout(self, media_card_dto: MediaCardDTO) -> None:
        """Set data labels for the card with provided information.
        Only the fields that are set in the DTO will be created.
        Also sets the source path label, which is obligatory.
        This method is called in the constructor and should not be called again.

        Args:
            media_card_dto: Data Transfer Object for the card.
        """
        self._data_layout: QVBoxLayout = QVBoxLayout()

        self._source_label = QLabel(f"source: {media_card_dto.source}")
        self._data_layout.addWidget(self._source_label)

        self._data_labels = {}
        for key, value in asdict(media_card_dto).items():
            if key in self._obligatory_labels:
                continue
            if value is None:
                continue
            label = QLabel(f"{key}: {value}")
            label.setFont(RegularFont())
            self._data_labels[key] = label
            self._data_layout.addWidget(label)

        self._main_layout.addLayout(self._data_layout)

    def _set_title_label(self, title: str) -> None:
        """Set obligatory labels for the card.
        Adds the title label to the main layout.
        This method is called in the constructor and should not be called again.

        Args:
            title: title of the media file.
        """
        self._title_label = QLabel(title)
        self._title_label.setAlignment(Qt.AlignCenter)
        self._title_label.setFont(TitleFont())
        self._main_layout.addWidget(self._title_label)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    dto = MediaCardDTO(
        title="a_video_file.mov",
        source="/path/to/a_video_file.mov",
        resolution="1920x1080",
        format="mov",
        size="1.2GB",
        rate="60fps",
    )

    card = MediaCard(media_card_dto=dto)
    card.show()

    app.exec()
