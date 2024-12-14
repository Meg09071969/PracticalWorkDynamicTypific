calls = 0  # Глобальная переменная для подсчёта вызовов
def count_calls():  # Увеличивает значение глобальной переменной calls
    global calls
    calls += 1


def string_info(string):  # Принимает строку и возвращает кортеж, длина строки, строка в верхнем регистре, строка в нижнем регистре
    count_calls()  # Увеличиваем счётчик вызовов
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    """Проверяет, содержится ли строка string в списке list_to_search, игнорируя регистр букв. Возвращает True или False"""

    count_calls()  # Увеличиваем счётчик вызовов
    # Приводим строку и элементы списка к одному регистру для сравнения
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

# Пример использования функций:
# Вызов string_info с произвольными строками
print(string_info("Hello World"))  # (11, 'HELLO WORLD', 'hello world')
print(string_info("Python"))       # (6, 'PYTHON', 'python')

# Вызов is_contains с произвольными данными
print(is_contains("urban", ["URBAN", "City", "village"]))  # True
print(is_contains("Sea", ["ocean", "lake", "river"]))      # False


print("Количество вызовов:", calls)  # Вывод значения calls