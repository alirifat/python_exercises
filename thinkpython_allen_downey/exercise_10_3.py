def cummulative_sum(t):
    t_cumsum = []
    i = 1
    while i <= len(t):
        t_cumsum.append(sum(t[0:i]))
        i += 1
    return t_cumsum

print(cummulative_sum([1,2,3,4,5,6]))
