from classes.dictionary.default_dictionary import DefaultDictionary

ru_en_dict = DefaultDictionary({"один": "one", "два": "two"}, "Русский", "Английский")
en_ru_dict = DefaultDictionary({"one": "один", "two": "два"}, "Английский", "Русский")

print(ru_en_dict.add_new_translation("два", "three"))
