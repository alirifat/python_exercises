def remove_duplicates(t):
    t_unique = []
    for element in t:
        if not element in t_unique:
            t_unique.append(element)
    return t_unique

print(remove_duplicates(['a', 'b', 1, 2, 'a', '2', 3, 1]))
