class DefaultDictionary:
    # приватные методы класса
    __dictionary = {}
    __primary_language = "default_1"
    __secondary_language = "default_2"

    # базовые шаблоны
    __translation_exists = "Перевод слова \"{}\" уже есть в словаре. Желаете обновить перевод?\n"
    __successfully_added_translation = "Перевод слова \"{}\" был добавлен.\n"
    __actions_after_adding = "Нажмите клавишу ENTER, если хотите добавить ещё один перевод или S для выхода в меню программы.\n"

    def __init__(self, dictionary, primary_language, secondary_language):
        self.__dictionary = dictionary
        self.__primary_language = primary_language
        self.__secondary_language = secondary_language

    # очищаю строку от мусора и привожу её к нижнему регистру
    def purify(self, dirty_string):
        print("Execution of the purify method")
        return dirty_string.trim().lower()

    # добавляю в словарь новый перевод
    def add_new_translation(self, word, translation):
        if word in self.__dictionary:
            print(self.__translation_exists.format(word))

        self.__dictionary[word] = translation

    # возвращаю копию словаря
    def get_dictionary(self):
        return self.__dictionary.copy()


