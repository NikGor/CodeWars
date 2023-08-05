number_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000
}


def parse_int(string):
    string = string.replace(' and ', ' ')
    string = string.replace('-', ' ')
    numbers = string.split(' ')
    arr = []
    for item in numbers:
        arr.append(number_dict[item])
    # цикл в котором если элемент a[i - 1] < a[i] то заменяем a[i] на a[i - 1] * a[i], а a[i] удаляем
    i = 0
    total = 0
    temp = 1

    while i < len(arr):
        if arr[i] == 100:
            temp *= arr[i]
        elif arr[i] in [1000, 1000000]:
            temp *= arr[i]
            total += temp
            temp = 0
        else:
            temp += arr[i]

        i += 1

    return sum(arr)


print(parse_int("one"))  # 1
print(parse_int("twenty"))  # 20
print(parse_int("two hundred forty-six"))  # 246
print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))  # 783919
