def ack(m, n):
    if m < 0 or n < 0:
        return -1
    elif m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

known = {}

def ack_memo(m, n):
    if m < 0 or n < 0:
        return -1
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack_memo(m-1, 1)
    elif (m, n) in known:
        return known[m, n]
    else:
        known[m, n] = ack_memo(m-1, ack_memo(m, n-1))
        return known[m, n]

print(ack(3, 6))
print(ack_memo(3,8))

# the ack function only reaches (m=3, n=6), the memo version reaches (m=3, n=8).
# It does not go beyond that
