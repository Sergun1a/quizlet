from classes.dictionary.default_dictionary import DefaultDictionary
from classes.menu.menu import Menu

# инициирую импортированные классы
ru_en_dict = DefaultDictionary({"один": "one", "два": "two"}, "Русский", "Английский")
en_ru_dict = DefaultDictionary({"one": "один", "two": "два"}, "Английский", "Русский")
menu = Menu()


menu_action = menu.main_menu()
if menu_action == "1":
    menu.translatation_type_select((ru_en_dict, en_ru_dict))
