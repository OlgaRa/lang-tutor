from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QIcon, QAction, QMenuBar, QPushButton, \
    QGridLayout, QLabel

from english_card import load_cards, Card, find_card_by_word

import sys
from english_card import load_cards, save_cards

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super(ControlPanel, self).__init__(parent)
        self.new_button = QPushButton("+", self)
        self.new_button.move(10, 5)

        self.del_button = QPushButton("del", self)
        self.del_button.move(110, 5)

        self.tutor_button = QPushButton("Lesson", self)
        self.tutor_button.move(210, 5)

        self.setMinimumSize(305, 50)


class CardEditWidget(QWidget):
    def __init__(self, parent=None):
        super(CardEditWidget, self).__init__(parent)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.grid.addWidget(QLabel('Word', self), 0, 0)
        self.grid.addWidget(QLabel('Translation', self), 1, 0)
        self.grid.addWidget(QLabel('Example', self), 2, 0)

        #self.grid.addWidget(QLabel('4:', self), 3, 0)
        self.word_edit = QLineEdit(self)
        self.grid.addWidget(self.word_edit, 0, 1)

        self.translation_edit = QLineEdit(self)
        self.grid.addWidget(self.translation_edit, 1, 1)

        self.example_edit = QLineEdit(self)
        self.grid.addWidget(self.example_edit, 2, 1)

        self.word_status_label = QLabel("", self)
        self.grid.addWidget(self.word_status_label, 3, 0)

        self.save_button = QPushButton("Save", self)
        self.grid.addWidget(self.save_button, 3, 1)

    def show_card(self, card):
        """
        Show card in widget
        :param card: The card to whos
        :type card: Card
        """
        self.word_edit.setText(card.word)
        self.translation_edit.setText(card.translation)
        self.example_edit.setText(card.example)
        self.word_status_label.setText(str(card.correct_answer_count))
        pass



class CardListWidged(QWidget):
    def __init__(self):
        super(CardListWidged, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.word_list = QListWidget(self)
        self.word_list.currentItemChanged.connect(self.on_item_changed)
        self.layout.addWidget(self.word_list)

        #making control panel
        self.control_panel = ControlPanel(self)
        self.layout.addWidget(self.control_panel)

        #create word edit widget
        self.card_edit_widget = CardEditWidget(self)
        self.layout.addWidget(self.card_edit_widget)
        self.cards = []
        self.cards = load_cards()
        self._update_word_list()


    def _update_word_list(self):
        self.word_list.clear()
        words = []
        for card in self.cards:
            words.append(card.word)
        self.word_list.addItems(words)

    def on_item_changed(self, curr, prev):
        word = curr.text()
        card = find_card_by_word(self.cards, word)
        self.card_edit_widget.show_card(card)


if __name__ == '__main__':
    # The app doesn't receive sys.argv, because we're using
    # sys.argv[1] to receive the image directory
    app = QApplication([])
    eat_card = None




    ex = CardListWidged()
    # card = find_card_by_word(ex.cards, "eat")
    # ex.word_edit.show_card(card)
    ex.show()
    sys.exit(app.exec_())

