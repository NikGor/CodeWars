def are_you_playing_banjo(name):
    result = f'{name} plays banjo' if name.lower().startswith('r') else f'{name} does not play banjo'
    return result


print(are_you_playing_banjo('riko'))
