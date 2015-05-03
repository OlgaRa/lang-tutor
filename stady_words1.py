
from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QIcon, QAction, QMenuBar, QPushButton, \
    QGridLayout, QLabel, QFont

from english_card import load_cards, Card, find_card_by_word

import sys
from english_card import load_cards, save_cards
from PyQt4.QtCore import Qt

class CardShowControlPanel(QWidget):
    def __init__(self, parent=None):
        super(CardShowControlPanel, self).__init__(parent)
        self.show_translation_button = QPushButton("Show translation", self)
        self.show_translation_button.move(80, 5)
        self.show_translation_button.resize(150, 30)

        self.true_button = QPushButton("True", self)
        self.true_button.move(50, 5)
        self.true_button.hide()


        self.false_button = QPushButton("False", self)
        self.false_button.move(150, 5)
        self.false_button.hide()



        self.setMinimumSize(305, 50)


class TrueFalseCardShowWidget(QWidget):
    def __init__(self, parent=None):
        super(TrueFalseCardShowWidget, self).__init__(parent)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.word_label = QLabel('Word')
        self.word_label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.word_label, 0, 0)
        self.word_label.setFont(QFont('SansSerif', 13))

        self.example_label = QLabel('Example')
        self.example_label.setWordWrap(True);
        self.example_label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.example_label, 1, 0)
        self.example_label.setFont(QFont('SansSerif', 13))

        self.translation_label = QLabel('Translation')
        self.translation_label.setWordWrap(True);
        self.translation_label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.translation_label, 2, 0)
        self.translation_label.setFont(QFont('SansSerif', 13))
        self.translation_label.hide()

    def show_card(self, card):
        """
        Show card
        :param card: the card to show
        :type card:Card
        """
        self.word_label.setText(card.word)
        self.example_label.setText(card.example)
        self.translation_label.setText(card.translation)
        self.translation_label.hide()




class TrueFalseLessonWidget(QWidget):

    @property
    def _current_card(self):
        """
        :return: Current cart that we learn
        :rtype: Card
        """
        return self._cards[self._card_index]

    def __init__(self):
        super(TrueFalseLessonWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #create show word widget
        self.card_show_widget = TrueFalseCardShowWidget(self)
        self.layout.addWidget(self.card_show_widget)

        #making control panel
        self.control_panel = CardShowControlPanel(self)
        self.layout.addWidget(self.control_panel)
        self.control_panel.show_translation_button.clicked.connect(self.on_show_translation_button_clicked)
        self.control_panel.true_button.clicked.connect(self.on_true_button_clicked)

        self._cards = []
        self._card_index = 0

    def set_cards(self, cards):
        """
        Sets cards to learn
        :param cards: List of cards to learn
        :type cards: [Card]
        """
        self._cards = cards
        self._card_index = 0

    def _current_card_learned(self):
        if self._card_index == len(cards) - 1:
            self.card_show_widget.word_label.setText("Все выучено")
        else:
            self._card_index += 1
            self.card_show_widget.show_card(self._current_card)



    def on_show_translation_button_clicked(self):

        self.control_panel.true_button.show()
        self.control_panel.show_translation_button.hide()

        self.control_panel.false_button.show()

        self.card_show_widget.translation_label.show()

    def on_true_button_clicked(self):
        pass

    def on_false_button_clicked(self):
        pass








    def on_true_button_clicked(self):
        #self.card_show_widget.word_label.setText()
        self.control_panel.true_button.hide()
        self.control_panel.show_translation_button.show()


if __name__ == '__main__':
    # The app doesn't receive sys.argv, because we're using
    # sys.argv[1] to receive the image directory
    app = QApplication([])
    eat_card = Card()
    eat_card.word = "eat"
    eat_card.translation = "Жрать"
    eat_card.example = "Cats eat mouses"

    cards = [eat_card]


    ex = TrueFalseLessonWidget()
    ex._cards = cards
    ex.card_show_widget.show_card(eat_card)
    # card = find_card_by_word(ex.cards, "eat")
    # ex.word_edit.show_card(card)
    ex.show()
    sys.exit(app.exec_())


#
#
# from english_card import load_cards, Card
#
# cards = load_cards()
# words = []
# for card in cards:
#     words.append(card.word)
#
# if __name__ == '__main__':
#     # The app doesn't receive sys.argv, because we're using
#     # sys.argv[1] to receive the image directory
#     app = QApplication([])
#
#     # Create a window, set its size, and give it a layout
#     win = QWidget()
#     win.setWindowTitle('Language Tutor')
#     win.setMinimumSize(600, 400)
#     layout = QVBoxLayout()
#     win.setLayout(layout)
#
#     # Create one of our ImageFileList objects using the image
#     # directory passed in from the command line
#     lst = QListWidget(win)
#     lst.addItems(words)
#
#     layout.addWidget(lst)
#
#     entry = QLineEdit(win)
#
#     layout.addWidget(entry)
#
#
#     def on_item_changed(curr, prev):
#         entry.setText(curr.text())
#
#
#     lst.currentItemChanged.connect(on_item_changed)
#
#     win.show()
#     app.exec_()