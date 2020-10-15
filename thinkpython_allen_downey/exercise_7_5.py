def estimate_pi():
    from math import factorial, sqrt
    constant = (2 * sqrt(2)) / 9801
    total = 0
    k = 0
    while True:
         numerator = factorial(4*k)*(1103 + 26390*k)
         denominator = (factorial(k)**4)*(396**(4*k))
         last_term = numerator / denominator
         total += last_term
         if last_term < 1e-15:
             break
         k += 1
    return constant * total

print(estimate_pi())
