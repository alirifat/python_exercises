def capitalize_nested(t):
    capitalized = []
    for nested in t:
        if type(nested) == list:
            inner_nested = []
            for item in nested:
                inner_nested.append(item.upper())
            capitalized.append(inner_nested)
        else:
            capitalized.append(nested.upper())
    return capitalized

nested = ['write', ['a', 'function', 'called'],
          ['nested_sum', 'that', 'takes', 'a', 'nested', 'list'],
          'of', 'integers', ['and', 'add', 'up', 'the', 'elements', 'from'],
          'all', ['of', 'the', 'nested', 'lists']]
print(capitalize_nested(nested))
