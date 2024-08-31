from typing import List

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from interface.widgets.card import MediaCard, MediaCardDTO


class CardContainer(QWidget):
    """Container for MediaCard widgets."""

    _cards: List[MediaCard]

    _main_layout: QVBoxLayout

    def __init__(self, parent=None):
        super().__init__(parent)
        self._main_layout = QVBoxLayout()
        self._cards = []

        self._add_card_button = QPushButton("Add Card")
        self._add_card_button.setEnabled(False)
        self._main_layout.addWidget(self._add_card_button)

        self.setLayout(self._main_layout)

    def add_card(self, dto: MediaCardDTO):
        card = MediaCard(dto)
        self._cards.append(card)
        self._main_layout.addWidget(card)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

    app = QApplication([])

    container = CardContainer()
    container.add_card(MediaCardDTO("Title", "Source", "Description"))
    container.add_card(MediaCardDTO("Title", "Source", "Description"))
    container.show()

    app.exec()
