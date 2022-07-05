import random
from helpers.helpers import wait, clear_screen, purify


class Quizlet:
    __ru_en_correct_translations = 0
    __ru_en_total_translations = 0
    __en_ru_correct_translations = 0
    __en_ru_total_translations = 0

    __ru_en_dict = {}
    __en_ru_dict = {}

    __ru_en_translations = {}
    __en_ru_translations = {}

    def __init__(self, dictionaries):
        self.__ru_en_dict = dictionaries[0]
        self.__en_ru_dict = dictionaries[1]
        self.__ru_en_translations = dictionaries[0].get_dictionary()
        self.__en_ru_translations = dictionaries[1].get_dictionary()

    def get_ru_translations(self):
        return self.__ru_en_translations

    def get_en_translations(self):
        return self.__en_ru_translations

    # запрашиваю перевод случайного слова из выбранного словаря
    def random_translation(self):
        chosen_dict = random.randint(0, 1)
        lang = ""
        if (len(self.get_ru_translations()) == 0) & (len(self.get_en_translations()) == 0):
            return "out_of_translations"

        if (len(self.get_ru_translations()) > 0) & (len(self.get_en_translations()) > 0):
            if chosen_dict == 0:
                lang = "ru"
                dictionary = self.__ru_en_dict
                translations = self.__ru_en_translations
            else:
                lang = "en"
                dictionary = self.__en_ru_dict
                translations = self.__en_ru_translations

        if (len(self.get_ru_translations()) > 0) & (len(self.get_en_translations()) == 0):
            lang = "ru"
            dictionary = self.__ru_en_dict
            translations = self.__ru_en_translations

        if (len(self.get_ru_translations()) == 0) & (len(self.get_en_translations()) > 0):
            lang = "en"
            dictionary = self.__en_ru_dict
            translations = self.__en_ru_translations

        print("Перевод из языка \"{}\" на \"{}\" язык\n\n".format(
            dictionary.get_primary_language(), dictionary.get_secondary_language()))
        basic_word = random.sample(translations.keys(), 1)[0]
        translation = purify(input(basic_word + "\t=>\t"))
        if lang == "ru":
            self.__ru_en_total_translations = self.__ru_en_total_translations + 1
        if lang == "en":
            self.__en_ru_total_translations = self.__en_ru_total_translations + 1
        if basic_word in translations:
            if translation == translations[basic_word]:
                if lang == "ru":
                    self.__ru_en_correct_translations = self.__ru_en_correct_translations + 1
                if lang == "en":
                    self.__en_ru_correct_translations = self.__en_ru_correct_translations + 1
                print("\nПравильно\n")
                translations.pop(basic_word)
            else:
                print("\nНеверно. Правильный перевод: {}\n".format(dictionary.get_dictionary()[basic_word]))

    def post_translation_actions(self):
        print("\nКлавиша \"N\" - продолжить викторину(следующий перевод)\n"
              "Клавиша \"S\" - завершить викторину и выйти в главное меню\n"
              "Клавиша \"R\" - завершить викторину и просмотреть результаты")

    def results(self, reason=""):
        clear_screen()
        print(reason)
        # избегаю деления на ноль
        if self.__en_ru_total_translations == 0:
            en_ru_procent = (self.__en_ru_correct_translations / 1) * 100
        else:
            en_ru_procent = (self.__en_ru_correct_translations / self.__en_ru_total_translations) * 100

        if self.__ru_en_total_translations == 0:
            ru_en_procent = (self.__ru_en_correct_translations / 1) * 100
        else:
            ru_en_procent = (self.__ru_en_correct_translations / self.__ru_en_total_translations) * 100

        print("Всего было переведено слов: {}\n".format(
            self.__ru_en_total_translations + self.__en_ru_total_translations))
        print("Всего переводов с Русского на Английский : {}\n".format(
            self.__ru_en_total_translations))
        print("Правильных переводов с Русского на Английский : {} из {} ({:.2f}%)\n".format(
            self.__ru_en_correct_translations, self.__ru_en_total_translations,
            ru_en_procent))
        print("Всего переводов с Английского на Русский : {}\n".format(
            self.__en_ru_total_translations))
        print("Правильных переводов с Английского на Русский : {} из {} ({:.2f}%)\n".format(
            self.__en_ru_correct_translations, self.__en_ru_total_translations,
            en_ru_procent))
        print("\n\nНажмите клавишу \"S\" для выхода в главное меню\n")
