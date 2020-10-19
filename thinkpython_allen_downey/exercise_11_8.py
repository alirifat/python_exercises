# get prime numbers
def get_primes():
    prime1 = int(input('Please enter the first prime number:'))
    prime2 = int(input('Please enter the second prime number:'))
    return prime1, prime2


# check if each number is prime
def is_prime(i):
    if i < 2:
        return False
    if i == 2:
        return True
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                return False
    return True


# calculate n to be used as modulus for private and public keys
def calculate_modulus(prime1, prime2):
    n = prime1 * prime2
    return n


# find totient - which is kept as secret
def find_totient(prime1, prime2):
    phi = (prime1 - 1) * (prime2 - 1)
    return phi


# calculates the greatest common divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


# find a number to coprime to totient
def find_coprime(phi):
    for e in range(2, phi):
        if gcd(phi, e) == 1:
            return e

# find the moduler inverse d
def modular_inverse(e, phi):
    for i in range(1, phi):
        if (e * i) % phi == 1:
            return i

def get_keys():
    flag = True
    while flag:
        prime1, prime2 = get_primes()
        if is_prime(prime1) and is_prime(prime2):
            flag = False
    n = calculate_modulus(prime1, prime2)
    phi = find_totient(prime1, prime2)
    e = find_coprime(phi)
    d = modular_inverse(e, phi)
    public = (e, n)
    private = (d, n)
    return public, private

def encryption(public_key, text):
    e, n = public_key
    encrypted = []
    for char in text:
        m = ord(char)
        c = (m**e) % n
        encrypted.append(c)
    return ', '.join([str(i) for i in encrypted])

def decryption(private_key, encrypted):
    d, n = private_key
    decrypted = []
    for i in encrypted.split(', '):
        c = int(i)
        m = (c**d) % n
        char = chr(m)
        decrypted.append(char)
    return ''.join(decrypted)

public_key, private_key = get_keys()
print(public_key, private_key)
encrypted = encryption(public_key, 'Hello')
print(encrypted)
print(decryption(private_key, encrypted))
