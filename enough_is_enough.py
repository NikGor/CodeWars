# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
from typing import List
from collections import Counter


def delete_nth(order: List, max_e):
    error_types = {
        not isinstance(order, list): TypeError("Входной аргумент должен быть списком"),
        max_e < 0: ValueError("Количество вхождений не может быть отрицательным"),
        not isinstance(max_e, int): ValueError("Количество вхождений должно быть целым числом")
    }

    for condition, error in error_types.items():
        if condition:
            raise error
    
    counter = Counter(order)
    new_order = []
    for item in order:
        if counter.get(item, 0) < max_e:
            new_order.append(item)
            counter[item]= counter.get(item, 0) + 1

    return new_order


photo_collection = [
    "beach", "sunset", "beach", "sea", "palm_tree", "palm_tree", "sunset",
    "mountain", "lake", "mountain", "mountain", "lake", "lake", "river",
    "dolphin", "dolphin", "dolphin", "ocean", "ocean", "ocean", "sky", "sky"
]
new_order = delete_nth(photo_collection, 2)
print(new_order)
