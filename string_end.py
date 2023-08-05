def is_ended_by(string, suffix):
    return string.endswith(suffix)


is_ended_by('abc', 'bc') # returns true
is_ended_by('abc', 'd') # returns false
