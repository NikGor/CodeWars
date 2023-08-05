opposite_directions = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST'
}


def dir_reduc(arr):
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposite_directions[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack


map = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc(map))
