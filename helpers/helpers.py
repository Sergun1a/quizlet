import os

# ожидание корректного ответа на вопрос от пользователя
def wait(expected_input):
    user_answer = purify(input())
    while user_answer not in map(purify,expected_input):
        print("Некорректный ввод. Ожидаемые ответы: " + str(expected_input))
        user_answer = purify(input())
    return user_answer


# очищаю строку от мусора и привожу её к нижнему регистру
def purify(dirty_string):
    return dirty_string.strip().lower()


# очищаю вывод в консоли
def clear_screen():
    os.system('cls')
