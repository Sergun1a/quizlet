from helpers.helpers import wait, clear_screen, purify


class Menu:
    def main_menu(self):
        clear_screen()
        print("""
        Выберите желаемое действие
        1. Добавить перевод в один из словарей
        2. Начать проверку знаний
        3. Получить справку о работе в программе
        """)
        return wait(("1", "2", "3"))

    # выбираю тип перевода. С русского на английский или наоборот с английского на русский
    def translatation_type_select(self, dictionaries):
        clear_screen()
        print("1. " + dictionaries[0].get_primary_language() + " на " + dictionaries[0].get_secondary_language())
        print("2. " + dictionaries[1].get_primary_language() + " на " + dictionaries[1].get_secondary_language())
        chosen_type = wait(("1", "2"))
        self.translation_start(dictionaries[int(chosen_type) - 1])

    def translation_start(self, dictionary):
        clear_screen()
        translation_data = dictionary.request_translation_data()
        dictionary.add_new_translation(translation_data[0], translation_data[1])
        chosen_action = dictionary.post_addition_actions()
        if chosen_action == purify("N"):
            self.translation_start(dictionary)
        if chosen_action == purify("S"):
            self.main_menu()
