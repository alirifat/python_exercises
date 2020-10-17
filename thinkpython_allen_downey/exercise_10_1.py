def nested_sum(t):
    total = 0
    for nested in t:
        if type(nested) == list:
            for item in nested:
                total += item
        else:
            total += nested
    return total

nested = [[1,2,3], 4, [5,6], [7], [8,9,10,11]]
print(nested_sum(nested))
