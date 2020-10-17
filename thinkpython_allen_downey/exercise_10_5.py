def chop(t):
    del t[0], t[-1]
    
t = [1,2,3,4,5,6]
print(chop(t))
print(t)
