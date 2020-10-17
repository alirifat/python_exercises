def prefix_suffix(prefixes, suffix):
    for letter in prefixes:
        if (letter == 'O') or (letter == 'Q'):
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

prefix_suffix(prefixes, suffix)
