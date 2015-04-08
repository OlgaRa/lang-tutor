# Create word-card

import random
import pickle

cards = [] #Все карточки
LEARN_COUNT = 10

class Card():
    word = ""
    translation = ""
    example = ""
    correct_answer_count = 0

    @property
    def is_learned(self):
        """True if card is learned"""
        if self.correct_answer_count >= LEARN_COUNT:
            return True
        else:
            return False

    @property
    def is_active(self):
        if self.is_learned:
            return False
        if self.correct_answer_count != 0:
            return True
        else:
            return False

    def print_card(self):
        print("Слово:", self.word, end="")
        print(". Перевод: ", self.translation)
        print("Пример: ", self.example)
        print("Колличество правильных ответов: ", self.correct_answer_count)

    def create_card(self):
        self.word = input("Введите слово: ")
        self.translation = input("Введите перевод: ")
        self.example = input("Введите пример: ")

def get_cards_to_learn(massiv, cards_to_select=10):
    results_arr = []
    for card in massiv:
        assert isinstance(card, Card)
        if card.is_active:
            results_arr.append(card)
        if len(results_arr) == 10:
            return results_arr

    for card in massiv:
        assert isinstance(card, Card)
        if not card.is_active and not card.is_learned:
            results_arr.append(card)
        if len(results_arr) == 10:
            return results_arr

    return results_arr



def fill_test_cards(massiv):
    new_card1 = Card()
    new_card1.word = "dog"
    new_card1.translation = "собака"
    new_card1.example = "a dog is a pet"

    new_card2 = Card()
    new_card2.word = "cat"
    new_card2.translation = "кошка"
    new_card2.example = "A cat says Mey"

    new_card3 = Card()
    new_card3.word = "mouse"
    new_card3.translation = "мышка"
    new_card3.example = "Cats eat mouses"
    massiv += [new_card1, new_card2, new_card3]

def show_all_cards(massiv):
    number = 1
    for word in massiv:
        print(number, "-"), word.print_card()
        number += 1

def add_new_word(massiv):
    new_word = Card()
    new_word.create_card()
    massiv.append(new_word)

#new_card4 = Card()
#new_card4.create_card()

#words.append(new_card4)
#new_card4.print_card()

def save_cards(massiv):
    try:
        with open('cards.pickle', 'wb') as f:
            pickle.dump(massiv, f)
    except Exception as err:
        print("Ошибка записи файла. Причина: ", err)


def load_cards():
    try:
        with open('cards.pickle', 'rb') as f:
            return pickle.load(f)
    except Exception as err:
        print("Ошибка открытия файла. Причина: ", err)
        return []


def learn_word(massiv):
    index = random.randint(0, len(massiv)- 1)
    random_card = massiv[index]
    print("Как переводится слово - ", random_card.word)
    number = 0
    for translation in massiv:
        number += 1
        print(number, "-", translation.translation)
    true_translation = int(input("Какой вариант перевода правильный? (1-3)"))
    true_translation -= 1
    if true_translation == index:
        print("Молодец! Ты абсолютно прав, правильный перевод:", random_card.translation)
        random_card.correct_answer_count += 1
    else:
        print("К сожалению, это не так, правильный перевод:", random_card.translation)
        random_card.correct_answer_count -= 1

def find_card_by_word(cards_to_search, word):
    for card in cards_to_search:
        if card.word == word:
            return card

if __name__ == "__main__":

    #fill_test_cards(cards)
    #save_cards(cards)
    cards.extend(load_cards())
    print("Загружено {} карт".format(len(cards)))

    choice = None

    while choice != "0":
        print(
            """
            Программа для изучения слов:
            0 - Выйти
            1 - Показать слова
            2 - Добавить слово
            3 - Учить слова
            4 - Удалить слово

            """
            )
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print ("До свидания.")

        # вывод списка слов
        elif choice == "1":
            print("Слова:")
            show_all_cards(cards)

        # добавление слова
        elif choice == "2":
            add_new_word(cards)
            save_cards(cards)

        # учить слова
        elif choice == "3":
            tries = 0
            while tries != 5:
                cards_to_learn = get_cards_to_learn(cards)
                learn_word(cards_to_learn)
                tries += 1
            save_cards(cards)

        # удалить слово
        elif choice == "4":
            delete_word = int(input("Какое слово вы хотите удалить, введите номер: "))
            delete_word -= 1
            cards.remove(cards[delete_word])
            print("Слово удалено.")
            save_cards(cards)

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)