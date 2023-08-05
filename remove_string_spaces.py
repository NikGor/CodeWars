def no_space(x):
    error_types = {
        not isinstance(x, str): TypeError('Входной элемент должен быть строкой')
    }

    for condition, error in error_types.items():
        if condition:
            raise error

    return x.replace(' ', '')


test_cases = [
    "8 j 8   mBliB8g  imjB8B8  jl  B",
    "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd",
    "8aaaaa dddd r     "
]

# Тестирование функции
for test_case in test_cases:
    result = no_space(test_case)
    print(f"Input: {test_case} -> Output: {result}")
