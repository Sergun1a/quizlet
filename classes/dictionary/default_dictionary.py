from helpers.helpers import wait, purify


class DefaultDictionary:
    # приватные методы класса
    __dictionary = {}
    __primary_language = "default_1"
    __secondary_language = "default_2"

    # базовые шаблоны
    __translation_exists = "Перевод слова \"{}\" уже есть в словаре. Желаете обновить перевод?\tY|N\n"
    __successfully_added_translation = "Перевод слова \"{}\" был добавлен.\n"
    __actions_after_adding = "Нажмите клавишу N, если хотите добавить ещё один перевод или клавишу S для выхода в меню программы.\tN|S\n"

    def __init__(self, dictionary, primary_language, secondary_language):
        self.__dictionary = dictionary
        self.__primary_language = primary_language
        self.__secondary_language = secondary_language

    # добавляю в словарь новый перевод
    def add_new_translation(self, word, translation):
        user_input = purify('Y')
        if purify(word) in self.__dictionary:
            print(self.__translation_exists.format(word))
            user_input = wait(('Y', 'N'))

        if user_input == purify('Y'):
            self.__dictionary[purify(word)] = purify(translation)
            print(self.__successfully_added_translation.format(word))

    # вывожу сообщение с вариантами действия после добавления перевода
    def post_addition_actions(self):
        print(self.__actions_after_adding)
        return wait(('N', 'S'))

    # возвращаю копию словаря
    def get_dictionary(self):
        return self.__dictionary.copy()

    # запрашиваю у пользователя данные о переводе слова
    def request_translation_data(self):
        print("Базовый язык: {}. Перевод на {}\n".format(self.__primary_language, self.__secondary_language))
        primary_word = purify(input("Введите слово на базовом языке\n"))
        translation = purify(input("Введите перевод для \"{0}\"\n".format(primary_word)))
        return primary_word, translation

    def get_primary_language(self):
        return self.__primary_language

    def get_secondary_language(self):
        return self.__secondary_language
