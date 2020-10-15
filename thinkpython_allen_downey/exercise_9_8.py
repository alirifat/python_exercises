def is_palindrome(s):
    return s == s[::-1]

def find_odometer(i):
    if is_palindrome(str(i)[2:]) and \
       is_palindrome(str(i+1)[1:]) and \
       is_palindrome(str(i+2)[1:5]) and \
       is_palindrome(str(i+3)):
        print(i)

for i in range(100000, 999999):
    find_odometer(i)

# Another way to solve only using if statements
def find_odometer(i):
    s = str(i)
    if s[2:] == s[2:][::-1]:
        s = str(i+1)
        if s[1:] == s[1:][::-1]:
            s = str(i+2)
            if s[1:5] == s[1:5][::-1]:
                s = str(i+3)
                if s == s[::-1]:
                    print(i)

for i in range(100000, 999999):
    find_odometer(i)
