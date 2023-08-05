def find_needle(haystack):
    keyword = 'needle'
    return f'return found the needle at position {haystack.index(keyword)}'


haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print(find_needle(haystack))
