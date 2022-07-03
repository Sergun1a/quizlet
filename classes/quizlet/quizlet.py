import random
from helpers.helpers import wait, clear_screen, purify


class Quizlet:
    __ru_en_correct_translations = 0
    __ru_en_total_translations = 0
    __en_ru_correct_translations = 0
    __en_ru_total_translations = 0

    __ru_en_dict = {}
    __en_ru_dict = {}

    def __init__(self, dictionaries):
        self.__ru_en_dict = dictionaries[0]
        self.__en_ru_dict = dictionaries[1]

    # запрашиваю перевод случайного слова из выбранного словаря
    def random_translation(self):
        chosen_dict = random.randint(0, 1)
        dictionary = self.__ru_en_dict if chosen_dict == 0 else self.__en_ru_dict
        print("Перевод из языка \"{}\" на \"{}\" язык\n\n".format(
            dictionary.get_primary_language(), dictionary.get_secondary_language()))
        basic_word = random.sample(dictionary.get_dictionary().keys(), 1)[0]
        translation = purify(input(basic_word + "\t=>\t"))
        if chosen_dict == 0:
            self.__ru_en_total_translations = self.__ru_en_total_translations + 1
        else:
            self.__en_ru_total_translations = self.__en_ru_total_translations + 1

        if translation == dictionary.get_dictionary()[basic_word]:
            if chosen_dict == 0:
                self.__ru_en_correct_translations = self.__ru_en_correct_translations + 1
            else:
                self.__en_ru_correct_translations = self.__en_ru_correct_translations + 1
            print("\nПравильно\n")
        else:
            print("\nНеверно. Правильный перевод: {}\n".format(dictionary.get_dictionary()[basic_word]))

    def post_translation_actions(self):
        print("\nКлавиша \"N\" - продолжить викторину(следующий перевод)\n"
              "Клавиша \"S\" - завершить викторину и выйти в главное меню\n"
              "Клавиша \"R\" - завершить викторину и просмотреть результаты")

    def results(self):
        clear_screen()
        print("Всего было переведено слов: {}\n".format(
            self.__ru_en_total_translations + self.__en_ru_total_translations))
        print("Всего переводов с Русского на Английский : {}\n".format(
            self.__ru_en_total_translations))
        print("Правильных переводов с Русского на Английский : {} из {} ({:.2f}%)\n".format(
            self.__ru_en_correct_translations, self.__ru_en_total_translations,
            (self.__ru_en_correct_translations / self.__ru_en_total_translations) * 100))
        print("Всего переводов с Английского на Русский : {}\n".format(
            self.__en_ru_total_translations))
        print("Правильных переводов с Английского на Русский : {} из {} ({:.2f}%)\n".format(
            self.__en_ru_correct_translations, self.__en_ru_total_translations,
            (self.__en_ru_correct_translations / self.__en_ru_total_translations) * 100))
        print("\n\nНажмите клавишу \"S\" для выхода в главное меню\n")
