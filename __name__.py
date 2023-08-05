def generate_module_name(task_name):
    # Удаляем все символы, кроме букв, цифр и пробелов
    cleaned_name = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in task_name)
    # Разделяем слова и приводим их к нижнему регистру
    words = cleaned_name.split()
    lowercase_words = [word.lower() for word in words]
    # Объединяем слова через подчеркивание для формирования имени модуля
    module_name = '_'.join(lowercase_words)
    return module_name + '.py'

# Пример использования
task_name = "Replace With Alphabet Position"
module_name = generate_module_name(task_name)
print(module_name)  # Выведет: count_ip_addresses.py
